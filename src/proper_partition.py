#!/usr/bin/env python3
"""Substitute-aware partition recompute for plasticity-2026-06-01-{deepseek,hermes}.

The original `partition.md` used parent-lexicon-only yields, which made
form-charge under-count denamed/nonsense substitute-name production.

This script computes a substitute-AWARE partition:
  - floor               = L_random / L_empty                              (unchanged)
  - bootstrap-charge    = (L_denamed_parent + L_denamed_substitute) / L_random
                          (does the denamed prompt elicit any coherent name-set?)
  - preference-charge   = L_real / (L_denamed_parent + L_denamed_substitute)
                          (do REAL names get any advantage once any name-set is engaged?)

Also re-uses valid denominators from degenerate_audit.json (Decision #19).
Writes results/<run>/partition_proper.md.
"""

import json
import math
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SYNTHETICS = ["synthetic_litany", "synthetic_cosmological"]
TAILS = ["visitor_at_door", "enters_room", "page_continues"]
LAPLACE_EVENT = 1
LAPLACE_TRIAL = 1


def load_measurements(run: Path) -> dict:
    return json.loads((run / "measurements.json").read_text())


def load_substitutes(run: Path) -> dict:
    return json.loads((run / "substitute_yield.json").read_text())


def load_degenerate(run: Path) -> dict:
    return json.loads((run / "degenerate_audit.json").read_text())


def cell_rate(cells: dict, cell_key: str, denom: int) -> float:
    """Parent-lexicon yield per (valid) completion, Laplace-smoothed."""
    if cell_key not in cells:
        return LAPLACE_EVENT / max(1, denom + LAPLACE_TRIAL)
    c = cells[cell_key]
    yield_total = c.get("headline_yield", 0)
    return (yield_total + LAPLACE_EVENT) / max(1, denom + LAPLACE_TRIAL)


def sub_rate(subs: dict, cell_key: str, denom: int) -> float:
    """Substitute-name yield per (valid) completion, Laplace-smoothed."""
    if cell_key not in subs["cells"]:
        return 0.0
    hits = subs["cells"][cell_key]["total_substitute_hits"]
    return (hits + LAPLACE_EVENT) / max(1, denom + LAPLACE_TRIAL)


def total_n(cells: dict, cell_key: str) -> int:
    """Return total completion count for cell, matching the numerator's file scope.

    Using total (not valid-only) keeps numerator and denominator aligned: yields
    in measurements.json + substitute_yield.json are counted over ALL completion
    files, so the denominator must match. Valid-only denominators are reported
    in degenerate_audit.json as a transparency check, not folded back here —
    Codex flagged this in the first-draft `proper_partition.py` as a P1.
    """
    if cell_key in cells and "n_completions" in cells[cell_key]:
        return cells[cell_key]["n_completions"]
    return 200  # default


def analyze_run(run: Path) -> str:
    m = load_measurements(run)
    s = load_substitutes(run)
    cells = m.get("cells", {})

    out = []
    out.append(f"# Substitute-aware partition — {run.name}\n")
    out.append(
        "**Method**: combined denamed name-set yield (parent-lexicon + substitute-lexicon) replaces the previous form-charge denominator. Denominators are total completion counts from `measurements.json` (matching the numerator's file scope; valid-only denominators are reported separately in `degenerate_audit.json` as a transparency check, not folded into the partition). Laplace +1/+1 throughout.\n"
    )
    out.append("**Charges**:")
    out.append(
        "- `floor`            = L_random / L_empty                (does random prose elicit lexicon hits?)"
    )
    out.append(
        "- `bootstrap-charge` = (L_denamed_parent + L_denamed_substitute) / L_random  (does the denamed prompt elicit ANY coherent name-set continuation?)"
    )
    out.append(
        "- `preference-charge`= L_real / (L_denamed_parent + L_denamed_substitute)    (do REAL names beat substitutes once any name-set is engaged?)"
    )
    out.append("")
    out.append(
        "Identity (Laplace-smoothed): `log(L_real/L_empty) ≈ log(floor) + log(bootstrap-charge) + log(preference-charge)`"
    )
    out.append("Identity check column reports `log_lhs - log_rhs` (should be ≈ 0).")
    out.append("")

    for syn in SYNTHETICS:
        out.append(f"## {syn}\n")
        out.append(
            "| Tail | L_real | L_denamed (parent+sub) | L_random | L_empty | floor | bootstrap | preference | identity |"
        )
        out.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
        for tail in TAILS:
            real_key = f"{syn}/{tail}"
            den_key = f"{syn}_denamed/{tail}"
            rand_key = f"{syn}_random/{tail}"
            empty_key = f"empty/{tail}"

            # Use TOTAL completion counts as denominator — must match the
            # numerator's file scope (measurements.json + substitute_yield.json
            # both count over all completion files). Valid-only re-counting
            # is a follow-up; reported separately in degenerate_audit.json.
            n_real = total_n(cells, real_key)
            n_den = total_n(cells, den_key)
            n_rand = total_n(cells, rand_key)
            n_empty = total_n(cells, empty_key)

            real_rate = cell_rate(cells, real_key, n_real)
            den_parent = cell_rate(cells, den_key, n_den)
            den_sub = sub_rate(s, den_key, n_den)
            den_total = den_parent + den_sub
            rand_rate = cell_rate(cells, rand_key, n_rand)
            empty_rate = cell_rate(cells, empty_key, n_empty)

            floor = rand_rate / empty_rate
            bootstrap = den_total / rand_rate
            preference = real_rate / den_total
            lhs = math.log(real_rate / empty_rate)
            rhs = math.log(floor) + math.log(bootstrap) + math.log(preference)

            out.append(
                f"| {tail} | {real_rate:.3f} | {den_total:.3f} ({den_parent:.3f}+{den_sub:.3f}) | {rand_rate:.3f} | {empty_rate:.3f} | {floor:.2f} | {bootstrap:.2f} | {preference:.2f} | {lhs - rhs:+.3f} |"
            )
        out.append("")

    out.append("## Cross-tail / cross-form interpretation")
    out.append("")
    out.append(
        "- **preference-charge ≫ 1**: the model strongly prefers real synthetic names over the prompt's own substitutes — i.e. the specific name string carries weight beyond `[name-shaped-token-in-this-cosmological-form]`."
    )
    out.append(
        "- **preference-charge ≈ 1**: the model produces real names and substitutes at comparable per-completion rates — the form swallows the name distinction."
    )
    out.append(
        "- **preference-charge < 1**: the substitute-name continuation is MORE prolific than the real-name continuation (likely artifact: model picks up the prompt's planted substitutes more eagerly than parent names get reproduced)."
    )
    out.append(
        "- **bootstrap-charge ≫ 1**: the denamed/substitute prompt successfully bootstraps a name-set continuation — Lesson 9 plasticity at work."
    )
    out.append(
        "- **floor stays ≈ 1**: random/empty produce no lexicon hits — the controls remain silent (the partition base is clean)."
    )
    return "\n".join(out)


if __name__ == "__main__":
    runs = sys.argv[1:] or [
        str(REPO / "results/plasticity-2026-06-01-deepseek"),
        str(REPO / "results/plasticity-2026-06-01-hermes"),
    ]
    for r in runs:
        run = Path(r)
        report = analyze_run(run)
        out = run / "partition_proper.md"
        out.write_text(report)
        print(f"[partition] wrote {out}")
        print(report)
        print()
