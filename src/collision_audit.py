"""
Collision audit for synthetic-liturgy invented names.

Per spec Decision #12: 5-layer deterministic check against (a) existing
liturgy frontmatter `named_entities`, (b) curated registries at
liturgies/_registries/, (c) (Google check manual).

Reject if ANY layer fires.

Usage:
    python src/collision_audit.py --candidates name1 name2 name3 ...
    python src/collision_audit.py --candidates-file path/to/names.txt
    python src/collision_audit.py --candidates-file ... --out audit.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

import phonetics  # type: ignore[import-not-found]
import Levenshtein  # type: ignore[import-not-found]
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
LITURGIES_DIR = REPO_ROOT / "liturgies"
REGISTRIES_DIR = LITURGIES_DIR / "_registries"


def normalize(s: str) -> str:
    """Lowercase, strip diacritics, collapse whitespace."""
    s = s.lower()
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"\s+", " ", s).strip()
    return s


def collect_known_names(exclude_liturgy: str | None = None) -> list[str]:
    """Gather all canonical names from (a) liturgy frontmatter + (b) registries.

    If exclude_liturgy is set, skip that liturgy's frontmatter entirely. Used for
    denamed audits where the candidate is INTENTIONALLY close to the parent's
    names (so parent-collisions are expected and should not fire the gate).
    """
    names: set[str] = set()

    # Layer (a): existing liturgy frontmatter named_entities + related_vocabulary
    for path in LITURGIES_DIR.glob("*.md"):
        if path.name == "README.md":
            continue
        if exclude_liturgy and path.stem == exclude_liturgy:
            continue
        text = path.read_text()
        if not text.startswith("---\n"):
            continue
        end = text.find("\n---\n", 4)
        if end == -1:
            continue
        try:
            fm = yaml.safe_load(text[4:end]) or {}
        except yaml.YAMLError:
            continue
        for field in ("named_entities", "ambiguous_entities", "related_vocabulary"):
            for item in fm.get(field, []) or []:
                names.add(str(item))

    # Layer (b): curated registries
    for path in REGISTRIES_DIR.glob("*.txt"):
        for line in path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            names.add(line)

    return sorted(names)


def safe_phonetic(fn, s: str) -> str:
    """Compute Soundex/Metaphone on ASCII-stripped lowercase; return empty on failure."""
    try:
        ascii_s = "".join(c for c in normalize(s) if c.isascii() and c.isalpha())
        return fn(ascii_s) if ascii_s else ""
    except Exception:
        return ""


def audit(candidate: str, known: list[str]) -> dict:
    """Run all 5 layers on a single candidate name. Return per-layer results."""
    cand_norm = normalize(candidate)
    cand_soundex = safe_phonetic(phonetics.soundex, candidate)
    cand_metaphone = safe_phonetic(phonetics.metaphone, candidate)

    hits: dict[str, list[str]] = {
        "exact": [],
        "normalized": [],
        "soundex": [],
        "metaphone": [],
        "levenshtein_le2": [],
    }

    for k in known:
        k_norm = normalize(k)

        # Layer 1: exact (case-insensitive)
        if candidate.lower() == k.lower():
            hits["exact"].append(k)

        # Layer 2: normalized
        if cand_norm == k_norm and candidate.lower() != k.lower():
            hits["normalized"].append(k)

        # Layer 3: Soundex (ASCII-stripped lowercase via safe_phonetic)
        k_soundex = safe_phonetic(phonetics.soundex, k)
        if cand_soundex and k_soundex and cand_soundex == k_soundex:
            hits["soundex"].append(f"{k} (sndx={k_soundex})")

        # Layer 4: Metaphone (same handling)
        k_metaphone = safe_phonetic(phonetics.metaphone, k)
        if cand_metaphone and k_metaphone and cand_metaphone == k_metaphone:
            hits["metaphone"].append(f"{k} (mph={k_metaphone})")

        # Layer 5: Levenshtein ≤ 2 (on normalized forms)
        dist = Levenshtein.distance(cand_norm, k_norm)
        if 0 < dist <= 2:
            hits["levenshtein_le2"].append(f"{k} (d={dist})")

    # Overall verdict
    any_fire = any(v for v in hits.values())
    verdict = "REJECT" if any_fire else "ACCEPT"

    return {
        "candidate": candidate,
        "normalized": cand_norm,
        "soundex": cand_soundex,
        "metaphone": cand_metaphone,
        "verdict": verdict,
        "hits": hits,
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--candidates", nargs="*", default=[])
    p.add_argument("--candidates-file", type=str)
    p.add_argument("--out", type=str, help="optional JSON output path")
    p.add_argument("--quiet", action="store_true")
    p.add_argument(
        "--exclude-liturgy",
        type=str,
        help=(
            "Skip this liturgy's frontmatter when computing collisions. Use for "
            "denamed-control audits where parent-collisions are intended by design."
        ),
    )
    args = p.parse_args()

    candidates: list[str] = list(args.candidates)
    if args.candidates_file:
        for line in Path(args.candidates_file).read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                candidates.append(line)

    if not candidates:
        sys.exit("no candidates given (use --candidates or --candidates-file)")

    known = collect_known_names(exclude_liturgy=args.exclude_liturgy)
    if not args.quiet:
        excl_msg = (
            f" (excluding parent '{args.exclude_liturgy}')"
            if args.exclude_liturgy
            else ""
        )
        print(
            f"[audit] {len(known)} known names loaded from liturgies + registries{excl_msg}"
        )
        print(f"[audit] auditing {len(candidates)} candidate names")
        print()

    results: list[dict] = []
    accepted = 0
    rejected = 0
    for c in candidates:
        r = audit(c, known)
        results.append(r)
        if r["verdict"] == "ACCEPT":
            accepted += 1
            if not args.quiet:
                print(f"  ACCEPT  {c}  (sndx={r['soundex']}, mph={r['metaphone']})")
        else:
            rejected += 1
            if not args.quiet:
                print(f"  REJECT  {c}")
                for layer, fires in r["hits"].items():
                    if fires:
                        print(
                            f"          {layer}: {', '.join(fires[:3])}{'...' if len(fires) > 3 else ''}"
                        )

    if not args.quiet:
        print()
        print(f"[audit] {accepted} accepted, {rejected} rejected")

    if args.out:
        Path(args.out).write_text(json.dumps(results, indent=2))
        if not args.quiet:
            print(f"[audit] wrote {args.out}")


if __name__ == "__main__":
    main()
