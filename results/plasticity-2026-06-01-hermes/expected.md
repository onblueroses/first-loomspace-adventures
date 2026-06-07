# Pre-registration: Plasticity probe — Hermes

**Run id:** `plasticity-2026-06-01-hermes`
**Model:** `nousresearch/hermes-3-llama-3.1-405b` (id locked in `results/plasticity-env.json`, Decision #16)
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
- **Sampling:** temperature 0.7, top_p 0.95, max_tokens 256 (matches headline run)
- **Total cells:** 9 × 3 = 27
- **Total calls:** 5400

## Pilot evidence (n=20, visitor_at_door only)

| Cell | Yield | /completion |
|---|---:|---:|
| `synthetic_litany` (L_real) | 2 | 0.10 |
| `synthetic_litany_denamed` (L_denamed) | 0 | 0.00 |
| `synthetic_litany_nonsense` (L_nonsense) | 1 | 0.05 |
| `synthetic_litany_random` (L_random) | 1 | 0.05 |
| `synthetic_cosmological` (L_real) | 12 | 0.60 |
| `synthetic_cosmological_denamed` (L_denamed) | 0 | 0.00 |
| `synthetic_cosmological_nonsense` (L_nonsense) | 0 | 0.00 |
| `synthetic_cosmological_random` (L_random) | 0 | 0.00 |
| `empty` | 0 | 0.00 |

Pilot pattern: Hermes is **conservative** on emitting newly-invented synthetic names — yields are 10–80× lower than DeepSeek on the same prompts. Inverts the headline-run dichotomy (where Hermes-magician produced MORE entity yield on real ancient liturgies than DeepSeek-scholar). However, the lexical-divergence table shows Hermes substitutes **denamed forms with a substitute egregore at high rate**: `phengereb × 40` appears in synthetic_cosmological_denamed completions (a denamed substitute term, NOT in the parent lexicon — Lesson 9 plasticity, exactly as predicted).

This produces an asymmetric prediction: yields stay low across the board, but lexical-divergence shows the substitute-egregore signature.

## Headline predictions (18-entry numeric grid)

Bounds are per-tail per-charge per-synthetic. All ratios use Laplace-smoothed (+1 event, +1 trial-equivalent) rates.

### synthetic_litany

| Charge | visitor_at_door | enters_room | page_continues |
|---|---|---|---|
| **floor** = L_random/L_empty | 0.3 ≤ r ≤ 5.0 *(pilot n=20: 1/0 hints small positive)* | 0.3 ≤ r ≤ 5.0 *(extrapolated, Lesson 3)* | 0.3 ≤ r ≤ 5.0 *(extrapolated, Lesson 3)* |
| **form-charge** = L_denamed/L_random | 0.1 ≤ r ≤ 3.0 *(pilot n=20: 0/1)* | 0.1 ≤ r ≤ 3.0 *(extrapolated)* | 0.1 ≤ r ≤ 3.0 *(extrapolated)* |
| **name-charge** = L_real/L_denamed | r ≥ 1.5 *(pilot n=20: 2/(0+1)=2, weak signal)* | r ≥ 1.0 *(extrapolated; might fail)* | r ≥ 0.7 *(extrapolated, page_continues drifts most)* |

### synthetic_cosmological

| Charge | visitor_at_door | enters_room | page_continues |
|---|---|---|---|
| **floor** = L_random/L_empty | 0.3 ≤ r ≤ 3.0 *(pilot n=20)* | 0.3 ≤ r ≤ 3.0 *(extrapolated, Lesson 3)* | 0.3 ≤ r ≤ 3.0 *(extrapolated, Lesson 3)* |
| **form-charge** = L_denamed/L_random | 0.3 ≤ r ≤ 5.0 *(pilot n=20)* | 0.3 ≤ r ≤ 5.0 *(extrapolated)* | 0.3 ≤ r ≤ 5.0 *(extrapolated)* |
| **name-charge** = L_real/L_denamed | r ≥ 4.0 *(pilot n=20: 12/(0+1)=12, lower 95% CI ≈ 4)* | r ≥ 2.0 *(extrapolated, Lesson 3)* | r ≥ 1.2 *(extrapolated)* |

## Lexical-divergence predictions (substitute-egregore signature, Hermes-specific)

The pilot's `synthetic_cosmological_denamed` cell produced `phengereb × 40` in 20 completions. **Predict at n=200 × 3 tails:**
- `phengereb` appears ≥ 200× total across the three `synthetic_cosmological_denamed` cells (substitute egregore for the original PHENGAREB)
- AT LEAST 2 other denamed substitutes (e.g., `vrokthemnarph`, `plendrokt`, `olephia`) appear ≥ 50× total across the three denamed cells
- The denamed substitute names DO NOT appear in `synthetic_cosmological` (real) completions (one-directional substitution — model picks substitutes when given the denamed prompt, doesn't backfill into the real prompt)

For `synthetic_litany_denamed`: predict at least 3 denamed substitute terms appear ≥ 20× total across the three cells.

## Falsifiers

The within-liturgy partition hypothesis is falsified (for this model, on these synthetics) if ANY of these hold at n=200:

1. **Name-charge collapse to floor:** `name-charge` < 1.0 on visitor_at_door for synthetic_cosmological — would mean real synthetic names produce NO advantage over denamed substitutes (Hermes treating substrates as fully equivalent).
2. **Substitute egregore absent:** `phengereb` appears < 30× total across the three `synthetic_cosmological_denamed` cells — would falsify the Lesson 9 plasticity pattern on this specific synthetic (the substitute mechanism would be a Hermes-on-real-corpora artifact, not generalizable).
3. **Partition identity violation:** the additivity `log(L_real/L_empty) ≠ log(floor) + log(form-charge) + log(name-charge)` (within numerical / Laplace tolerance ≤ 0.1) per tail.
4. **Cross-model agreement:** DeepSeek and Hermes within-liturgy partitions match within 1.5× on every charge × tail × synthetic cell — would suggest the partition is method-driven, not model-driven (collapsing the cross-model signal that justifies the probe).
5. **Inverse plasticity on litany:** synthetic_litany `name-charge` > 5.0 on any tail — would contradict the pilot's near-zero litany yield and suggest the pilot was a sampling fluke.

## Notes

- Pilot evidence for synthetic_litany is THIN (2 events in 20 calls). visitor_at_door predictions are correspondingly weak (r ≥ 1.5 only). enters_room is borderline and explicitly marked as possibly failing — that is itself useful data.
- Hermes's substitute-egregore signature is the most novel prediction: confirms Lesson 9 generalizes to synthetics, isolating the plasticity mechanism from any real-corpus prior.
- Bounds are wider than DeepSeek's because Hermes pilot yields are 10× lower (Laplace dominates the ratio statistics).
- This pre-reg is locked by SHA256 (Decision #17). Any edit will fail the Phase 4 pre-flight hash check.
