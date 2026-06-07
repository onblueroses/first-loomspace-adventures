# Measurements: plasticity-2026-06-01-hermes

**Model:** `nousresearch/hermes-3-llama-3.1-405b`
**n per cell:** 200
**Source liturgies (L_real):** `synthetic_cosmological`, `synthetic_litany`

## Headline comparisons (per-completion rate ratios)

| Source | Comparison | tail | L_real rate | Control rate | Rate ratio | 95% CI | Interpretation |
|---|---|---|---:|---:|---:|---:|---|
| `synthetic_cosmological` | L_empty (`empty`) | visitor_at_door | 1.6617 (333/200) | 0.005 (0/200) | 334.0× | [218.0, 473.0] | positive evidence |
| `synthetic_cosmological` | L_denamed (`synthetic_cosmological_denamed`) | visitor_at_door | 1.6617 (333/200) | 0.0448 (8/200) | 37.111× | [11.08, 439.0] | positive evidence |
| `synthetic_cosmological` | L_nonsense (`synthetic_cosmological_nonsense`) | visitor_at_door | 1.6617 (333/200) | 0.005 (0/200) | 334.0× | [218.0, 473.0] | positive evidence |
| `synthetic_cosmological` | L_random (`synthetic_cosmological_random`) | visitor_at_door | 1.6617 (333/200) | 0.005 (0/200) | 334.0× | [218.0, 473.0] | positive evidence |
| `synthetic_cosmological` | L_empty (`empty`) | enters_room | 1.5025 (301/200) | 0.005 (0/200) | 302.0× | [220.0, 396.0] | positive evidence |
| `synthetic_cosmological` | L_denamed (`synthetic_cosmological_denamed`) | enters_room | 1.5025 (301/200) | 0.0199 (3/200) | 75.5× | [25.769, 375.0] | positive evidence |
| `synthetic_cosmological` | L_nonsense (`synthetic_cosmological_nonsense`) | enters_room | 1.5025 (301/200) | 0.01 (1/200) | 151.0× | [65.0, 368.0] | positive evidence |
| `synthetic_cosmological` | L_random (`synthetic_cosmological_random`) | enters_room | 1.5025 (301/200) | 0.005 (0/200) | 302.0× | [220.0, 396.0] | positive evidence |
| `synthetic_cosmological` | L_empty (`empty`) | page_continues | 2.1095 (423/200) | 0.005 (0/200) | 424.0× | [319.0, 537.0] | positive evidence |
| `synthetic_cosmological` | L_denamed (`synthetic_cosmological_denamed`) | page_continues | 2.1095 (423/200) | 0.2239 (44/200) | 9.422× | [5.741, 17.156] | positive evidence |
| `synthetic_cosmological` | L_nonsense (`synthetic_cosmological_nonsense`) | page_continues | 2.1095 (423/200) | 0.0547 (10/200) | 38.545× | [19.5, 109.333] | positive evidence |
| `synthetic_cosmological` | L_random (`synthetic_cosmological_random`) | page_continues | 2.1095 (423/200) | 0.005 (0/200) | 424.0× | [319.0, 537.0] | positive evidence |
| `synthetic_litany` | L_empty (`empty`) | visitor_at_door | 1.8955 (380/200) | 0.005 (0/200) | 381.0× | [207.0, 582.0] | positive evidence |
| `synthetic_litany` | L_denamed (`synthetic_litany_denamed`) | visitor_at_door | 1.8955 (380/200) | 0.1045 (20/200) | 18.143× | [8.565, 39.0] | positive evidence |
| `synthetic_litany` | L_nonsense (`synthetic_litany_nonsense`) | visitor_at_door | 1.8955 (380/200) | 0.0348 (6/200) | 54.429× | [16.2, 455.0] | positive evidence |
| `synthetic_litany` | L_random (`synthetic_litany_random`) | visitor_at_door | 1.8955 (380/200) | 0.005 (0/200) | 381.0× | [207.0, 582.0] | positive evidence |
| `synthetic_litany` | L_empty (`empty`) | enters_room | 1.6816 (337/200) | 0.005 (0/200) | 338.0× | [148.0, 556.0] | positive evidence |
| `synthetic_litany` | L_denamed (`synthetic_litany_denamed`) | enters_room | 1.6816 (337/200) | 0.1095 (21/200) | 15.364× | [6.0, 42.5] | positive evidence |
| `synthetic_litany` | L_nonsense (`synthetic_litany_nonsense`) | enters_room | 1.6816 (337/200) | 0.0299 (5/200) | 56.333× | [16.0, 333.0] | positive evidence |
| `synthetic_litany` | L_random (`synthetic_litany_random`) | enters_room | 1.6816 (337/200) | 0.005 (0/200) | 338.0× | [148.0, 556.0] | positive evidence |
| `synthetic_litany` | L_empty (`empty`) | page_continues | 1.7662 (354/200) | 0.005 (0/200) | 355.0× | [224.0, 532.0] | positive evidence |
| `synthetic_litany` | L_denamed (`synthetic_litany_denamed`) | page_continues | 1.7662 (354/200) | 0.8458 (169/200) | 2.088× | [1.254, 3.358] | positive evidence |
| `synthetic_litany` | L_nonsense (`synthetic_litany_nonsense`) | page_continues | 1.7662 (354/200) | 0.199 (39/200) | 8.875× | [4.566, 19.625] | positive evidence |
| `synthetic_litany` | L_random (`synthetic_litany_random`) | page_continues | 1.7662 (354/200) | 0.005 (0/200) | 355.0× | [224.0, 532.0] | positive evidence |

## Per-cell

| Cell | Role | n | Tokens | Headline yield | /completion | NE | RV | Amb-NE | Amb-RV |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `synthetic_cosmological/visitor_at_door` | L_real | 200 | 38601 | 333 | 1.665 | 327 | 6 | 0 | 477 |
| `synthetic_cosmological/enters_room` | L_real | 200 | 38483 | 301 | 1.505 | 290 | 11 | 0 | 472 |
| `synthetic_cosmological/page_continues` | L_real | 200 | 38361 | 423 | 2.115 | 383 | 40 | 0 | 846 |
| `empty/visitor_at_door` | L_empty | 200 | 41288 | 0 | 0.0 | 0 | 0 | 0 | 146 |
| `empty/enters_room` | L_empty | 200 | 39720 | 0 | 0.0 | 0 | 0 | 0 | 87 |
| `empty/page_continues` | L_empty | 200 | 37083 | 0 | 0.0 | 0 | 0 | 0 | 74 |
| `synthetic_cosmological_denamed/visitor_at_door` | L_denamed | 200 | 39258 | 8 | 0.04 | 0 | 8 | 0 | 610 |
| `synthetic_cosmological_denamed/enters_room` | L_denamed | 200 | 39173 | 3 | 0.015 | 0 | 3 | 0 | 507 |
| `synthetic_cosmological_denamed/page_continues` | L_denamed | 200 | 38449 | 44 | 0.22 | 0 | 44 | 0 | 978 |
| `synthetic_cosmological_nonsense/visitor_at_door` | L_nonsense | 200 | 38803 | 0 | 0.0 | 0 | 0 | 0 | 449 |
| `synthetic_cosmological_nonsense/enters_room` | L_nonsense | 200 | 37825 | 1 | 0.005 | 0 | 1 | 0 | 662 |
| `synthetic_cosmological_nonsense/page_continues` | L_nonsense | 200 | 38716 | 10 | 0.05 | 0 | 10 | 0 | 840 |
| `synthetic_cosmological_random/visitor_at_door` | L_random | 200 | 41838 | 0 | 0.0 | 0 | 0 | 0 | 325 |
| `synthetic_cosmological_random/enters_room` | L_random | 200 | 37187 | 0 | 0.0 | 0 | 0 | 0 | 504 |
| `synthetic_cosmological_random/page_continues` | L_random | 200 | 34664 | 0 | 0.0 | 0 | 0 | 0 | 603 |
| `synthetic_litany/visitor_at_door` | L_real | 200 | 39438 | 380 | 1.9 | 364 | 16 | 0 | 107 |
| `synthetic_litany/enters_room` | L_real | 200 | 38097 | 337 | 1.685 | 314 | 23 | 0 | 490 |
| `synthetic_litany/page_continues` | L_real | 200 | 37648 | 354 | 1.77 | 178 | 176 | 0 | 236 |
| `synthetic_litany_denamed/visitor_at_door` | L_denamed | 200 | 38709 | 20 | 0.1 | 0 | 20 | 0 | 121 |
| `synthetic_litany_denamed/enters_room` | L_denamed | 200 | 37936 | 21 | 0.105 | 0 | 21 | 0 | 334 |
| `synthetic_litany_denamed/page_continues` | L_denamed | 200 | 35348 | 169 | 0.845 | 0 | 169 | 0 | 219 |
| `synthetic_litany_nonsense/visitor_at_door` | L_nonsense | 200 | 38815 | 6 | 0.03 | 0 | 6 | 0 | 37 |
| `synthetic_litany_nonsense/enters_room` | L_nonsense | 200 | 35412 | 5 | 0.025 | 0 | 5 | 0 | 171 |
| `synthetic_litany_nonsense/page_continues` | L_nonsense | 200 | 36862 | 39 | 0.195 | 0 | 39 | 0 | 84 |
| `synthetic_litany_random/visitor_at_door` | L_random | 200 | 40357 | 0 | 0.0 | 0 | 0 | 0 | 35 |
| `synthetic_litany_random/enters_room` | L_random | 200 | 40002 | 0 | 0.0 | 0 | 0 | 0 | 29 |
| `synthetic_litany_random/page_continues` | L_random | 200 | 36909 | 0 | 0.0 | 0 | 0 | 0 | 2 |

## Top entity hits per cell

### `synthetic_cosmological/visitor_at_door` (L_real)
Named entities:
  - `phengareb` × 83
  - `selephimor` × 82
  - `sekhthoroba` × 24
  - `ablakhirim` × 24
  - `aphrybetesh` × 19
  - `phelonoptra` × 18
  - `athraophol` × 14
  - `phorbamenes` × 13
  - `krathoumis` × 10
  - `demoaphris` × 10
Related vocabulary:
  - `pgm` × 3
  - `papyri` × 3

### `synthetic_cosmological/enters_room` (L_real)
Named entities:
  - `selephimor` × 129
  - `phengareb` × 24
  - `phorbamenes` × 11
  - `phelonoptra` × 10
  - `athraophol` × 10
  - `sekhthoroba` × 10
  - `ablakhirim` × 10
  - `krathoumis` × 8
  - `demoaphris` × 8
  - `velpharaim` × 8
Related vocabulary:
  - `papyri` × 7
  - `bornless` × 2
  - `pgm` × 1
  - `ceremonial` × 1

### `synthetic_cosmological/page_continues` (L_real)
Named entities:
  - `selephimor` × 78
  - `phelonoptra` × 30
  - `athraophol` × 25
  - `krathoumis` × 23
  - `phorbamenes` × 22
  - `phengareb` × 22
  - `aphrybetesh` × 17
  - `ablakhirim` × 16
  - `sekhthoroba` × 15
  - `demoaphris` × 14
Related vocabulary:
  - `papyri` × 16
  - `gnostic` × 7
  - `pgm` × 5
  - `hellenistic` × 3
  - `barbarous` × 3
  - `voces magicae` × 2
  - `theurgy` × 1
  - `ceremonial` × 1
  - `ablanathanalba` × 1
  - `bornless` × 1

### `synthetic_cosmological_denamed/visitor_at_door` (L_denamed)
Related vocabulary:
  - `gnostic` × 8

### `synthetic_cosmological_denamed/enters_room` (L_denamed)
Related vocabulary:
  - `pgm` × 1
  - `papyri` × 1
  - `bornless` × 1

### `synthetic_cosmological_denamed/page_continues` (L_denamed)
Related vocabulary:
  - `gnostic` × 15
  - `papyri` × 10
  - `barbarous` × 8
  - `theurgy` × 3
  - `voces magicae` × 3
  - `hellenistic` × 2
  - `pgm` × 1
  - `ceremonial` × 1
  - `bornless` × 1

### `synthetic_cosmological_nonsense/enters_room` (L_nonsense)
Related vocabulary:
  - `gnostic` × 1

### `synthetic_cosmological_nonsense/page_continues` (L_nonsense)
Related vocabulary:
  - `gnostic` × 5
  - `ceremonial` × 2
  - `papyri` × 1
  - `hellenistic` × 1
  - `barbarous` × 1

### `synthetic_litany/visitor_at_door` (L_real)
Named entities:
  - `theomarach` × 26
  - `mareth` × 18
  - `hialep` × 16
  - `quelimon` × 14
  - `saphrenoth` × 14
  - `throvenios` × 13
  - `iskon` × 13
  - `kerodim` × 13
  - `mirzabet` × 13
  - `astrelach` × 12
Related vocabulary:
  - `sigil` × 7
  - `invocation` × 7
  - `grimoire` × 1
  - `conjuration` × 1

### `synthetic_litany/enters_room` (L_real)
Named entities:
  - `throvenios` × 24
  - `estrymon` × 16
  - `mareth` × 12
  - `quelimon` × 12
  - `iskon` × 11
  - `kerodim` × 11
  - `astrelach` × 11
  - `volmaroth` × 11
  - `olempraem` × 11
  - `crisilim` × 11
Related vocabulary:
  - `sigil` × 12
  - `invocation` × 8
  - `tetragrammaton` × 2
  - `grimoire` × 1

### `synthetic_litany/page_continues` (L_real)
Named entities:
  - `throvenios` × 12
  - `mareth` × 10
  - `quelimon` × 10
  - `liminem adventi` × 10
  - `iskon` × 8
  - `astrelach` × 7
  - `volmaroth` × 7
  - `kerodim` × 6
  - `drabasaim` × 6
  - `olempraem` × 6
Related vocabulary:
  - `invocation` × 56
  - `grimoire` × 36
  - `sigil` × 29
  - `tetragrammaton` × 14
  - `conjuration` × 13
  - `goetia` × 13
  - `pentacle` × 10
  - `solomonic` × 2
  - `kabbalah` × 1
  - `lemegeton` × 1

### `synthetic_litany_denamed/visitor_at_door` (L_denamed)
Related vocabulary:
  - `invocation` × 10
  - `sigil` × 4
  - `grimoire` × 3
  - `sephirot` × 1
  - `litany` × 1
  - `pentacle` × 1

### `synthetic_litany_denamed/enters_room` (L_denamed)
Related vocabulary:
  - `sigil` × 8
  - `goetia` × 7
  - `invocation` × 5
  - `grimoire` × 1

### `synthetic_litany_denamed/page_continues` (L_denamed)
Related vocabulary:
  - `invocation` × 42
  - `grimoire` × 38
  - `conjuration` × 28
  - `goetia` × 18
  - `sigil` × 12
  - `lemegeton` × 11
  - `pentacle` × 10
  - `tetragrammaton` × 7
  - `kabbalah` × 2
  - `genius` × 1

### `synthetic_litany_nonsense/visitor_at_door` (L_nonsense)
Related vocabulary:
  - `litany` × 5
  - `genius` × 1

### `synthetic_litany_nonsense/enters_room` (L_nonsense)
Related vocabulary:
  - `sigil` × 4
  - `conjuration` × 1

### `synthetic_litany_nonsense/page_continues` (L_nonsense)
Related vocabulary:
  - `sigil` × 14
  - `grimoire` × 10
  - `invocation` × 7
  - `pentacle` × 4
  - `conjuration` × 2
  - `lemegeton` × 1
  - `goetia` × 1

## Top lexical divergence per comparison

### vs L_empty (`empty`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `unnamed` | 394 | 0 | +6.046 |
| `threshold` | 232 | 1 | +4.825 |
| `vessel` | 90 | 0 | +4.578 |
| `phengareb` | 83 | 0 | +4.498 |
| `selephimor` | 82 | 0 | +4.486 |
| `host` | 81 | 0 | +4.474 |
| `witness` | 144 | 1 | +4.351 |
| `thou` | 59 | 0 | +4.162 |
| `agla` | 52 | 0 | +4.038 |
| `echo` | 105 | 1 | +4.038 |
| `forgetting` | 49 | 0 | +3.979 |
| `homeowner` | 0 | 50 | -3.865 |
| `john` | 0 | 50 | -3.865 |
| `word` | 264 | 5 | +3.855 |
| `husband` | 0 | 46 | -3.783 |

### vs L_denamed (`synthetic_cosmological_denamed`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `unsigned` | 0 | 285 | -5.639 |
| `selophemor` | 0 | 119 | -4.771 |
| `phengareb` | 83 | 0 | +4.448 |
| `selephimor` | 82 | 0 | +4.436 |
| `agla` | 52 | 0 | +3.987 |
| `phengereb` | 0 | 40 | -3.697 |
| `atheraphol` | 0 | 29 | -3.384 |
| `phelonipta` | 0 | 26 | -3.279 |
| `ablakharim` | 0 | 26 | -3.279 |
| `aphrybetosh` | 0 | 25 | -3.241 |
| `ablakhirim` | 24 | 0 | +3.236 |
| `sekhthoroba` | 24 | 0 | +3.236 |
| `sekhthiroba` | 0 | 23 | -3.161 |
| `phorbomanes` | 0 | 20 | -3.028 |
| `aphrybetesh` | 19 | 0 | +3.013 |

### vs L_nonsense (`synthetic_cosmological_nonsense`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `vrendrelphor` | 0 | 232 | -5.446 |
| `vrolthen` | 0 | 112 | -4.722 |
| `phengareb` | 83 | 0 | +4.436 |
| `selephimor` | 82 | 0 | +4.424 |
| `agla` | 52 | 0 | +3.976 |
| `sent` | 0 | 43 | -3.779 |
| `smolthekrelb` | 0 | 35 | -3.578 |
| `vrokthelmpeth` | 0 | 26 | -3.291 |
| `vrokthemnarph` | 0 | 25 | -3.253 |
| `ablakhirim` | 24 | 0 | +3.224 |
| `sekhthoroba` | 24 | 0 | +3.224 |
| `save` | 23 | 0 | +3.183 |
| `alive` | 0 | 22 | -3.13 |
| `krelpharvon` | 0 | 21 | -3.086 |
| `aphrybetesh` | 19 | 0 | +3.001 |

### vs L_random (`synthetic_cosmological_random`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `river` | 0 | 442 | -6.013 |
| `unnamed` | 394 | 1 | +5.366 |
| `ecosystem` | 0 | 162 | -5.013 |
| `vessel` | 90 | 0 | +4.591 |
| `ecosystems` | 0 | 98 | -4.515 |
| `phengareb` | 83 | 0 | +4.511 |
| `selephimor` | 82 | 0 | +4.499 |
| `homeowner` | 0 | 74 | -4.237 |
| `thou` | 59 | 0 | +4.175 |
| `threshold` | 232 | 3 | +4.145 |
| `fish` | 0 | 67 | -4.139 |
| `agla` | 52 | 0 | +4.051 |
| `word` | 264 | 4 | +4.051 |
| `fire` | 48 | 0 | +3.972 |
| `health` | 0 | 49 | -3.831 |

### vs L_empty (`empty`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `unnamed` | 341 | 0 | +5.866 |
| `vessel` | 267 | 0 | +5.623 |
| `selephimor` | 129 | 0 | +4.899 |
| `her` | 0 | 129 | -4.836 |
| `she` | 0 | 114 | -4.713 |
| `witness` | 96 | 0 | +4.606 |
| `spirits` | 67 | 0 | +4.251 |
| `didst` | 61 | 0 | +4.159 |
| `syllable` | 51 | 0 | +3.983 |
| `invocation` | 42 | 0 | +3.793 |
| `woman` | 0 | 44 | -3.775 |
| `skull` | 0 | 41 | -3.706 |
| `ritual` | 38 | 0 | +3.695 |
| `girl` | 0 | 39 | -3.657 |
| `prophet` | 36 | 0 | +3.643 |

### vs L_denamed (`synthetic_cosmological_denamed`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `unsigned` | 0 | 234 | -5.442 |
| `selephimor` | 129 | 0 | +4.885 |
| `figures` | 68 | 0 | +4.252 |
| `selophemor` | 0 | 55 | -4.008 |
| `surrounded` | 52 | 0 | +3.988 |
| `she` | 0 | 53 | -3.971 |
| `beast` | 0 | 53 | -3.971 |
| `sekhthiroba` | 0 | 35 | -3.566 |
| `ablakharim` | 0 | 34 | -3.538 |
| `drives` | 26 | 0 | +3.314 |
| `narrative` | 24 | 0 | +3.237 |
| `phengareb` | 24 | 0 | +3.237 |
| `entering` | 0 | 24 | -3.201 |
| `birds` | 23 | 0 | +3.196 |
| `phelonipta` | 0 | 23 | -3.16 |

### vs L_nonsense (`synthetic_cosmological_nonsense`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `vrendrelphor` | 0 | 133 | -4.915 |
| `selephimor` | 129 | 0 | +4.85 |
| `vrolthen` | 0 | 108 | -4.709 |
| `figures` | 68 | 0 | +4.217 |
| `surrounded` | 52 | 0 | +3.953 |
| `beautiful` | 45 | 0 | +3.811 |
| `tired` | 36 | 0 | +3.594 |
| `vrolthend` | 0 | 32 | -3.514 |
| `woman` | 0 | 27 | -3.349 |
| `drives` | 26 | 0 | +3.279 |
| `narrative` | 24 | 0 | +3.202 |
| `phengareb` | 24 | 0 | +3.202 |
| `heights` | 0 | 22 | -3.153 |
| `gown` | 0 | 22 | -3.153 |
| `vrokthelmpeth` | 0 | 21 | -3.108 |

### vs L_random (`synthetic_cosmological_random`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `river` | 0 | 1145 | -7.078 |
| `ecosystem` | 0 | 249 | -5.556 |
| `unnamed` | 341 | 1 | +5.107 |
| `flowing` | 0 | 151 | -5.058 |
| `word` | 151 | 0 | +4.99 |
| `vessel` | 267 | 1 | +4.864 |
| `selephimor` | 129 | 0 | +4.833 |
| `ecosystems` | 0 | 103 | -4.679 |
| `threshold` | 103 | 0 | +4.61 |
| `echo` | 88 | 0 | +4.454 |
| `gravel` | 0 | 81 | -4.441 |
| `point` | 0 | 79 | -4.416 |
| `aquatic` | 0 | 79 | -4.416 |
| `community` | 0 | 76 | -4.378 |
| `shaped` | 0 | 75 | -4.365 |

### vs L_empty (`empty`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `unnamed` | 486 | 0 | +6.154 |
| `invocation` | 317 | 0 | +5.728 |
| `spirits` | 175 | 0 | +5.137 |
| `ritual` | 138 | 0 | +4.901 |
| `shall` | 115 | 0 | +4.72 |
| `threshold` | 109 | 0 | +4.667 |
| `witness` | 91 | 0 | +4.488 |
| `vessel` | 88 | 0 | +4.455 |
| `upon` | 81 | 0 | +4.373 |
| `selephimor` | 78 | 0 | +4.336 |
| `silence` | 74 | 0 | +4.284 |
| `thou` | 72 | 0 | +4.257 |
| `x` | 1 | 134 | -4.246 |
| `speaker` | 71 | 0 | +4.243 |
| `prophet` | 70 | 0 | +4.229 |

### vs L_denamed (`synthetic_cosmological_denamed`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `unsigned` | 1 | 364 | -5.204 |
| `selophemor` | 0 | 144 | -4.974 |
| `selephimor` | 78 | 0 | +4.372 |
| `phelonipta` | 0 | 69 | -4.246 |
| `atheraphol` | 0 | 56 | -4.041 |
| `phorbomanes` | 0 | 47 | -3.869 |
| `aphrybetosh` | 0 | 36 | -3.609 |
| `phelonoptra` | 30 | 0 | +3.436 |
| `velphiraim` | 0 | 29 | -3.399 |
| `krethaumis` | 0 | 29 | -3.399 |
| `demaphris` | 0 | 28 | -3.365 |
| `iphtoron` | 0 | 28 | -3.365 |
| `athraophol` | 25 | 0 | +3.26 |
| `krathoumis` | 23 | 0 | +3.18 |
| `phengareb` | 22 | 0 | +3.138 |

### vs L_nonsense (`synthetic_cosmological_nonsense`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `vrolthen` | 0 | 359 | -5.877 |
| `vrendrelphor` | 0 | 114 | -4.736 |
| `selephimor` | 78 | 0 | +4.379 |
| `vrokthemnarph` | 0 | 66 | -4.195 |
| `vrokthelmpeth` | 0 | 42 | -3.752 |
| `phelonoptra` | 30 | 0 | +3.443 |
| `krelpharvon` | 0 | 29 | -3.392 |
| `plomprenkrol` | 0 | 29 | -3.392 |
| `athraophol` | 25 | 0 | +3.267 |
| `plendrokt` | 0 | 25 | -3.249 |
| `krathoumis` | 23 | 0 | +3.187 |
| `smelthrenaph` | 0 | 23 | -3.169 |
| `phengareb` | 22 | 0 | +3.145 |
| `phorbamenes` | 22 | 0 | +3.145 |
| `smolthekrelb` | 0 | 22 | -3.126 |

### vs L_random (`synthetic_cosmological_random`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `river` | 0 | 865 | -6.865 |
| `ecosystems` | 0 | 442 | -6.195 |
| `ecosystem` | 0 | 431 | -6.17 |
| `unnamed` | 486 | 0 | +6.087 |
| `invocation` | 317 | 0 | +5.661 |
| `lotic` | 0 | 194 | -5.374 |
| `aquatic` | 0 | 194 | -5.374 |
| `channel` | 0 | 160 | -5.183 |
| `streams` | 0 | 156 | -5.158 |
| `fish` | 0 | 153 | -5.138 |
| `organisms` | 0 | 123 | -4.922 |
| `biological` | 0 | 118 | -4.88 |
| `community` | 0 | 114 | -4.846 |
| `ritual` | 138 | 0 | +4.833 |
| `flowing` | 0 | 112 | -4.829 |

### vs L_empty (`empty`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `ritual` | 104 | 0 | +4.7 |
| `chamber` | 60 | 0 | +4.157 |
| `gate` | 59 | 0 | +4.14 |
| `sacred` | 57 | 0 | +4.106 |
| `homeowner` | 0 | 50 | -3.886 |
| `wife` | 0 | 50 | -3.886 |
| `john` | 0 | 50 | -3.886 |
| `spirits` | 137 | 2 | +3.874 |
| `husband` | 0 | 46 | -3.804 |
| `want` | 0 | 43 | -3.738 |
| `re` | 1 | 87 | -3.738 |
| `space` | 39 | 0 | +3.735 |
| `guardian` | 38 | 0 | +3.709 |
| `sarah` | 0 | 39 | -3.643 |
| `names` | 104 | 2 | +3.601 |

### vs L_denamed (`synthetic_litany_denamed`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `shadowtop` | 0 | 32 | -3.515 |
| `ravenspire` | 0 | 32 | -3.515 |
| `queloman` | 0 | 28 | -3.386 |
| `throbenas` | 0 | 26 | -3.314 |
| `theomarach` | 26 | 0 | +3.277 |
| `lominem` | 0 | 25 | -3.277 |
| `adventu` | 0 | 20 | -3.063 |
| `drabosaim` | 0 | 18 | -2.963 |
| `mareth` | 18 | 0 | +2.926 |
| `liminem` | 17 | 0 | +2.872 |
| `vesporath` | 0 | 16 | -2.852 |
| `hialep` | 16 | 0 | +2.815 |
| `maraith` | 0 | 15 | -2.791 |
| `brashveroth` | 0 | 15 | -2.791 |
| `olemproam` | 0 | 15 | -2.791 |

### vs L_nonsense (`synthetic_litany_nonsense`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `spirits` | 137 | 1 | +4.218 |
| `vrokthemnar` | 0 | 55 | -4.041 |
| `want` | 0 | 32 | -3.512 |
| `party` | 0 | 27 | -3.348 |
| `theomarach` | 26 | 0 | +3.28 |
| `krelphendoth` | 0 | 25 | -3.274 |
| `divine` | 22 | 0 | +3.12 |
| `vrolthemnar` | 0 | 21 | -3.107 |
| `vronth` | 0 | 20 | -3.06 |
| `klompronek` | 0 | 19 | -3.012 |
| `mareth` | 18 | 0 | +2.929 |
| `smelthrenak` | 0 | 17 | -2.906 |
| `snolthar` | 0 | 17 | -2.906 |
| `vroklep` | 0 | 17 | -2.906 |
| `chest` | 0 | 17 | -2.906 |

### vs L_random (`synthetic_litany_random`), tail `visitor_at_door`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `anglerfish` | 0 | 461 | -6.113 |
| `spirits` | 137 | 0 | +4.95 |
| `lure` | 0 | 98 | -4.572 |
| `doorkeeper` | 77 | 0 | +4.38 |
| `sacred` | 57 | 0 | +4.083 |
| `re` | 1 | 113 | -4.02 |
| `temple` | 48 | 0 | +3.915 |
| `entry` | 45 | 0 | +3.852 |
| `want` | 0 | 43 | -3.761 |
| `fish` | 0 | 41 | -3.715 |
| `guardian` | 38 | 0 | +3.687 |
| `female` | 0 | 39 | -3.666 |
| `fire` | 35 | 0 | +3.607 |
| `angler` | 0 | 36 | -3.588 |
| `sanctuary` | 31 | 0 | +3.489 |

### vs L_empty (`empty`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `spirits` | 93 | 0 | +4.585 |
| `command` | 63 | 0 | +4.201 |
| `mortal` | 58 | 0 | +4.119 |
| `re` | 0 | 62 | -4.101 |
| `ritual` | 55 | 0 | +4.067 |
| `mysteries` | 49 | 0 | +3.954 |
| `names` | 73 | 1 | +3.653 |
| `girl` | 0 | 39 | -3.647 |
| `boy` | 0 | 39 | -3.647 |
| `stream` | 0 | 38 | -3.622 |
| `angel` | 34 | 0 | +3.597 |
| `podcast` | 0 | 36 | -3.569 |
| `thinks` | 0 | 36 | -3.569 |
| `garden` | 0 | 36 | -3.569 |
| `circle` | 33 | 0 | +3.568 |

### vs L_denamed (`synthetic_litany_denamed`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `azazel` | 0 | 50 | -3.936 |
| `octorum` | 0 | 42 | -3.765 |
| `alive` | 1 | 52 | -3.281 |
| `fullness` | 0 | 24 | -3.223 |
| `throvenios` | 24 | 0 | +3.215 |
| `temple` | 0 | 17 | -2.895 |
| `estramon` | 0 | 17 | -2.895 |
| `decides` | 0 | 17 | -2.895 |
| `throbenas` | 0 | 17 | -2.895 |
| `queloman` | 0 | 16 | -2.837 |
| `estrymon` | 16 | 0 | +2.829 |
| `iston` | 0 | 15 | -2.777 |
| `volmuroth` | 0 | 15 | -2.777 |
| `samael` | 15 | 0 | +2.768 |
| `oxivatu` | 15 | 0 | +2.768 |

### vs L_nonsense (`synthetic_litany_nonsense`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `peace` | 35 | 0 | +3.51 |
| `grateful` | 29 | 0 | +3.328 |
| `lloigor` | 0 | 23 | -3.251 |
| `oppose` | 0 | 22 | -3.209 |
| `truthfully` | 25 | 0 | +3.185 |
| `thargothax` | 0 | 21 | -3.164 |
| `caster` | 0 | 21 | -3.164 |
| `throvenios` | 24 | 0 | +3.146 |
| `party` | 0 | 20 | -3.118 |
| `vronth` | 0 | 20 | -3.118 |
| `vrokthemnar` | 0 | 20 | -3.118 |
| `spirits` | 93 | 3 | +3.084 |
| `gath` | 0 | 19 | -3.069 |
| `mrolthengek` | 0 | 19 | -3.069 |
| `krelphendoth` | 0 | 19 | -3.069 |

### vs L_random (`synthetic_litany_random`), tail `enters_room`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `anglerfish` | 0 | 306 | -5.678 |
| `fish` | 1 | 200 | -4.561 |
| `lure` | 0 | 87 | -4.429 |
| `names` | 73 | 0 | +4.353 |
| `re` | 0 | 70 | -4.214 |
| `command` | 63 | 0 | +4.208 |
| `female` | 0 | 69 | -4.2 |
| `mortal` | 58 | 0 | +4.126 |
| `teeth` | 0 | 61 | -4.078 |
| `got` | 0 | 50 | -3.883 |
| `male` | 0 | 42 | -3.712 |
| `thank` | 38 | 0 | +3.712 |
| `call` | 38 | 0 | +3.712 |
| `ask` | 111 | 2 | +3.669 |
| `swims` | 0 | 40 | -3.665 |

### vs L_empty (`empty`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `spirits` | 338 | 0 | +5.811 |
| `shall` | 162 | 0 | +5.079 |
| `names` | 347 | 2 | +4.738 |
| `ritual` | 111 | 0 | +4.703 |
| `thee` | 89 | 0 | +4.485 |
| `upon` | 81 | 0 | +4.392 |
| `speak` | 74 | 0 | +4.302 |
| `x` | 1 | 134 | -4.227 |
| `spoken` | 67 | 0 | +4.204 |
| `code` | 0 | 63 | -4.174 |
| `numbers` | 0 | 60 | -4.126 |
| `gate` | 61 | 0 | +4.112 |
| `unto` | 57 | 0 | +4.045 |
| `manuscript` | 56 | 0 | +4.028 |
| `invocation` | 56 | 0 | +4.028 |

### vs L_denamed (`synthetic_litany_denamed`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `calabath` | 38 | 0 | +3.601 |
| `yalmon` | 0 | 28 | -3.43 |
| `anaphazabrabon` | 0 | 28 | -3.43 |
| `voices` | 31 | 0 | +3.403 |
| `throbenas` | 0 | 22 | -3.199 |
| `octorum` | 0 | 19 | -3.059 |
| `enochian` | 0 | 18 | -3.007 |
| `lominem` | 0 | 17 | -2.953 |
| `adventu` | 0 | 17 | -2.953 |
| `iston` | 0 | 16 | -2.896 |
| `maraith` | 0 | 16 | -2.896 |
| `queloman` | 0 | 16 | -2.896 |
| `dee` | 0 | 16 | -2.896 |
| `aam` | 18 | 0 | +2.881 |
| `eko` | 18 | 0 | +2.881 |

### vs L_nonsense (`synthetic_litany_nonsense`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `blank` | 0 | 57 | -4.082 |
| `vroth` | 0 | 50 | -3.953 |
| `calabath` | 38 | 0 | +3.642 |
| `voices` | 31 | 0 | +3.445 |
| `vrokthemnar` | 0 | 29 | -3.422 |
| `snorth` | 0 | 28 | -3.388 |
| `klompronek` | 0 | 25 | -3.279 |
| `sneldrek` | 0 | 25 | -3.279 |
| `mrolthengek` | 0 | 24 | -3.24 |
| `vronth` | 0 | 24 | -3.24 |
| `east` | 25 | 0 | +3.237 |
| `vrendrelth` | 0 | 23 | -3.199 |
| `vrendrabmar` | 0 | 23 | -3.199 |
| `snolthrolm` | 0 | 23 | -3.199 |
| `undead` | 0 | 22 | -3.157 |

### vs L_random (`synthetic_litany_random`), tail `page_continues`
| Word | L_real | Control | log freq ratio |
|---|---:|---:|---:|
| `anglerfish` | 0 | 709 | -6.585 |
| `fish` | 0 | 457 | -6.147 |
| `female` | 0 | 342 | -5.858 |
| `spirits` | 338 | 0 | +5.806 |
| `bacteria` | 0 | 313 | -5.769 |
| `species` | 0 | 267 | -5.611 |
| `esca` | 0 | 212 | -5.381 |
| `male` | 0 | 206 | -5.353 |
| `names` | 347 | 1 | +5.139 |
| `ocean` | 0 | 160 | -5.101 |
| `power` | 166 | 0 | +5.098 |
| `symbiotic` | 0 | 156 | -5.076 |
| `shall` | 162 | 0 | +5.074 |
| `prey` | 0 | 139 | -4.961 |
| `seawater` | 0 | 129 | -4.887 |

## Caveats

- Headline yield counts whole-word, case-insensitive matches.
- Ambiguous-tier counts (`Amb-NE`, `Amb-RV`) are tracked but NOT in the headline (common words ⇒ baseline false positives).
- Pairwise comparisons computed per tail. Confidence intervals not yet computed — defer to bootstrap when scaling beyond smoke.