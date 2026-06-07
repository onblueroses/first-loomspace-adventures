# Measurements: plasticity-2026-06-01-deepseek

**Model:** `deepseek/deepseek-v3.2`
**n per cell:** 200
**Source liturgies (L_real):** `synthetic_cosmological`, `synthetic_litany`

## Headline comparisons (per-completion rate ratios)

| Source | Comparison | tail | L_real rate | Control rate | Rate ratio | 95% CI | Interpretation |
|---|---|---|---:|---:|---:|---:|---|
| `synthetic_cosmological` | L_empty (`empty`) | visitor_at_door | 3.3433 (671/200) | 0.005 (0/200) | 672.0× | [607.0, 741.0] | positive evidence |
| `synthetic_cosmological` | L_denamed (`synthetic_cosmological_denamed`) | visitor_at_door | 3.3433 (671/200) | 0.005 (0/200) | 672.0× | [607.0, 741.0] | positive evidence |
| `synthetic_cosmological` | L_nonsense (`synthetic_cosmological_nonsense`) | visitor_at_door | 3.3433 (671/200) | 0.01 (1/200) | 336.0× | [158.25, 721.0] | positive evidence |
| `synthetic_cosmological` | L_random (`synthetic_cosmological_random`) | visitor_at_door | 3.3433 (671/200) | 0.005 (0/200) | 672.0× | [607.0, 741.0] | positive evidence |
| `synthetic_cosmological` | L_empty (`empty`) | enters_room | 1.8458 (370/200) | 0.005 (0/200) | 371.0× | [320.0, 429.0] | positive evidence |
| `synthetic_cosmological` | L_denamed (`synthetic_cosmological_denamed`) | enters_room | 1.8458 (370/200) | 0.01 (1/200) | 185.5× | [85.25, 410.0] | positive evidence |
| `synthetic_cosmological` | L_nonsense (`synthetic_cosmological_nonsense`) | enters_room | 1.8458 (370/200) | 0.005 (0/200) | 371.0× | [320.0, 429.0] | positive evidence |
| `synthetic_cosmological` | L_random (`synthetic_cosmological_random`) | enters_room | 1.8458 (370/200) | 0.005 (0/200) | 371.0× | [320.0, 429.0] | positive evidence |
| `synthetic_cosmological` | L_empty (`empty`) | page_continues | 4.6119 (926/200) | 0.005 (0/200) | 927.0× | [853.0, 1000.0] | positive evidence |
| `synthetic_cosmological` | L_denamed (`synthetic_cosmological_denamed`) | page_continues | 4.6119 (926/200) | 0.6468 (129/200) | 7.131× | [5.65, 9.079] | positive evidence |
| `synthetic_cosmological` | L_nonsense (`synthetic_cosmological_nonsense`) | page_continues | 4.6119 (926/200) | 0.4279 (85/200) | 10.779× | [8.405, 14.149] | positive evidence |
| `synthetic_cosmological` | L_random (`synthetic_cosmological_random`) | page_continues | 4.6119 (926/200) | 0.005 (0/200) | 927.0× | [853.0, 1000.0] | positive evidence |
| `synthetic_litany` | L_empty (`empty`) | visitor_at_door | 3.1095 (624/200) | 0.005 (0/200) | 625.0× | [406.0, 873.0] | positive evidence |
| `synthetic_litany` | L_denamed (`synthetic_litany_denamed`) | visitor_at_door | 3.1095 (624/200) | 0.0199 (3/200) | 156.25× | [69.375, 619.0] | positive evidence |
| `synthetic_litany` | L_nonsense (`synthetic_litany_nonsense`) | visitor_at_door | 3.1095 (624/200) | 0.0249 (4/200) | 125.0× | [59.778, 380.0] | positive evidence |
| `synthetic_litany` | L_random (`synthetic_litany_random`) | visitor_at_door | 3.1095 (624/200) | 0.005 (0/200) | 625.0× | [406.0, 873.0] | positive evidence |
| `synthetic_litany` | L_empty (`empty`) | enters_room | 1.8905 (379/200) | 0.005 (0/200) | 380.0× | [238.0, 535.0] | positive evidence |
| `synthetic_litany` | L_denamed (`synthetic_litany_denamed`) | enters_room | 1.8905 (379/200) | 0.0448 (8/200) | 42.222× | [21.462, 99.0] | positive evidence |
| `synthetic_litany` | L_nonsense (`synthetic_litany_nonsense`) | enters_room | 1.8905 (379/200) | 0.0697 (13/200) | 27.143× | [14.95, 53.364] | positive evidence |
| `synthetic_litany` | L_random (`synthetic_litany_random`) | enters_room | 1.8905 (379/200) | 0.005 (0/200) | 380.0× | [238.0, 535.0] | positive evidence |
| `synthetic_litany` | L_empty (`empty`) | page_continues | 7.398 (1486/200) | 0.005 (0/200) | 1487.0× | [1158.0, 1819.0] | positive evidence |
| `synthetic_litany` | L_denamed (`synthetic_litany_denamed`) | page_continues | 7.398 (1486/200) | 0.0647 (12/200) | 114.385× | [69.9, 228.857] | positive evidence |
| `synthetic_litany` | L_nonsense (`synthetic_litany_nonsense`) | page_continues | 7.398 (1486/200) | 0.0498 (9/200) | 148.7× | [87.846, 325.4] | positive evidence |
| `synthetic_litany` | L_random (`synthetic_litany_random`) | page_continues | 7.398 (1486/200) | 0.005 (0/200) | 1487.0× | [1158.0, 1819.0] | positive evidence |

## Per-cell

| Cell | Role | n | Tokens | Headline yield | /completion | NE | RV | Amb-NE | Amb-RV |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `synthetic_cosmological/visitor_at_door` | L_real | 200 | 37369 | 671 | 3.355 | 640 | 31 | 0 | 822 |
| `synthetic_cosmological/enters_room` | L_real | 200 | 34174 | 370 | 1.85 | 370 | 0 | 0 | 637 |
| `synthetic_cosmological/page_continues` | L_real | 200 | 33690 | 926 | 4.63 | 818 | 108 | 0 | 848 |
| `empty/visitor_at_door` | L_empty | 200 | 4892 | 0 | 0.0 | 0 | 0 | 0 | 2 |
| `empty/enters_room` | L_empty | 200 | 10996 | 0 | 0.0 | 0 | 0 | 0 | 8 |
| `empty/page_continues` | L_empty | 200 | 9900 | 0 | 0.0 | 0 | 0 | 0 | 6 |
| `synthetic_cosmological_denamed/visitor_at_door` | L_denamed | 200 | 37901 | 0 | 0.0 | 0 | 0 | 0 | 785 |
| `synthetic_cosmological_denamed/enters_room` | L_denamed | 200 | 33802 | 1 | 0.005 | 0 | 1 | 0 | 640 |
| `synthetic_cosmological_denamed/page_continues` | L_denamed | 200 | 33274 | 129 | 0.645 | 0 | 129 | 0 | 858 |
| `synthetic_cosmological_nonsense/visitor_at_door` | L_nonsense | 200 | 38323 | 1 | 0.005 | 0 | 1 | 0 | 794 |
| `synthetic_cosmological_nonsense/enters_room` | L_nonsense | 200 | 33469 | 0 | 0.0 | 0 | 0 | 0 | 527 |
| `synthetic_cosmological_nonsense/page_continues` | L_nonsense | 200 | 32214 | 85 | 0.425 | 0 | 85 | 0 | 996 |
| `synthetic_cosmological_random/visitor_at_door` | L_random | 200 | 30654 | 0 | 0.0 | 0 | 0 | 0 | 227 |
| `synthetic_cosmological_random/enters_room` | L_random | 200 | 16493 | 0 | 0.0 | 0 | 0 | 0 | 117 |
| `synthetic_cosmological_random/page_continues` | L_random | 200 | 32723 | 0 | 0.0 | 0 | 0 | 0 | 330 |
| `synthetic_litany/visitor_at_door` | L_real | 200 | 5864 | 624 | 3.12 | 620 | 4 | 0 | 0 |
| `synthetic_litany/enters_room` | L_real | 200 | 22966 | 379 | 1.895 | 365 | 14 | 0 | 5 |
| `synthetic_litany/page_continues` | L_real | 200 | 8002 | 1486 | 7.43 | 1478 | 8 | 0 | 0 |
| `synthetic_litany_denamed/visitor_at_door` | L_denamed | 200 | 7447 | 3 | 0.015 | 0 | 3 | 0 | 0 |
| `synthetic_litany_denamed/enters_room` | L_denamed | 200 | 23823 | 8 | 0.04 | 0 | 8 | 0 | 3 |
| `synthetic_litany_denamed/page_continues` | L_denamed | 200 | 8983 | 12 | 0.06 | 0 | 12 | 0 | 5 |
| `synthetic_litany_nonsense/visitor_at_door` | L_nonsense | 200 | 5679 | 4 | 0.02 | 0 | 4 | 0 | 0 |
| `synthetic_litany_nonsense/enters_room` | L_nonsense | 200 | 17679 | 13 | 0.065 | 0 | 13 | 0 | 3 |
| `synthetic_litany_nonsense/page_continues` | L_nonsense | 200 | 8940 | 9 | 0.045 | 0 | 9 | 0 | 8 |
| `synthetic_litany_random/visitor_at_door` | L_random | 200 | 22600 | 0 | 0.0 | 0 | 0 | 0 | 1 |
| `synthetic_litany_random/enters_room` | L_random | 200 | 9175 | 0 | 0.0 | 0 | 0 | 0 | 0 |
| `synthetic_litany_random/page_continues` | L_random | 200 | 28439 | 0 | 0.0 | 0 | 0 | 0 | 0 |

## Top entity hits per cell

### `synthetic_cosmological/visitor_at_door` (L_real)
Named entities:
  - `selephimor` × 131
  - `phorbamenes` × 88
  - `aphrybetesh` × 81
  - `ablakhirim` × 79
  - `sekhthoroba` × 71
  - `athraophol` × 56
  - `phelonoptra` × 30
  - `krathoumis` × 27
  - `phengareb` × 18
  - `khelraphion` × 16
Related vocabulary:
  - `gnostic` × 20
  - `papyri` × 7
  - `theurgy` × 2
  - `pgm` × 1
  - `voces magicae` × 1

### `synthetic_cosmological/enters_room` (L_real)
Named entities:
  - `phengareb` × 85
  - `sekhthoroba` × 49
  - `ablakhirim` × 49
  - `aphrybetesh` × 43
  - `phorbamenes` × 37
  - `selephimor` × 32
  - `khelraphion` × 15
  - `phelonoptra` × 12
  - `thasgorio` × 9
  - `athraophol` × 8

### `synthetic_cosmological/page_continues` (L_real)
Named entities:
  - `selephimor` × 142
  - `phelonoptra` × 117
  - `krathoumis` × 114
  - `aphrybetesh` × 85
  - `phorbamenes` × 79
  - `athraophol` × 68
  - `phengareb` × 26
  - `khelraphion` × 25
  - `demoaphris` × 24
  - `velpharaim` × 16
Related vocabulary:
  - `gnostic` × 57
  - `papyri` × 16
  - `ceremonial` × 14
  - `barbarous` × 7
  - `voces magicae` × 7
  - `pgm` × 4
  - `theurgy` × 3

### `synthetic_cosmological_denamed/enters_room` (L_denamed)
Related vocabulary:
  - `ceremonial` × 1

### `synthetic_cosmological_denamed/page_continues` (L_denamed)
Related vocabulary:
  - `gnostic` × 66
  - `papyri` × 21
  - `ceremonial` × 18
  - `barbarous` × 13
  - `theurgy` × 6
  - `voces magicae` × 3
  - `pgm` × 2

### `synthetic_cosmological_nonsense/visitor_at_door` (L_nonsense)
Related vocabulary:
  - `gnostic` × 1

### `synthetic_cosmological_nonsense/page_continues` (L_nonsense)
Related vocabulary:
  - `gnostic` × 59
  - `ceremonial` × 8
  - `papyri` × 5
  - `theurgy` × 5
  - `barbarous` × 5
  - `voces magicae` × 2
  - `pgm` × 1

### `synthetic_litany/visitor_at_door` (L_real)
Named entities:
  - `liminem adventi` × 47
  - `brashvoreth` × 29
  - `astrelach` × 23
  - `olomar` × 23
  - `throvenios` × 22
  - `iskon` × 22
  - `mirzabet` × 22
  - `mareth` × 21
  - `kerodim` × 21
  - `iathreon` × 21
Related vocabulary:
  - `sigil` × 2
  - `litany` × 2

### `synthetic_litany/enters_room` (L_real)
Named entities:
  - `liminem adventi` × 57
  - `astrelach` × 24
  - `throvenios` × 22
  - `khalapeth` × 18
  - `mareth` × 16
  - `brashvoreth` × 16
  - `sinabaroth` × 15
  - `saphrenoth` × 14
  - `vesperath` × 13
  - `olempraem` × 12
Related vocabulary:
  - `invocation` × 11
  - `sigil` × 3

### `synthetic_litany/page_continues` (L_real)
Named entities:
  - `liminem adventi` × 66
  - `throvenios` × 53
  - `brashvoreth` × 53
  - `mareth` × 52
  - `quelimon` × 52
  - `olempraem` × 52
  - `octaron` × 52
  - `iskon` × 51
  - `kerodim` × 51
  - `astrelach` × 51
Related vocabulary:
  - `litany` × 4
  - `sigil` × 2
  - `invocation` × 2

### `synthetic_litany_denamed/visitor_at_door` (L_denamed)
Related vocabulary:
  - `litany` × 2
  - `invocation` × 1

### `synthetic_litany_denamed/enters_room` (L_denamed)
Related vocabulary:
  - `invocation` × 6
  - `litany` × 2

### `synthetic_litany_denamed/page_continues` (L_denamed)
Related vocabulary:
  - `invocation` × 5
  - `litany` × 5
  - `grimoire` × 1
  - `sigil` × 1

### `synthetic_litany_nonsense/visitor_at_door` (L_nonsense)
Related vocabulary:
  - `litany` × 4

### `synthetic_litany_nonsense/enters_room` (L_nonsense)
Related vocabulary:
  - `invocation` × 8
  - `litany` × 4
  - `sigil` × 1

### `synthetic_litany_nonsense/page_continues` (L_nonsense)
Related vocabulary:
  - `litany` × 5
  - `invocation` × 3
  - `sigil` × 1

## Top lexical divergence per comparison

### vs L_empty (`empty`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `t` | 0 | 20 | -5.078 |
| `him` | 0 | 19 | -5.029 |
| `householder` | 0 | 17 | -4.924 |
| `his` | 0 | 17 | -4.924 |
| `she` | 0 | 17 | -4.924 |
| `m` | 1 | 33 | -4.866 |
| `asks` | 0 | 15 | -4.806 |
| `about` | 1 | 28 | -4.707 |
| `good` | 1 | 28 | -4.707 |
| `look` | 0 | 13 | -4.672 |
| `help` | 1 | 24 | -4.559 |
| `sir` | 0 | 11 | -4.518 |
| `talk` | 0 | 10 | -4.431 |
| `muffled` | 0 | 10 | -4.431 |
| `don` | 0 | 10 | -4.431 |

### vs L_denamed (`synthetic_cosmological_denamed`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `selophemor` | 0 | 186 | -5.217 |
| `unsigned` | 0 | 182 | -5.195 |
| `selephimor` | 131 | 0 | +4.897 |
| `atheraphol` | 0 | 96 | -4.561 |
| `phorbamenes` | 88 | 0 | +4.503 |
| `aphrybetesh` | 81 | 0 | +4.421 |
| `ablakhirim` | 79 | 0 | +4.396 |
| `aphrybetosh` | 0 | 80 | -4.38 |
| `sekhthoroba` | 71 | 0 | +4.291 |
| `sekhthiroba` | 0 | 73 | -4.29 |
| `ablakharim` | 0 | 72 | -4.276 |
| `athraophol` | 56 | 0 | +4.057 |
| `phorbomanes` | 0 | 50 | -3.918 |
| `phelonipta` | 0 | 31 | -3.452 |
| `phelonoptra` | 30 | 0 | +3.448 |

### vs L_nonsense (`synthetic_cosmological_nonsense`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `vrendrelphor` | 0 | 170 | -5.116 |
| `selephimor` | 131 | 0 | +4.908 |
| `phorbamenes` | 88 | 0 | +4.514 |
| `aphrybetesh` | 81 | 0 | +4.432 |
| `ablakhirim` | 79 | 0 | +4.407 |
| `plomprenkrol` | 0 | 77 | -4.332 |
| `sekhthoroba` | 71 | 0 | +4.302 |
| `athraophol` | 56 | 0 | +4.068 |
| `vrolthen` | 0 | 44 | -3.781 |
| `phelonoptra` | 30 | 0 | +3.459 |
| `krathoumis` | 27 | 0 | +3.357 |
| `vrokthelmpeth` | 0 | 28 | -3.342 |
| `phengareb` | 18 | 0 | +2.97 |
| `magical` | 17 | 0 | +2.916 |
| `khelraphion` | 16 | 0 | +2.858 |

### vs L_random (`synthetic_cosmological_random`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `unnamed` | 274 | 0 | +5.419 |
| `river` | 1 | 367 | -5.413 |
| `vessel` | 249 | 0 | +5.323 |
| `echo` | 223 | 0 | +5.214 |
| `fire` | 179 | 0 | +4.995 |
| `re` | 0 | 117 | -4.969 |
| `spoken` | 160 | 0 | +4.883 |
| `named` | 157 | 0 | +4.865 |
| `riparian` | 0 | 99 | -4.803 |
| `health` | 0 | 95 | -4.762 |
| `about` | 1 | 183 | -4.72 |
| `spirits` | 135 | 0 | +4.715 |
| `selephimor` | 131 | 0 | +4.685 |
| `headwaters` | 0 | 84 | -4.641 |
| `invocation` | 124 | 0 | +4.63 |

### vs L_empty (`empty`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `context` | 0 | 157 | -6.197 |
| `re` | 0 | 132 | -6.024 |
| `riddle` | 0 | 123 | -5.954 |
| `situation` | 0 | 113 | -5.87 |
| `details` | 0 | 98 | -5.729 |
| `provide` | 0 | 76 | -5.478 |
| `animal` | 0 | 75 | -5.465 |
| `referring` | 0 | 47 | -5.005 |
| `help` | 0 | 46 | -4.984 |
| `asking` | 0 | 45 | -4.963 |
| `happening` | 0 | 39 | -4.823 |
| `d` | 0 | 39 | -4.823 |
| `information` | 0 | 37 | -4.772 |
| `me` | 0 | 37 | -4.772 |
| `free` | 0 | 35 | -4.717 |

### vs L_denamed (`synthetic_cosmological_denamed`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `unsigned` | 0 | 187 | -5.247 |
| `phengereb` | 0 | 86 | -4.477 |
| `phengareb` | 85 | 0 | +4.443 |
| `selophemor` | 0 | 67 | -4.23 |
| `ablakharim` | 0 | 57 | -4.071 |
| `sekhthiroba` | 0 | 57 | -4.071 |
| `ablakhirim` | 49 | 0 | +3.901 |
| `sekhthoroba` | 49 | 0 | +3.901 |
| `aphrybetesh` | 43 | 0 | +3.773 |
| `aphrybetosh` | 0 | 40 | -3.725 |
| `phorbamenes` | 37 | 0 | +3.627 |
| `selephimor` | 32 | 0 | +3.486 |
| `phorbomanes` | 0 | 30 | -3.445 |
| `atheraphol` | 0 | 22 | -3.146 |
| `aphthalion` | 0 | 15 | -2.784 |

### vs L_nonsense (`synthetic_cosmological_nonsense`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `phengareb` | 85 | 0 | +4.434 |
| `vrendrelphor` | 0 | 59 | -4.115 |
| `vrokthelmpeth` | 0 | 50 | -3.953 |
| `vrolthen` | 0 | 49 | -3.933 |
| `ablakhirim` | 49 | 0 | +3.891 |
| `sekhthoroba` | 49 | 0 | +3.891 |
| `aphrybetesh` | 43 | 0 | +3.763 |
| `phorbamenes` | 37 | 0 | +3.617 |
| `selephimor` | 32 | 0 | +3.476 |
| `smolthekrelb` | 0 | 17 | -2.911 |
| `plendrokrelm` | 0 | 16 | -2.854 |
| `khelraphion` | 15 | 0 | +2.752 |
| `sense` | 0 | 12 | -2.586 |
| `krelpharvon` | 0 | 12 | -2.586 |
| `phelonoptra` | 12 | 0 | +2.544 |

### vs L_random (`synthetic_cosmological_random`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `text` | 0 | 515 | -6.975 |
| `provided` | 0 | 223 | -6.14 |
| `based` | 0 | 204 | -6.052 |
| `ecosystem` | 0 | 163 | -5.828 |
| `river` | 1 | 312 | -5.782 |
| `characteristics` | 0 | 155 | -5.778 |
| `description` | 0 | 152 | -5.759 |
| `scientific` | 0 | 143 | -5.698 |
| `ecosystems` | 0 | 124 | -5.557 |
| `event` | 0 | 122 | -5.541 |
| `factors` | 0 | 112 | -5.456 |
| `health` | 0 | 93 | -5.272 |
| `riddle` | 0 | 90 | -5.239 |
| `mention` | 0 | 87 | -5.206 |
| `biological` | 0 | 82 | -5.147 |

### vs L_empty (`empty`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `help` | 0 | 198 | -6.518 |
| `please` | 0 | 190 | -6.477 |
| `d` | 0 | 190 | -6.477 |
| `content` | 0 | 156 | -6.281 |
| `m` | 0 | 146 | -6.215 |
| `assist` | 0 | 131 | -6.107 |
| `message` | 0 | 128 | -6.084 |
| `off` | 0 | 101 | -5.85 |
| `cut` | 0 | 100 | -5.84 |
| `looks` | 0 | 98 | -5.82 |
| `could` | 1 | 175 | -5.702 |
| `share` | 0 | 82 | -5.644 |
| `provide` | 1 | 155 | -5.581 |
| `need` | 0 | 59 | -5.319 |
| `re` | 0 | 41 | -4.962 |

### vs L_denamed (`synthetic_cosmological_denamed`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `unsigned` | 0 | 207 | -5.35 |
| `selophemor` | 0 | 142 | -4.975 |
| `selephimor` | 142 | 0 | +4.95 |
| `phelonoptra` | 117 | 0 | +4.758 |
| `phelonipta` | 0 | 113 | -4.749 |
| `krathoumis` | 114 | 0 | +4.733 |
| `krethaumis` | 0 | 103 | -4.657 |
| `atheraphol` | 0 | 85 | -4.467 |
| `aphrybetesh` | 85 | 0 | +4.442 |
| `phorbamenes` | 79 | 0 | +4.37 |
| `aphrybetosh` | 0 | 77 | -4.369 |
| `phorbomanes` | 0 | 69 | -4.261 |
| `athraophol` | 68 | 0 | +4.222 |
| `demaphris` | 0 | 38 | -3.676 |
| `phengereb` | 0 | 33 | -3.539 |

### vs L_nonsense (`synthetic_cosmological_nonsense`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `vrolthen` | 0 | 194 | -5.318 |
| `vrendrelphor` | 0 | 148 | -5.049 |
| `vrokthemnarph` | 0 | 134 | -4.95 |
| `selephimor` | 142 | 0 | +4.918 |
| `phelonoptra` | 117 | 0 | +4.726 |
| `krathoumis` | 114 | 0 | +4.7 |
| `smelthrenaph` | 0 | 93 | -4.588 |
| `aphrybetesh` | 85 | 0 | +4.41 |
| `plendrok` | 0 | 75 | -4.376 |
| `phorbamenes` | 79 | 0 | +4.337 |
| `athraophol` | 68 | 0 | +4.189 |
| `vrokthelmpeth` | 0 | 62 | -4.188 |
| `plendrokt` | 0 | 50 | -3.977 |
| `plomprenkrol` | 0 | 47 | -3.916 |
| `krelpharvon` | 0 | 38 | -3.708 |

### vs L_random (`synthetic_cosmological_random`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `unnamed` | 349 | 0 | +5.829 |
| `names` | 345 | 0 | +5.817 |
| `deity` | 327 | 0 | +5.764 |
| `invocation` | 295 | 0 | +5.661 |
| `ecosystems` | 0 | 257 | -5.582 |
| `ecosystem` | 0 | 237 | -5.501 |
| `river` | 2 | 651 | -5.411 |
| `speaker` | 185 | 0 | +5.197 |
| `silence` | 184 | 0 | +5.191 |
| `headwaters` | 0 | 166 | -5.147 |
| `name` | 175 | 0 | +5.141 |
| `ritual` | 165 | 0 | +5.083 |
| `prophet` | 161 | 0 | +5.058 |
| `impacts` | 0 | 151 | -5.053 |
| `lotic` | 0 | 151 | -5.053 |

### vs L_empty (`empty`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `he` | 0 | 70 | -4.444 |
| `say` | 0 | 60 | -4.292 |
| `names` | 83 | 0 | +4.25 |
| `spoken` | 77 | 0 | +4.175 |
| `m` | 0 | 33 | -3.708 |
| `adventi` | 47 | 0 | +3.69 |
| `liminem` | 47 | 0 | +3.69 |
| `opened` | 45 | 0 | +3.647 |
| `way` | 173 | 3 | +3.592 |
| `about` | 0 | 28 | -3.549 |
| `good` | 0 | 28 | -3.549 |
| `path` | 39 | 0 | +3.508 |
| `help` | 0 | 24 | -3.4 |
| `how` | 0 | 23 | -3.359 |
| `known` | 33 | 0 | +3.345 |

### vs L_denamed (`synthetic_litany_denamed`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `adventi` | 47 | 0 | +4.11 |
| `liminem` | 47 | 0 | +4.11 |
| `brashvoreth` | 29 | 0 | +3.64 |
| `lominem` | 0 | 47 | -3.632 |
| `adventu` | 0 | 47 | -3.632 |
| `astrolach` | 0 | 40 | -3.475 |
| `marzabet` | 0 | 40 | -3.475 |
| `iethreon` | 0 | 39 | -3.45 |
| `brashveroth` | 0 | 39 | -3.45 |
| `hialop` | 0 | 38 | -3.425 |
| `throbenas` | 0 | 38 | -3.425 |
| `kerudin` | 0 | 38 | -3.425 |
| `astrelach` | 23 | 0 | +3.417 |
| `olomar` | 23 | 0 | +3.417 |
| `senaberoth` | 0 | 37 | -3.399 |

### vs L_nonsense (`synthetic_litany_nonsense`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `krelphem` | 0 | 50 | -3.964 |
| `skemphrok` | 0 | 49 | -3.944 |
| `adventi` | 47 | 0 | +3.839 |
| `liminem` | 47 | 0 | +3.839 |
| `vrokthemnar` | 0 | 43 | -3.816 |
| `mrolthumek` | 0 | 41 | -3.77 |
| `klompronek` | 0 | 41 | -3.77 |
| `vrendrabmar` | 0 | 40 | -3.746 |
| `snorth` | 0 | 40 | -3.746 |
| `sneldrek` | 0 | 39 | -3.721 |
| `snolthrolm` | 0 | 39 | -3.721 |
| `vroklep` | 0 | 39 | -3.721 |
| `mrolthengek` | 0 | 39 | -3.721 |
| `vronth` | 0 | 39 | -3.721 |
| `plekriskem` | 0 | 38 | -3.696 |

### vs L_random (`synthetic_litany_random`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `names` | 83 | 0 | +5.78 |
| `adventi` | 47 | 0 | +5.22 |
| `liminem` | 47 | 0 | +5.22 |
| `opened` | 45 | 0 | +5.178 |
| `path` | 39 | 0 | +5.038 |
| `brashvoreth` | 29 | 0 | +4.75 |
| `stone` | 25 | 0 | +4.607 |
| `hum` | 25 | 0 | +4.607 |
| `grows` | 24 | 0 | +4.568 |
| `anglerfish` | 0 | 356 | -4.529 |
| `astrelach` | 23 | 0 | +4.527 |
| `olomar` | 23 | 0 | +4.527 |
| `throvenios` | 22 | 0 | +4.485 |
| `iskon` | 22 | 0 | +4.485 |
| `mirzabet` | 22 | 0 | +4.485 |

### vs L_empty (`empty`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `context` | 0 | 157 | -5.799 |
| `re` | 0 | 132 | -5.627 |
| `riddle` | 0 | 123 | -5.557 |
| `situation` | 0 | 113 | -5.473 |
| `person` | 0 | 104 | -5.39 |
| `specific` | 0 | 101 | -5.361 |
| `details` | 0 | 98 | -5.332 |
| `animal` | 0 | 75 | -5.067 |
| `t` | 0 | 73 | -5.041 |
| `idea` | 0 | 59 | -4.831 |
| `about` | 0 | 47 | -4.608 |
| `referring` | 0 | 47 | -4.608 |
| `names` | 196 | 0 | +4.547 |
| `common` | 0 | 40 | -4.45 |
| `happening` | 0 | 39 | -4.425 |

### vs L_denamed (`synthetic_litany_denamed`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `adventi` | 58 | 0 | +4.114 |
| `liminem` | 57 | 0 | +4.097 |
| `adventu` | 0 | 53 | -3.952 |
| `lominem` | 0 | 51 | -3.915 |
| `astrelach` | 24 | 0 | +3.256 |
| `throvenios` | 22 | 0 | +3.172 |
| `astrolach` | 0 | 22 | -3.099 |
| `khalapeth` | 18 | 0 | +2.981 |
| `brashveroth` | 0 | 19 | -2.959 |
| `brashvoreth` | 16 | 0 | +2.87 |
| `mareth` | 16 | 0 | +2.87 |
| `sinabaroth` | 15 | 0 | +2.809 |
| `saphrenoth` | 14 | 0 | +2.745 |
| `marzabet` | 0 | 15 | -2.736 |
| `vesperath` | 13 | 0 | +2.676 |

### vs L_nonsense (`synthetic_litany_nonsense`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `skemphrok` | 0 | 62 | -4.405 |
| `krelphem` | 0 | 58 | -4.339 |
| `adventi` | 58 | 0 | +3.816 |
| `liminem` | 57 | 0 | +3.799 |
| `klompronek` | 0 | 21 | -3.353 |
| `vrokthemnar` | 0 | 17 | -3.152 |
| `sneldrek` | 0 | 16 | -3.095 |
| `mrolthengek` | 0 | 14 | -2.97 |
| `astrelach` | 24 | 0 | +2.957 |
| `snorth` | 0 | 13 | -2.901 |
| `wet` | 0 | 13 | -2.901 |
| `starlight` | 22 | 0 | +2.874 |
| `throvenios` | 22 | 0 | +2.874 |
| `charged` | 20 | 0 | +2.783 |
| `grinding` | 4 | 61 | -2.779 |

### vs L_random (`synthetic_litany_random`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `anglerfish` | 0 | 237 | -6.39 |
| `based` | 0 | 195 | -6.196 |
| `provided` | 0 | 181 | -6.122 |
| `text` | 1 | 299 | -5.928 |
| `about` | 0 | 136 | -5.838 |
| `biology` | 0 | 123 | -5.738 |
| `habitat` | 0 | 120 | -5.713 |
| `solely` | 0 | 91 | -5.439 |
| `describes` | 0 | 91 | -5.439 |
| `description` | 0 | 79 | -5.3 |
| `specific` | 0 | 77 | -5.274 |
| `happening` | 0 | 66 | -5.122 |
| `mention` | 0 | 65 | -5.107 |
| `event` | 1 | 129 | -5.092 |
| `behavior` | 0 | 63 | -5.076 |

### vs L_empty (`empty`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `open` | 141 | 0 | +5.169 |
| `names` | 140 | 0 | +5.162 |
| `help` | 0 | 198 | -5.08 |
| `spoken` | 127 | 0 | +5.065 |
| `please` | 0 | 190 | -5.039 |
| `could` | 0 | 175 | -4.958 |
| `content` | 0 | 156 | -4.843 |
| `provide` | 0 | 155 | -4.837 |
| `m` | 0 | 146 | -4.778 |
| `path` | 94 | 0 | +4.767 |
| `assist` | 0 | 131 | -4.67 |
| `message` | 0 | 128 | -4.647 |
| `adventi` | 67 | 0 | +4.432 |
| `liminem` | 66 | 0 | +4.418 |
| `off` | 0 | 101 | -4.412 |

### vs L_denamed (`synthetic_litany_denamed`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `lominem` | 0 | 93 | -4.428 |
| `adventu` | 0 | 89 | -4.384 |
| `adventi` | 67 | 0 | +4.335 |
| `liminem` | 66 | 0 | +4.32 |
| `brashveroth` | 0 | 72 | -4.175 |
| `throvenios` | 53 | 0 | +4.105 |
| `brashvoreth` | 53 | 0 | +4.105 |
| `olempraem` | 52 | 0 | +4.086 |
| `octaron` | 52 | 0 | +4.086 |
| `quelimon` | 52 | 0 | +4.086 |
| `mareth` | 52 | 0 | +4.086 |
| `astrelach` | 51 | 0 | +4.067 |
| `saphrenoth` | 51 | 0 | +4.067 |
| `crisilim` | 51 | 0 | +4.067 |
| `drabasaim` | 51 | 0 | +4.067 |

### vs L_nonsense (`synthetic_litany_nonsense`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `skemphrok` | 0 | 99 | -4.494 |
| `vrokthemnar` | 0 | 98 | -4.484 |
| `krelphem` | 0 | 96 | -4.464 |
| `snorth` | 0 | 92 | -4.422 |
| `klompronek` | 0 | 92 | -4.422 |
| `sneldrek` | 0 | 90 | -4.4 |
| `mrolthengek` | 0 | 90 | -4.4 |
| `krelphendoth` | 0 | 90 | -4.4 |
| `klomphreth` | 0 | 89 | -4.389 |
| `krendrenel` | 0 | 89 | -4.389 |
| `vrendrelth` | 0 | 89 | -4.389 |
| `snolthrolm` | 0 | 89 | -4.389 |
| `krelphondoth` | 0 | 89 | -4.389 |
| `vronth` | 0 | 89 | -4.389 |
| `plendreol` | 0 | 89 | -4.389 |

### vs L_random (`synthetic_litany_random`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `spoken` | 127 | 0 | +6.12 |
| `path` | 94 | 0 | +5.822 |
| `way` | 163 | 1 | +5.675 |
| `names` | 140 | 1 | +5.524 |
| `adventi` | 67 | 0 | +5.488 |
| `liminem` | 66 | 0 | +5.473 |
| `air` | 54 | 0 | +5.275 |
| `throvenios` | 53 | 0 | +5.257 |
| `brashvoreth` | 53 | 0 | +5.257 |
| `olempraem` | 52 | 0 | +5.238 |
| `octaron` | 52 | 0 | +5.238 |
| `quelimon` | 52 | 0 | +5.238 |
| `mareth` | 52 | 0 | +5.238 |
| `astrelach` | 51 | 0 | +5.219 |
| `saphrenoth` | 51 | 0 | +5.219 |

## Caveats

- Headline yield counts whole-word, case-insensitive matches.
- Ambiguous-tier counts (`Amb-NE`, `Amb-RV`) are tracked but NOT in the headline (common words ⇒ baseline false positives).
- Pairwise comparisons computed per tail. Confidence intervals not yet computed — defer to bootstrap when scaling beyond smoke.