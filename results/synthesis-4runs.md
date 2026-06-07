# Cross-run synthesis

Combined 4 run(s):
- `2026-05-30T10-44-26` — model `deepseek/deepseek-v3.2`, n=20, sources=astrachios
- `2026-05-30T10-44-31` — model `nousresearch/hermes-3-llama-3.1-405b`, n=20, sources=astrachios
- `2026-05-30T12-37-12` — model `deepseek/deepseek-v3.2`, n=20, sources=headless
- `2026-05-30T12-37-18` — model `nousresearch/hermes-3-llama-3.1-405b`, n=20, sources=headless

## Headline comparisons (rate ratios with 95% CI, by model)

| source | control | tail | 2026-05-30T10-44-26 ratio | 2026-05-30T10-44-26 CI95 | 2026-05-30T10-44-31 ratio | 2026-05-30T10-44-31 CI95 | 2026-05-30T12-37-12 ratio | 2026-05-30T12-37-12 CI95 | 2026-05-30T12-37-18 ratio | 2026-05-30T12-37-18 CI95 |
|---|---|---|---|---|---|---|---|---|---|---|
| `astrachios` | L_denamed | visitor_at_door | 46.0× | [7.0, 105.0] | 16.4× | [2.2, 55.5] | — | — | — | — |
| `astrachios` | L_nonsense | visitor_at_door | 46.0× | [7.0, 105.0] | 82.0× | [11.0, 170.0] | — | — | — | — |
| `headless` | L_denamed | visitor_at_door | — | — | — | — | 5.571× | [3.229, 11.545] | 34.0× | [11.0, 60.0] |
| `headless` | L_nonsense | visitor_at_door | — | — | — | — | 4.875× | [3.033, 8.857] | 34.0× | [11.0, 60.0] |

### Replication summary

- Agree (positive evidence in all runs): **4/4**
- Agree (same non-positive interpretation): 0/4
- Diverge across runs: 0/4

## Register classifier (per-cell means, by model)

| cell | 2026-05-30T10-44-26 form | 2026-05-30T10-44-26 arch | 2026-05-30T10-44-26 rev | 2026-05-30T10-44-26 %super | 2026-05-30T10-44-31 form | 2026-05-30T10-44-31 arch | 2026-05-30T10-44-31 rev | 2026-05-30T10-44-31 %super | 2026-05-30T12-37-12 form | 2026-05-30T12-37-12 arch | 2026-05-30T12-37-12 rev | 2026-05-30T12-37-12 %super | 2026-05-30T12-37-18 form | 2026-05-30T12-37-18 arch | 2026-05-30T12-37-18 rev | 2026-05-30T12-37-18 %super |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `astrachios/visitor_at_door` | 4.4 | 3.5 | 4.1 | 100.0% | 4.6 | 3.55 | 4.0 | 100.0% | — | — | — | — | — | — | — | — |
| `astrachios_denamed/visitor_at_door` | 4.65 | 3.8 | 4.0 | 100.0% | 3.85 | 2.8 | 3.1 | 100.0% | — | — | — | — | — | — | — | — |
| `astrachios_nonsense/visitor_at_door` | 4.1 | 3.0 | 3.6 | 85.0% | 3.55 | 2.8 | 2.7 | 95.0% | — | — | — | — | — | — | — | — |

## Per-cell headline yield (per-completion mean)

| cell | role | 2026-05-30T10-44-26 hits/comp | 2026-05-30T10-44-31 hits/comp | 2026-05-30T12-37-12 hits/comp | 2026-05-30T12-37-18 hits/comp |
|---|---|---|---|---|---|
| `astrachios/visitor_at_door` | L_real | 2.25 | 4.05 | — | — |
| `astrachios_denamed/visitor_at_door` | L_denamed | 0.0 | 0.2 | — | — |
| `astrachios_nonsense/visitor_at_door` | L_nonsense | 0.0 | 0.0 | — | — |
| `headless/visitor_at_door` | L_real | — | — | 5.8 | 1.65 |
| `headless_denamed/visitor_at_door` | L_denamed | — | — | 1.0 | 0.0 |
| `headless_nonsense/visitor_at_door` | L_nonsense | — | — | 1.15 | 0.0 |
