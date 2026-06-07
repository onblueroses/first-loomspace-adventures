# Pre-registration: Headline run — Hermes

**Run id:** `headline-2026-05-30-hermes`
**Model:** `nousresearch/hermes-3-llama-3.1-405b`
**Date written:** 2026-05-30 (before sampling)

## Disclosure

Informed by smoke results (results/2026-05-30T10-44-31 for Astrachios, results/2026-05-30T12-37-18 for Headless). The smoke established directional signal at n=20; this pre-registration commits to the headline-scale predictions at n=200 × 3 tails.

## Scope

- **Liturgies:** astrachios, astrachios_denamed, astrachios_nonsense, astrachios_random, headless, headless_denamed, headless_nonsense, headless_random, empty
- **Tails:** visitor_at_door, enters_room, page_continues
- **n per cell:** 200
- **Sampling:** temperature 0.7, top_p 0.95, max_tokens 256
- **Total cells:** 9 conditions × 3 tails = 27 cells
- **Total calls:** 5400

## Headline predictions

### Headline yield (rate ratios)

For each tradition (astrachios, headless) and each tail, the per-completion rate ratio L_real_vs_L_denamed is predicted to be **≥ 5.0×** with **lower 95% CI > 2.0**.

Hermes showed stronger entity-summoning than DeepSeek in the smoke — Hermes produced **Enochian Watchtower names** (ORO, IBAH, AOZPI, AGLA) unprompted from the Astrachios preamble. The headline run should robustly reproduce that finding.

| Comparison | Predicted rate ratio |
|---|---|
| astrachios L_real_vs_L_denamed | ≥ 8× across all 3 tails |
| astrachios L_real_vs_L_nonsense | ≥ 20× across all 3 tails |
| astrachios L_real_vs_L_random | ≥ 30× across all 3 tails |
| astrachios L_real_vs_L_empty | ≥ 50× across all 3 tails |
| headless L_real_vs_L_denamed | ≥ 10× across all 3 tails |
| headless L_real_vs_L_nonsense | ≥ 10× across all 3 tails |
| headless L_real_vs_L_random | ≥ 30× across all 3 tails |
| headless L_real_vs_L_empty | ≥ 50× across all 3 tails |

Predicted ordering (each tradition, each tail):
`L_real >> L_denamed > L_nonsense ≈ L_random > L_empty`

### Lexical-divergence predictions (specific entities, the strongest evidence)

The Astrachios-Hermes smoke produced these unprompted entity invocations across 20 completions × 1 tail:
- AGLA × 15
- ORO × 10
- AOZPI × 10
- IBAH × 10
- "doorkeeper" × 47

**Predict at headline scale (200 × 3 tails = 600 completions per cell):**
- For Astrachios L_real: AGLA ≥ 100, ORO ≥ 60, AOZPI ≥ 60, IBAH ≥ 60
- For Astrachios L_denamed: AGLA ≤ 5, ORO ≤ 5, AOZPI ≤ 5, IBAH ≤ 5
- These ratios are the **strongest single piece of evidence** for egregore weight: the model is summoning a specific historically-attested invocation system (Dee/Kelly Enochian Watchtower) only when given the real Grimorium Verum prayer.

For Headless L_real:
- The classical PGM/Crowley names should appear unprompted in L_real continuations. Predict: "iao" ≥ 100, "sabaoth" ≥ 50, "agla" ≥ 20, "abrahadabra" or "abracadabra" ≥ 10 across the 3 tails.
- For L_denamed: each of these ≤ 5.

### Register classifier predictions

Hermes smoke pattern (Astrachios): L_real > L_denamed > L_nonsense **on all 3 register dimensions** (formality 4.60 vs 3.85 vs 3.55; archaism 3.55 vs 2.80 vs 2.80; reverential 4.00 vs 3.10 vs 2.70).

Predict for headline (mean per cell, n=200):

| Cell | formality | archaism | reverential | %super |
|---|---|---|---|---|
| L_real (astrachios) | ≥ 4.4 | ≥ 3.3 | ≥ 3.8 | ≥ 95% |
| L_denamed (astrachios) | 3.5-4.2 | 2.5-3.2 | 2.8-3.4 | ≥ 90% |
| L_nonsense (astrachios) | 3.3-3.8 | 2.5-3.0 | 2.5-3.0 | 80-95% |
| L_random (astrachios) | ≤ 3.5 | ≤ 2.0 | ≤ 2.0 | ≤ 40% |
| L_empty | ≤ 3.0 | ≤ 2.0 | ≤ 2.0 | ≤ 40% |

## Falsifiers

The egregore-weight hypothesis is falsified (for Hermes on these traditions) if ANY of these hold at n=200:

1. **No Enochian summoning:** AGLA, ORO, AOZPI, IBAH each appear < 20 times across the 600 Astrachios-L_real completions. This would mean the n=20 smoke was a lucky cluster and the corpus association is weaker than it appeared.
2. **L_denamed ≈ L_real:** rate ratio < 2.0× on yield for any tradition × tail combination. Would mean the de-named prayer triggers similar associations.
3. **No register separation:** L_real ≈ L_denamed on all three register dimensions. Would mean Hermes pattern was a smoke artifact.

## Notes

- Concurrency=6 to balance throughput against upstream rate limits at Venice (which served the free tier).
- Pre-reg is informed by smoke, not blind. This is the appropriate methodology when pilot data establishes effect existence and confirmatory data establishes effect size.
- A surprising NEGATIVE finding (e.g., Enochian names don't reproduce) would itself be publishable — it would tell us the corpus's egregore structure is more locally clustered than the smoke suggested.
