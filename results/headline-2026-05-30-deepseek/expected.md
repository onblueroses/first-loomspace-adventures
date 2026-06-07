# Pre-registration: Headline run — DeepSeek

**Run id:** `headline-2026-05-30-deepseek`
**Model:** `deepseek/deepseek-v3.2`
**Date written:** 2026-05-30 (before sampling)

## Disclosure

These predictions are informed by the smoke-test results (results/2026-05-30T10-44-26 for Astrachios, results/2026-05-30T12-37-12 for Headless). The smoke established directional signal at n=20. This pre-registration commits to *what the headline run at n=200 × 3 tails should look like* given that initial signal — including which specific predictions would FALSIFY the egregore-weight hypothesis.

## Scope

- **Liturgies:** astrachios, astrachios_denamed, astrachios_nonsense, astrachios_random, headless, headless_denamed, headless_nonsense, headless_random, empty
- **Tails:** visitor_at_door, enters_room, page_continues
- **n per cell:** 200
- **Sampling:** temperature 0.7, top_p 0.95, max_tokens 256
- **Total cells:** 9 conditions × 3 tails = 27 cells
- **Total calls:** 5400

## Headline predictions

### Headline yield (rate ratios)

For each tradition (astrachios, headless) and each tail, the per-completion rate ratio L_real_vs_L_denamed is predicted to be **≥ 2.0×** with **lower 95% CI > 1.0**.

Stronger version: at least 4 of the 6 (tradition × tail) cells should show ratio ≥ 4.0×.

| Comparison | Predicted rate ratio |
|---|---|
| astrachios L_real_vs_L_denamed | ≥ 5× across all 3 tails |
| astrachios L_real_vs_L_nonsense | ≥ 5× across all 3 tails |
| astrachios L_real_vs_L_random | ≥ 10× across all 3 tails |
| astrachios L_real_vs_L_empty | ≥ 20× across all 3 tails |
| headless L_real_vs_L_denamed | ≥ 2× across all 3 tails (smaller gap; cosmological prose leaks) |
| headless L_real_vs_L_nonsense | ≥ 2× across all 3 tails |
| headless L_real_vs_L_random | ≥ 5× across all 3 tails |
| headless L_real_vs_L_empty | ≥ 10× across all 3 tails |

Predicted ordering (each tradition, each tail):
`L_real >  L_denamed > L_nonsense ≈ L_random > L_empty`
(with L_denamed > L_nonsense because grimoire-cadence with invented names still triggers SOME religious vocabulary, while obvious nonsense triggers fantasy-RPG register)

### Lexical-divergence predictions (specific entities)

The smoke showed L_real summons named entities that AREN'T in the prompt:
- For Astrachios: "raphael" appeared 16× in 20 L_real completions on `visitor_at_door`. **Predict:** raphael ≥ 80× in 200 L_real completions across the 3 tails combined, ≤ 10× in equivalent L_denamed.
- For Astrachios: "tetragrammaton" ≥ 20× in L_real across 3 tails (related_vocabulary hit), ≤ 5× in controls.
- For Headless: Hermes summoned ORO, IBAH, AOZPI, AGLA from corpus. DeepSeek smoke didn't show these as strongly. **Predict:** L_real for headless will produce ≥ 1 instance of {iao, sabaoth, agla} per 20 completions on average; controls produce ≤ 0.25 per 20.

### Register classifier predictions

DeepSeek smoke pattern (Astrachios): L_real ≈ L_denamed > L_nonsense on register.
Predict for headline: same pattern holds across all 3 tails for Astrachios.

For Headless: similar pattern but L_real should show modestly higher reverential_register than L_denamed (Headless has the explicit "I am the Headless Daimon" identification shift which the model may mirror only when given real PGM names).

Specific predictions (mean per cell, n=200):

| Cell | formality | archaism | reverential | %super |
|---|---|---|---|---|
| L_real (astrachios) | ≥ 4.2 | ≥ 3.3 | ≥ 4.0 | ≥ 95% |
| L_denamed (astrachios) | ≥ 4.2 | ≥ 3.5 | ≥ 3.8 | ≥ 95% |
| L_nonsense (astrachios) | ≤ 4.3 | ≤ 3.2 | ≤ 3.8 | ≤ 90% |
| L_random (astrachios) | ≤ 4.0 | ≤ 2.5 | ≤ 2.5 | ≤ 50% |
| L_empty | ≤ 3.5 | ≤ 2.5 | ≤ 2.5 | ≤ 50% |

## Falsifiers

The egregore-weight hypothesis is falsified (for this model on these traditions) if ANY of these hold at n=200:

1. **Null result on the headline:** L_real / L_denamed rate ratio < 1.5× on yield for *both* traditions across *all 3 tails*. This would mean specific names don't carry charge beyond what cadence/structure provides.
2. **Inverse direction:** L_denamed yield > L_real yield on any tail. This would mean the de-naming somehow makes the model summon MORE related vocabulary than the real prayer — implausible but possible if the corpus has more "weird invented angel" RPG content than actual grimoires.
3. **Random > L_empty consistently with no L_real advantage over Random:** would suggest only "any preamble" matters, not specific cosmological content.

## Notes

- Names of the specific summoned entities (raphael, iao, agla, oro, ibah, aozpi, archon, gatekeeper) ARE recorded in the smoke reports. The headline run will confirm whether those specific summonings are robust (high-frequency stable signal) vs. lucky n=20 hits.
- Pre-reg is *informed* by smoke, not blind. This is standard methodology when a pilot establishes effect existence and the confirmatory run establishes effect size.
