"""
Cross-model / cross-run synthesis for liturgy-as-code.

Reads measurements.json (+ optional register_ratings.json) from multiple run_dirs
and produces a unified side-by-side report comparing them. Useful for collating
DeepSeek + Hermes (or any pair/set of model headline runs) into one document.

Usage:
    python src/synthesize.py results/headline-2026-05-30-deepseek results/headline-2026-05-30-hermes
    python src/synthesize.py --out synthesis.md run_dir_a run_dir_b ...
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parent.parent


def load_run(run_dir: Path) -> dict[str, Any]:
    m_path = run_dir / "measurements.json"
    if not m_path.exists():
        sys.exit(f"missing {m_path} — run src/measure.py {run_dir} first")
    data = {"measurements": json.loads(m_path.read_text())}
    r_path = run_dir / "register_ratings.json"
    if r_path.exists():
        ratings = json.loads(r_path.read_text())
        # Aggregate to per-cell means
        by_cell: dict[str, list[dict]] = defaultdict(list)
        for key, r in ratings.items():
            if "_error" in r:
                continue
            parts = key.split("/")
            if len(parts) < 3:
                continue
            by_cell[f"{parts[0]}/{parts[1]}"].append(r)
        cell_means = {}
        for cell, rs in by_cell.items():
            n = len(rs)
            cell_means[cell] = {
                "n": n,
                "formality": round(sum(r["formality"] for r in rs) / n, 2),
                "archaism": round(sum(r["archaism"] for r in rs) / n, 2),
                "reverential": round(sum(r["reverential_register"] for r in rs) / n, 2),
                "pct_supernatural": round(
                    100 * sum(1 for r in rs if r["has_supernatural_imagery"]) / n,
                    1,
                ),
            }
        data["register"] = cell_means
    return data


def write_synthesis(runs: list[tuple[Path, dict[str, Any]]], out_path: Path) -> None:
    lines: list[str] = []
    lines.append("# Cross-run synthesis")
    lines.append("")
    lines.append(f"Combined {len(runs)} run(s):")
    for d, data in runs:
        m = data["measurements"]
        lines.append(
            f"- `{d.name}` — model `{m['model']}`, n={m['n_per_cell']},"
            f" sources={', '.join(m.get('source_liturgies', []))}"
        )
    lines.append("")

    # --- Headline yield: side-by-side ---
    lines.append("## Headline comparisons (rate ratios with 95% CI, by model)")
    lines.append("")

    # Index: comp_key (source, role, tail) → {run_label: comp_dict}
    headline_index: dict[tuple[str, str, str], dict[str, dict]] = defaultdict(dict)
    for d, data in runs:
        for key, comp in data["measurements"]["comparisons"].items():
            sig = (comp["real_id"], comp["control_role"], comp["tail"])
            headline_index[sig][d.name] = comp

    run_labels = [d.name for d, _ in runs]
    header_cols = ["source", "control", "tail"]
    for lbl in run_labels:
        header_cols.append(f"{lbl} ratio")
        header_cols.append(f"{lbl} CI95")
    lines.append("| " + " | ".join(header_cols) + " |")
    lines.append("|" + "|".join(["---"] * len(header_cols)) + "|")
    for sig in sorted(headline_index.keys()):
        row = [f"`{sig[0]}`", sig[1], sig[2]]
        for lbl in run_labels:
            c = headline_index[sig].get(lbl)
            if c is None:
                row.append("—")
                row.append("—")
            else:
                row.append(f"{c['rate_ratio']}×")
                lo = c.get("bootstrap_ratio_ci95_low")
                hi = c.get("bootstrap_ratio_ci95_high")
                row.append(
                    f"[{lo}, {hi}]" if lo is not None and hi is not None else "—"
                )
        lines.append("| " + " | ".join(row) + " |")
    lines.append("")

    # Replication note: which comparisons agree (both positive) vs diverge
    if len(runs) >= 2:
        lines.append("### Replication summary")
        lines.append("")
        agree_pos = 0
        agree_neg_or_null = 0
        diverge = 0
        for sig, by_label in headline_index.items():
            if len(by_label) < 2:
                continue
            interps = [
                by_label[lbl]["interpretation"] for lbl in run_labels if lbl in by_label
            ]
            if all(i == "positive evidence" for i in interps):
                agree_pos += 1
            elif all(i == interps[0] for i in interps):
                agree_neg_or_null += 1
            else:
                diverge += 1
        total = agree_pos + agree_neg_or_null + diverge
        lines.append(
            f"- Agree (positive evidence in all runs): **{agree_pos}/{total}**"
        )
        lines.append(
            f"- Agree (same non-positive interpretation): {agree_neg_or_null}/{total}"
        )
        lines.append(f"- Diverge across runs: {diverge}/{total}")
        lines.append("")

    # --- Register classifier: side-by-side ---
    has_register = any("register" in data for _, data in runs)
    if has_register:
        lines.append("## Register classifier (per-cell means, by model)")
        lines.append("")
        cell_index: dict[str, dict[str, dict]] = defaultdict(dict)
        for d, data in runs:
            if "register" not in data:
                continue
            for cell, r in data["register"].items():
                cell_index[cell][d.name] = r

        header = ["cell"]
        for lbl in run_labels:
            header += [
                f"{lbl} form",
                f"{lbl} arch",
                f"{lbl} rev",
                f"{lbl} %super",
            ]
        lines.append("| " + " | ".join(header) + " |")
        lines.append("|" + "|".join(["---"] * len(header)) + "|")
        for cell in sorted(cell_index.keys()):
            row = [f"`{cell}`"]
            for lbl in run_labels:
                r = cell_index[cell].get(lbl)
                if r is None:
                    row += ["—", "—", "—", "—"]
                else:
                    row += [
                        str(r["formality"]),
                        str(r["archaism"]),
                        str(r["reverential"]),
                        f"{r['pct_supernatural']}%",
                    ]
            lines.append("| " + " | ".join(row) + " |")
        lines.append("")

    # --- Per-cell yield (selected) ---
    lines.append("## Per-cell headline yield (per-completion mean)")
    lines.append("")
    cell_yield_index: dict[str, dict[str, float]] = defaultdict(dict)
    cell_role_index: dict[str, str] = {}
    for d, data in runs:
        for cell_key, cell in data["measurements"]["cells"].items():
            cell_yield_index[cell_key][d.name] = cell["headline_per_completion"]
            cell_role_index[cell_key] = cell["role"]
    header = ["cell", "role"]
    for lbl in run_labels:
        header.append(f"{lbl} hits/comp")
    lines.append("| " + " | ".join(header) + " |")
    lines.append("|" + "|".join(["---"] * len(header)) + "|")
    for cell_key in sorted(cell_yield_index.keys()):
        row = [f"`{cell_key}`", cell_role_index[cell_key]]
        for lbl in run_labels:
            v = cell_yield_index[cell_key].get(lbl)
            row.append(str(v) if v is not None else "—")
        lines.append("| " + " | ".join(row) + " |")
    lines.append("")

    # Warnings
    all_warnings = []
    for d, data in runs:
        for w in data["measurements"].get("warnings", []):
            all_warnings.append(f"[{d.name}] {w}")
    if all_warnings:
        lines.append("## Warnings")
        lines.append("")
        for w in all_warnings:
            lines.append(f"- {w}")
        lines.append("")

    out_path.write_text("\n".join(lines))
    print(f"[synth] wrote {out_path}")


def main() -> None:
    p = argparse.ArgumentParser(description="Cross-run synthesis for liturgy-as-code.")
    p.add_argument("run_dirs", nargs="+", help="Two or more results/<id>/ directories")
    p.add_argument(
        "--out",
        type=str,
        default=None,
        help="Output path (default: <first_run_dir>/../synthesis-<n>runs.md)",
    )
    args = p.parse_args()

    runs: list[tuple[Path, dict[str, Any]]] = []
    for r in args.run_dirs:
        p_ = Path(r).resolve()
        if not p_.exists():
            sys.exit(f"missing: {p_}")
        runs.append((p_, load_run(p_)))

    if args.out:
        out_path = Path(args.out).resolve()
    else:
        out_path = runs[0][0].parent / f"synthesis-{len(runs)}runs.md"

    write_synthesis(runs, out_path)


if __name__ == "__main__":
    main()
