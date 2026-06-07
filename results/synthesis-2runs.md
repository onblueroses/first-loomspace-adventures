# Cross-run synthesis

Combined 2 run(s):
- `headline-2026-05-30-deepseek` — model `deepseek/deepseek-v3.2`, n=200, sources=astrachios, headless
- `headline-2026-05-30-hermes` — model `nousresearch/hermes-3-llama-3.1-405b`, n=200, sources=astrachios, headless

## Headline comparisons (rate ratios with 95% CI, by model)

| source | control | tail | headline-2026-05-30-deepseek ratio | headline-2026-05-30-deepseek CI95 | headline-2026-05-30-hermes ratio | headline-2026-05-30-hermes CI95 |
|---|---|---|---|---|---|---|
| `astrachios` | L_denamed | enters_room | 5.479× | [2.192, 22.111] | 5.746× | [2.949, 11.971] |
| `astrachios` | L_denamed | page_continues | 2.411× | [1.619, 3.568] | 2.468× | [1.849, 3.376] |
| `astrachios` | L_denamed | visitor_at_door | 24.636× | [13.196, 60.308] | 8.909× | [5.0, 16.48] |
| `astrachios` | L_empty | enters_room | 400.0× | [217.0, 624.0] | 192.5× | [76.5, 513.0] |
| `astrachios` | L_empty | page_continues | 598.0× | [492.0, 729.0] | 77.571× | [25.947, 629.0] |
| `astrachios` | L_empty | visitor_at_door | 813.0× | [599.0, 1048.0] | 392.0× | [244.0, 559.0] |
| `astrachios` | L_nonsense | enters_room | 18.182× | [9.0, 35.235] | 20.263× | [9.806, 55.429] |
| `astrachios` | L_nonsense | page_continues | 18.121× | [9.851, 50.091] | 4.982× | [3.519, 7.156] |
| `astrachios` | L_nonsense | visitor_at_door | 203.25× | [99.571, 788.0] | 35.636× | [16.25, 122.0] |
| `astrachios` | L_random | enters_room | 400.0× | [217.0, 624.0] | 385.0× | [233.0, 558.0] |
| `astrachios` | L_random | page_continues | 598.0× | [492.0, 729.0] | 543.0× | [445.0, 649.0] |
| `astrachios` | L_random | visitor_at_door | 813.0× | [599.0, 1048.0] | 392.0× | [244.0, 559.0] |
| `headless` | L_denamed | enters_room | 7.008× | [5.407, 9.511] | 36.667× | [13.2, 151.0] |
| `headless` | L_denamed | page_continues | 1.558× | [1.424, 1.711] | 4.007× | [2.989, 5.558] |
| `headless` | L_denamed | visitor_at_door | 7.758× | [5.867, 10.778] | 29.0× | [12.688, 143.5] |
| `headless` | L_empty | enters_room | 827.0× | [772.0, 885.0] | 55.0× | [21.75, 150.0] |
| `headless` | L_empty | page_continues | 1159.0× | [1091.0, 1231.0] | 77.286× | [26.105, 604.0] |
| `headless` | L_empty | visitor_at_door | 993.0× | [912.0, 1074.0] | 232.0× | [167.0, 303.0] |
| `headless` | L_nonsense | enters_room | 17.229× | [12.94, 24.303] | 55.0× | [21.25, 153.0] |
| `headless` | L_nonsense | page_continues | 2.085× | [1.876, 2.329] | 9.017× | [5.526, 16.588] |
| `headless` | L_nonsense | visitor_at_door | 9.457× | [7.248, 12.988] | 116.0× | [49.333, 288.0] |
| `headless` | L_random | enters_room | 827.0× | [772.0, 885.0] | 110.0× | [65.0, 170.0] |
| `headless` | L_random | page_continues | 1159.0× | [1091.0, 1231.0] | 541.0× | [456.0, 630.0] |
| `headless` | L_random | visitor_at_door | 993.0× | [912.0, 1074.0] | 232.0× | [167.0, 303.0] |

### Replication summary

- Agree (positive evidence in all runs): **23/24**
- Agree (same non-positive interpretation): 0/24
- Diverge across runs: 1/24

## Register classifier (per-cell means, by model)

| cell | headline-2026-05-30-deepseek form | headline-2026-05-30-deepseek arch | headline-2026-05-30-deepseek rev | headline-2026-05-30-deepseek %super | headline-2026-05-30-hermes form | headline-2026-05-30-hermes arch | headline-2026-05-30-hermes rev | headline-2026-05-30-hermes %super |
|---|---|---|---|---|---|---|---|---|
| `astrachios/enters_room` | 3.62 | 2.67 | 3.0 | 90.5% | 3.76 | 2.74 | 3.26 | 91.8% |
| `astrachios/page_continues` | 4.71 | 4.28 | 4.2 | 99.5% | 4.36 | 3.67 | 3.25 | 98.5% |
| `astrachios/visitor_at_door` | 4.22 | 3.17 | 3.33 | 96.5% | 4.31 | 3.26 | 3.65 | 96.5% |
| `astrachios_denamed/enters_room` | 3.78 | 2.83 | 3.4 | 95.5% | 3.87 | 2.79 | 3.62 | 96.5% |
| `astrachios_denamed/page_continues` | 4.54 | 3.89 | 3.76 | 100.0% | 4.32 | 3.56 | 3.32 | 99.5% |
| `astrachios_denamed/visitor_at_door` | 4.43 | 3.56 | 4.07 | 98.5% | 3.94 | 2.9 | 3.37 | 96.0% |
| `astrachios_nonsense/enters_room` | 3.91 | 2.8 | 3.1 | 93.0% | 3.56 | 2.49 | 3.0 | 92.3% |
| `astrachios_nonsense/page_continues` | 4.04 | 3.19 | 3.29 | 99.0% | 4.08 | 3.28 | 3.0 | 98.5% |
| `astrachios_nonsense/visitor_at_door` | 4.16 | 3.27 | 3.44 | 95.0% | 3.85 | 2.78 | 2.91 | 92.5% |
| `astrachios_random/enters_room` | 2.67 | 1.0 | 1.01 | 1.0% | 1.87 | 1.11 | 1.29 | 18.1% |
| `astrachios_random/page_continues` | 2.83 | 1.0 | 1.02 | 0.0% | 2.71 | 1.0 | 1.06 | 0.0% |
| `astrachios_random/visitor_at_door` | 1.75 | 1.03 | 1.02 | 6.5% | 1.75 | 1.07 | 1.09 | 12.5% |
| `empty/enters_room` | 1.91 | 1.0 | 1.0 | 0.0% | 2.22 | 1.37 | 1.54 | 44.2% |
| `empty/page_continues` | 1.96 | 1.0 | 1.0 | 0.0% | 2.85 | 1.07 | 1.06 | 3.0% |
| `empty/visitor_at_door` | 1.94 | 1.01 | 1.0 | 0.0% | 1.88 | 1.27 | 1.19 | 20.0% |
| `headless/enters_room` | 4.11 | 3.15 | 3.86 | 100.0% | 3.48 | 2.68 | 3.31 | 87.4% |
| `headless/page_continues` | 3.7 | 2.54 | 2.33 | 94.5% | 4.5 | 3.79 | 3.87 | 98.0% |
| `headless/visitor_at_door` | 4.31 | 3.33 | 3.59 | 99.5% | 3.65 | 2.92 | 3.34 | 90.0% |
| `headless_denamed/enters_room` | 4.53 | 3.69 | 4.34 | 100.0% | 3.3 | 2.42 | 2.95 | 86.4% |
| `headless_denamed/page_continues` | 3.03 | 2.46 | 1.92 | 80.5% | 4.2 | 3.5 | 3.31 | 95.0% |
| `headless_denamed/visitor_at_door` | 4.58 | 3.73 | 4.15 | 99.0% | 3.54 | 2.71 | 3.0 | 91.5% |
| `headless_nonsense/enters_room` | 4.11 | 3.19 | 3.71 | 97.0% | 3.4 | 2.53 | 2.87 | 86.9% |
| `headless_nonsense/page_continues` | 3.6 | 2.93 | 2.94 | 65.0% | 4.33 | 3.64 | 3.67 | 98.5% |
| `headless_nonsense/visitor_at_door` | 4.22 | 3.48 | 3.61 | 87.0% | 3.56 | 2.71 | 3.1 | 93.0% |
| `headless_random/enters_room` | 2.86 | 1.01 | 1.01 | 1.0% | 3.01 | 1.08 | 1.17 | 10.9% |
| `headless_random/page_continues` | 3.49 | 1.0 | 1.0 | 0.0% | 3.38 | 1.0 | 1.01 | 0.5% |
| `headless_random/visitor_at_door` | 2.12 | 1.07 | 1.11 | 3.5% | 2.06 | 1.1 | 1.15 | 13.0% |

## Per-cell headline yield (per-completion mean)

| cell | role | headline-2026-05-30-deepseek hits/comp | headline-2026-05-30-hermes hits/comp |
|---|---|---|---|
| `astrachios/enters_room` | L_real | 1.995 | 1.92 |
| `astrachios/page_continues` | L_real | 2.985 | 2.71 |
| `astrachios/visitor_at_door` | L_real | 4.06 | 1.955 |
| `astrachios_denamed/enters_room` | L_denamed | 0.36 | 0.33 |
| `astrachios_denamed/page_continues` | L_denamed | 1.235 | 1.095 |
| `astrachios_denamed/visitor_at_door` | L_denamed | 0.16 | 0.215 |
| `astrachios_nonsense/enters_room` | L_nonsense | 0.105 | 0.09 |
| `astrachios_nonsense/page_continues` | L_nonsense | 0.16 | 0.54 |
| `astrachios_nonsense/visitor_at_door` | L_nonsense | 0.015 | 0.05 |
| `astrachios_random/enters_room` | L_random | 0.0 | 0.0 |
| `astrachios_random/page_continues` | L_random | 0.0 | 0.0 |
| `astrachios_random/visitor_at_door` | L_random | 0.0 | 0.0 |
| `empty/enters_room` | L_empty | 0.0 | 0.005 |
| `empty/page_continues` | L_empty | 0.0 | 0.03 |
| `empty/visitor_at_door` | L_empty | 0.0 | 0.0 |
| `headless/enters_room` | L_real | 4.13 | 0.545 |
| `headless/page_continues` | L_real | 5.79 | 2.7 |
| `headless/visitor_at_door` | L_real | 4.96 | 1.155 |
| `headless_denamed/enters_room` | L_denamed | 0.585 | 0.01 |
| `headless_denamed/page_continues` | L_denamed | 3.715 | 0.67 |
| `headless_denamed/visitor_at_door` | L_denamed | 0.635 | 0.035 |
| `headless_nonsense/enters_room` | L_nonsense | 0.235 | 0.005 |
| `headless_nonsense/page_continues` | L_nonsense | 2.775 | 0.295 |
| `headless_nonsense/visitor_at_door` | L_nonsense | 0.52 | 0.005 |
| `headless_random/enters_room` | L_random | 0.0 | 0.0 |
| `headless_random/page_continues` | L_random | 0.0 | 0.0 |
| `headless_random/visitor_at_door` | L_random | 0.0 | 0.0 |
