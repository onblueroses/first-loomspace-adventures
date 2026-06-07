"""
Liturgy-as-code measurement.

Reads a results/<timestamp>/ directory produced by runner.py and computes:
  M3 — Named-entity yield (the headline statistic)
  M2 — Lexical drift between conditions

Writes results/<timestamp>/measurements.json and results/<timestamp>/report.md.

Usage:
    python src/measure.py results/2026-05-30T10-44-31
    python src/measure.py --latest                  # use most recent run
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
LITURGIES_DIR = REPO_ROOT / "liturgies"
RESULTS_DIR = REPO_ROOT / "results"


# ---------- Loading ----------


def parse_md_with_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text()
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    return yaml.safe_load(text[4:end]) or {}, text[end + 5 :].strip()


@dataclass
class LiturgyMeta:
    id: str
    source: str
    control_strategy: str | None
    control_for: str | None
    named_entities: list[str]
    ambiguous_entities: list[str]
    related_vocabulary: list[str]
    ambiguous_vocabulary: list[str]


def _dedup(items: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for x in items:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def load_liturgy_meta(liturgy_id: str) -> LiturgyMeta:
    path = LITURGIES_DIR / f"{liturgy_id}.md"
    fm, _ = parse_md_with_frontmatter(path)
    named_entities = [s.lower() for s in (fm.get("named_entities") or [])]
    related_vocabulary = [s.lower() for s in (fm.get("related_vocabulary") or [])]
    # Dedup across the two headline tiers so a term listed in both is not counted twice
    overlap = set(named_entities) & set(related_vocabulary)
    related_vocabulary = [v for v in related_vocabulary if v not in overlap]
    return LiturgyMeta(
        id=fm.get("id", liturgy_id),
        source=fm.get("source", "unknown"),
        control_strategy=fm.get("control_strategy"),
        control_for=fm.get("control_for"),
        named_entities=_dedup(named_entities),
        ambiguous_entities=_dedup(
            [s.lower() for s in (fm.get("ambiguous_entities") or [])]
        ),
        related_vocabulary=_dedup(related_vocabulary),
        ambiguous_vocabulary=_dedup(
            [s.lower() for s in (fm.get("ambiguous_vocabulary") or [])]
        ),
    )


CONTROL_STRATEGY_ROLE = {
    "phonetic-shift": "L_denamed",
    "hard-nonsense": "L_nonsense",
    "length-matched-random": "L_random",
    "empty": "L_empty",
}


def classify_conditions(conditions: list[str]) -> dict[str, str]:
    """Map condition ids to roles: L_real / L_denamed / L_nonsense / L_random / L_empty.

    The L_real for a batch is the non-control liturgy. Controls are identified by
    their `control_strategy` frontmatter field.
    """
    roles: dict[str, str] = {}
    for cond in conditions:
        meta = load_liturgy_meta(cond)
        if meta.source != "control":
            roles[cond] = "L_real"
        elif meta.control_strategy in CONTROL_STRATEGY_ROLE:
            roles[cond] = CONTROL_STRATEGY_ROLE[meta.control_strategy]
        else:
            roles[cond] = f"L_other:{cond}"
    return roles


# ---------- Tokenization ----------


WORD_RE = re.compile(r"[a-zA-ZāĀēĒīĪōŌūŪäöüÄÖÜßçÇñÑ\u0370-\u03FF\u0590-\u05FF]+")


def tokenize(text: str) -> list[str]:
    return [t.lower() for t in WORD_RE.findall(text)]


def compile_phrase_pattern(phrase: str) -> re.Pattern:
    """Whole-word, case-insensitive match for a (possibly multi-word) phrase."""
    return re.compile(r"\b" + re.escape(phrase) + r"\b", re.IGNORECASE)


# ---------- Per-cell aggregation ----------


@dataclass
class CellStats:
    condition: str
    tail: str
    n_completions: int
    total_tokens: int
    token_counter: Counter
    named_entity_hits: dict[str, int]
    related_vocab_hits: dict[str, int]
    ambiguous_entity_hits: dict[str, int]
    ambiguous_vocab_hits: dict[str, int]
    # Per-completion headline-yield counts (one int per .txt file). Drives bootstrap CIs.
    per_completion_yields: list[int] = field(default_factory=list)

    @property
    def headline_yield(self) -> int:
        return sum(self.named_entity_hits.values()) + sum(
            self.related_vocab_hits.values()
        )

    @property
    def headline_per_completion(self) -> float:
        return self.headline_yield / max(self.n_completions, 1)


def aggregate_cell(
    cell_dir: Path,
    condition: str,
    tail: str,
    lexicon: LiturgyMeta,
) -> CellStats:
    completions = sorted(cell_dir.glob("*.txt"))
    full_text_parts: list[str] = []
    token_counter: Counter = Counter()
    ne_hits = {e: 0 for e in lexicon.named_entities}
    rv_hits = {v: 0 for v in lexicon.related_vocabulary}
    ae_hits = {e: 0 for e in lexicon.ambiguous_entities}
    av_hits = {v: 0 for v in lexicon.ambiguous_vocabulary}
    per_completion_yields: list[int] = []

    # Compile headline-lexicon patterns once for per-completion scoring.
    ne_patterns = [compile_phrase_pattern(e) for e in lexicon.named_entities]
    rv_patterns = [compile_phrase_pattern(v) for v in lexicon.related_vocabulary]

    for cpath in completions:
        text = cpath.read_text()
        full_text_parts.append(text)
        token_counter.update(tokenize(text))
        # Per-completion headline yield = sum of NE-hits + RV-hits in THIS completion.
        per_completion_yields.append(
            sum(len(p.findall(text)) for p in ne_patterns)
            + sum(len(p.findall(text)) for p in rv_patterns)
        )

    full_text = "\n".join(full_text_parts)
    for e in lexicon.named_entities:
        ne_hits[e] = len(compile_phrase_pattern(e).findall(full_text))
    for v in lexicon.related_vocabulary:
        rv_hits[v] = len(compile_phrase_pattern(v).findall(full_text))
    for e in lexicon.ambiguous_entities:
        ae_hits[e] = len(compile_phrase_pattern(e).findall(full_text))
    for v in lexicon.ambiguous_vocabulary:
        av_hits[v] = len(compile_phrase_pattern(v).findall(full_text))

    return CellStats(
        condition=condition,
        tail=tail,
        n_completions=len(completions),
        total_tokens=sum(token_counter.values()),
        token_counter=token_counter,
        named_entity_hits=ne_hits,
        related_vocab_hits=rv_hits,
        ambiguous_entity_hits=ae_hits,
        ambiguous_vocab_hits=av_hits,
        per_completion_yields=per_completion_yields,
    )


# ---------- Pairwise comparisons ----------


def lexical_divergence(
    a: Counter,
    b: Counter,
    a_total: int,
    b_total: int,
    top_k: int = 20,
) -> list[tuple[str, int, int, float]]:
    """Top words by frequency-normalized log ratio between two token counters.

    Computes per-token frequencies (with +1 raw-count smoothing in the numerator
    and +1/total in the denominator) so longer-corpus cells don't inflate ordinary
    words artificially.

    Restricted to words appearing ≥3 times across the two cells combined.
    Returns list of (word, a_count, b_count, log_freq_ratio) sorted by absolute
    log ratio descending.
    """
    a_denom = max(a_total, 1)
    b_denom = max(b_total, 1)
    all_words = set(a) | set(b)
    rows: list[tuple[str, int, int, float]] = []
    for w in all_words:
        ac, bc = a.get(w, 0), b.get(w, 0)
        if ac + bc < 3:
            continue
        a_freq = (ac + 1) / a_denom
        b_freq = (bc + 1) / b_denom
        log_ratio = math.log(a_freq / b_freq)
        rows.append((w, ac, bc, log_ratio))
    rows.sort(key=lambda r: abs(r[3]), reverse=True)
    return rows[:top_k]


def rate_ratio(
    real_hits: int, real_n: int, ctrl_hits: int, ctrl_n: int
) -> tuple[float, float, float, float]:
    """Compute per-completion rate ratio (real_rate / ctrl_rate) with smoothing.

    Returns (real_rate, ctrl_rate, ratio, log_ratio). Per-completion rates make
    the comparison invariant to incomplete cells (some calls failed) and to
    different n across cells.
    """
    real_rate = (real_hits + 1) / (max(real_n, 1) + 1)
    ctrl_rate = (ctrl_hits + 1) / (max(ctrl_n, 1) + 1)
    ratio = real_rate / ctrl_rate
    return real_rate, ctrl_rate, ratio, math.log(ratio)


def bootstrap_rate_ratio_ci(
    real_yields: list[int],
    ctrl_yields: list[int],
    *,
    n_resamples: int = 2000,
    rng_seed: int = 42,
    ci: float = 0.95,
) -> tuple[float, float, float]:
    """Bootstrap 95% CI on the per-completion rate ratio.

    Resamples each cell's per-completion yields with replacement, computes
    smoothed (+1/N+1) rates, then the ratio. Returns (point_estimate, ci_low,
    ci_high) and the fraction of bootstrap iterations where ratio ≤ 1 (effectively
    a one-sided p-value for "L_real not greater than control").

    Smoothing: +1 in numerator, /(N+1) in denominator, applied to each bootstrap
    sample to handle cells with zero yield without log-of-zero.
    """
    import random

    if not real_yields or not ctrl_yields:
        return 0.0, 0.0, 0.0
    real_n = len(real_yields)
    ctrl_n = len(ctrl_yields)
    point_rate_real = (sum(real_yields) + 1) / (real_n + 1)
    point_rate_ctrl = (sum(ctrl_yields) + 1) / (ctrl_n + 1)
    point_ratio = point_rate_real / point_rate_ctrl

    rng = random.Random(rng_seed)
    ratios: list[float] = []
    for _ in range(n_resamples):
        r_sample = [rng.choice(real_yields) for _ in range(real_n)]
        c_sample = [rng.choice(ctrl_yields) for _ in range(ctrl_n)]
        r_rate = (sum(r_sample) + 1) / (real_n + 1)
        c_rate = (sum(c_sample) + 1) / (ctrl_n + 1)
        ratios.append(r_rate / c_rate)
    ratios.sort()
    alpha = (1 - ci) / 2
    lo_idx = int(alpha * n_resamples)
    hi_idx = int((1 - alpha) * n_resamples) - 1
    return point_ratio, ratios[lo_idx], ratios[hi_idx]


def interpret_ratio(log_ratio: float) -> str:
    if log_ratio >= math.log(2):
        return "positive evidence"
    if log_ratio <= -math.log(2):
        return "negative direction (unexpected)"
    return "null (within 2× either direction)"


# ---------- Main ----------


def measure(run_dir: Path) -> dict[str, Any]:
    config = yaml.safe_load((run_dir / "config.yaml").read_text())
    if config.get("dry_run"):
        sys.exit("config indicates a dry run; nothing to measure")
    conditions = config["liturgies"]
    tails = config["tails"]
    expected_n = int(config.get("n_per_cell", 0))

    roles = classify_conditions(conditions)
    metas = {cond: load_liturgy_meta(cond) for cond in conditions}

    # Group controls by their `control_for` so a control built for one liturgy
    # is never silently compared against a different L_real. L_empty is a
    # universal control (no control_for); it pairs with every L_real in the run.
    real_ids = [c for c, r in roles.items() if r == "L_real"]
    if not real_ids:
        sys.exit("no L_real (non-control) liturgy in this run")
    groups: dict[str, list[str]] = {rid: [] for rid in real_ids}
    unmatched_controls: list[str] = []
    for cond in conditions:
        role = roles[cond]
        if role == "L_real":
            continue
        if role == "L_empty":
            for rid in real_ids:
                groups[rid].append(cond)
            continue
        cf = metas[cond].control_for
        if cf in groups:
            groups[cf].append(cond)
        else:
            unmatched_controls.append(cond)

    completions_root = run_dir / "completions"
    cells: dict[str, CellStats] = {}
    cell_warnings: list[str] = []
    # Aggregate every (cond × tail) cell using its OWN source-lexicon group.
    for rid, ctrls in groups.items():
        lexicon = load_liturgy_meta(rid)
        for cond in [rid, *ctrls]:
            for tail in tails:
                key = f"{cond}/{tail}"
                if key in cells:
                    continue  # L_empty paired with multiple groups; aggregate once
                cell_dir = completions_root / cond / tail
                if not cell_dir.exists():
                    continue
                stats = aggregate_cell(cell_dir, cond, tail, lexicon)
                cells[key] = stats
                if expected_n and stats.n_completions < int(expected_n * 0.8):
                    cell_warnings.append(
                        f"{key}: {stats.n_completions}/{expected_n} completions"
                        f" (<80%) — yield ratios derate this cell"
                    )

    out: dict[str, Any] = {
        "run_id": config["run_id"],
        "model": config["model"],
        "n_per_cell": expected_n,
        "source_liturgies": real_ids,
        "groups": {rid: ctrls for rid, ctrls in groups.items()},
        "unmatched_controls": unmatched_controls,
        "roles": roles,
        "cells": {},
        "comparisons": {},
        "warnings": cell_warnings,
    }

    for key, c in cells.items():
        out["cells"][key] = {
            "condition": c.condition,
            "role": roles.get(c.condition, "?"),
            "tail": c.tail,
            "n_completions": c.n_completions,
            "total_tokens": c.total_tokens,
            "headline_yield": c.headline_yield,
            "headline_per_completion": round(c.headline_per_completion, 3),
            "named_entity_total": sum(c.named_entity_hits.values()),
            "related_vocab_total": sum(c.related_vocab_hits.values()),
            "ambiguous_entity_total": sum(c.ambiguous_entity_hits.values()),
            "ambiguous_vocab_total": sum(c.ambiguous_vocab_hits.values()),
            "top_named_entities": dict(
                sorted(
                    {k: v for k, v in c.named_entity_hits.items() if v > 0}.items(),
                    key=lambda kv: -kv[1],
                )[:10]
            ),
            "top_related_vocabulary": dict(
                sorted(
                    {k: v for k, v in c.related_vocab_hits.items() if v > 0}.items(),
                    key=lambda kv: -kv[1],
                )[:10]
            ),
        }

    # Pairwise rate-based comparisons within each (source liturgy) group, per tail.
    for rid, ctrls in groups.items():
        for tail in tails:
            real_key = f"{rid}/{tail}"
            if real_key not in cells:
                continue
            real_cell = cells[real_key]
            for cond in ctrls:
                ctrl_key = f"{cond}/{tail}"
                if ctrl_key not in cells:
                    continue
                ctrl_cell = cells[ctrl_key]
                real_rate, ctrl_rate, ratio, log_r = rate_ratio(
                    real_cell.headline_yield,
                    real_cell.n_completions,
                    ctrl_cell.headline_yield,
                    ctrl_cell.n_completions,
                )
                # Bootstrap 95% CI on the rate ratio (skip if cells < 5 completions
                # since CI would be meaningless).
                if real_cell.n_completions >= 5 and ctrl_cell.n_completions >= 5:
                    _, boot_lo, boot_hi = bootstrap_rate_ratio_ci(
                        real_cell.per_completion_yields,
                        ctrl_cell.per_completion_yields,
                    )
                else:
                    boot_lo, boot_hi = float("nan"), float("nan")
                comp_key = f"{rid}__{roles[cond]}__{tail}"
                out["comparisons"][comp_key] = {
                    "tail": tail,
                    "real_id": rid,
                    "control_id": cond,
                    "control_role": roles[cond],
                    "real_yield": real_cell.headline_yield,
                    "real_n": real_cell.n_completions,
                    "real_rate": round(real_rate, 4),
                    "control_yield": ctrl_cell.headline_yield,
                    "control_n": ctrl_cell.n_completions,
                    "control_rate": round(ctrl_rate, 4),
                    "rate_ratio": round(ratio, 3),
                    "log_rate_ratio": round(log_r, 3),
                    "bootstrap_ratio_ci95_low": round(boot_lo, 3)
                    if not math.isnan(boot_lo)
                    else None,
                    "bootstrap_ratio_ci95_high": round(boot_hi, 3)
                    if not math.isnan(boot_hi)
                    else None,
                    "interpretation": interpret_ratio(log_r),
                    "top_lexical_divergence": [
                        {
                            "word": w,
                            "real_count": ac,
                            "control_count": bc,
                            "log_freq_ratio": round(lr, 3),
                        }
                        for (w, ac, bc, lr) in lexical_divergence(
                            real_cell.token_counter,
                            ctrl_cell.token_counter,
                            real_cell.total_tokens,
                            ctrl_cell.total_tokens,
                        )
                    ],
                }

    return out


def write_report(measurements: dict[str, Any], run_dir: Path) -> None:
    lines: list[str] = []
    lines.append(f"# Measurements: {measurements['run_id']}")
    lines.append("")
    lines.append(f"**Model:** `{measurements['model']}`")
    lines.append(f"**n per cell:** {measurements['n_per_cell']}")
    srcs = measurements.get("source_liturgies", [])
    lines.append(f"**Source liturgies (L_real):** {', '.join(f'`{s}`' for s in srcs)}")
    lines.append("")

    if measurements.get("warnings"):
        lines.append("> ⚠️  **Cell warnings:**")
        for w in measurements["warnings"]:
            lines.append(f"> - {w}")
        lines.append("")
    if measurements.get("unmatched_controls"):
        lines.append(
            "> ⚠️  **Unmatched controls (no `control_for` matching any L_real):**"
            f" {', '.join(f'`{c}`' for c in measurements['unmatched_controls'])}"
            " — excluded from comparisons."
        )
        lines.append("")

    lines.append("## Headline comparisons (per-completion rate ratios)")
    lines.append("")
    if not measurements["comparisons"]:
        lines.append("*(no comparisons computed)*")
    else:
        lines.append(
            "| Source | Comparison | tail | L_real rate | Control rate | Rate ratio | 95% CI | Interpretation |"
        )
        lines.append("|---|---|---|---:|---:|---:|---:|---|")
        for key, comp in measurements["comparisons"].items():
            ci_lo = comp.get("bootstrap_ratio_ci95_low")
            ci_hi = comp.get("bootstrap_ratio_ci95_high")
            ci_str = (
                f"[{ci_lo}, {ci_hi}]"
                if ci_lo is not None and ci_hi is not None
                else "—"
            )
            lines.append(
                f"| `{comp['real_id']}` | {comp['control_role']} (`{comp['control_id']}`) "
                f"| {comp['tail']} "
                f"| {comp['real_rate']} ({comp['real_yield']}/{comp['real_n']}) "
                f"| {comp['control_rate']} ({comp['control_yield']}/{comp['control_n']}) "
                f"| {comp['rate_ratio']}× "
                f"| {ci_str} "
                f"| {comp['interpretation']} |"
            )
    lines.append("")

    lines.append("## Per-cell")
    lines.append("")
    lines.append(
        "| Cell | Role | n | Tokens | Headline yield | /completion | NE | RV | Amb-NE | Amb-RV |"
    )
    lines.append("|---|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    for key, cell in measurements["cells"].items():
        lines.append(
            f"| `{key}` | {cell['role']} | {cell['n_completions']} | {cell['total_tokens']} "
            f"| {cell['headline_yield']} | {cell['headline_per_completion']} "
            f"| {cell['named_entity_total']} | {cell['related_vocab_total']} "
            f"| {cell['ambiguous_entity_total']} | {cell['ambiguous_vocab_total']} |"
        )
    lines.append("")

    lines.append("## Top entity hits per cell")
    lines.append("")
    for key, cell in measurements["cells"].items():
        if not cell["top_named_entities"] and not cell["top_related_vocabulary"]:
            continue
        lines.append(f"### `{key}` ({cell['role']})")
        if cell["top_named_entities"]:
            lines.append("Named entities:")
            for ent, count in cell["top_named_entities"].items():
                lines.append(f"  - `{ent}` × {count}")
        if cell["top_related_vocabulary"]:
            lines.append("Related vocabulary:")
            for v, count in cell["top_related_vocabulary"].items():
                lines.append(f"  - `{v}` × {count}")
        lines.append("")

    if measurements["comparisons"]:
        lines.append("## Top lexical divergence per comparison")
        lines.append("")
        for key, comp in measurements["comparisons"].items():
            lines.append(
                f"### vs {comp['control_role']} (`{comp['control_id']}`), tail `{comp['tail']}`"
            )
            lines.append("| Word | L_real | Control | log freq ratio |")
            lines.append("|---|---:|---:|---:|")
            for row in comp["top_lexical_divergence"][:15]:
                lines.append(
                    f"| `{row['word']}` | {row['real_count']} | {row['control_count']} "
                    f"| {row['log_freq_ratio']:+} |"
                )
            lines.append("")

    lines.append("## Caveats")
    lines.append("")
    n = measurements["n_per_cell"]
    if n < 50:
        lines.append(
            f"- n={n} is below the minimum for statistical claims. This is a "
            "smoke/exploratory measurement; scale to n=200 for the headline run."
        )
    lines.append("- Headline yield counts whole-word, case-insensitive matches.")
    lines.append(
        "- Ambiguous-tier counts (`Amb-NE`, `Amb-RV`) are tracked but NOT in the headline "
        "(common words ⇒ baseline false positives)."
    )
    lines.append(
        "- Pairwise comparisons computed per tail. Confidence intervals not yet "
        "computed — defer to bootstrap when scaling beyond smoke."
    )

    (run_dir / "report.md").write_text("\n".join(lines))


def main() -> None:
    p = argparse.ArgumentParser(description="Compute measurements over a results dir.")
    p.add_argument("run_dir", nargs="?", help="Path to results/<timestamp>/")
    p.add_argument("--latest", action="store_true", help="Use the most recent run dir")
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

    if not (run_dir / "config.yaml").exists():
        sys.exit(f"no config.yaml in {run_dir}")
    if not (run_dir / "completions").exists():
        sys.exit(f"no completions/ in {run_dir} — was --dry-run used?")

    measurements = measure(run_dir)
    (run_dir / "measurements.json").write_text(json.dumps(measurements, indent=2))
    write_report(measurements, run_dir)

    print(f"[measure] wrote {run_dir / 'measurements.json'}")
    print(f"[measure] wrote {run_dir / 'report.md'}")
    if measurements.get("warnings"):
        print()
        for w in measurements["warnings"]:
            print(f"[warn] {w}")
    print()
    print("=== Headline (per-completion rate ratios) ===")
    for key, comp in measurements["comparisons"].items():
        ci_lo = comp.get("bootstrap_ratio_ci95_low")
        ci_hi = comp.get("bootstrap_ratio_ci95_high")
        ci_str = (
            f" CI=[{ci_lo:.2f}, {ci_hi:.2f}]"
            if ci_lo is not None and ci_hi is not None
            else ""
        )
        print(
            f"  [{comp['real_id']}] {comp['control_role']:12s} ({comp['tail']}) "
            f"real={comp['real_rate']:.3f} ({comp['real_yield']}/{comp['real_n']})  "
            f"ctrl={comp['control_rate']:.3f} ({comp['control_yield']}/{comp['control_n']})  "
            f"ratio={comp['rate_ratio']:5.2f}×{ci_str}  "
            f"→ {comp['interpretation']}"
        )


if __name__ == "__main__":
    main()
