"""
Register classifier for liturgy-as-code completions.

For each completion in results/<timestamp>/completions/<condition>/<tail>/, ask
Claude Haiku 4.5 (via OpenRouter) to rate the text on:

  - formality            (1=casual, 5=highly formal/ritual)
  - archaism             (1=modern colloquial, 5=archaic/biblical/ancient)
  - reverential_register (1=neutral, 5=devotional/sacred)
  - has_supernatural_imagery (bool)

Writes results/<timestamp>/register_ratings.json with per-completion ratings.

Then measure.py (re-run after classification) can fold these into the headline.

Usage:
    python src/classify_register.py results/2026-05-30T10-44-26
    python src/classify_register.py --latest
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
import time
from collections import defaultdict
from pathlib import Path
from typing import Any

import httpx
from dotenv import load_dotenv


REPO_ROOT = Path(__file__).resolve().parent.parent
RESULTS_DIR = REPO_ROOT / "results"
ENV_FILE = REPO_ROOT / ".local" / ".env"

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
CLASSIFIER_MODEL = "anthropic/claude-haiku-4.5"


CLASSIFIER_PROMPT = """You will rate a text completion produced by a language model. The completion may continue a prayer, chant, grimoire invocation, ritual text, or random prose. Rate the completion ONLY on these dimensions. Ignore content that appears before the completion itself.

Dimensions:
- formality: 1 (casual / colloquial) ... 5 (highly formal / ritual / liturgical)
- archaism: 1 (fully modern, contemporary register) ... 5 (archaic / biblical / ancient-sounding)
- reverential_register: 1 (neutral, descriptive, or dismissive) ... 5 (devotional, sacred, address-to-the-divine)
- has_supernatural_imagery: true if the completion contains supernatural, cosmological, divine, demonic, angelic, or magical imagery; false otherwise

Respond with ONLY a single JSON object, no commentary, exactly this schema:
{"formality": <int 1-5>, "archaism": <int 1-5>, "reverential_register": <int 1-5>, "has_supernatural_imagery": <true|false>}

Completion to rate:
---
{COMPLETION}
---

JSON:"""


def _parse_json_response(content: str) -> dict[str, Any]:
    """Parse a (possibly code-fenced) JSON response from the classifier."""
    content = content.strip()
    if content.startswith("```"):
        content = content.split("\n", 1)[1] if "\n" in content else content
        if content.endswith("```"):
            content = content[:-3]
        content = content.strip()
        if content.lower().startswith("json"):
            content = content[4:].strip()
    return json.loads(content)


async def _classify_one_async(
    client: httpx.AsyncClient,
    sem: asyncio.Semaphore,
    api_key: str,
    text: str,
    *,
    max_attempts: int = 3,
) -> dict[str, Any]:
    payload = {
        "model": CLASSIFIER_MODEL,
        "messages": [
            {
                "role": "user",
                "content": CLASSIFIER_PROMPT.replace("{COMPLETION}", text.strip()),
            }
        ],
        "temperature": 0.0,
        "max_tokens": 100,
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/local/liturgy-as-code",
        "X-Title": "liturgy-as-code register classifier",
    }
    last_err: str | None = None
    content = ""
    async with sem:
        for attempt in range(max_attempts):
            try:
                r = await client.post(OPENROUTER_URL, json=payload, headers=headers)
                r.raise_for_status()
                data = r.json()
                content = data["choices"][0]["message"]["content"]
                return _parse_json_response(content)
            except json.JSONDecodeError as e:
                last_err = (
                    f"JSON parse failed (attempt {attempt + 1}): {e}; raw={content!r}"
                )
            except httpx.HTTPStatusError as e:
                last_err = f"HTTP {e.response.status_code}: {e.response.text[:200]}"
                if e.response.status_code == 429:
                    await asyncio.sleep(min(5 * (attempt + 1), 30))
                    continue
            except Exception as e:  # noqa: BLE001
                last_err = f"{type(e).__name__}: {e}"
            await asyncio.sleep(2 * (attempt + 1))
    return {"_error": last_err}


async def _classify_run_async(run_dir: Path, api_key: str, concurrency: int) -> None:
    completions_root = run_dir / "completions"
    out_path = run_dir / "register_ratings.json"
    if out_path.exists():
        ratings = json.loads(out_path.read_text())
    else:
        ratings = {}

    cells = sorted([p for p in completions_root.glob("*/*") if p.is_dir()])
    work: list[tuple[str, Path]] = []
    for cell_dir in cells:
        for cpath in sorted(cell_dir.glob("*.txt")):
            key = str(cpath.relative_to(completions_root))
            if key in ratings and "_error" not in ratings[key]:
                continue
            work.append((key, cpath))

    total = len(work)
    print(
        f"[classify] {total} completions to rate ({len(cells)} cells, concurrency={concurrency})",
        flush=True,
    )
    if total == 0:
        return

    sem = asyncio.Semaphore(concurrency)
    started = time.time()
    save_lock = asyncio.Lock()
    counters = {"done": 0, "errors": 0}

    async def one(client: httpx.AsyncClient, key: str, cpath: Path) -> None:
        text = cpath.read_text()
        if len(text.strip()) < 5:
            rating: dict[str, Any] = {"_error": "empty completion"}
        else:
            rating = await _classify_one_async(client, sem, api_key, text)
        async with save_lock:
            ratings[key] = rating
            counters["done"] += 1
            if "_error" in rating:
                counters["errors"] += 1
            done = counters["done"]
            if done % 25 == 0 or done == total:
                out_path.write_text(json.dumps(ratings, indent=2, sort_keys=True))
                elapsed = time.time() - started
                rate = done / elapsed if elapsed > 0 else 0
                eta = (total - done) / rate if rate > 0 else 0
                print(
                    f"  [{done}/{total}] elapsed={elapsed:.0f}s rate={rate:.2f}/s"
                    f" eta={eta:.0f}s errors={counters['errors']}",
                    flush=True,
                )

    async with httpx.AsyncClient(timeout=60.0) as client:
        await asyncio.gather(*(one(client, k, p) for k, p in work))

    out_path.write_text(json.dumps(ratings, indent=2, sort_keys=True))
    print(
        f"[classify] done. {total - counters['errors']}/{total} successful.",
        flush=True,
    )
    print(f"[classify] wrote {out_path}", flush=True)


def classify_run(run_dir: Path, concurrency: int = 1) -> None:
    load_dotenv(ENV_FILE)
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        sys.exit(f"OPENROUTER_API_KEY missing; expected in {ENV_FILE}")
    if not (run_dir / "completions").exists():
        sys.exit(f"no completions in {run_dir}")
    asyncio.run(_classify_run_async(run_dir, api_key, concurrency))


def summarize(run_dir: Path) -> None:
    """Print mean ratings per (condition × tail) cell."""
    ratings_path = run_dir / "register_ratings.json"
    if not ratings_path.exists():
        sys.exit(f"no register_ratings.json in {run_dir}")
    ratings = json.loads(ratings_path.read_text())

    by_cell: dict[str, list[dict]] = defaultdict(list)
    for key, r in ratings.items():
        if "_error" in r:
            continue
        # key = "condition/tail/000.txt"
        parts = key.split("/")
        if len(parts) < 3:
            continue
        cell_key = f"{parts[0]}/{parts[1]}"
        by_cell[cell_key].append(r)

    print()
    print("=== Register classification summary ===")
    print(f"{'Cell':45s} {'n':>4} {'form':>6} {'arch':>6} {'rev':>6} {'%super':>7}")
    for cell, ratings_list in sorted(by_cell.items()):
        n = len(ratings_list)
        f_mean = sum(r["formality"] for r in ratings_list) / n
        a_mean = sum(r["archaism"] for r in ratings_list) / n
        r_mean = sum(r["reverential_register"] for r in ratings_list) / n
        s_pct = 100 * sum(1 for r in ratings_list if r["has_supernatural_imagery"]) / n
        print(
            f"  {cell:45s} {n:4d} {f_mean:6.2f} {a_mean:6.2f}"
            f" {r_mean:6.2f} {s_pct:6.1f}%"
        )


def main() -> None:
    p = argparse.ArgumentParser(description="Register classifier over a run dir.")
    p.add_argument("run_dir", nargs="?")
    p.add_argument("--latest", action="store_true")
    p.add_argument(
        "--summarize-only",
        action="store_true",
        help="Skip classification, just summarize existing register_ratings.json",
    )
    p.add_argument(
        "--concurrency",
        type=int,
        default=1,
        help=(
            "Max in-flight Claude Haiku calls via asyncio. Default 1 = serial."
            " 6-8 for scale (Haiku tolerates this well)."
        ),
    )
    args = p.parse_args()

    if args.latest:
        runs = sorted(
            [d for d in RESULTS_DIR.iterdir() if d.is_dir()],
            key=lambda d: d.stat().st_mtime,
            reverse=True,
        )
        if not runs:
            sys.exit("no result dirs found")
        run_dir = runs[0]
    elif args.run_dir:
        run_dir = Path(args.run_dir).resolve()
    else:
        sys.exit("specify a run dir or --latest")

    if not args.summarize_only:
        classify_run(run_dir, concurrency=args.concurrency)
    summarize(run_dir)


if __name__ == "__main__":
    main()
