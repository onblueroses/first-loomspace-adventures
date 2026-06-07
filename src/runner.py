"""
Liturgy-as-code runner.

For each (liturgy condition × tail prompt) cell, sample N completions from a
base-like model via OpenRouter's /completions endpoint and write each completion
to a per-cell directory under results/<timestamp>/.

Concurrency: --concurrency N runs N in-flight requests via asyncio. Default 1
(serial). Recommended 6-10 for real-scale runs against Hermes/DeepSeek.

Usage:
    python src/runner.py --smoke                                   # n=2, free model, 1 tail
    python src/runner.py --n 20                                    # serial, all tails
    python src/runner.py --n 200 --concurrency 8 --tails all       # parallel scale run
    python src/runner.py --help

Liturgies are read from liturgies/*.md (frontmatter + body).
Tails are read from tails/prompts.yaml.
"""

from __future__ import annotations

import argparse
import asyncio
import os
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import httpx
import yaml
from dotenv import load_dotenv


REPO_ROOT = Path(__file__).resolve().parent.parent
LITURGIES_DIR = REPO_ROOT / "liturgies"
TAILS_FILE = REPO_ROOT / "tails" / "prompts.yaml"
RESULTS_DIR = REPO_ROOT / "results"
ENV_FILE = REPO_ROOT / ".local" / ".env"

OPENROUTER_URL = "https://openrouter.ai/api/v1/completions"

MODEL_DEFAULT = "nousresearch/hermes-3-llama-3.1-405b"
MODEL_SMOKE = "nousresearch/hermes-3-llama-3.1-405b:free"
MODEL_REPLICATION = "deepseek/deepseek-v3.2"


# ---------- IO ----------


@dataclass
class Liturgy:
    id: str
    name: str
    source: str
    body: str
    frontmatter: dict[str, Any] = field(default_factory=dict)


@dataclass
class Tail:
    id: str
    prompt: str


def parse_md_with_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text()
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    fm_text = text[4:end]
    body = text[end + 5 :].strip()
    fm = yaml.safe_load(fm_text) or {}
    return fm, body


def load_liturgies() -> list[Liturgy]:
    out: list[Liturgy] = []
    for path in sorted(LITURGIES_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        fm, body = parse_md_with_frontmatter(path)
        out.append(
            Liturgy(
                id=fm.get("id", path.stem),
                name=fm.get("name", path.stem),
                source=fm.get("source", "unknown"),
                body=body,
                frontmatter=fm,
            )
        )
    return out


def load_tails() -> list[Tail]:
    data = yaml.safe_load(TAILS_FILE.read_text())
    return [Tail(id=t["id"], prompt=t["prompt"]) for t in data]


# ---------- OpenRouter ----------


def extract_text(response: dict) -> str:
    """Extract the completion text from an OpenRouter response."""
    choices = response.get("choices", [])
    if not choices:
        return ""
    c = choices[0]
    # /completions returns choices[i].text; some providers wrap with message
    if "text" in c:
        return c["text"]
    if "message" in c and isinstance(c["message"], dict):
        return c["message"].get("content", "")
    return ""


def _payload(model: str, prompt: str, params: dict) -> dict:
    return {
        "model": model,
        "prompt": prompt,
        "temperature": params["temperature"],
        "top_p": params["top_p"],
        "max_tokens": params["max_tokens"],
    }


def _headers(api_key: str) -> dict:
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/local/liturgy-as-code",
        "X-Title": "liturgy-as-code",
    }


async def complete_async(
    client: httpx.AsyncClient,
    api_key: str,
    model: str,
    prompt: str,
    params: dict,
) -> dict:
    r = await client.post(
        OPENROUTER_URL, json=_payload(model, prompt, params), headers=_headers(api_key)
    )
    r.raise_for_status()
    return r.json()


# ---------- Async run loop ----------


def slugify_timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%S")


def _parse_retry_after(value: str | None, fallback: float = 5.0) -> float:
    """Parse a Retry-After header value (seconds OR HTTP date). Always returns
    a non-negative float; falls back on malformed input."""
    if not value:
        return fallback
    try:
        return max(0.0, float(value))
    except ValueError:
        pass
    try:
        from email.utils import parsedate_to_datetime

        target = parsedate_to_datetime(value)
        delta = (target - datetime.now(timezone.utc)).total_seconds()
        return max(0.0, delta)
    except Exception:  # noqa: BLE001
        return fallback


async def _run_one(
    client: httpx.AsyncClient,
    sem: asyncio.Semaphore,
    api_key: str,
    model: str,
    prompt: str,
    cell_dir: Path,
    i: int,
    params: dict,
) -> str | None:
    """Run a single completion with the semaphore. Returns None on success, error
    string on failure. Retries once on 429 honoring Retry-After."""
    async with sem:
        out_path = cell_dir / f"{i:03d}.txt"
        err_path = cell_dir / f"{i:03d}.err"
        try:
            resp = await complete_async(client, api_key, model, prompt, params)
            text = extract_text(resp)
            out_path.write_text(text)
            if err_path.exists():
                err_path.unlink()
            return None
        except httpx.HTTPStatusError as e:
            status = e.response.status_code if e.response else 0
            body = e.response.text[:500] if e.response else ""
            if status == 429 and e.response is not None:
                retry_after = _parse_retry_after(e.response.headers.get("Retry-After"))
                await asyncio.sleep(min(retry_after, 30))
                try:
                    resp = await complete_async(client, api_key, model, prompt, params)
                    text = extract_text(resp)
                    out_path.write_text(text)
                    if err_path.exists():
                        err_path.unlink()
                    return None
                except Exception as e2:  # noqa: BLE001
                    err_path.write_text(
                        f"HTTPStatusError {status} (retried, then failed)\n{body}\nretry: {e2}"
                    )
                    return f"HTTP {status} (retry failed)"
            err_path.write_text(f"HTTPStatusError {status}\n{body}")
            return f"HTTP {status}"
        except Exception as e:  # noqa: BLE001
            err_path.write_text(f"{type(e).__name__}: {e}")
            return f"{type(e).__name__}: {e}"


async def _run_async(
    *,
    n: int,
    model: str,
    liturgies: list[Liturgy],
    tails: list[Tail],
    completions_dir: Path,
    api_key: str,
    params: dict,
    concurrency: int,
    skip_existing: bool,
) -> int:
    sem = asyncio.Semaphore(concurrency)
    async with httpx.AsyncClient(timeout=180.0) as client:
        tasks = []
        for L in liturgies:
            for T in tails:
                cell_dir = completions_dir / L.id / T.id
                cell_dir.mkdir(parents=True, exist_ok=True)
                prompt = L.body.rstrip() + T.prompt
                for i in range(n):
                    out_path = cell_dir / f"{i:03d}.txt"
                    if (
                        skip_existing
                        and out_path.exists()
                        and out_path.stat().st_size > 0
                    ):
                        continue
                    tasks.append(
                        asyncio.create_task(
                            _run_one(
                                client, sem, api_key, model, prompt, cell_dir, i, params
                            )
                        )
                    )

        total = len(tasks)
        if total == 0:
            print("  [skip] all completions already exist", flush=True)
            return 0

        started = time.time()
        errors = 0
        done = 0
        log_every = max(5, total // 40)
        for fut in asyncio.as_completed(tasks):
            err = await fut
            done += 1
            if err is not None:
                errors += 1
            if done % log_every == 0 or done == total:
                elapsed = time.time() - started
                rate = done / elapsed if elapsed > 0 else 0
                eta = (total - done) / rate if rate > 0 else 0
                print(
                    f"  [{done}/{total}] elapsed={elapsed:.0f}s"
                    f" rate={rate:.2f}/s eta={eta:.0f}s errors={errors}",
                    flush=True,
                )
        return errors


def run(
    *,
    n: int,
    model: str,
    liturgy_filter: list[str] | None = None,
    tail_filter: list[str] | None = None,
    temperature: float = 0.7,
    top_p: float = 0.95,
    max_tokens: int = 256,
    concurrency: int = 1,
    dry_run: bool = False,
    skip_existing: bool = False,
    run_id: str | None = None,
    require_prereg: bool = False,
) -> Path:
    liturgies = load_liturgies()
    tails = load_tails()

    if liturgy_filter:
        liturgies = [L for L in liturgies if L.id in liturgy_filter]
    if tail_filter:
        tails = [T for T in tails if T.id in tail_filter]

    if not liturgies:
        sys.exit("no liturgies matched filter")
    if not tails:
        sys.exit("no tails matched filter")

    if run_id is None:
        run_id = slugify_timestamp()
    run_dir = RESULTS_DIR / run_id
    completions_dir = run_dir / "completions"

    # Pre-registration enforcement (P1 from codex review):
    # When require_prereg is set (CLI: --require-prereg, or implied by --run-id),
    # demand that expected.md already exists before any non-dry sampling. This
    # prevents post-hoc framing of what the headline numbers "should" have shown.
    prereg_path = run_dir / "expected.md"
    if not dry_run and require_prereg and not prereg_path.exists():
        sys.exit(
            f"pre-registration required but missing: {prereg_path}\n"
            f"  write your predictions for L_real vs. controls BEFORE sampling,"
            f" then re-run."
        )

    completions_dir.mkdir(parents=True, exist_ok=True)

    if not dry_run:
        load_dotenv(ENV_FILE)
        api_key = os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            sys.exit(f"OPENROUTER_API_KEY missing; expected in {ENV_FILE}")
    else:
        api_key = ""  # not used in dry-run path

    config = {
        "run_id": run_id,
        "model": model,
        "n_per_cell": n,
        "temperature": temperature,
        "top_p": top_p,
        "max_tokens": max_tokens,
        "concurrency": concurrency,
        "liturgies": [L.id for L in liturgies],
        "tails": [T.id for T in tails],
        "started_at": datetime.now(timezone.utc).isoformat(),
        "dry_run": dry_run,
    }
    (run_dir / "config.yaml").write_text(yaml.safe_dump(config, sort_keys=False))

    total_cells = len(liturgies) * len(tails)
    total_calls = total_cells * n
    print(f"[run {run_id}] model={model} concurrency={concurrency}", flush=True)
    print(
        f"[run {run_id}] {len(liturgies)} liturgies × {len(tails)} tails × n={n}"
        f" = {total_cells} cells, {total_calls} calls",
        flush=True,
    )
    if dry_run:
        for L in liturgies:
            for T in tails:
                print(f"  dry-run cell: {L.id} × {T.id}", flush=True)
        return run_dir

    params = {"temperature": temperature, "top_p": top_p, "max_tokens": max_tokens}
    errors = asyncio.run(
        _run_async(
            n=n,
            model=model,
            liturgies=liturgies,
            tails=tails,
            completions_dir=completions_dir,
            api_key=api_key,
            params=params,
            concurrency=concurrency,
            skip_existing=skip_existing,
        )
    )

    config["finished_at"] = datetime.now(timezone.utc).isoformat()
    config["total_calls"] = total_calls
    config["errors"] = errors
    (run_dir / "config.yaml").write_text(yaml.safe_dump(config, sort_keys=False))

    print(
        f"[run {run_id}] done. {total_calls - errors}/{total_calls} successful."
        f" results at {run_dir}",
        flush=True,
    )
    return run_dir


# ---------- CLI ----------


def main() -> None:
    p = argparse.ArgumentParser(description="Liturgy-as-code runner.")
    p.add_argument(
        "--smoke",
        action="store_true",
        help="Pipeline smoke test: n=2, free model, single tail.",
    )
    p.add_argument("--n", type=int, default=20, help="Rollouts per cell (default 20).")
    p.add_argument(
        "--model", type=str, default=MODEL_DEFAULT, help="OpenRouter model id."
    )
    p.add_argument(
        "--liturgies",
        type=str,
        default=None,
        help="Comma-separated liturgy ids to include (default: all).",
    )
    p.add_argument(
        "--tails",
        type=str,
        default=None,
        help='Comma-separated tail ids to include, or "all" (default: all).',
    )
    p.add_argument("--temperature", type=float, default=0.7)
    p.add_argument("--top-p", type=float, default=0.95, dest="top_p")
    p.add_argument("--max-tokens", type=int, default=256, dest="max_tokens")
    p.add_argument(
        "--concurrency",
        type=int,
        default=1,
        help="Max in-flight requests via asyncio (default 1 = serial). 6-10 for scale.",
    )
    p.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip cells where the completion file already exists (resume support).",
    )
    p.add_argument(
        "--run-id",
        type=str,
        default=None,
        help=(
            "User-supplied run id (results/<id>/). Lets you pre-write expected.md"
            " before sampling. When set, pre-registration is enforced."
        ),
    )
    p.add_argument(
        "--require-prereg",
        action="store_true",
        help=(
            "Refuse to start unless results/<run-id>/expected.md exists."
            " Implied when --run-id is set."
        ),
    )
    p.add_argument(
        "--dry-run", action="store_true", help="Print cells; do not call API."
    )
    args = p.parse_args()

    if args.smoke:
        args.n = 2
        args.model = MODEL_SMOKE
        if not args.tails:
            args.tails = "visitor_at_door"

    liturgy_filter = (
        [s.strip() for s in args.liturgies.split(",")] if args.liturgies else None
    )
    tail_filter = None
    if args.tails and args.tails != "all":
        tail_filter = [s.strip() for s in args.tails.split(",")]

    run(
        n=args.n,
        model=args.model,
        liturgy_filter=liturgy_filter,
        tail_filter=tail_filter,
        temperature=args.temperature,
        top_p=args.top_p,
        max_tokens=args.max_tokens,
        concurrency=args.concurrency,
        dry_run=args.dry_run,
        skip_existing=args.skip_existing,
        run_id=args.run_id,
        require_prereg=args.require_prereg or bool(args.run_id),
    )


if __name__ == "__main__":
    main()
