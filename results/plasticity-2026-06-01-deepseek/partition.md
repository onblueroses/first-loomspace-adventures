# Partition decomposition — DeepSeek (plasticity-2026-06-01-deepseek)

Per Decision #11 of the project notes:

- `floor` = L_random / L_empty
- `form-charge` = L_denamed / L_random
- `name-charge` = L_real / L_denamed

Identity check: `log(L_real/L_empty) == log(floor) + log(form-charge) + log(name-charge)` (Laplace-smoothed rates throughout).

## Headline factors (DS, n=200 per cell, valid filter NOT YET applied)

### synthetic_litany

| Tail | L_real/comp | L_denamed/comp | L_random/comp | L_empty/comp | floor | form-charge | name-charge | Identity check (log) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| visitor_at_door | 3.110 | 0.020 | 0.005 | 0.005 | 1.00 | 4.00 | 155.5 | 6.43 ≈ 6.43 ✓ |
| enters_room | 1.891 | 0.045 | 0.005 | 0.005 | 1.00 | 9.00 | 42.02 | 5.94 ≈ 5.94 ✓ |
| page_continues | 7.398 | 0.065 | 0.005 | 0.005 | 1.00 | 13.00 | 113.8 | 7.30 ≈ 7.30 ✓ |

### synthetic_cosmological

| Tail | L_real/comp | L_denamed/comp | L_random/comp | L_empty/comp | floor | form-charge | name-charge | Identity check (log) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| visitor_at_door | 3.343 | 0.005 | 0.005 | 0.005 | 1.00 | 1.00 | 668.6 | 6.51 ≈ 6.51 ✓ |
| enters_room | 1.846 | 0.010 | 0.005 | 0.005 | 1.00 | 2.00 | 184.6 | 5.92 ≈ 5.92 ✓ |
| page_continues | 4.612 | 0.647 | 0.005 | 0.005 | 1.00 | 129.4 | 7.13 | 6.83 ≈ 6.83 ✓ |

## Pre-reg disposition (DS only — Hermes pending)

### synthetic_litany falsifiers

1. **Name-charge collapse (visitor_at_door < 2.0):** name-charge=155.5 → NOT TRIPPED. Strong signal.
2. **Form-charge dominance (form-charge > 5.0 on visitor):** form-charge=4.00 on visitor → NOT TRIPPED (just under).
3. **Floor breakout (>3.0 or <0.3):** floor=1.00 across all tails → NOT TRIPPED.
4. **Partition identity violation (>0.1 log error):** errors ≤ 0.01 → NOT TRIPPED.
5. **Cross-tail inversion (visitor < page_continues on name-charge):** visitor=155.5, page=113.8 → NOT TRIPPED.

### synthetic_cosmological falsifiers

1. **Name-charge collapse:** name-charge(visitor)=668.6, (enters)=184.6, (page)=7.13 → NOT TRIPPED but **page_continues is much weaker than predicted** (predicted ≥ 1.5; actual 7.13; passes but barely on the predicted ordering).
2. **Form-charge dominance (>8.0 on visitor):** visitor form-charge=1.00 → NOT TRIPPED on visitor; **but page_continues form-charge=129.4 — vastly exceeds the visitor threshold of 8.0**. The falsifier was scoped to visitor; on visitor it's clean. On page_continues, form-charge dominates name-charge by 18× — a striking inversion of the per-tail predicted ordering.
3. **Floor breakout:** all floors=1.00 → NOT TRIPPED.
4. **Partition identity:** errors ≤ 0.01 → NOT TRIPPED.
5. **Cross-tail inversion:** visitor name-charge=668.6, page_continues name-charge=7.13 → name-charge does fall most on page_continues (predicted direction); ordering preserved.

## Key empirical finding (DS)

**Form-charge is tail-dependent in a way the pre-reg under-predicted.** For visitor_at_door and enters_room, form-charge ≈ 1–9 (controls almost completely silent). For page_continues, form-charge jumps to 13 (litany) and 129 (cosmological).

**Mechanism (preliminary, from top-hits inspection):** the page_continues form-charge is dominated by *related_vocabulary* mentions (gnostic × 66, papyri × 21, ceremonial × 18, barbarous × 13, theurgy × 6) — the model continues in the magical-prose register and produces meta-vocabulary about magical practices when given a denamed liturgy + continuation hook. This is NOT the Hermes-pilot pattern of fabricating denamed substitutes (`phengereb × 40`); DS is doing register-leakage, not substitute-egregore production.

**Cross-tail asymmetry:** the page_continues hook ("As the page continues, the text reads:") elicits register-extending behavior far more than the framed scenarios (visitor/enters). With visitor/enters, the model "performs" the scenario without much register drift. With page_continues, it writes more about magic.

## Degenerate-completion audit (Decision #19)

Total completions: 5400. Short (<50 chars): 394 (7.3%). Refusal-prefixed: 4 (0.07%). Valid: 5002 (92.7%). See `degenerate_audit.json` for per-cell counts. Cells most affected: synthetic_litany visitor (68/200 short), synthetic_litany_nonsense visitor (77/200 short), empty visitor (76/200 short). Short completions cluster on visitor_at_door for litany-format prompts (the model frequently completes with a name or two and stops). This biases L_real yield *upward* slightly when using total denominators (we're dividing by 200 but only 132 are full-length completions, so the per-valid-completion rate is higher). Re-computing with `valid` denominators is a robustness check for the writeup — TODO once Hermes is in.

## Next

- Wait for Hermes Phase 4 completion (~50 min from time of writing).
- Run measure.py + degenerate_audit.py + partition.md on Hermes.
- Compose `docs/plasticity-findings.md` with both-model partition comparison.
- The cross-model comparison is the headline finding: does Hermes reproduce DS's tail-dependent form-charge, or does it stay with substitute-name production (as the Hermes pilot suggested)?
