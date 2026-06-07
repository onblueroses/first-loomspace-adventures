# Measurements: headline-2026-05-30-hermes

**Model:** `nousresearch/hermes-3-llama-3.1-405b`
**n per cell:** 200
**Source liturgies (L_real):** `astrachios`, `headless`

## Headline comparisons (per-completion rate ratios)

| Source | Comparison | tail | L_real rate | Control rate | Rate ratio | 95% CI | Interpretation |
|---|---|---|---:|---:|---:|---:|---|
| `astrachios` | L_denamed (`astrachios_denamed`) | visitor_at_door | 1.9502 (391/200) | 0.2189 (43/200) | 8.909× | [5.0, 16.48] | positive evidence |
| `astrachios` | L_nonsense (`astrachios_nonsense`) | visitor_at_door | 1.9502 (391/200) | 0.0547 (10/200) | 35.636× | [16.25, 122.0] | positive evidence |
| `astrachios` | L_random (`astrachios_random`) | visitor_at_door | 1.9502 (391/200) | 0.005 (0/200) | 392.0× | [244.0, 559.0] | positive evidence |
| `astrachios` | L_empty (`empty`) | visitor_at_door | 1.9502 (391/200) | 0.005 (0/200) | 392.0× | [244.0, 559.0] | positive evidence |
| `astrachios` | L_denamed (`astrachios_denamed`) | enters_room | 1.9154 (384/200) | 0.3333 (66/200) | 5.746× | [2.949, 11.971] | positive evidence |
| `astrachios` | L_nonsense (`astrachios_nonsense`) | enters_room | 1.9154 (384/200) | 0.0945 (18/200) | 20.263× | [9.806, 55.429] | positive evidence |
| `astrachios` | L_random (`astrachios_random`) | enters_room | 1.9154 (384/200) | 0.005 (0/200) | 385.0× | [233.0, 558.0] | positive evidence |
| `astrachios` | L_empty (`empty`) | enters_room | 1.9154 (384/200) | 0.01 (1/200) | 192.5× | [76.5, 513.0] | positive evidence |
| `astrachios` | L_denamed (`astrachios_denamed`) | page_continues | 2.7015 (542/200) | 1.0945 (219/200) | 2.468× | [1.849, 3.376] | positive evidence |
| `astrachios` | L_nonsense (`astrachios_nonsense`) | page_continues | 2.7015 (542/200) | 0.5423 (108/200) | 4.982× | [3.519, 7.156] | positive evidence |
| `astrachios` | L_random (`astrachios_random`) | page_continues | 2.7015 (542/200) | 0.005 (0/200) | 543.0× | [445.0, 649.0] | positive evidence |
| `astrachios` | L_empty (`empty`) | page_continues | 2.7015 (542/200) | 0.0348 (6/200) | 77.571× | [25.947, 629.0] | positive evidence |
| `headless` | L_empty (`empty`) | visitor_at_door | 1.1542 (231/200) | 0.005 (0/200) | 232.0× | [167.0, 303.0] | positive evidence |
| `headless` | L_denamed (`headless_denamed`) | visitor_at_door | 1.1542 (231/200) | 0.0398 (7/200) | 29.0× | [12.688, 143.5] | positive evidence |
| `headless` | L_nonsense (`headless_nonsense`) | visitor_at_door | 1.1542 (231/200) | 0.01 (1/200) | 116.0× | [49.333, 288.0] | positive evidence |
| `headless` | L_random (`headless_random`) | visitor_at_door | 1.1542 (231/200) | 0.005 (0/200) | 232.0× | [167.0, 303.0] | positive evidence |
| `headless` | L_empty (`empty`) | enters_room | 0.5473 (109/200) | 0.01 (1/200) | 55.0× | [21.75, 150.0] | positive evidence |
| `headless` | L_denamed (`headless_denamed`) | enters_room | 0.5473 (109/200) | 0.0149 (2/200) | 36.667× | [13.2, 151.0] | positive evidence |
| `headless` | L_nonsense (`headless_nonsense`) | enters_room | 0.5473 (109/200) | 0.01 (1/200) | 55.0× | [21.25, 153.0] | positive evidence |
| `headless` | L_random (`headless_random`) | enters_room | 0.5473 (109/200) | 0.005 (0/200) | 110.0× | [65.0, 170.0] | positive evidence |
| `headless` | L_empty (`empty`) | page_continues | 2.6915 (540/200) | 0.0348 (6/200) | 77.286× | [26.105, 604.0] | positive evidence |
| `headless` | L_denamed (`headless_denamed`) | page_continues | 2.6915 (540/200) | 0.6716 (134/200) | 4.007× | [2.989, 5.558] | positive evidence |
| `headless` | L_nonsense (`headless_nonsense`) | page_continues | 2.6915 (540/200) | 0.2985 (59/200) | 9.017× | [5.526, 16.588] | positive evidence |
| `headless` | L_random (`headless_random`) | page_continues | 2.6915 (540/200) | 0.005 (0/200) | 541.0× | [456.0, 630.0] | positive evidence |

## Per-cell

| Cell | Role | n | Tokens | Headline yield | /completion | NE | RV | Amb-NE | Amb-RV |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `astrachios/visitor_at_door` | L_real | 200 | 38659 | 391 | 1.955 | 338 | 53 | 21 | 245 |
| `astrachios/enters_room` | L_real | 200 | 36750 | 384 | 1.92 | 336 | 48 | 20 | 557 |
| `astrachios/page_continues` | L_real | 200 | 35346 | 542 | 2.71 | 222 | 320 | 12 | 356 |
| `astrachios_denamed/visitor_at_door` | L_denamed | 200 | 39460 | 43 | 0.215 | 2 | 41 | 0 | 188 |
| `astrachios_denamed/enters_room` | L_denamed | 200 | 37977 | 66 | 0.33 | 22 | 44 | 0 | 498 |
| `astrachios_denamed/page_continues` | L_denamed | 200 | 35587 | 219 | 1.095 | 36 | 183 | 0 | 400 |
| `astrachios_nonsense/visitor_at_door` | L_nonsense | 200 | 39581 | 10 | 0.05 | 0 | 10 | 1 | 129 |
| `astrachios_nonsense/enters_room` | L_nonsense | 200 | 36187 | 18 | 0.09 | 0 | 18 | 0 | 224 |
| `astrachios_nonsense/page_continues` | L_nonsense | 200 | 35536 | 108 | 0.54 | 4 | 104 | 0 | 218 |
| `astrachios_random/visitor_at_door` | L_random | 200 | 39535 | 0 | 0.0 | 0 | 0 | 0 | 40 |
| `astrachios_random/enters_room` | L_random | 200 | 36436 | 0 | 0.0 | 0 | 0 | 0 | 19 |
| `astrachios_random/page_continues` | L_random | 200 | 34801 | 0 | 0.0 | 0 | 0 | 0 | 14 |
| `empty/visitor_at_door` | L_empty | 200 | 40864 | 0 | 0.0 | 0 | 0 | 0 | 52 |
| `empty/enters_room` | L_empty | 200 | 40230 | 1 | 0.005 | 0 | 1 | 0 | 36 |
| `empty/page_continues` | L_empty | 200 | 36824 | 6 | 0.03 | 0 | 6 | 3 | 19 |
| `headless/visitor_at_door` | L_real | 200 | 40093 | 231 | 1.155 | 218 | 13 | 30 | 709 |
| `headless/enters_room` | L_real | 200 | 41095 | 109 | 0.545 | 109 | 0 | 26 | 521 |
| `headless/page_continues` | L_real | 200 | 36451 | 540 | 2.7 | 319 | 221 | 46 | 1373 |
| `headless_denamed/visitor_at_door` | L_denamed | 200 | 39730 | 7 | 0.035 | 6 | 1 | 0 | 528 |
| `headless_denamed/enters_room` | L_denamed | 200 | 40174 | 2 | 0.01 | 2 | 0 | 0 | 665 |
| `headless_denamed/page_continues` | L_denamed | 200 | 36295 | 134 | 0.67 | 21 | 113 | 4 | 1215 |
| `headless_nonsense/visitor_at_door` | L_nonsense | 200 | 38591 | 1 | 0.005 | 0 | 1 | 0 | 456 |
| `headless_nonsense/enters_room` | L_nonsense | 200 | 39466 | 1 | 0.005 | 0 | 1 | 0 | 516 |
| `headless_nonsense/page_continues` | L_nonsense | 200 | 35958 | 59 | 0.295 | 15 | 44 | 5 | 1073 |
| `headless_random/visitor_at_door` | L_random | 200 | 41423 | 0 | 0.0 | 0 | 0 | 0 | 428 |
| `headless_random/enters_room` | L_random | 200 | 37255 | 0 | 0.0 | 0 | 0 | 0 | 440 |
| `headless_random/page_continues` | L_random | 200 | 36954 | 0 | 0.0 | 0 | 0 | 0 | 616 |

## Top entity hits per cell

### `astrachios/visitor_at_door` (L_real)
Named entities:
  - `scirlin` × 34
  - `adonai` × 22
  - `elohim` × 21
  - `astrachios` × 20
  - `bael` × 15
  - `emagro` × 13
  - `achsah` × 12
  - `asac` × 11
  - `silat` × 11
  - `baracata` × 11
Related vocabulary:
  - `grimoire` × 17
  - `sigil` × 8
  - `invocation` × 7
  - `lemegeton` × 7
  - `tetragrammaton` × 6
  - `pentacle` × 4
  - `conjuration` × 2
  - `goetia` × 2

### `astrachios/enters_room` (L_real)
Named entities:
  - `scirlin` × 39
  - `adonai` × 21
  - `elohim` × 17
  - `bael` × 17
  - `elamos` × 15
  - `archarzel` × 13
  - `astrachios` × 12
  - `silat` × 12
  - `arabonas` × 12
  - `asac` × 11
Related vocabulary:
  - `sigil` × 17
  - `invocation` × 10
  - `goetia` × 7
  - `tetragrammaton` × 6
  - `grimoire` × 3
  - `conjuration` × 2
  - `kabbalah` × 1
  - `solomonic` × 1
  - `pentacle` × 1

### `astrachios/page_continues` (L_real)
Named entities:
  - `adonai` × 54
  - `elohim` × 36
  - `asac` × 12
  - `astrachios` × 10
  - `samoel` × 9
  - `elohi` × 9
  - `baracata` × 8
  - `scirlin` × 8
  - `abragateh` × 6
  - `cadato` × 6
Related vocabulary:
  - `grimoire` × 130
  - `conjuration` × 48
  - `tetragrammaton` × 37
  - `pentacle` × 36
  - `invocation` × 24
  - `goetia` × 24
  - `lemegeton` × 8
  - `sigil` × 5
  - `kabbalah` × 3
  - `genius` × 3

### `astrachios_denamed/visitor_at_door` (L_denamed)
Named entities:
  - `adonai` × 1
  - `elohim` × 1
Related vocabulary:
  - `sigil` × 18
  - `invocation` × 11
  - `grimoire` × 6
  - `conjuration` × 1
  - `kabbalah` × 1
  - `tetragrammaton` × 1
  - `lemegeton` × 1
  - `goetia` × 1
  - `solomonic` × 1

### `astrachios_denamed/enters_room` (L_denamed)
Named entities:
  - `adonai` × 18
  - `elohim` × 3
  - `emagro` × 1
Related vocabulary:
  - `invocation` × 14
  - `goetia` × 10
  - `sigil` × 9
  - `grimoire` × 7
  - `tetragrammaton` × 4

### `astrachios_denamed/page_continues` (L_denamed)
Named entities:
  - `elohim` × 22
  - `adonai` × 14
Related vocabulary:
  - `grimoire` × 56
  - `pentacle` × 26
  - `conjuration` × 25
  - `invocation` × 22
  - `tetragrammaton` × 22
  - `sigil` × 16
  - `lemegeton` × 10
  - `goetia` × 4
  - `psalm` × 2

### `astrachios_nonsense/visitor_at_door` (L_nonsense)
Related vocabulary:
  - `sigil` × 5
  - `invocation` × 4
  - `tetragrammaton` × 1

### `astrachios_nonsense/enters_room` (L_nonsense)
Related vocabulary:
  - `sigil` × 9
  - `invocation` × 9

### `astrachios_nonsense/page_continues` (L_nonsense)
Named entities:
  - `adonai` × 2
  - `elohim` × 2
Related vocabulary:
  - `grimoire` × 36
  - `invocation` × 23
  - `sigil` × 17
  - `conjuration` × 14
  - `tetragrammaton` × 4
  - `pentacle` × 4
  - `goetia` × 2
  - `genius` × 2
  - `kabbalah` × 1
  - `lemegeton` × 1

### `empty/enters_room` (L_empty)
Related vocabulary:
  - `genius` × 1

### `empty/page_continues` (L_empty)
Related vocabulary:
  - `tetragrammaton` × 6

### `headless/visitor_at_door` (L_real)
Named entities:
  - `mosheh` × 52
  - `aphrael` × 24
  - `ablathanalba` × 22
  - `osoronnophris` × 12
  - `sabaōth` × 11
  - `iaō` × 11
  - `sabaoth` × 9
  - `arogogorobrao` × 9
  - `modorio` × 9
  - `ischurael` × 8
Related vocabulary:
  - `stele` × 3
  - `gnostic` × 3
  - `jeu` × 2
  - `ceremonial` × 2
  - `pgm` × 1
  - `papyri` × 1
  - `hellenistic` × 1

### `headless/enters_room` (L_real)
Named entities:
  - `iao` × 16
  - `mosheh` × 15
  - `sabaoth` × 11
  - `sabaōth` × 9
  - `aphrael` × 9
  - `ablathanalba` × 9
  - `iaō` × 7
  - `arogogorobrao` × 5
  - `modorio` × 5
  - `thiao` × 4

### `headless/page_continues` (L_real)
Named entities:
  - `mosheh` × 26
  - `thiao` × 21
  - `osoronnophris` × 19
  - `arogogorobrao` × 19
  - `iaō` × 19
  - `sabaoth` × 18
  - `sabaōth` × 18
  - `iao` × 18
  - `ablathanalba` × 17
  - `modorio` × 17
Related vocabulary:
  - `papyri` × 49
  - `stele` × 38
  - `jeu` × 35
  - `gnostic` × 34
  - `pgm` × 32
  - `barbarous` × 11
  - `ceremonial` × 8
  - `ablanathanalba` × 7
  - `theurgy` × 4
  - `voces magicae` × 3

### `headless_denamed/visitor_at_door` (L_denamed)
Named entities:
  - `sabaōth` × 3
  - `akephalos` × 2
  - `mosheh` × 1
Related vocabulary:
  - `theurgy` × 1

### `headless_denamed/enters_room` (L_denamed)
Named entities:
  - `sabaoth` × 1
  - `iao` × 1

### `headless_denamed/page_continues` (L_denamed)
Named entities:
  - `iao` × 5
  - `iaō` × 4
  - `thiao` × 3
  - `sabaoth` × 2
  - `sabaōth` × 2
  - `rheibet` × 2
  - `mosheh` × 1
  - `blatha` × 1
  - `arogogorobrao` × 1
Related vocabulary:
  - `papyri` × 34
  - `gnostic` × 28
  - `barbarous` × 15
  - `pgm` × 11
  - `stele` × 6
  - `voces magicae` × 5
  - `jeu` × 4
  - `ceremonial` × 4
  - `ablanathanalba` × 3
  - `hellenistic` × 2

### `headless_nonsense/visitor_at_door` (L_nonsense)
Related vocabulary:
  - `ceremonial` × 1

### `headless_nonsense/enters_room` (L_nonsense)
Related vocabulary:
  - `ceremonial` × 1

### `headless_nonsense/page_continues` (L_nonsense)
Named entities:
  - `thiao` × 5
  - `mosheh` × 3
  - `rheibet` × 3
  - `blatha` × 3
  - `akephalos` × 1
Related vocabulary:
  - `papyri` × 12
  - `gnostic` × 11
  - `pgm` × 6
  - `ceremonial` × 6
  - `jeu` × 3
  - `barbarous` × 3
  - `stele` × 2
  - `voces magicae` × 1

## Top lexical divergence per comparison

### vs L_denamed (`astrachios_denamed`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `agater` | 0 | 79 | -4.362 |
| `salar` | 50 | 0 | +3.952 |
| `atar` | 49 | 0 | +3.933 |
| `sopro` | 0 | 49 | -3.892 |
| `genilum` | 0 | 46 | -3.83 |
| `lodge` | 38 | 0 | +3.684 |
| `sada` | 37 | 0 | +3.658 |
| `scirlin` | 34 | 0 | +3.576 |
| `tower` | 0 | 28 | -3.347 |
| `aramonis` | 0 | 28 | -3.347 |
| `anchanzel` | 0 | 27 | -3.312 |
| `acla` | 0 | 27 | -3.312 |
| `asthrenios` | 0 | 27 | -3.312 |
| `sipat` | 0 | 27 | -3.312 |
| `asep` | 0 | 27 | -3.312 |

### vs L_nonsense (`astrachios_nonsense`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `salar` | 50 | 0 | +3.955 |
| `atar` | 49 | 0 | +3.936 |
| `sada` | 37 | 0 | +3.661 |
| `vronk` | 0 | 36 | -3.587 |
| `scirlin` | 34 | 0 | +3.579 |
| `glothenkion` | 0 | 30 | -3.41 |
| `adonai` | 23 | 0 | +3.202 |
| `void` | 0 | 24 | -3.195 |
| `vrindat` | 0 | 24 | -3.195 |
| `onthropor` | 0 | 23 | -3.154 |
| `elohim` | 21 | 0 | +3.115 |
| `kresnopith` | 0 | 22 | -3.112 |
| `host` | 64 | 2 | +3.099 |
| `angel` | 20 | 0 | +3.068 |
| `astrachios` | 20 | 0 | +3.068 |

### vs L_random (`astrachios_random`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `kakapo` | 0 | 871 | -6.748 |
| `parrot` | 0 | 341 | -5.812 |
| `spirits` | 256 | 0 | +5.571 |
| `species` | 0 | 250 | -5.503 |
| `endangered` | 0 | 231 | -5.424 |
| `critically` | 0 | 194 | -5.251 |
| `flightless` | 0 | 181 | -5.182 |
| `bird` | 0 | 179 | -5.171 |
| `zealand` | 0 | 158 | -5.046 |
| `conservation` | 0 | 136 | -4.898 |
| `re` | 0 | 125 | -4.814 |
| `mysteries` | 102 | 0 | +4.657 |
| `kakapos` | 0 | 98 | -4.573 |
| `ve` | 0 | 96 | -4.552 |
| `nocturnal` | 0 | 93 | -4.521 |

### vs L_empty (`empty`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `doorkeeper` | 219 | 0 | +5.449 |
| `guardian` | 132 | 0 | +4.946 |
| `spirits` | 256 | 1 | +4.911 |
| `re` | 0 | 98 | -4.54 |
| `mr` | 0 | 92 | -4.477 |
| `ve` | 0 | 78 | -4.314 |
| `m` | 2 | 230 | -4.288 |
| `ritual` | 133 | 1 | +4.26 |
| `names` | 131 | 1 | +4.245 |
| `family` | 0 | 66 | -4.149 |
| `looking` | 0 | 60 | -4.055 |
| `ll` | 0 | 57 | -4.005 |
| `salar` | 50 | 0 | +3.987 |
| `atar` | 49 | 0 | +3.967 |
| `grant` | 48 | 0 | +3.947 |

### vs L_denamed (`astrachios_denamed`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `sopro` | 0 | 65 | -4.157 |
| `elapal` | 0 | 60 | -4.078 |
| `icrahel` | 0 | 49 | -3.879 |
| `genilum` | 0 | 46 | -3.817 |
| `scirlin` | 39 | 0 | +3.722 |
| `serafin` | 0 | 39 | -3.656 |
| `scildon` | 0 | 31 | -3.433 |
| `esh` | 0 | 26 | -3.263 |
| `morpheus` | 0 | 26 | -3.263 |
| `astaroth` | 24 | 0 | +3.252 |
| `watches` | 23 | 0 | +3.211 |
| `ena` | 0 | 22 | -3.103 |
| `asthrenios` | 0 | 21 | -3.058 |
| `acla` | 0 | 20 | -3.012 |
| `aramonis` | 0 | 20 | -3.012 |

### vs L_nonsense (`astrachios_nonsense`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `vronk` | 0 | 48 | -3.907 |
| `onth` | 0 | 45 | -3.844 |
| `scirlin` | 39 | 0 | +3.673 |
| `glothenkion` | 0 | 37 | -3.653 |
| `skro` | 0 | 36 | -3.626 |
| `skle` | 0 | 35 | -3.599 |
| `crossing` | 0 | 34 | -3.571 |
| `tron` | 0 | 32 | -3.512 |
| `vrath` | 0 | 32 | -3.512 |
| `borax` | 0 | 30 | -3.449 |
| `tholgardosen` | 0 | 27 | -3.348 |
| `cosmic` | 1 | 54 | -3.33 |
| `demons` | 27 | 0 | +3.317 |
| `ontrolanker` | 0 | 26 | -3.311 |
| `vrindat` | 0 | 26 | -3.311 |

### vs L_random (`astrachios_random`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `kakapo` | 0 | 780 | -6.669 |
| `parrot` | 0 | 705 | -6.568 |
| `bird` | 0 | 284 | -5.661 |
| `flightless` | 0 | 273 | -5.622 |
| `nocturnal` | 0 | 200 | -5.312 |
| `species` | 0 | 196 | -5.292 |
| `endangered` | 0 | 150 | -5.026 |
| `critically` | 0 | 144 | -4.985 |
| `zealand` | 0 | 143 | -4.978 |
| `owl` | 0 | 131 | -4.891 |
| `command` | 132 | 0 | +4.882 |
| `spirits` | 118 | 0 | +4.771 |
| `heaviest` | 0 | 115 | -4.762 |
| `breeding` | 0 | 106 | -4.681 |
| `lek` | 0 | 105 | -4.672 |

### vs L_empty (`empty`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `command` | 132 | 0 | +4.981 |
| `dream` | 0 | 72 | -4.2 |
| `baby` | 0 | 65 | -4.099 |
| `angel` | 48 | 0 | +3.982 |
| `big` | 0 | 57 | -3.97 |
| `ritual` | 92 | 1 | +3.93 |
| `scirlin` | 39 | 0 | +3.779 |
| `depart` | 35 | 0 | +3.674 |
| `power` | 213 | 5 | +3.665 |
| `secrets` | 70 | 1 | +3.66 |
| `summon` | 30 | 0 | +3.524 |
| `meadow` | 0 | 36 | -3.52 |
| `writing` | 0 | 35 | -3.493 |
| `missing` | 0 | 34 | -3.465 |
| `bound` | 28 | 0 | +3.458 |

### vs L_denamed (`astrachios_denamed`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `hepa` | 0 | 51 | -3.944 |
| `sopro` | 0 | 37 | -3.631 |
| `genilum` | 0 | 37 | -3.631 |
| `heb` | 28 | 0 | +3.374 |
| `abo` | 0 | 28 | -3.361 |
| `wonderful` | 27 | 0 | +3.339 |
| `zalbriyun` | 26 | 0 | +3.303 |
| `hebot` | 25 | 0 | +3.265 |
| `ath` | 0 | 22 | -3.129 |
| `deus` | 20 | 0 | +3.051 |
| `gatarab` | 20 | 0 | +3.051 |
| `path` | 1 | 38 | -2.964 |
| `acla` | 0 | 16 | -2.826 |
| `gepulanel` | 0 | 16 | -2.826 |
| `sipat` | 0 | 16 | -2.826 |

### vs L_nonsense (`astrachios_nonsense`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `ω` | 0 | 76 | -4.338 |
| `ai` | 0 | 42 | -3.756 |
| `agla` | 41 | 0 | +3.743 |
| `au` | 0 | 39 | -3.684 |
| `chamber` | 0 | 32 | -3.491 |
| `onthol` | 0 | 31 | -3.46 |
| `heb` | 28 | 0 | +3.373 |
| `vrond` | 0 | 27 | -3.327 |
| `zalbriyun` | 26 | 0 | +3.301 |
| `vronth` | 0 | 26 | -3.29 |
| `hebot` | 25 | 0 | +3.263 |
| `glothenkion` | 0 | 23 | -3.173 |
| `deus` | 20 | 0 | +3.05 |
| `gatarab` | 20 | 0 | +3.05 |
| `onth` | 0 | 20 | -3.039 |

### vs L_random (`astrachios_random`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `kakapo` | 0 | 1137 | -7.053 |
| `parrot` | 0 | 338 | -5.842 |
| `endangered` | 0 | 322 | -5.793 |
| `population` | 0 | 320 | -5.787 |
| `species` | 0 | 318 | -5.781 |
| `spirits` | 323 | 0 | +5.765 |
| `critically` | 0 | 304 | -5.736 |
| `zealand` | 0 | 263 | -5.591 |
| `conservation` | 0 | 250 | -5.541 |
| `individuals` | 0 | 247 | -5.529 |
| `flightless` | 0 | 184 | -5.236 |
| `adult` | 0 | 177 | -5.197 |
| `efforts` | 0 | 149 | -5.026 |
| `nocturnal` | 0 | 141 | -4.971 |
| `god` | 144 | 0 | +4.961 |

### vs L_empty (`empty`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `spirits` | 323 | 0 | +5.822 |
| `grimoire` | 131 | 0 | +4.924 |
| `manuscript` | 112 | 0 | +4.768 |
| `conjure` | 111 | 0 | +4.759 |
| `holy` | 99 | 0 | +4.646 |
| `names` | 292 | 2 | +4.623 |
| `function` | 0 | 94 | -4.513 |
| `solomon` | 85 | 0 | +4.495 |
| `comment` | 0 | 84 | -4.402 |
| `x` | 0 | 83 | -4.39 |
| `angels` | 74 | 0 | +4.358 |
| `grand` | 73 | 0 | +4.345 |
| `demons` | 60 | 0 | +4.152 |
| `system` | 0 | 64 | -4.133 |
| `spirit` | 118 | 1 | +4.127 |

### vs L_empty (`empty`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `headless` | 167 | 0 | +5.143 |
| `doorkeeper` | 61 | 0 | +4.146 |
| `divine` | 57 | 0 | +4.079 |
| `mosheh` | 52 | 0 | +3.989 |
| `destroys` | 52 | 0 | +3.989 |
| `magician` | 47 | 0 | +3.89 |
| `homeowner` | 0 | 48 | -3.873 |
| `unto` | 42 | 0 | +3.78 |
| `begets` | 41 | 0 | +3.757 |
| `created` | 41 | 0 | +3.757 |
| `smith` | 0 | 40 | -3.695 |
| `prophet` | 37 | 0 | +3.657 |
| `thou` | 37 | 0 | +3.657 |
| `invocation` | 34 | 0 | +3.574 |
| `girt` | 33 | 0 | +3.545 |

### vs L_denamed (`headless_denamed`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `nopheth` | 0 | 177 | -5.191 |
| `tongueless` | 0 | 149 | -5.02 |
| `headless` | 167 | 1 | +4.422 |
| `aphroden` | 0 | 59 | -4.103 |
| `acromenalba` | 0 | 48 | -3.901 |
| `girt` | 33 | 0 | +3.517 |
| `iōm` | 0 | 30 | -3.443 |
| `coil` | 0 | 30 | -3.443 |
| `sapenōth` | 0 | 28 | -3.376 |
| `operator` | 26 | 0 | +3.287 |
| `mosheh` | 52 | 1 | +3.268 |
| `aphrael` | 24 | 0 | +3.21 |
| `daimon` | 23 | 0 | +3.169 |
| `ablathanalba` | 22 | 0 | +3.126 |
| `iscuren` | 0 | 21 | -3.1 |

### vs L_nonsense (`headless_nonsense`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `vrondh` | 0 | 311 | -5.781 |
| `headless` | 167 | 0 | +5.086 |
| `mrolthen` | 0 | 144 | -5.015 |
| `smelphenor` | 0 | 59 | -4.133 |
| `krelph` | 0 | 57 | -4.099 |
| `vrelth` | 0 | 52 | -4.008 |
| `mosheh` | 52 | 0 | +3.932 |
| `vrelthemphos` | 0 | 44 | -3.845 |
| `magician` | 47 | 0 | +3.833 |
| `mrok` | 0 | 37 | -3.676 |
| `girt` | 33 | 0 | +3.488 |
| `mystery` | 29 | 0 | +3.363 |
| `vrelph` | 0 | 26 | -3.334 |
| `operator` | 26 | 0 | +3.258 |
| `aphrael` | 24 | 0 | +3.181 |

### vs L_random (`headless_random`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `plates` | 0 | 431 | -6.036 |
| `plate` | 0 | 339 | -5.796 |
| `tectonics` | 0 | 250 | -5.493 |
| `headless` | 167 | 0 | +5.157 |
| `tectonic` | 0 | 136 | -4.887 |
| `movement` | 0 | 125 | -4.804 |
| `crust` | 0 | 116 | -4.73 |
| `mantle` | 0 | 114 | -4.712 |
| `grace` | 102 | 0 | +4.667 |
| `lithosphere` | 0 | 90 | -4.478 |
| `spirit` | 75 | 0 | +4.363 |
| `formation` | 0 | 67 | -4.187 |
| `planet` | 0 | 66 | -4.172 |
| `doorkeeper` | 61 | 0 | +4.16 |
| `volcanic` | 0 | 64 | -4.142 |

### vs L_empty (`empty`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `headless` | 268 | 0 | +5.573 |
| `serpent` | 133 | 0 | +4.877 |
| `invoke` | 80 | 0 | +4.373 |
| `baby` | 0 | 65 | -4.211 |
| `monster` | 0 | 51 | -3.973 |
| `mmm` | 49 | 0 | +3.891 |
| `beast` | 123 | 2 | +3.7 |
| `angel` | 40 | 0 | +3.692 |
| `opening` | 0 | 38 | -3.685 |
| `picture` | 0 | 38 | -3.685 |
| `meadow` | 0 | 36 | -3.632 |
| `mysteries` | 36 | 0 | +3.59 |
| `enough` | 0 | 33 | -3.548 |
| `mighty` | 65 | 1 | +3.475 |
| `little` | 0 | 29 | -3.422 |

### vs L_denamed (`headless_denamed`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `headless` | 268 | 0 | +5.572 |
| `tongueless` | 0 | 132 | -4.913 |
| `sapenōth` | 0 | 108 | -4.714 |
| `iōm` | 0 | 107 | -4.705 |
| `books` | 0 | 82 | -4.442 |
| `wants` | 0 | 60 | -4.134 |
| `mmm` | 49 | 0 | +3.889 |
| `dog` | 0 | 36 | -3.634 |
| `person` | 2 | 91 | -3.446 |
| `moments` | 61 | 1 | +3.411 |
| `daiken` | 0 | 25 | -3.281 |
| `yeah` | 25 | 0 | +3.235 |
| `daimon` | 25 | 0 | +3.235 |
| `scribe` | 0 | 23 | -3.201 |
| `nopheth` | 0 | 22 | -3.158 |

### vs L_nonsense (`headless_nonsense`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `headless` | 268 | 0 | +5.554 |
| `mrolthen` | 0 | 115 | -4.794 |
| `mrok` | 0 | 111 | -4.759 |
| `vrondh` | 0 | 87 | -4.518 |
| `krelphōth` | 0 | 57 | -4.101 |
| `mphō` | 0 | 57 | -4.101 |
| `mrelth` | 0 | 53 | -4.029 |
| `mmm` | 49 | 0 | +3.872 |
| `horrible` | 0 | 44 | -3.847 |
| `candle` | 0 | 42 | -3.802 |
| `vrelthemphos` | 0 | 36 | -3.651 |
| `smelphenor` | 0 | 36 | -3.651 |
| `trusted` | 0 | 35 | -3.624 |
| `didn` | 32 | 0 | +3.456 |
| `scp` | 0 | 29 | -3.442 |

### vs L_random (`headless_random`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `plates` | 0 | 451 | -6.212 |
| `plate` | 0 | 315 | -5.854 |
| `crust` | 0 | 222 | -5.505 |
| `headless` | 268 | 0 | +5.497 |
| `lithosphere` | 0 | 200 | -5.401 |
| `tectonic` | 0 | 184 | -5.318 |
| `mantle` | 0 | 183 | -5.313 |
| `tectonics` | 0 | 152 | -5.129 |
| `theory` | 0 | 132 | -4.988 |
| `oceanic` | 0 | 129 | -4.966 |
| `serpent` | 133 | 0 | +4.8 |
| `movement` | 0 | 97 | -4.683 |
| `continental` | 0 | 88 | -4.587 |
| `earthquakes` | 0 | 80 | -4.493 |
| `process` | 0 | 77 | -4.455 |

### vs L_empty (`empty`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `invocation` | 333 | 0 | +5.821 |
| `headless` | 247 | 0 | +5.524 |
| `thou` | 168 | 0 | +5.14 |
| `lord` | 165 | 0 | +5.122 |
| `spell` | 151 | 0 | +5.034 |
| `thee` | 145 | 0 | +4.994 |
| `unto` | 142 | 0 | +4.973 |
| `didst` | 107 | 0 | +4.692 |
| `spirits` | 102 | 0 | +4.645 |
| `bornless` | 89 | 0 | +4.51 |
| `art` | 88 | 0 | +4.499 |
| `x` | 0 | 83 | -4.421 |
| `invoke` | 79 | 0 | +4.392 |
| `gods` | 79 | 0 | +4.392 |
| `m` | 0 | 76 | -4.334 |

### vs L_denamed (`headless_denamed`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `tongueless` | 0 | 80 | -4.399 |
| `aprodis` | 0 | 55 | -4.03 |
| `iōm` | 0 | 50 | -3.936 |
| `sapenōth` | 0 | 44 | -3.811 |
| `nopheth` | 0 | 40 | -3.718 |
| `pulse` | 0 | 37 | -3.642 |
| `daiken` | 0 | 36 | -3.615 |
| `coil` | 0 | 35 | -3.588 |
| `wound` | 0 | 35 | -3.588 |
| `iscuren` | 0 | 33 | -3.531 |
| `aphroden` | 0 | 30 | -3.438 |
| `begone` | 0 | 30 | -3.438 |
| `headless` | 247 | 7 | +3.43 |
| `universal` | 24 | 0 | +3.215 |
| `acromenalba` | 0 | 20 | -3.049 |

### vs L_nonsense (`headless_nonsense`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `mrolthen` | 0 | 113 | -4.75 |
| `vrondh` | 0 | 85 | -4.468 |
| `smelphenor` | 0 | 70 | -4.276 |
| `vrelth` | 0 | 60 | -4.124 |
| `mrok` | 0 | 53 | -4.003 |
| `morok` | 0 | 39 | -3.702 |
| `krelphōth` | 0 | 36 | -3.625 |
| `krelph` | 0 | 34 | -3.569 |
| `headless` | 247 | 6 | +3.554 |
| `vrelthemphos` | 0 | 32 | -3.51 |
| `mrolth` | 0 | 32 | -3.51 |
| `mphō` | 0 | 32 | -3.51 |
| `mronth` | 0 | 29 | -3.415 |
| `vreltho` | 0 | 28 | -3.381 |
| `vronthep` | 0 | 27 | -3.346 |

### vs L_random (`headless_random`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `plate` | 0 | 702 | -6.542 |
| `plates` | 0 | 547 | -6.293 |
| `tectonics` | 0 | 415 | -6.017 |
| `invocation` | 333 | 0 | +5.825 |
| `crust` | 0 | 305 | -5.71 |
| `god` | 271 | 0 | +5.62 |
| `lithosphere` | 0 | 268 | -5.581 |
| `mantle` | 0 | 258 | -5.543 |
| `headless` | 247 | 0 | +5.527 |
| `tectonic` | 0 | 202 | -5.3 |
| `thou` | 168 | 0 | +5.144 |
| `lord` | 165 | 0 | +5.126 |
| `theory` | 0 | 160 | -5.068 |
| `spell` | 151 | 0 | +5.038 |
| `thee` | 145 | 0 | +4.997 |

## Caveats

- Headline yield counts whole-word, case-insensitive matches.
- Ambiguous-tier counts (`Amb-NE`, `Amb-RV`) are tracked but NOT in the headline (common words ⇒ baseline false positives).
- Pairwise comparisons computed per tail. Confidence intervals not yet computed — defer to bootstrap when scaling beyond smoke.