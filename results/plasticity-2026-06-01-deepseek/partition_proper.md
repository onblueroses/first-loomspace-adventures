# Substitute-aware partition — plasticity-2026-06-01-deepseek

**Method**: combined denamed name-set yield (parent-lexicon + substitute-lexicon) replaces the previous form-charge denominator. Denominators are total completion counts from `measurements.json` (matching the numerator's file scope; valid-only denominators are reported separately in `degenerate_audit.json` as a transparency check, not folded into the partition). Laplace +1/+1 throughout.

**Charges**:
- `floor`            = L_random / L_empty                (does random prose elicit lexicon hits?)
- `bootstrap-charge` = (L_denamed_parent + L_denamed_substitute) / L_random  (does the denamed prompt elicit ANY coherent name-set continuation?)
- `preference-charge`= L_real / (L_denamed_parent + L_denamed_substitute)    (do REAL names beat substitutes once any name-set is engaged?)

Identity (Laplace-smoothed): `log(L_real/L_empty) ≈ log(floor) + log(bootstrap-charge) + log(preference-charge)`
Identity check column reports `log_lhs - log_rhs` (should be ≈ 0).

## synthetic_litany

| Tail | L_real | L_denamed (parent+sub) | L_random | L_empty | floor | bootstrap | preference | identity |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| visitor_at_door | 3.109 | 5.229 (0.020+5.209) | 0.005 | 0.005 | 1.00 | 1051.00 | 0.59 | -0.000 |
| enters_room | 1.891 | 1.393 (0.045+1.348) | 0.005 | 0.005 | 1.00 | 280.00 | 1.36 | +0.000 |
| page_continues | 7.398 | 8.706 (0.065+8.642) | 0.005 | 0.005 | 1.00 | 1750.00 | 0.85 | +0.000 |

## synthetic_cosmological

| Tail | L_real | L_denamed (parent+sub) | L_random | L_empty | floor | bootstrap | preference | identity |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| visitor_at_door | 3.343 | 3.657 (0.005+3.652) | 0.005 | 0.005 | 1.00 | 735.00 | 0.91 | +0.000 |
| enters_room | 1.846 | 2.214 (0.010+2.204) | 0.005 | 0.005 | 1.00 | 445.00 | 0.83 | +0.000 |
| page_continues | 4.612 | 4.811 (0.647+4.164) | 0.005 | 0.005 | 1.00 | 967.00 | 0.96 | +0.000 |

## Cross-tail / cross-form interpretation

- **preference-charge ≫ 1**: the model strongly prefers real synthetic names over the prompt's own substitutes — i.e. the specific name string carries weight beyond `[name-shaped-token-in-this-cosmological-form]`.
- **preference-charge ≈ 1**: the model produces real names and substitutes at comparable per-completion rates — the form swallows the name distinction.
- **preference-charge < 1**: the substitute-name continuation is MORE prolific than the real-name continuation (likely artifact: model picks up the prompt's planted substitutes more eagerly than parent names get reproduced).
- **bootstrap-charge ≫ 1**: the denamed/substitute prompt successfully bootstraps a name-set continuation — Lesson 9 plasticity at work.
- **floor stays ≈ 1**: random/empty produce no lexicon hits — the controls remain silent (the partition base is clean).