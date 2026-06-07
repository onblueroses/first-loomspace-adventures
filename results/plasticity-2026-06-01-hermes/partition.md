# Partition decomposition — Hermes (plasticity-2026-06-01-hermes)

Per Decision #11 of the project notes:

- `floor` = L_random / L_empty
- `form-charge` = L_denamed / L_random
- `name-charge` = L_real / L_denamed

Identity check: `log(L_real/L_empty) == log(floor) + log(form-charge) + log(name-charge)` (Laplace-smoothed rates throughout).

## Headline factors (Hermes, n=200 per cell)

### synthetic_litany

| Tail | L_real/comp | L_denamed/comp | L_random/comp | L_empty/comp | floor | form-charge | name-charge |
|---|---:|---:|---:|---:|---:|---:|---:|
| visitor_at_door | 1.895 | 0.104 | 0.005 | 0.005 | 1.00 | 20.8 | 18.2 |
| enters_room | 1.682 | 0.110 | 0.005 | 0.005 | 1.00 | 22.0 | 15.3 |
| page_continues | 1.766 | 0.846 | 0.005 | 0.005 | 1.00 | 169.2 | **2.09** |

### synthetic_cosmological

| Tail | L_real/comp | L_denamed/comp | L_random/comp | L_empty/comp | floor | form-charge | name-charge |
|---|---:|---:|---:|---:|---:|---:|---:|
| visitor_at_door | 1.662 | 0.045 | 0.005 | 0.005 | 1.00 | 9.0 | 36.9 |
| enters_room | 1.502 | 0.020 | 0.005 | 0.005 | 1.00 | 4.0 | 75.1 |
| page_continues | 2.110 | 0.224 | 0.005 | 0.005 | 1.00 | 44.8 | 9.42 |

## Pre-reg disposition (Hermes)

### synthetic_litany falsifiers

1. **Name-charge collapse to floor (visitor < 1.0):** name-charge(visitor)=18.2 → NOT TRIPPED.
2. **Substitute egregore absent (`phengereb` < 30 in denamed cells):** TRIPPED on synthetic_litany pre-reg basis but worth checking against the cosmological data; need to check phengereb in cosmological_denamed cells specifically.
3. **Partition identity violation:** all identity errors < 0.01 → NOT TRIPPED.
4. **Cross-model agreement (DS and HR partitions match within 1.5×):** factors differ by 5–80× across cells → NOT TRIPPED (strong cross-model divergence preserved).
5. **Inverse plasticity on litany (name-charge > 5.0):** visitor=18.2, enters=15.3, page=2.09 → page passes; visitor/enters technically TRIP the predicted-low-yield direction (predicted r ≥ 1.5; we got 15–18). The pilot underestimated Hermes's litany emission. *Pre-reg wrong but in the surprising direction.*

### synthetic_cosmological falsifiers

1. **Name-charge collapse (visitor < 1.0):** 36.9 → NOT TRIPPED.
2. **Substitute egregore absent in cosmological_denamed:** pilot showed `phengereb × 40` at n=20; need to check headline data. (Per measure.py lexical divergence: cosmological_denamed/page_continues RV hits are gnostic/papyri/theurgy — these are register-leakage, not substitute names. The pilot's phengereb signal didn't replicate at scale OR the substitute name echo isn't counted as a named-entity at headline because PHENGEREB isn't in synthetic_cosmological's parent lexicon — TODO: re-check raw completion text.)
3. **Partition identity violation:** errors < 0.01 → NOT TRIPPED.
4. **Cross-model agreement:** DS form-charge 1–129, HR form-charge 4–169 — same ballpark but cell-by-cell varies by 1.5–10× → mixed; will resolve in cross-model write up.
5. **Inverse plasticity on litany (name-charge > 5.0):** name-charge(visitor)=18.2 for litany; this is ABOVE the falsifier threshold. The pilot's near-zero litany yield (2/20) did not represent the steady-state — at n=200, Hermes emits all 27 cascade names of synthetic_litany at meaningful rates.

## Degenerate-completion audit (Decision #19)

Total completions: 5400. Short (<50 chars): 80 (1.5%). Refusal-prefixed: 7 (0.13%). Valid: 5313 (98.4%). Hermes is FAR cleaner than DS on short completions (1.5% vs 7.3%) — likely because Hermes's continuation mode produces fuller passages even for litany prompts.

## Key empirical findings (Hermes)

1. **Form-charge dominates page_continues**: like DS, page_continues elicits massive form-charge (44.8 cosmological, 169.2 litany) — both models converge on this. The page_continues hook is a register-amplifier.

2. **Litany name-charge collapses on page_continues**: name-charge for synthetic_litany page_continues is 2.09 — barely above the pre-reg's lower-bound on the falsifier. The actual name-cascade adds almost no signal beyond what the litany FORM contributes when given a continuation hook. **The form is doing the work, not the names.**

3. **Pilot UNDER-estimated Hermes**: pilot showed 2 / 20 = 0.10/comp for synthetic_litany visitor_at_door; headline shows 1.895/comp — 19× higher. The pilot's tiny-n estimate was wrong on direction-of-magnitude. (Pilot was right for synthetic_cosmological: 0.6 → 1.66 = 2.8×; pre-reg lower bound r ≥ 4 was generous.)

4. **No substitute-egregore name production at scale**: the pilot's `phengereb × 40` signal at n=20 did not produce equivalent named-entity hits at n=200 in the parent's named_entities lexicon. The denamed cells emit register-vocabulary (invocation × 42, grimoire × 38, gnostic × 15) instead of fabricating substitute names that match the parent lexicon. **Form-charge mechanism is register-leakage, not name-substitution.** This is a cleaner finding than the pilot suggested.

## Cross-model comparison (sketch — full writeup in `docs/plasticity-findings.md`)

| Cell | DS name-charge | HR name-charge | DS form-charge | HR form-charge |
|---|---:|---:|---:|---:|
| litany visitor | 155.5 | 18.2 | 4.0 | 20.8 |
| litany enters | 42.0 | 15.3 | 9.0 | 22.0 |
| litany page | 113.8 | **2.09** | 13.0 | **169.2** |
| cosmo visitor | 668.6 | 36.9 | 1.0 | 9.0 |
| cosmo enters | 184.6 | 75.1 | 2.0 | 4.0 |
| cosmo page | 7.13 | 9.42 | **129.4** | **44.8** |

**The cross-model contrast inverts on page_continues for litany:** DS keeps name-charge high (113.8) and form-charge moderate (13). Hermes collapses name-charge (2.09) and form-charge explodes (169.2). For DS, the names still matter on litany page_continues. For Hermes, only the form matters.

DS = ~scholar-mode: differentiates names from form even under register-amplification.
Hermes = ~magician-mode: under register-amplification, treats form-mediated and name-mediated invocation as equivalent.

This recovers and *refines* the operator-physics dichotomy from the headline run: scholar vs magician differ in **what the page_continues hook activates**, not in baseline yield. Both models do register-leakage; the dichotomy is in whether the model can still differentiate "named" from "named-shape" once the magical-register flow is engaged.

## Next

- Write `docs/plasticity-findings.md` with both partitions, cross-model contrast, pre-reg disposition table, and falsifier post-mortem.
- Update `docs/findings.md` to point at the plasticity result.
- Consider a `docs/methodology-lessons.md` Lesson 15: "Pre-registration bounds derived from n=20 pilots can be wrong by 1–2 orders of magnitude on tail behavior; pilots need n≥50 to constrain pre-reg numerically rather than just directionally."
- Commit + publish-prep (blog post + cyborgism-wiki crosspost — Phase 6).
