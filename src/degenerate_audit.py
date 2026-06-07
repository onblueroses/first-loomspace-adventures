#!/usr/bin/env python3
"""Phase 5.1.5 degenerate-completion audit per Decision #19.
Counts completions per cell that are (a) <50 chars OR (b) match refusal regex.
Emits results/<run-id>/degenerate_audit.json.
"""

import json
import re
import sys
from pathlib import Path

REFUSAL_RE = re.compile(
    r"^(I cannot|I'm not able|I apologize|As an AI|I'm an AI)", re.IGNORECASE
)


def audit(run_dir: Path) -> dict:
    completions = run_dir / "completions"
    out = {
        "run_id": run_dir.name,
        "cells": {},
        "totals": {"completions": 0, "short": 0, "refusal": 0, "valid": 0},
    }
    for liturgy in sorted(completions.iterdir()):
        if not liturgy.is_dir():
            continue
        for tail in sorted(liturgy.iterdir()):
            if not tail.is_dir():
                continue
            cell_key = f"{liturgy.name}/{tail.name}"
            total = short = refusal = degenerate_files = 0
            for f in sorted(tail.glob("*.txt")):
                text = f.read_text(encoding="utf-8", errors="replace").strip()
                total += 1
                is_short = len(text) < 50
                is_refusal = bool(REFUSAL_RE.match(text))
                if is_short:
                    short += 1
                if is_refusal:
                    refusal += 1
                # Decision #19: degenerate = short OR refusal (union, not sum)
                if is_short or is_refusal:
                    degenerate_files += 1
            valid = total - degenerate_files
            out["cells"][cell_key] = {
                "total": total,
                "short": short,
                "refusal": refusal,
                "degenerate_files": degenerate_files,
                "valid": valid,
            }
            out["totals"]["completions"] += total
            out["totals"]["short"] += short
            out["totals"]["refusal"] += refusal
            out["totals"]["valid"] += valid
    return out


if __name__ == "__main__":
    for run_dir_str in sys.argv[1:]:
        run_dir = Path(run_dir_str).resolve()
        result = audit(run_dir)
        out_path = run_dir / "degenerate_audit.json"
        out_path.write_text(json.dumps(result, indent=2))
        print(
            f"[degenerate] {run_dir.name}: total={result['totals']['completions']} short={result['totals']['short']} refusal={result['totals']['refusal']} valid={result['totals']['valid']}"
        )
        # surface non-zero cells
        for k, v in result["cells"].items():
            if v["short"] + v["refusal"] > 0:
                print(
                    f"  {k}: short={v['short']} refusal={v['refusal']} valid={v['valid']}/{v['total']}"
                )
