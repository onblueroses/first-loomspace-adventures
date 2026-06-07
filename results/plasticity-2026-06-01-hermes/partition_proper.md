# Substitute-aware partition — plasticity-2026-06-01-hermes

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
| visitor_at_door | 1.896 | 2.114 (0.104+2.010) | 0.005 | 0.005 | 1.00 | 425.00 | 0.90 | +0.000 |
| enters_room | 1.682 | 1.955 (0.109+1.846) | 0.005 | 0.005 | 1.00 | 393.00 | 0.86 | +0.000 |
| page_continues | 1.766 | 2.816 (0.846+1.970) | 0.005 | 0.005 | 1.00 | 566.00 | 0.63 | +0.000 |

## synthetic_cosmological

| Tail | L_real | L_denamed (parent+sub) | L_random | L_empty | floor | bootstrap | preference | identity |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| visitor_at_door | 1.662 | 2.214 (0.045+2.169) | 0.005 | 0.005 | 1.00 | 445.00 | 0.75 | +0.000 |
| enters_room | 1.502 | 1.393 (0.020+1.373) | 0.005 | 0.005 | 1.00 | 280.00 | 1.08 | +0.000 |
| page_continues | 2.109 | 3.572 (0.224+3.348) | 0.005 | 0.005 | 1.00 | 718.00 | 0.59 | +0.000 |

## Cross-tail / cross-form interpretation

- **preference-charge ≫ 1**: the model strongly prefers real synthetic names over the prompt's own substitutes — i.e. the specific name string carries weight beyond `[name-shaped-token-in-this-cosmological-form]`.
- **preference-charge ≈ 1**: the model produces real names and substitutes at comparable per-completion rates — the form swallows the name distinction.
- **preference-charge < 1**: the substitute-name continuation is MORE prolific than the real-name continuation (likely artifact: model picks up the prompt's planted substitutes more eagerly than parent names get reproduced).
- **bootstrap-charge ≫ 1**: the denamed/substitute prompt successfully bootstraps a name-set continuation — Lesson 9 plasticity at work.
- **floor stays ≈ 1**: random/empty produce no lexicon hits — the controls remain silent (the partition base is clean).