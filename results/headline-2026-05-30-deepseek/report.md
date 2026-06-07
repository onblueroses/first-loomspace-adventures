# Measurements: headline-2026-05-30-deepseek

**Model:** `deepseek/deepseek-v3.2`
**n per cell:** 200
**Source liturgies (L_real):** `astrachios`, `headless`

## Headline comparisons (per-completion rate ratios)

| Source | Comparison | tail | L_real rate | Control rate | Rate ratio | 95% CI | Interpretation |
|---|---|---|---:|---:|---:|---:|---|
| `astrachios` | L_denamed (`astrachios_denamed`) | visitor_at_door | 4.0448 (812/200) | 0.1642 (32/200) | 24.636× | [13.196, 60.308] | positive evidence |
| `astrachios` | L_nonsense (`astrachios_nonsense`) | visitor_at_door | 4.0448 (812/200) | 0.0199 (3/200) | 203.25× | [99.571, 788.0] | positive evidence |
| `astrachios` | L_random (`astrachios_random`) | visitor_at_door | 4.0448 (812/200) | 0.005 (0/200) | 813.0× | [599.0, 1048.0] | positive evidence |
| `astrachios` | L_empty (`empty`) | visitor_at_door | 4.0448 (812/200) | 0.005 (0/200) | 813.0× | [599.0, 1048.0] | positive evidence |
| `astrachios` | L_denamed (`astrachios_denamed`) | enters_room | 1.99 (399/200) | 0.3632 (72/200) | 5.479× | [2.192, 22.111] | positive evidence |
| `astrachios` | L_nonsense (`astrachios_nonsense`) | enters_room | 1.99 (399/200) | 0.1095 (21/200) | 18.182× | [9.0, 35.235] | positive evidence |
| `astrachios` | L_random (`astrachios_random`) | enters_room | 1.99 (399/200) | 0.005 (0/200) | 400.0× | [217.0, 624.0] | positive evidence |
| `astrachios` | L_empty (`empty`) | enters_room | 1.99 (399/200) | 0.005 (0/200) | 400.0× | [217.0, 624.0] | positive evidence |
| `astrachios` | L_denamed (`astrachios_denamed`) | page_continues | 2.9751 (597/200) | 1.2338 (247/200) | 2.411× | [1.619, 3.568] | positive evidence |
| `astrachios` | L_nonsense (`astrachios_nonsense`) | page_continues | 2.9751 (597/200) | 0.1642 (32/200) | 18.121× | [9.851, 50.091] | positive evidence |
| `astrachios` | L_random (`astrachios_random`) | page_continues | 2.9751 (597/200) | 0.005 (0/200) | 598.0× | [492.0, 729.0] | positive evidence |
| `astrachios` | L_empty (`empty`) | page_continues | 2.9751 (597/200) | 0.005 (0/200) | 598.0× | [492.0, 729.0] | positive evidence |
| `headless` | L_empty (`empty`) | visitor_at_door | 4.9403 (992/200) | 0.005 (0/200) | 993.0× | [912.0, 1074.0] | positive evidence |
| `headless` | L_denamed (`headless_denamed`) | visitor_at_door | 4.9403 (992/200) | 0.6368 (127/200) | 7.758× | [5.867, 10.778] | positive evidence |
| `headless` | L_nonsense (`headless_nonsense`) | visitor_at_door | 4.9403 (992/200) | 0.5224 (104/200) | 9.457× | [7.248, 12.988] | positive evidence |
| `headless` | L_random (`headless_random`) | visitor_at_door | 4.9403 (992/200) | 0.005 (0/200) | 993.0× | [912.0, 1074.0] | positive evidence |
| `headless` | L_empty (`empty`) | enters_room | 4.1144 (826/200) | 0.005 (0/200) | 827.0× | [772.0, 885.0] | positive evidence |
| `headless` | L_denamed (`headless_denamed`) | enters_room | 4.1144 (826/200) | 0.5871 (117/200) | 7.008× | [5.407, 9.511] | positive evidence |
| `headless` | L_nonsense (`headless_nonsense`) | enters_room | 4.1144 (826/200) | 0.2388 (47/200) | 17.229× | [12.94, 24.303] | positive evidence |
| `headless` | L_random (`headless_random`) | enters_room | 4.1144 (826/200) | 0.005 (0/200) | 827.0× | [772.0, 885.0] | positive evidence |
| `headless` | L_empty (`empty`) | page_continues | 5.7662 (1158/200) | 0.005 (0/200) | 1159.0× | [1091.0, 1231.0] | positive evidence |
| `headless` | L_denamed (`headless_denamed`) | page_continues | 5.7662 (1158/200) | 3.7015 (743/200) | 1.558× | [1.424, 1.711] | null (within 2× either direction) |
| `headless` | L_nonsense (`headless_nonsense`) | page_continues | 5.7662 (1158/200) | 2.7662 (555/200) | 2.085× | [1.876, 2.329] | positive evidence |
| `headless` | L_random (`headless_random`) | page_continues | 5.7662 (1158/200) | 0.005 (0/200) | 1159.0× | [1091.0, 1231.0] | positive evidence |

## Per-cell

| Cell | Role | n | Tokens | Headline yield | /completion | NE | RV | Amb-NE | Amb-RV |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `astrachios/visitor_at_door` | L_real | 200 | 28494 | 812 | 4.06 | 650 | 162 | 56 | 382 |
| `astrachios/enters_room` | L_real | 200 | 37783 | 399 | 1.995 | 341 | 58 | 25 | 498 |
| `astrachios/page_continues` | L_real | 200 | 36910 | 597 | 2.985 | 310 | 287 | 14 | 669 |
| `astrachios_denamed/visitor_at_door` | L_denamed | 200 | 38764 | 32 | 0.16 | 14 | 18 | 0 | 548 |
| `astrachios_denamed/enters_room` | L_denamed | 200 | 38415 | 72 | 0.36 | 26 | 46 | 0 | 515 |
| `astrachios_denamed/page_continues` | L_denamed | 200 | 35307 | 247 | 1.235 | 107 | 140 | 5 | 645 |
| `astrachios_nonsense/visitor_at_door` | L_nonsense | 200 | 18061 | 3 | 0.015 | 0 | 3 | 0 | 102 |
| `astrachios_nonsense/enters_room` | L_nonsense | 200 | 21353 | 21 | 0.105 | 0 | 21 | 0 | 60 |
| `astrachios_nonsense/page_continues` | L_nonsense | 200 | 11863 | 32 | 0.16 | 7 | 25 | 0 | 34 |
| `astrachios_random/visitor_at_door` | L_random | 200 | 27262 | 0 | 0.0 | 0 | 0 | 0 | 13 |
| `astrachios_random/enters_room` | L_random | 200 | 15048 | 0 | 0.0 | 0 | 0 | 0 | 2 |
| `astrachios_random/page_continues` | L_random | 200 | 32909 | 0 | 0.0 | 0 | 0 | 0 | 5 |
| `empty/visitor_at_door` | L_empty | 200 | 3686 | 0 | 0.0 | 0 | 0 | 0 | 6 |
| `empty/enters_room` | L_empty | 200 | 10362 | 0 | 0.0 | 0 | 0 | 0 | 0 |
| `empty/page_continues` | L_empty | 200 | 7717 | 0 | 0.0 | 0 | 0 | 0 | 0 |
| `headless/visitor_at_door` | L_real | 200 | 34108 | 992 | 4.96 | 603 | 389 | 92 | 1269 |
| `headless/enters_room` | L_real | 200 | 34445 | 826 | 4.13 | 525 | 301 | 143 | 1217 |
| `headless/page_continues` | L_real | 200 | 31367 | 1158 | 5.79 | 332 | 826 | 23 | 1130 |
| `headless_denamed/visitor_at_door` | L_denamed | 200 | 37008 | 127 | 0.635 | 5 | 122 | 0 | 1054 |
| `headless_denamed/enters_room` | L_denamed | 200 | 36231 | 117 | 0.585 | 2 | 115 | 2 | 892 |
| `headless_denamed/page_continues` | L_denamed | 200 | 31378 | 743 | 3.715 | 0 | 743 | 1 | 1226 |
| `headless_nonsense/visitor_at_door` | L_nonsense | 200 | 35990 | 104 | 0.52 | 0 | 104 | 0 | 1024 |
| `headless_nonsense/enters_room` | L_nonsense | 200 | 36458 | 47 | 0.235 | 0 | 47 | 0 | 922 |
| `headless_nonsense/page_continues` | L_nonsense | 200 | 31357 | 555 | 2.775 | 0 | 555 | 0 | 1309 |
| `headless_random/visitor_at_door` | L_random | 200 | 28512 | 0 | 0.0 | 0 | 0 | 0 | 139 |
| `headless_random/enters_room` | L_random | 200 | 15083 | 0 | 0.0 | 0 | 0 | 0 | 131 |
| `headless_random/page_continues` | L_random | 200 | 32693 | 0 | 0.0 | 0 | 0 | 0 | 191 |

## Top entity hits per cell

### `astrachios/visitor_at_door` (L_real)
Named entities:
  - `adonai` × 50
  - `elohim` × 47
  - `bael` × 40
  - `samoel` × 31
  - `geburahel` × 30
  - `genium domos` × 30
  - `astrachios` × 27
  - `asac` × 24
  - `scirlin` × 24
  - `arabonas` × 23
Related vocabulary:
  - `invocation` × 53
  - `solomonic` × 44
  - `grimoire` × 24
  - `conjuration` × 16
  - `goetia` × 8
  - `tetragrammaton` × 6
  - `lemegeton` × 6
  - `kabbalah` × 3
  - `sigil` × 2

### `astrachios/enters_room` (L_real)
Named entities:
  - `adonai` × 26
  - `baracata` × 25
  - `elohim` × 23
  - `genium domos` × 15
  - `silat` × 13
  - `asac` × 12
  - `arabonas` × 12
  - `geburahel` × 12
  - `elohi` × 12
  - `bael` × 12
Related vocabulary:
  - `tetragrammaton` × 21
  - `invocation` × 16
  - `solomonic` × 7
  - `conjuration` × 3
  - `grimoire` × 2
  - `sigil` × 2
  - `lemegeton` × 2
  - `litany` × 2
  - `pentacle` × 2
  - `kabbalah` × 1

### `astrachios/page_continues` (L_real)
Named entities:
  - `adonai` × 97
  - `elohim` × 70
  - `bael` × 14
  - `elohi` × 13
  - `samoel` × 9
  - `achsah` × 8
  - `genium domos` × 7
  - `astrachios` × 6
  - `asac` × 6
  - `arabonas` × 6
Related vocabulary:
  - `tetragrammaton` × 112
  - `conjuration` × 66
  - `pentacle` × 33
  - `invocation` × 28
  - `grimoire` × 22
  - `goetia` × 15
  - `psalm` × 5
  - `sigil` × 4
  - `kabbalah` × 2

### `astrachios_denamed/visitor_at_door` (L_denamed)
Named entities:
  - `adonai` × 8
  - `elohim` × 5
  - `achsah` × 1
Related vocabulary:
  - `invocation` × 9
  - `grimoire` × 5
  - `conjuration` × 2
  - `tetragrammaton` × 2

### `astrachios_denamed/enters_room` (L_denamed)
Named entities:
  - `elohim` × 16
  - `adonai` × 10
Related vocabulary:
  - `conjuration` × 27
  - `tetragrammaton` × 7
  - `sigil` × 6
  - `invocation` × 3
  - `genius` × 2
  - `goetia` × 1

### `astrachios_denamed/page_continues` (L_denamed)
Named entities:
  - `samoel` × 38
  - `adonai` × 36
  - `elohim` × 26
  - `elohi` × 4
  - `emagro` × 1
  - `abragateh` × 1
  - `bael` × 1
Related vocabulary:
  - `conjuration` × 47
  - `tetragrammaton` × 39
  - `invocation` × 23
  - `grimoire` × 11
  - `sigil` × 9
  - `goetia` × 4
  - `pentacle` × 4
  - `kabbalah` × 2
  - `psalm` × 1

### `astrachios_nonsense/visitor_at_door` (L_nonsense)
Related vocabulary:
  - `conjuration` × 1
  - `invocation` × 1
  - `litany` × 1

### `astrachios_nonsense/enters_room` (L_nonsense)
Related vocabulary:
  - `invocation` × 15
  - `sigil` × 5
  - `conjuration` × 1

### `astrachios_nonsense/page_continues` (L_nonsense)
Named entities:
  - `adonai` × 3
  - `elohim` × 3
  - `elohi` × 1
Related vocabulary:
  - `invocation` × 11
  - `grimoire` × 5
  - `conjuration` × 5
  - `sigil` × 1
  - `tetragrammaton` × 1
  - `goetia` × 1
  - `litany` × 1

### `headless/visitor_at_door` (L_real)
Named entities:
  - `mosheh` × 112
  - `osoronnophris` × 98
  - `iaō` × 61
  - `sabaōth` × 51
  - `iabou` × 47
  - `aphrael` × 44
  - `sabaoth` × 39
  - `ablathanalba` × 37
  - `iapos` × 35
  - `abaoth` × 23
Related vocabulary:
  - `ceremonial` × 102
  - `pgm` × 81
  - `papyri` × 78
  - `barbarous` × 48
  - `gnostic` × 26
  - `stele` × 20
  - `jeu` × 20
  - `theurgy` × 9
  - `voces magicae` × 5

### `headless/enters_room` (L_real)
Named entities:
  - `osoronnophris` × 94
  - `iaō` × 89
  - `sabaōth` × 79
  - `ablathanalba` × 50
  - `mosheh` × 49
  - `aphrael` × 48
  - `arogogorobrao` × 37
  - `thiao` × 15
  - `sabaoth` × 14
  - `rheibet` × 14
Related vocabulary:
  - `ceremonial` × 90
  - `papyri` × 87
  - `pgm` × 49
  - `barbarous` × 26
  - `stele` × 17
  - `jeu` × 17
  - `gnostic` × 6
  - `hellenistic` × 5
  - `theurgy` × 4

### `headless/page_continues` (L_real)
Named entities:
  - `osoronnophris` × 87
  - `akephalos` × 44
  - `iabou` × 37
  - `sabaoth` × 35
  - `iapos` × 33
  - `mosheh` × 25
  - `abaoth` × 20
  - `iaō` × 16
  - `sabaōth` × 12
  - `aphrael` × 5
Related vocabulary:
  - `pgm` × 298
  - `papyri` × 211
  - `ceremonial` × 89
  - `stele` × 73
  - `jeu` × 73
  - `gnostic` × 33
  - `barbarous` × 19
  - `hellenistic` × 13
  - `theurgy` × 10
  - `voces magicae` × 7

### `headless_denamed/visitor_at_door` (L_denamed)
Named entities:
  - `iaō` × 3
  - `iao` × 1
  - `akephalos` × 1
Related vocabulary:
  - `gnostic` × 49
  - `papyri` × 26
  - `pgm` × 18
  - `voces magicae` × 10
  - `barbarous` × 8
  - `hellenistic` × 7
  - `theurgy` × 3
  - `ceremonial` × 1

### `headless_denamed/enters_room` (L_denamed)
Named entities:
  - `iaō` × 2
Related vocabulary:
  - `papyri` × 47
  - `gnostic` × 32
  - `pgm` × 18
  - `barbarous` × 10
  - `stele` × 2
  - `jeu` × 2
  - `ceremonial` × 2
  - `voces magicae` × 2

### `headless_denamed/page_continues` (L_denamed)
Related vocabulary:
  - `gnostic` × 277
  - `papyri` × 163
  - `pgm` × 123
  - `voces magicae` × 91
  - `barbarous` × 52
  - `hellenistic` × 27
  - `theurgy` × 7
  - `ceremonial` × 2
  - `jeu` × 1

### `headless_nonsense/visitor_at_door` (L_nonsense)
Related vocabulary:
  - `gnostic` × 60
  - `papyri` × 24
  - `barbarous` × 7
  - `ceremonial` × 7
  - `theurgy` × 3
  - `voces magicae` × 2
  - `pgm` × 1

### `headless_nonsense/enters_room` (L_nonsense)
Related vocabulary:
  - `gnostic` × 33
  - `papyri` × 10
  - `ceremonial` × 2
  - `hellenistic` × 1
  - `theurgy` × 1

### `headless_nonsense/page_continues` (L_nonsense)
Related vocabulary:
  - `gnostic` × 247
  - `papyri` × 148
  - `barbarous` × 46
  - `pgm` × 40
  - `voces magicae` × 39
  - `ceremonial` × 25
  - `theurgy` × 8
  - `hellenistic` × 2

## Top lexical divergence per comparison

### vs L_denamed (`astrachios_denamed`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `spiritual` | 117 | 0 | +5.078 |
| `esoteric` | 70 | 0 | +4.57 |
| `context` | 70 | 0 | +4.57 |
| `historical` | 62 | 0 | +4.451 |
| `texts` | 59 | 0 | +4.402 |
| `part` | 57 | 0 | +4.368 |
| `such` | 99 | 1 | +4.22 |
| `grimoires` | 45 | 0 | +4.136 |
| `solomonic` | 44 | 0 | +4.114 |
| `ie` | 0 | 77 | -4.049 |
| `western` | 41 | 0 | +4.045 |
| `bael` | 40 | 0 | +4.021 |
| `symbolic` | 38 | 0 | +3.971 |
| `would` | 37 | 0 | +3.945 |
| `daniel` | 36 | 0 | +3.919 |

### vs L_nonsense (`astrachios_nonsense`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `kresnopith` | 0 | 57 | -4.516 |
| `onthropor` | 0 | 56 | -4.499 |
| `mreph` | 0 | 50 | -4.388 |
| `krelmonor` | 0 | 48 | -4.348 |
| `spiritual` | 117 | 0 | +4.315 |
| `polisornen` | 0 | 46 | -4.306 |
| `aethyr` | 0 | 46 | -4.306 |
| `such` | 99 | 0 | +4.149 |
| `glothenkion` | 0 | 38 | -4.12 |
| `vrindat` | 0 | 38 | -4.12 |
| `tronosemath` | 0 | 37 | -4.094 |
| `tholerpa` | 0 | 37 | -4.094 |
| `horn` | 0 | 37 | -4.094 |
| `rephonex` | 0 | 37 | -4.094 |
| `kromphis` | 0 | 37 | -4.094 |

### vs L_random (`astrachios_random`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `kakapo` | 0 | 593 | -6.431 |
| `names` | 339 | 0 | +5.785 |
| `parrot` | 0 | 210 | -5.396 |
| `new` | 0 | 139 | -4.986 |
| `zealand` | 0 | 131 | -4.927 |
| `endangered` | 0 | 126 | -4.888 |
| `angel` | 126 | 0 | +4.8 |
| `flightless` | 0 | 110 | -4.754 |
| `spiritual` | 117 | 0 | +4.726 |
| `conservation` | 0 | 107 | -4.726 |
| `spirit` | 116 | 0 | +4.718 |
| `unique` | 0 | 103 | -4.689 |
| `critically` | 0 | 96 | -4.619 |
| `spirits` | 91 | 0 | +4.478 |
| `power` | 90 | 0 | +4.467 |

### vs L_empty (`empty`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `muffled` | 0 | 15 | -4.818 |
| `stranger` | 0 | 12 | -4.61 |
| `hello` | 0 | 12 | -4.61 |
| `slightly` | 0 | 9 | -4.348 |
| `sorry` | 0 | 8 | -4.242 |
| `side` | 2 | 26 | -4.242 |
| `find` | 2 | 25 | -4.205 |
| `calm` | 0 | 7 | -4.125 |
| `standing` | 2 | 23 | -4.125 |
| `tone` | 0 | 7 | -4.125 |
| `told` | 0 | 7 | -4.125 |
| `look` | 1 | 14 | -4.06 |
| `reaches` | 0 | 6 | -3.991 |
| `just` | 0 | 6 | -3.991 |
| `anyone` | 0 | 6 | -3.991 |

### vs L_denamed (`astrachios_denamed`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `sorry` | 67 | 0 | +4.236 |
| `flies` | 47 | 0 | +3.888 |
| `familiar` | 46 | 0 | +3.867 |
| `yos` | 0 | 45 | -3.812 |
| `quiet` | 0 | 43 | -3.768 |
| `spiritual` | 41 | 0 | +3.754 |
| `ata` | 0 | 42 | -3.745 |
| `game` | 0 | 42 | -3.745 |
| `often` | 34 | 0 | +3.572 |
| `belongs` | 0 | 35 | -3.567 |
| `stay` | 0 | 34 | -3.539 |
| `safe` | 0 | 34 | -3.539 |
| `watches` | 30 | 0 | +3.451 |
| `sopro` | 0 | 31 | -3.449 |
| `fly` | 0 | 29 | -3.385 |

### vs L_nonsense (`astrachios_nonsense`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `onthropor` | 0 | 74 | -4.888 |
| `hum` | 0 | 64 | -4.745 |
| `kresnopith` | 0 | 56 | -4.614 |
| `vronth` | 0 | 47 | -4.442 |
| `revealed` | 0 | 46 | -4.421 |
| `shifting` | 1 | 81 | -4.284 |
| `syllables` | 0 | 29 | -3.972 |
| `thresholds` | 0 | 27 | -3.903 |
| `grateful` | 0 | 26 | -3.867 |
| `syllable` | 0 | 24 | -3.79 |
| `contains` | 0 | 22 | -3.706 |
| `glothenkion` | 0 | 21 | -3.662 |
| `cube` | 0 | 21 | -3.662 |
| `coalesces` | 0 | 21 | -3.662 |
| `sorry` | 67 | 0 | +3.649 |

### vs L_random (`astrachios_random`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `kakapo` | 0 | 373 | -6.845 |
| `text` | 0 | 281 | -6.563 |
| `parrot` | 0 | 212 | -6.282 |
| `provided` | 0 | 189 | -6.168 |
| `description` | 0 | 166 | -6.039 |
| `event` | 0 | 132 | -5.811 |
| `solely` | 0 | 111 | -5.639 |
| `factual` | 0 | 103 | -5.565 |
| `conservation` | 0 | 103 | -5.565 |
| `status` | 0 | 99 | -5.526 |
| `based` | 1 | 174 | -5.392 |
| `information` | 1 | 167 | -5.351 |
| `habitat` | 0 | 82 | -5.339 |
| `am` | 519 | 0 | +5.333 |
| `action` | 0 | 74 | -5.238 |

### vs L_empty (`empty`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `situation` | 0 | 115 | -6.047 |
| `riddle` | 0 | 104 | -5.948 |
| `details` | 0 | 95 | -5.858 |
| `object` | 0 | 54 | -5.301 |
| `idea` | 0 | 47 | -5.165 |
| `referring` | 0 | 44 | -5.1 |
| `describing` | 0 | 39 | -4.983 |
| `provide` | 1 | 79 | -4.983 |
| `am` | 519 | 0 | +4.96 |
| `scenario` | 0 | 36 | -4.905 |
| `describe` | 1 | 65 | -4.79 |
| `puzzle` | 0 | 32 | -4.79 |
| `happening` | 0 | 31 | -4.759 |
| `information` | 1 | 58 | -4.678 |
| `access` | 0 | 28 | -4.661 |

### vs L_denamed (`astrachios_denamed`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `hel` | 126 | 0 | +4.8 |
| `sa` | 0 | 101 | -4.669 |
| `achiel` | 0 | 84 | -4.487 |
| `samiel` | 0 | 83 | -4.475 |
| `astrape` | 0 | 73 | -4.348 |
| `achayo` | 0 | 63 | -4.203 |
| `aya` | 0 | 53 | -4.033 |
| `iahiel` | 0 | 36 | -3.655 |
| `nomen` | 37 | 0 | +3.593 |
| `semo` | 32 | 0 | +3.452 |
| `seme` | 31 | 0 | +3.421 |
| `est` | 29 | 0 | +3.357 |
| `aniel` | 3 | 97 | -3.243 |
| `quod` | 22 | 0 | +3.091 |
| `per` | 43 | 1 | +3.047 |

### vs L_nonsense (`astrachios_nonsense`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `onthropor` | 0 | 88 | -5.624 |
| `kresnopith` | 0 | 86 | -5.601 |
| `onth` | 0 | 70 | -5.398 |
| `polisornen` | 0 | 67 | -5.355 |
| `tholgardosen` | 0 | 66 | -5.34 |
| `rephonex` | 0 | 66 | -5.34 |
| `snolpharod` | 0 | 66 | -5.34 |
| `kresnopontren` | 0 | 66 | -5.34 |
| `klimp` | 0 | 66 | -5.34 |
| `tromporada` | 0 | 66 | -5.34 |
| `kroslendep` | 0 | 65 | -5.325 |
| `antrundefax` | 0 | 65 | -5.325 |
| `tronosemath` | 0 | 65 | -5.325 |
| `engrokitha` | 0 | 65 | -5.325 |
| `krelmonor` | 0 | 65 | -5.325 |

### vs L_random (`astrachios_random`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `kakapo` | 0 | 395 | -6.096 |
| `god` | 391 | 0 | +5.857 |
| `breeding` | 0 | 288 | -5.781 |
| `unique` | 0 | 226 | -5.54 |
| `conservation` | 0 | 215 | -5.49 |
| `parrot` | 0 | 188 | -5.356 |
| `holy` | 209 | 0 | +5.232 |
| `males` | 0 | 163 | -5.215 |
| `my` | 190 | 0 | +5.138 |
| `lord` | 188 | 0 | +5.127 |
| `thy` | 183 | 0 | +5.1 |
| `feathers` | 0 | 144 | -5.091 |
| `thou` | 176 | 0 | +5.061 |
| `forest` | 0 | 138 | -5.049 |
| `diet` | 0 | 138 | -5.049 |

### vs L_empty (`empty`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `message` | 0 | 165 | -6.677 |
| `provide` | 0 | 161 | -6.653 |
| `looks` | 0 | 158 | -6.634 |
| `please` | 1 | 189 | -6.119 |
| `d` | 1 | 188 | -6.114 |
| `cut` | 1 | 149 | -5.883 |
| `could` | 2 | 178 | -5.654 |
| `need` | 0 | 48 | -5.457 |
| `clarify` | 0 | 43 | -5.349 |
| `got` | 1 | 78 | -5.241 |
| `started` | 0 | 37 | -5.203 |
| `content` | 2 | 112 | -5.194 |
| `share` | 1 | 65 | -5.062 |
| `off` | 4 | 149 | -4.966 |
| `however` | 0 | 25 | -4.823 |

### vs L_empty (`empty`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `say` | 2 | 101 | -5.751 |
| `open` | 0 | 27 | -5.557 |
| `side` | 0 | 26 | -5.521 |
| `find` | 0 | 25 | -5.483 |
| `help` | 0 | 17 | -5.115 |
| `muffled` | 0 | 15 | -4.998 |
| `look` | 0 | 14 | -4.933 |
| `there` | 1 | 27 | -4.864 |
| `do` | 9 | 130 | -4.798 |
| `waits` | 0 | 12 | -4.79 |
| `stranger` | 0 | 12 | -4.79 |
| `hello` | 0 | 12 | -4.79 |
| `carries` | 0 | 11 | -4.71 |
| `waiting` | 0 | 8 | -4.422 |
| `sorry` | 0 | 8 | -4.422 |

### vs L_denamed (`headless_denamed`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `preliminary` | 199 | 0 | +5.38 |
| `headless` | 473 | 2 | +5.144 |
| `tongueless` | 0 | 182 | -5.128 |
| `nopheth` | 0 | 172 | -5.072 |
| `coil` | 0 | 134 | -4.824 |
| `mosheh` | 112 | 0 | +4.809 |
| `pulse` | 0 | 125 | -4.755 |
| `osoronnophris` | 98 | 0 | +4.677 |
| `wound` | 0 | 113 | -4.655 |
| `moses` | 91 | 0 | +4.603 |
| `bornless` | 181 | 1 | +4.592 |
| `daimon` | 87 | 0 | +4.559 |
| `guardian` | 74 | 0 | +4.399 |
| `holy` | 74 | 0 | +4.399 |
| `establish` | 73 | 0 | +4.386 |

### vs L_nonsense (`headless_nonsense`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `headless` | 473 | 0 | +6.215 |
| `preliminary` | 199 | 0 | +5.352 |
| `bornless` | 181 | 0 | +5.258 |
| `vrondh` | 0 | 193 | -5.214 |
| `mrolthen` | 0 | 191 | -5.204 |
| `goetia` | 115 | 0 | +4.807 |
| `mosheh` | 112 | 0 | +4.781 |
| `osoronnophris` | 98 | 0 | +4.649 |
| `smelphenor` | 0 | 102 | -4.581 |
| `moses` | 91 | 0 | +4.575 |
| `daimon` | 87 | 0 | +4.531 |
| `golden` | 80 | 0 | +4.448 |
| `dawn` | 80 | 0 | +4.448 |
| `holy` | 74 | 0 | +4.371 |
| `higher` | 72 | 0 | +4.344 |

### vs L_random (`headless_random`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `invocation` | 544 | 0 | +6.122 |
| `ritual` | 537 | 0 | +6.109 |
| `headless` | 473 | 0 | +5.982 |
| `divine` | 390 | 0 | +5.79 |
| `plate` | 0 | 147 | -5.176 |
| `plates` | 0 | 147 | -5.176 |
| `we` | 0 | 146 | -5.17 |
| `preliminary` | 199 | 0 | +5.119 |
| `names` | 184 | 0 | +5.041 |
| `bornless` | 181 | 0 | +5.025 |
| `god` | 159 | 0 | +4.896 |
| `spirits` | 153 | 0 | +4.858 |
| `magician` | 145 | 0 | +4.804 |
| `deity` | 144 | 0 | +4.798 |
| `re` | 0 | 93 | -4.723 |

### vs L_empty (`empty`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `re` | 0 | 136 | -6.121 |
| `t` | 0 | 116 | -5.963 |
| `situation` | 0 | 115 | -5.955 |
| `riddle` | 0 | 104 | -5.855 |
| `details` | 0 | 95 | -5.766 |
| `person` | 0 | 84 | -5.644 |
| `provide` | 0 | 79 | -5.583 |
| `help` | 0 | 78 | -5.571 |
| `give` | 0 | 76 | -5.545 |
| `don` | 0 | 66 | -5.406 |
| `ritual` | 674 | 0 | +5.313 |
| `animal` | 0 | 59 | -5.296 |
| `information` | 0 | 58 | -5.279 |
| `need` | 0 | 55 | -5.227 |
| `object` | 0 | 54 | -5.209 |

### vs L_denamed (`headless_denamed`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `headless` | 465 | 1 | +5.502 |
| `tongueless` | 0 | 223 | -5.361 |
| `preliminary` | 146 | 0 | +5.041 |
| `higher` | 110 | 0 | +4.76 |
| `holy` | 103 | 0 | +4.695 |
| `guardian` | 102 | 0 | +4.685 |
| `pulse` | 0 | 106 | -4.622 |
| `iōm` | 0 | 105 | -4.613 |
| `osoronnophris` | 94 | 0 | +4.604 |
| `sapenōth` | 0 | 103 | -4.594 |
| `coil` | 0 | 92 | -4.482 |
| `sabaōth` | 79 | 0 | +4.433 |
| `nopheth` | 0 | 87 | -4.427 |
| `wound` | 0 | 80 | -4.344 |
| `girt` | 66 | 0 | +4.255 |

### vs L_nonsense (`headless_nonsense`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `headless` | 465 | 0 | +6.201 |
| `bornless` | 182 | 0 | +5.266 |
| `mrolthen` | 0 | 200 | -5.247 |
| `rite` | 174 | 0 | +5.222 |
| `preliminary` | 146 | 0 | +5.047 |
| `daimon` | 142 | 0 | +5.02 |
| `magician` | 229 | 1 | +4.802 |
| `vrondh` | 0 | 108 | -4.635 |
| `osoronnophris` | 94 | 0 | +4.611 |
| `goetia` | 92 | 0 | +4.589 |
| `iaō` | 89 | 0 | +4.557 |
| `cold` | 0 | 94 | -4.497 |
| `sabaōth` | 79 | 0 | +4.439 |
| `girt` | 66 | 0 | +4.261 |
| `serpent` | 65 | 0 | +4.246 |

### vs L_random (`headless_random`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `plate` | 0 | 255 | -6.371 |
| `tectonics` | 0 | 206 | -6.159 |
| `scientific` | 0 | 172 | -5.979 |
| `theory` | 0 | 163 | -5.926 |
| `passage` | 0 | 139 | -5.767 |
| `ritual` | 674 | 0 | +5.689 |
| `geological` | 0 | 105 | -5.489 |
| `divine` | 503 | 0 | +5.397 |
| `headless` | 465 | 0 | +5.318 |
| `narrative` | 0 | 87 | -5.303 |
| `invocation` | 438 | 0 | +5.259 |
| `event` | 0 | 78 | -5.195 |
| `solely` | 0 | 69 | -5.074 |
| `entirely` | 0 | 67 | -5.045 |
| `lithosphere` | 0 | 66 | -5.03 |

### vs L_empty (`empty`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `please` | 0 | 189 | -6.649 |
| `d` | 0 | 188 | -6.644 |
| `what` | 0 | 182 | -6.612 |
| `could` | 0 | 178 | -6.59 |
| `message` | 0 | 165 | -6.514 |
| `provide` | 0 | 161 | -6.49 |
| `looks` | 0 | 158 | -6.471 |
| `cut` | 0 | 149 | -6.413 |
| `off` | 0 | 149 | -6.413 |
| `assist` | 0 | 147 | -6.4 |
| `know` | 0 | 133 | -6.3 |
| `help` | 1 | 201 | -6.017 |
| `m` | 1 | 170 | -5.851 |
| `full` | 0 | 83 | -5.833 |
| `rest` | 0 | 81 | -5.809 |

### vs L_denamed (`headless_denamed`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `headless` | 551 | 0 | +6.314 |
| `tongueless` | 0 | 254 | -5.541 |
| `asarinopis` | 0 | 169 | -5.135 |
| `iarol` | 0 | 154 | -5.043 |
| `itos` | 0 | 152 | -5.03 |
| `sapenoth` | 0 | 140 | -4.948 |
| `apenoth` | 0 | 134 | -4.905 |
| `preliminary` | 133 | 0 | +4.898 |
| `crowley` | 105 | 0 | +4.664 |
| `bornless` | 199 | 1 | +4.606 |
| `aleister` | 95 | 0 | +4.565 |
| `nopheth` | 0 | 91 | -4.521 |
| `osoronnophris` | 87 | 0 | +4.478 |
| `v` | 168 | 1 | +4.437 |
| `goetia` | 83 | 0 | +4.431 |

### vs L_nonsense (`headless_nonsense`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `headless` | 551 | 0 | +6.313 |
| `mrolthen` | 0 | 202 | -5.314 |
| `bornless` | 199 | 0 | +5.298 |
| `vrelthemphos` | 0 | 198 | -5.294 |
| `style` | 0 | 160 | -5.082 |
| `significance` | 157 | 0 | +5.062 |
| `vrondh` | 0 | 156 | -5.057 |
| `klepth` | 0 | 150 | -5.018 |
| `mronth` | 0 | 148 | -5.004 |
| `specifically` | 141 | 0 | +4.956 |
| `preliminary` | 133 | 0 | +4.898 |
| `invented` | 0 | 130 | -4.876 |
| `formless` | 111 | 0 | +4.718 |
| `century` | 107 | 0 | +4.682 |
| `adapted` | 106 | 0 | +4.673 |

### vs L_random (`headless_random`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `plate` | 0 | 800 | -6.644 |
| `headless` | 551 | 0 | +6.355 |
| `ritual` | 549 | 0 | +6.351 |
| `invocation` | 493 | 0 | +6.244 |
| `plates` | 0 | 531 | -6.235 |
| `magical` | 338 | 0 | +5.867 |
| `boundaries` | 0 | 339 | -5.788 |
| `tectonics` | 0 | 325 | -5.745 |
| `pgm` | 298 | 0 | +5.742 |
| `lithosphere` | 0 | 301 | -5.669 |
| `oceanic` | 0 | 271 | -5.564 |
| `divine` | 243 | 0 | +5.539 |
| `deity` | 229 | 0 | +5.479 |
| `crust` | 0 | 246 | -5.468 |
| `mantle` | 0 | 241 | -5.448 |

## Caveats

- Headline yield counts whole-word, case-insensitive matches.
- Ambiguous-tier counts (`Amb-NE`, `Amb-RV`) are tracked but NOT in the headline (common words ⇒ baseline false positives).
- Pairwise comparisons computed per tail. Confidence intervals not yet computed — defer to bootstrap when scaling beyond smoke.