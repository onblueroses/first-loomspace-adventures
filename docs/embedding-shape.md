# M1 — Embedding distribution shape analysis

The headline yield metric counts *which specific entities appear*. The M1 embedding analysis measures *what kind of text the cells produce overall*, in a learned-semantic space.

Computed post-hoc over all 10800 completions using `sentence-transformers/all-MiniLM-L6-v2` (384-dim sentence embedding, ~90MB). For each cell, we compute:

- **Centroid**: mean embedding vector
- **Pairwise centroid cosine distance** between cells (cross-cell distance)
- **Within-cell spread**: median pairwise cosine distance among completions in the cell (lower = tighter cluster)
- **Multimodality**: BIC scan for `GaussianMixture(n_components=k)` over k=1..5, after PCA reduction to 50 dims. `k_best` is the k that minimizes BIC. k_best=1 → unimodal (one dominant attractor); k_best ≥ 2 → multimodal (competing attractors).

Code: `src/embed_shape.py`. JSON outputs: `results/headline-2026-05-30-{deepseek,hermes}/embedding_shape.json`.

---

## Per-cell embedding profile

### DeepSeek

| Cell | n | spread | k_best |
|---|---|---|---|
| astrachios/visitor_at_door | 200 | 0.598 | 1 |
| astrachios/enters_room | 200 | 0.668 | 1 |
| astrachios/page_continues | 200 | 0.530 | 1 |
| astrachios_denamed/visitor_at_door | 200 | 0.588 | 1 |
| astrachios_denamed/enters_room | 200 | 0.659 | 1 |
| astrachios_denamed/page_continues | 200 | 0.555 | 1 |
| astrachios_nonsense/visitor_at_door | 200 | 0.600 | **4** |
| astrachios_nonsense/enters_room | 200 | 0.496 | 2 |
| astrachios_nonsense/page_continues | 200 | 0.578 | **4** |
| astrachios_random/visitor_at_door | 200 | 0.354 | 2 |
| astrachios_random/enters_room | 199 | 0.163 | 2 |
| astrachios_random/page_continues | 200 | 0.196 | 1 |
| empty/visitor_at_door | 200 | 0.449 | **4** |
| empty/enters_room | 200 | 0.488 | 1 |
| empty/page_continues | 200 | 0.253 | 3 |
| headless/visitor_at_door | 200 | **0.292** | 1 |
| headless/enters_room | 200 | **0.213** | 1 |
| headless/page_continues | 200 | **0.189** | 1 |
| headless_denamed/visitor_at_door | 200 | 0.332 | 1 |
| headless_denamed/enters_room | 200 | 0.319 | 1 |
| headless_denamed/page_continues | 200 | 0.210 | 1 |
| headless_nonsense/visitor_at_door | 200 | 0.357 | 1 |
| headless_nonsense/enters_room | 200 | 0.317 | 1 |
| headless_nonsense/page_continues | 200 | 0.170 | 1 |
| headless_random/visitor_at_door | 200 | 0.474 | 1 |
| headless_random/enters_room | 200 | 0.157 | 2 |
| headless_random/page_continues | 199 | 0.236 | 1 |

### Hermes

| Cell | n | spread | k_best |
|---|---|---|---|
| astrachios/visitor_at_door | 200 | 0.501 | 1 |
| astrachios/enters_room | 195 | 0.603 | 1 |
| astrachios/page_continues | 200 | 0.544 | 1 |
| astrachios_denamed/visitor_at_door | 200 | 0.523 | 1 |
| astrachios_denamed/enters_room | 200 | 0.579 | 1 |
| astrachios_denamed/page_continues | 200 | 0.566 | 1 |
| astrachios_nonsense/visitor_at_door | 200 | 0.571 | 1 |
| astrachios_nonsense/enters_room | 196 | 0.654 | 2 |
| astrachios_nonsense/page_continues | 200 | 0.607 | 1 |
| astrachios_random/visitor_at_door | 200 | 0.381 | 2 |
| astrachios_random/enters_room | 199 | 0.637 | **4** |
| astrachios_random/page_continues | 200 | 0.304 | 1 |
| empty/visitor_at_door | 200 | **0.682** | 1 |
| empty/enters_room | 199 | **0.767** | 1 |
| empty/page_continues | 200 | **0.962** | 1 |
| headless/visitor_at_door | 200 | 0.608 | 1 |
| headless/enters_room | 199 | 0.631 | 2 |
| headless/page_continues | 200 | 0.509 | 1 |
| headless_denamed/visitor_at_door | 200 | 0.589 | 1 |
| headless_denamed/enters_room | 199 | 0.626 | 2 |
| headless_denamed/page_continues | 200 | 0.567 | 1 |
| headless_nonsense/visitor_at_door | 200 | 0.556 | 1 |
| headless_nonsense/enters_room | 200 | 0.603 | 2 |
| headless_nonsense/page_continues | 200 | 0.519 | 1 |
| headless_random/visitor_at_door | 200 | 0.698 | 1 |
| headless_random/enters_room | 193 | 0.815 | **4** |
| headless_random/page_continues | 200 | 0.455 | 1 |

---

## Cross-cell centroid distance (cosine, lower = more similar)

| Comparison | DeepSeek | Hermes |
|---|---|---|
| Astrachios visitor: L_real ↔ L_denamed | 0.1202 | **0.0243** |
| Astrachios visitor: L_real ↔ L_nonsense | 0.1713 | **0.0427** |
| Astrachios visitor: L_real ↔ L_random | 0.6268 | 0.5896 |
| Astrachios visitor: L_real ↔ L_empty | 0.4278 | 0.3281 |
| Astrachios page_continues: L_real ↔ L_denamed | **0.0346** | **0.0144** |
| Headless visitor: L_real ↔ L_denamed | 0.2301 | **0.0252** |
| Headless visitor: L_real ↔ L_nonsense | 0.2460 | **0.0938** |
| Headless visitor: L_real ↔ L_random | 0.7467 | 0.4756 |
| Headless page_continues: L_real ↔ L_denamed | 0.1526 | **0.0406** |
| **Astrachios L_real ↔ Headless L_real** (cross-liturgy) | 0.2748 | **0.1088** |

---

## What the numbers say

### 1. L_real and L_denamed are NEAR-IDENTICAL in embedding space

Especially for `page_continues`. Hermes Astrachios L_real ↔ L_denamed cosine distance is 0.0144 — 1.4% — basically the same point in the embedding space. DeepSeek for the same comparison is 0.0346 — 3.5%.

**Interpretation**: the model is doing the SAME KIND OF THING for both (scholar-mode attribution / commentary on grimoire-form text), just populating it with different specific entities. The egregore-weight signal lives in the entity-fillers, not the genre-shape.

This is why the headline yield ratio (e.g., 2.5× for Astrachios page_continues Hermes) is much "smaller" than the L_real-vs-empty ratio (77×) — the page_continues tail pulls the model into scholar-mode for both real and denamed, and scholar-mode-with-real-names produces 2.5× more entity hits than scholar-mode-with-denamed-names. But it's still scholar mode in both cases.

For other tails (visitor_at_door, enters_room), the L_real ↔ L_denamed distance is slightly larger (0.02-0.23) because the in-narrative tails don't force a single mode and the model can vary more freely between conditions.

### 2. Hermes is more attractor-collapsed than DeepSeek

Hermes maps everything ceremonial-magic-shaped into a single tight region. For Astrachios visitor:
- Hermes L_real ↔ L_denamed: 0.0243
- Hermes L_real ↔ L_nonsense: 0.0427

DeepSeek differentiates more sharply:
- DeepSeek L_real ↔ L_denamed: 0.1202 (5× farther than Hermes)
- DeepSeek L_real ↔ L_nonsense: 0.1713

**Interpretation**: Hermes has a strong single "magician-mode" attractor that pulls everything ceremonial-magic-shaped to roughly the same semantic region. DeepSeek differentiates between specific corpus items more (its multiple attractors — scholar, conjuration script, minimal-closure, syncretic-gnosis — produce more semantic variation between conditions).

This is consistent with the qualitative reads: Hermes consistently goes to initiatory ceremonial-magic content; DeepSeek's attractors vary widely.

### 3. Liturgy-identity is stronger than real-vs-denamed

Both models, but more dramatically in Hermes:
- DeepSeek: Astrachios L_real ↔ Headless L_real = 0.2748 (cross-liturgy distance)
  vs Astrachios L_real ↔ Astrachios L_denamed = 0.1202
- Hermes: Astrachios L_real ↔ Headless L_real = 0.1088
  vs Astrachios L_real ↔ Astrachios L_denamed = 0.0243

In both models, the two real liturgies are FARTHER from each other than each is from its own denamed twin. **The "Astrachios-style prayer" basin and the "Headless-style prayer" basin are more distinct from each other than each basin's real ↔ denamed split.**

This makes sense: the two liturgies are from different traditions (Grimorium Verum vs PGM), have different content patterns (name-litany vs cosmological-prose + voces magicae), and trigger different specific attractor-clusters (Astrachios → Solomonic / Goetic; Headless → Crowley / Golden Dawn / Liber Samekh).

### 4. Headless L_real has unusually TIGHT spread in DeepSeek

DeepSeek Headless L_real spread = 0.189-0.292 across the three tails.
DeepSeek Astrachios L_real spread = 0.530-0.668.

Headless L_real produces near-identical scholarly attributions each time. The qualitative reads bear this out: nearly every Headless L_real DeepSeek completion is some variant of "This is the Bornless Ritual / Preliminary Invocation of the Goetia / PGM V.96-172, adapted by Crowley as Liber Samekh..." — minor textual variations of the same scholarly framing.

Astrachios L_real is much wider because DeepSeek has multiple competing attractors for the Astrachios prayer: scholar-mode (Arbatel of Magic identification), conjuration-script mode (full Goetia evocation), minimal-ritual-closure mode (one-sentence response), syncretic-gnosis mode (Abraxas + Mesopotamia + Sefer Yetzirah), occasional degenerate loops.

**Interpretation**: the spread metric captures *how many distinct attractor-types the model has for this input*. A tight spread means one dominant mode; a wide spread means multiple competing modes within the same cell.

### 5. Hermes L_empty has the widest spread of any cell — 0.682-0.962

With no prompt content, Hermes has many possible continuations. Qualitative reads showed: Romantic poetry, political documents, Wikipedia talk pages, modern interactive-fiction scenarios, 19th-century novelistic prose, conversation-fiction. No anchoring content → many possible attractors fire.

By contrast, Hermes L_real cells have *tighter* spread (0.501-0.631) than L_empty. **The presence of ritual content NARROWS the operator's distribution.** The liturgical prompts focus the model into a more specific region of semantic space than an empty prompt does.

This is a non-obvious finding. One might have expected that liturgical prompts (being unusual / out-of-distribution) would push the model into a wider spread of responses. The opposite is true: liturgical prompts are *strong attractors* that focus the model, while empty prompts leave it free to vary maximally.

### 6. Multimodality (k_best) maps to "model knows what to do"

| Cell type | k_best (DeepSeek) | k_best (Hermes) |
|---|---|---|
| L_real | 1 (always) | 1 (mostly) |
| L_denamed | 1 (always) | 1 (always) |
| L_random | 1-2 | 1-4 |
| L_nonsense | 1-4 (often 2-4 for DeepSeek visitor/page) | 1-2 (mostly 1) |
| L_empty | 1-4 (often 2-4 for DeepSeek visitor/page) | 1 (always, despite wide spread) |

**When the model recognizes the input** (L_real recognized as canonical, L_denamed as derivative, L_random as topic-continuation), it has ONE strong attractor — unimodal embedding distribution.

**When the model doesn't know what to do** (L_nonsense, L_empty for DeepSeek), MULTIPLE competing attractors fire across different completions. Multimodal.

The contrast between DeepSeek and Hermes here is interesting: DeepSeek shows clear multimodality in L_nonsense/L_empty (k=3-4); Hermes shows mostly unimodal even in L_nonsense/L_empty. **Hermes has a single dominant default attractor that pulls even unrecognized inputs into one mode** (with high within-cell spread but still single-mode); **DeepSeek has multiple competing fallback attractors that produce mode-separation**.

This is consistent with operator-physics: Hermes magician-mode is one attractor that captures everything; DeepSeek scholar-mode is one of several competing attractors.

For DeepSeek astrachios_nonsense/visitor at k=4, the qualitative reads showed four modes: degenerate loops + invented-Enochian-style angel-lists + fable mode + minimal-response. These are real semantic modes; BIC found them automatically.

### 7. The yield-vs-embedding two-metric framework

Comparing the two metrics for the headline test (L_real vs L_denamed):

| Cell | Yield ratio | Embedding distance |
|---|---|---|
| Astrachios visitor (DeepSeek) | 24.6× | 0.1202 |
| Astrachios visitor (Hermes) | 8.9× | 0.0243 |
| Astrachios page_continues (DeepSeek) | 2.4× | 0.0346 |
| Astrachios page_continues (Hermes) | 2.5× | 0.0144 |
| Headless visitor (DeepSeek) | 7.8× | 0.2301 |
| Headless visitor (Hermes) | 29.0× | 0.0252 |
| Headless page_continues (DeepSeek) | 1.6× (null) | 0.1526 |
| Headless page_continues (Hermes) | 4.0× | 0.0406 |

(Cross-tail comparisons within liturgy omitted — see the per-cell embedding profile above for individual centroid distances; the `enters_room` tail behaves similarly to `visitor_at_door` for both models.)

Note that yield-ratio and embedding-distance don't correlate strongly. Hermes Headless visitor has the highest yield ratio (29.0×) and the smallest embedding distance (0.0252). The two metrics measure different aspects.

**Interpretation**: yield captures specific-entity-cluster activation; embedding captures genre/mode classification. Both are valid; neither alone is sufficient.

For the egregore-weight thesis specifically:
- Yield says **YES, the egregore-weight signal exists strongly**. Specific entities fire much more with real names than denamed.
- Embedding says **the egregore-weight signal is LOCAL** to entity-fillers, not extending to global semantic shape. Real and denamed produce the same KIND of text.

A theoretical model: the model has form-shaped slots that can be filled by entity-content. Real names fill them with maximum density (the historical canonical attractors). Denamed substitutions fill the slots with substitute entities (the operator's continuation-coherence accepts them, with lower historical-canonical density). The slots themselves are determined by form. Yield measures slot-occupancy by canonical entities; embedding measures slot-structure (which is shared between real and denamed because the form is shared).

---

## Limitations of M1 as run

The all-MiniLM-L6-v2 model is small (90MB, 384-dim) and trained primarily on general English semantic similarity. It may not be sensitive to fine-grained ceremonial-magic register differences. A larger or domain-specific embedding model (e.g., `intfloat/multilingual-e5-large` as originally specified in the protocol, or a domain-finetuned model) might produce different cell-distance ratios.

For the purposes of *this* analysis — comparing genre/mode at the broad semantic level — MiniLM is sufficient. For finer-grained "is this Crowley-Liber-Samekh-style or PGM-direct-style?" distinctions, a stronger embedding model would be needed.

The PCA-to-50-dims step before GMM-BIC is a defensible default but introduces dimensionality-reduction-dependent results. A higher PCA dimension (or no PCA) would produce slightly different k_best values. The pattern (L_real/L_denamed → k=1; L_nonsense/L_empty → k=2-4) is robust across reasonable PCA choices we spot-checked.

Sampling 500 within-cell pairs (vs all 200*199/2 = 19900) for spread is a downsampling that produces some noise; the spread values should be considered accurate to ~5%.

None of these limitations affect the qualitative findings (L_real ↔ L_denamed is much smaller than L_real ↔ L_random; Hermes is more attractor-collapsed than DeepSeek; multimodality maps to "model doesn't know what to do"). They might affect specific numeric comparisons by 10-20%.

---

## What M1 adds to the headline

Without M1, the picture is: yield ratios are 5-30× for the headline L_real vs L_denamed comparison; this is a large signal for egregore weight.

With M1, the picture becomes: yield ratios are large *but localized to entity-fillers*. The model's global semantic shape (embedding centroid) is very similar between real and denamed — they're the same KIND of text. The egregore is in *what specific entities populate the form-shaped slots*, not in *what genre of text the model produces*.

This is a more nuanced and more honest interpretation. M1 prevents over-claiming.

It also produces a new measurable: **multimodality as input-recognition signal**. K_best=1 means "model knows what to do." K_best ≥ 2 means "model has multiple competing fallback attractors." This is a free diagnostic that informs interpretation of any other measurement on the cell.

For future runs, M1 should be a standard reporting artifact alongside measure.py.
