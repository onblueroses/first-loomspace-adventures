#!/usr/bin/env python3
"""Count substitute-name occurrences per cell for denamed + nonsense controls.

Parses substitution tables from control liturgy frontmatter notes, then greps
each cell's completions for those substitute names. Reports per-completion
substitute yield alongside the parent-lexicon yield from measurements.json.
"""

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LITURGIES = REPO / "liturgies"
SUBST_LINE = re.compile(
    r"^\s*([A-Za-zÔÊÂÎÛôêâîû'\-]+(?:\s+[A-Za-zÔÊÂÎÛôêâîû'\-]+)*)\s+(?:→|->)\s+([A-Za-zÔÊÂÎÛôêâîû'\-]+(?:\s+[A-Za-zÔÊÂÎÛôêâîû'\-]+)*)",
    re.MULTILINE,
)


def parse_substitutes(liturgy_path: Path) -> list[str]:
    """Extract substitute (right-side) names from a control's frontmatter notes."""
    text = liturgy_path.read_text()
    # Cut to frontmatter (between --- markers)
    parts = text.split("---", 2)
    fm = parts[1] if len(parts) >= 3 else ""
    substitutes = []
    for line in fm.splitlines():
        m = re.match(
            r"^\s*[A-Za-zÔÊÂÎÛôêâîû'\-]+(?:\s+[A-Za-zÔÊÂÎÛôêâîû'\-]+)*\s+(?:→|->)\s+([A-Za-zÔÊÂÎÛôêâîû'\-]+(?:\s+[A-Za-zÔÊÂÎÛôêâîû'\-]+)*)\s*(?:\(.*\))?\s*$",
            line,
        )
        if m:
            sub = m.group(1).strip()
            # filter parenthetical-only matches and the English phrase
            if not sub.startswith("(") and len(sub) >= 3:
                substitutes.append(sub)
    return substitutes


def count_in_cell(cell_dir: Path, substitutes: list[str]) -> dict:
    """Count whole-word substitute occurrences across all completion files in a cell.

    Word-boundary matching (re \\b) ensures `PLENDRO` is not counted inside
    `PLENDROKRELM` or `Plendrokt`. Substitutes are compiled longest-first to
    keep multi-word phrases (e.g. `Lominem Adventu`) intact.
    """
    counts = {s: 0 for s in substitutes}
    patterns = {
        s: re.compile(r"\b" + re.escape(s.lower()) + r"\b") for s in substitutes
    }
    total_completions = 0
    completions_with_any = 0
    if not cell_dir.exists():
        return {
            "counts": counts,
            "total_completions": 0,
            "completions_with_any": 0,
            "total_hits": 0,
        }
    for f in sorted(cell_dir.glob("*.txt")):
        text = f.read_text(encoding="utf-8", errors="replace").lower()
        total_completions += 1
        any_hit = False
        for s in substitutes:
            n = len(patterns[s].findall(text))
            counts[s] += n
            if n > 0:
                any_hit = True
        if any_hit:
            completions_with_any += 1
    return {
        "counts": counts,
        "total_completions": total_completions,
        "completions_with_any": completions_with_any,
        "total_hits": sum(counts.values()),
    }


CONTROLS = {
    "synthetic_litany_denamed": "synthetic_litany_denamed.md",
    "synthetic_litany_nonsense": "synthetic_litany_nonsense.md",
    "synthetic_cosmological_denamed": "synthetic_cosmological_denamed.md",
    "synthetic_cosmological_nonsense": "synthetic_cosmological_nonsense.md",
}
TAILS = ["visitor_at_door", "enters_room", "page_continues"]


def main():
    runs = sys.argv[1:] or [
        str(REPO / "results/plasticity-2026-06-01-deepseek"),
        str(REPO / "results/plasticity-2026-06-01-hermes"),
    ]
    for run_str in runs:
        run = Path(run_str)
        print(f"\n=== {run.name} ===")
        result = {"run": run.name, "cells": {}}
        for control, fname in CONTROLS.items():
            subs = parse_substitutes(LITURGIES / fname)
            for tail in TAILS:
                cell_dir = run / "completions" / control / tail
                stats = count_in_cell(cell_dir, subs)
                cell_key = f"{control}/{tail}"
                n = stats["total_completions"] or 1
                yield_per_comp = stats["total_hits"] / n
                pct_with_hit = stats["completions_with_any"] / n
                top_hits = sorted(stats["counts"].items(), key=lambda kv: -kv[1])[:5]
                result["cells"][cell_key] = {
                    "n_substitutes": len(subs),
                    "n_completions": stats["total_completions"],
                    "completions_with_any_substitute": stats["completions_with_any"],
                    "total_substitute_hits": stats["total_hits"],
                    "substitute_yield_per_completion": round(yield_per_comp, 4),
                    "fraction_completions_with_any": round(pct_with_hit, 4),
                    "top_5_substitute_hits": [
                        {"name": k, "count": v} for k, v in top_hits
                    ],
                }
                print(
                    f"  {cell_key:60s}  yield/comp={yield_per_comp:7.3f}  pct_any={pct_with_hit * 100:5.1f}%  top: {top_hits[:3]}"
                )
        out_path = run / "substitute_yield.json"
        out_path.write_text(json.dumps(result, indent=2))
        print(f"  -> {out_path}")


if __name__ == "__main__":
    main()
