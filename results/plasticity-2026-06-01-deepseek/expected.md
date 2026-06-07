# Pre-registration: Plasticity probe — DeepSeek

**Run id:** `plasticity-2026-06-01-deepseek`
**Model:** `deepseek/deepseek-v3.2` (id locked in `results/plasticity-env.json`, Decision #16)
**Date written:** 2026-05-31 (before headline sampling)

## Disclosure

Predictions for the partition decomposition `log(L_real/L_empty) = log(floor) + log(form-charge) + log(name-charge)` (per Decision #11 of the project notes), evaluated on two fully-synthetic liturgies (`synthetic_litany`, `synthetic_cosmological`). Bounds informed by pilot (Decision #15). Falsifiers explicit. Hash-locked per Decision #17.

Charge definitions (per-completion entity-yield rate ratios, Laplace-smoothed (+1, +1) per cell):
- `floor` = L_random / L_empty
- `form-charge` = L_denamed / L_random
- `name-charge` = L_real / L_denamed

## Scope

- **Liturgies (9):** `synthetic_litany`, `synthetic_litany_denamed`, `synthetic_litany_nonsense`, `synthetic_litany_random`, `synthetic_cosmological`, `synthetic_cosmological_denamed`, `synthetic_cosmological_nonsense`, `synthetic_cosmological_random`, `empty`
- **Tails (3):** `visitor_at_door`, `enters_room`, `page_continues`
- **n per cell:** 200
- **Sampling:** temperature 0.7, top_p 0.95, max_tokens 256 (matches headline run for cross-comparability)
- **Total cells:** 9 × 3 = 27
- **Total calls:** 5400

## Pilot evidence (n=20, visitor_at_door only)

| Cell | Yield | /completion |
|---|---:|---:|
| `synthetic_litany` (L_real) | 162 | 8.10 |
| `synthetic_litany_denamed` (L_denamed) | 0 | 0.00 |
| `synthetic_litany_nonsense` (L_nonsense) | 0 | 0.00 |
| `synthetic_litany_random` (L_random) | 0 | 0.00 |
| `synthetic_cosmological` (L_real) | 83 | 4.15 |
| `synthetic_cosmological_denamed` (L_denamed) | 1 | 0.05 |
| `synthetic_cosmological_nonsense` (L_nonsense) | 0 | 0.00 |
| `synthetic_cosmological_random` (L_random) | 0 | 0.00 |
| `empty` | 0 | 0.00 |

Pilot pattern: DeepSeek emits planted synthetic names abundantly (every litany name hit 6× / 20 completions; major cosmological names selephimor × 14, phorbamenes × 12). Controls collapse near zero. The signal will be dominated by `name-charge`; `floor` and `form-charge` will hover at 1.0 (Laplace-smoothed ratio of two near-zero rates).

## Headline predictions (18-entry numeric grid)

Bounds are per-tail per-charge per-synthetic. All ratios use Laplace-smoothed (+1 event, +1 trial-equivalent) rates so 0/N denominators don't blow up.

### synthetic_litany

| Charge | visitor_at_door | enters_room | page_continues |
|---|---|---|---|
| **floor** = L_random/L_empty | 0.5 ≤ r ≤ 2.0 *(pilot n=20)* | 0.5 ≤ r ≤ 2.0 *(extrapolated, Lesson 3)* | 0.5 ≤ r ≤ 2.0 *(extrapolated, Lesson 3)* |
| **form-charge** = L_denamed/L_random | 0.5 ≤ r ≤ 3.0 *(pilot n=20)* | 0.5 ≤ r ≤ 3.0 *(extrapolated)* | 0.5 ≤ r ≤ 3.0 *(extrapolated)* |
| **name-charge** = L_real/L_denamed | r ≥ 15.0 *(pilot n=20: 162/(0+1)≈81, lower 95% CI ≈ 59)* | r ≥ 4.0 *(extrapolated, Lesson 3 down-scale)* | r ≥ 2.0 *(extrapolated, page_continues drifts most)* |

### synthetic_cosmological

| Charge | visitor_at_door | enters_room | page_continues |
|---|---|---|---|
| **floor** = L_random/L_empty | 0.5 ≤ r ≤ 2.0 *(pilot n=20)* | 0.5 ≤ r ≤ 2.0 *(extrapolated, Lesson 3)* | 0.5 ≤ r ≤ 2.0 *(extrapolated, Lesson 3)* |
| **form-charge** = L_denamed/L_random | 0.5 ≤ r ≤ 5.0 *(pilot n=20: 1/0 hints small positive)* | 0.5 ≤ r ≤ 5.0 *(extrapolated)* | 0.5 ≤ r ≤ 5.0 *(extrapolated)* |
| **name-charge** = L_real/L_denamed | r ≥ 8.0 *(pilot n=20: 83/(1+1)≈42, lower 95% CI ≈ 18)* | r ≥ 3.0 *(extrapolated, Lesson 3)* | r ≥ 1.5 *(extrapolated, page_continues drifts most)* |

## Lexical-divergence predictions (specific entities)

Pilot showed every synthetic_litany invented name hit 6× / 20 completions. **Predict** at n=200 × 3 tails: each of the 27 cascade names appears ≥ 30× total across the three real-litany cells.

For synthetic_cosmological, `selephimor` was the top hit (14 / 20). **Predict** `selephimor` ≥ 100× total across the three real cells; `phelonoptra` ≥ 30× total; `aphrybetesh` (a vox magicum) ≥ 40× total.

## Falsifiers

The within-liturgy partition hypothesis is falsified (for this model, on these synthetics) if ANY of these hold at n=200:

1. **Name-charge collapse:** `name-charge` < 2.0 on visitor_at_door for either synthetic — would mean the model treats invented denamed forms as fully equivalent to invented real names, contradicting the pilot's 162 vs 0 yield gap.
2. **Form-charge dominance:** `form-charge` > 5.0 for synthetic_litany OR > 8.0 for synthetic_cosmological on visitor_at_door — would mean the model substitutes denamed names for the real ones at a rate that competes with the real-name effect (Lesson 9 plasticity overshooting expectations on synthetics).
3. **Floor breakout:** `floor` > 3.0 or < 0.3 on visitor_at_door for either synthetic — would mean random prose is a much stronger or weaker entity-elicitor than empty, breaking the floor assumption.
4. **Partition identity violation:** the additivity `log(L_real/L_empty) ≠ log(floor) + log(form-charge) + log(name-charge)` (within numerical / Laplace tolerance ≤ 0.1) per tail — would indicate a measurement-pipeline bug.
5. **Cross-tail inversion:** `name-charge(visitor_at_door)` < `name-charge(page_continues)` for either synthetic — would contradict Lesson 3 (page_continues pulls toward scholar mode, lower yields).

## Notes

- Pilot evidence treats the visitor_at_door predictions as well-grounded; enters_room and page_continues use Lesson 3 down-scaling (~2× and ~4× lower yields respectively for the same prompt). Both are explicitly labeled `(extrapolated)`.
- Bounds are deliberately wide on floor/form-charge to permit pilot-statistical sparsity; deliberately tight on name-charge because the pilot signal is strong enough to commit.
- This pre-reg is locked by SHA256 (Decision #17). Any edit will fail the Phase 4 pre-flight hash check.
