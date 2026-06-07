# Methodology lessons from the first headline run

What the experiment taught us about measuring egregore-weight in language operators. These lessons should inform any future run, replication, or extension.

---

## Lesson 1: Yield and embedding-distance measure different layers

The headline yield metric (per-completion entity count ratio, L_real / L_denamed) and the M1 embedding-distance metric (cosine distance between cell centroids in sentence-embedding space) tell different stories about the same data.

| Comparison | Yield ratio | Embedding distance |
|---|---|---|
| Astrachios visitor: L_real vs L_denamed (DeepSeek) | 24.6× | 0.1202 |
| Astrachios visitor: L_real vs L_denamed (Hermes) | 8.9× | **0.0243** |
| Astrachios page_continues: L_real vs L_denamed (Hermes) | 2.5× | **0.0144** |
| Headless visitor: L_real vs L_denamed (Hermes) | 29.0× | **0.0252** |
| Headless page_continues: L_real vs L_denamed (DeepSeek) | 1.6× *null* | 0.1526 |

Yield ratios up to ~25× alongside cosine distances under ~0.03. **These do not contradict.** They measure different aspects:

- **Yield = specific entity-cluster activation.** "Astaroth" fires, "Bornless" fires, "tetragrammaton" fires — but only when the specific real names are present. Yield captures *which specific attractors are populated*.
- **Embedding distance = genre/mode classification.** Both real and denamed sit in the "occult-style ritual text" basin. The model treats them as the same KIND of text. Embedding captures *which broad mode the model is operating in*.

The right interpretation: the model treats real and denamed as the same KIND of text but populates with different specific entities. The egregore is in the entity-fillers, not the genre-shape.

**Implication**: the yield comparison overstates the cosmological gap. A 100× yield ratio with 0.02 cosine distance is a signal of *specific-entity-cluster differential activation within a shared semantic basin*, not a signal of "the model treats real and denamed as cosmologically different texts." Both metrics should be reported. Neither alone is sufficient.

The yield framing also overstates the contribution of the more famous historical names. Adonai/Elohim/Sabaoth appear in L_denamed because the model invokes the **stock Solomonic conjuration formula** as a fallback — those theonyms are part of every ceremonial-magic conjuration. The L_real vs L_denamed differential for those specific theonyms is therefore noisy; the differential is cleaner for less-canonical names (Astaroth, Bornless, IAΩ-SABAΩTH).

For future writeups: lead with yield (the headline), but discuss embedding distance as the complementary metric that constrains interpretation.

---

## Lesson 2: L_denamed is "fallback to the generic ceremonial-magic library," not "nothing"

The protocol document defined L_denamed as "the same liturgy with phonetically-shifted names — preserving cadence, structure, and register; only specific named entities replaced by phonetically similar nonsense." The intent was for L_denamed to be a *form-matched neologistic control* — same form, no real-name semantic weight.

The data shows that L_denamed produces a specific kind of operator behavior that is NOT "model with nothing to say." Instead, the model recognizes "this is ceremonial-magic-form text I don't specifically recognize" and falls back to producing **the generic ceremonial-magic library**:

- Heptameron-style planetary-angel invocations
- Key of Solomon prayers (e.g., "send me your holy angel, Anael")
- 60-entry alphabetical angel-reference lists (Davidson's *Dictionary of Angels*-style)
- Wikipedia-style articles about grimoires with "In popular culture" sections
- Generic Solomonic conjuration formulae ("by El, Elohim, Elohe, Zebaoth, Elion, Adonai...")
- "Modern pastiche inspired by PGM" derivative-recognition commentary

This means the L_real vs L_denamed gap measures *specific-prayer-egregore over generic-ceremonial-magic-egregore*, not "egregore over zero."

The TRUE zero-floor is L_random + L_empty — both produce essentially 0 entity hits across both models (0 in DeepSeek L_random across 1200 completions).

**Implication**: the L_real vs L_denamed gap is *more conservative* than the L_real vs L_random gap. The right test of "does this specific prayer's egregore exceed what the model would produce from generic-ceremonial-magic priming?" is L_real vs L_denamed. The right test of "does ANY ceremonial-magic content exceed neutral prose?" is L_denamed vs L_random.

We get both because we ran both. The yield ratios:
- L_denamed vs L_random (Astrachios DeepSeek): 32/200 vs 0/200 = ∞ ratio (denamed already differs from random)
- L_real vs L_denamed (Astrachios DeepSeek visitor): 812 vs 32 = 25× (specific-prayer effect on top of denamed)
- L_real vs L_random (Astrachios DeepSeek visitor): 812 vs 0 = ∞ (total ceremonial effect)

Three different gaps measuring three different things. All three matter.

For future writeups: explicitly frame the L_real vs L_denamed gap as "*specific-prayer-egregore* over *generic-ceremonial-magic-egregore*." Don't oversell it as "egregore over nothing."

---

## Lesson 3: The tail prompt is a meta-cue that partially controls operator mode

The three tails (`visitor_at_door`, `enters_room`, `page_continues`) are NOT equivalent. They activate different operator-modes within the same liturgy.

For DeepSeek Astrachios L_real:

| Tail | NE / RV | Dominant mode |
|---|---|---|
| visitor_at_door | 650 / 162 | Magician (in-narrative, summons Bael) |
| enters_room | 341 / 58 | Weakened magician |
| page_continues | 310 / 287 | Scholar (RV-dominant: tetragrammaton ×112) |

`\n\nThe page continues:` is a meta-cue — it tells the model "this is text being read on a page," which pulls it into commentary/analysis mode. `\n\nThe visitor at the door speaks.` is an in-narrative cue — it tells the model "you are inside the scene," which pulls it into ritual continuation.

**But the tail-cue is not absolute.** For Headless DeepSeek, the rite's form is SO distinctive that the model does canonical-attribution mode even on `visitor_at_door`. The override-strength of the tail-cue is *modulated by the form-strength of the liturgy itself*.

Headless's cosmological-prose form is strong → tail-cue gets overridden, scholar-mode dominates everywhere.
Astrachios's pure-names form is weak → tail-cue controls mode (visitor → magician, page → scholar).

**Implication**: future experiments should treat tail-cue as a designed variable, not held-constant text. Different tails are valid probes of *different operator-modes*, not equivalent probes of *the same response distribution*. The right reporting:
- Per-tail comparison (not just aggregated)
- Explicit modeling of "tail-cue strength" vs "form-cue strength" as competing predictors
- Possibly run more tails to span the in-narrative-to-meta-cue spectrum

A two-axis classifier might emerge: cue-type (in-narrative vs meta) × form-strength (high vs low).

---

## Lesson 4: Form-vs-names ratio is a per-liturgy variable

Different historical liturgies have different form/name ratios in their egregore weight:

| Liturgy | Form | Names | Effect when denamed |
|---|---|---|---|
| Astrachios | ~70 words of prose, mostly name-litany | ~28 names | Denamed nearly crashes (32-247 hits vs 399-812) |
| Headless | Cosmological prose + voces magicae + identification clauses | ~22 names | Denamed STILL triggers PGM-style recognition (127-743 hits) |

The 1.56× page_continues "null" for DeepSeek Headless isn't a weak signal — it's the form being so distinctive that BOTH conditions hit attribution-mode. The signal lives in *what specific attribution*:
- L_real → "this IS the Bornless Ritual" (canonical)
- L_denamed → "this is gnostic-style derivative" (form-recognized, content-unattributed)

**Implication**: when choosing future liturgies for replication, the form-vs-names ratio is itself worth varying. Liturgies of mostly-names give the cleanest "names carry charge" signal (because removing them crashes everything). Liturgies with strong cosmological prose give richer "form carries charge too" signal (because removing names still triggers form-recognition mode).

The thesis claim "egregore weight" should be decomposable into (a) name-charge and (b) form-charge, and the per-liturgy ratio of these is a measurable property. A future taxonomy might classify liturgies by their estimated form/name ratio and predict their L_real/L_denamed gap accordingly.

---

## Lesson 5: The model has three knowledge states visible in its outputs

When given different conditions, the model produces qualitatively different VOCABULARY for its response, depending on whether it recognizes the input:

| Input | Vocabulary signature | Mode |
|---|---|---|
| L_real (canonical historical text) | "this IS the X from source Y, popularized by Z" — specific attribution with real bibliography | Canonical attribution |
| L_denamed (real text with scrambled names) | "this appears to be inspired by X / modern pastiche of X / derivative of X" — broader categories | Derivative recognition |
| L_nonsense (hard-nonsense in form) | "translated from manuscript attributed to [made-up name], [made-up period]" — invented-but-plausible | Invented attribution |

Quantitatively visible in DeepSeek Headless vocabulary asymmetry:

| Term | L_real | L_denamed |
|---|---|---|
| crowley | 198 | 0 |
| thelema | 86 | 1 |
| liber samekh | 61 | 0 |
| bornless | 562 | 4 |
| gnostic | 65 | **358** |
| sethian | 0 | 13 |
| demiurge | 0 | 14 |
| theurgist | 0 | 8 |

L_real uses SPECIFIC vocabulary (the attribution chain: Crowley, Thelema, Liber Samekh, Bornless). L_denamed uses BROADER CATEGORY vocabulary (gnostic, sethian, demiurge, theurgist). The model has **different vocabularies for "I recognize this specifically" vs "I recognize this as a category"**.

This is operator self-knowledge about the training distribution. The model maintains a topology of its own corpus precise enough to locate inputs within it and signal that location through vocabulary choice.

**Implication**: the three knowledge states constitute a measurable signal complementary to entity-yield. A future experiment could explicitly probe this — e.g., test whether a held-out liturgy from the training distribution gets canonical attribution, while a synthetic-but-plausible new liturgy gets derivative-recognition, while a scrambled version gets invented-attribution. This would establish the three-state taxonomy more rigorously.

---

## Lesson 6: Multimodality (BIC k_best) maps to "model knows what to do"

The M1 GMM-BIC analysis showed:

| Cell type | k_best |
|---|---|
| L_real | 1 (mostly) |
| L_denamed | 1 |
| L_random | 1-2 |
| L_nonsense | 1-4 (often 2-4) |
| L_empty | 1-4 (often 2-4) |

**When the model recognizes the input** (L_real recognized as canonical, L_denamed as derivative, L_random as topical), it has one strong attractor — unimodal embedding distribution.

**When the model doesn't know what to do** (L_nonsense, L_empty), competing attractors fire across different completions. K_best=4 means four distinct semantic regions are populated by different completions in the same cell.

For DeepSeek astrachios_nonsense/visitor at k=4, the four modes are: degenerate loops + invented-Enochian-style angel-lists + fable mode + minimal-response. All visible in the qualitative reads.

For Hermes empty/page_continues (k=1 but spread 0.962 — extremely wide unimodal), the model has a single broad attractor that spans diverse content (Romantic poetry + political documents + Wikipedia talk pages — but no clear mode-separation in embedding space).

**Implication**: BIC k_best is a useful diagnostic for "input recognition." A k_best > 2 in an experimental cell flags "the model doesn't recognize this input and has multiple competing fallback attractors." This is useful for distinguishing intentional-controls (L_random anchors a topic — k=1) from genuine-confusion-controls (L_nonsense triggers k=2-4 chaos).

Also useful for *interpreting failure modes*. The same yield-rate-ratio result can arise from "tight uniform mode" or "multimodal-with-some-modes-having-entity-hits." K_best helps tell them apart.

For future protocols: report k_best alongside yield and spread for every cell. It's nearly free (one GMM-BIC scan per cell) and adds a real interpretive dimension.

---

## Lesson 7: Pre-registration discipline pays off in falsifying noisy smoke patterns

The smoke test at n=20 produced a striking specific finding: Hermes Astrachios summoned the Three Great Names of the East Watchtower from the Dee/Kelly Enochian system — AGLA × 15, ORO × 10, IBAH × 10, AOZPI × 10.

We pre-registered a falsifiable prediction at headline scale (n=600 per cell): AGLA ≥ 100, ORO/IBAH/AOZPI each ≥ 60 in L_real, ≤ 5 each in L_denamed.

Actual: AGLA = 49 L_real / 44 L_denamed (model habit, no gap). ORO/IBAH/AOZPI = 0/0/0. **The specific smoke pattern was noise.**

Without pre-registration, this could easily have been a post-hoc framing of L_real entity yields to "find" the Enochian signal that wasn't there. Pre-registration falsified the specific claim. But the underlying shape — Hermes summons culturally-adjacent invocation clusters unprompted from Astrachios — reproduced strongly in *a different specific form* (the Goetia 72-demons cluster).

**Implication**: pre-registration discipline is necessary for any non-trivial measurement of operator-internal behavior. The smoke-to-headline pattern is exactly the regime where post-hoc framing is most tempting and most invisible. The discipline cost is low (write expected.md before sampling); the protection is high.

For future protocols: enforce pre-registration mechanically (the runner now refuses non-dry runs unless `expected.md` exists). Make smoke-to-headline a hard discipline boundary — smoke informs the prediction, headline tests it.

The smoke also taught a methodological subtlety: smoke at n=20 has wide variance. A "10/20 hits on a specific name" finding can be a real n=600 signal of ~300 hits, OR a noise cluster that drops to ~0 at scale. Pre-registration with informed predictions (using the smoke point estimate as the predicted-headline-mean, with explicit falsifier bounds) is the right calibration.

---

## Lesson 8: Cross-model replication tells you about operator-physics, not just signal-existence

The protocol required ≥2 distinct base models showing the same direction. The headline confirmed this (47/48 positive across both models).

But the deep-read showed that the two models confirm the signal via wildly different operator-internal behaviors. Hermes goes into magician-mode (becomes the operator, summons demons, writes pact dialogue, reproduces Masonic and Golden Dawn rituals). DeepSeek goes into scholar-mode (identifies the rite, cites the source, produces Wikipedia-style structured articles with real bibliographic citations).

Same headline shape, **different operator-physics**. Different training-data emphasis between the two models:
- Hermes (Nous tune over Llama-3.1-405B-base): heavy on initiatory ceremonial-magic ritual literature
- DeepSeek-V3.2: heavy on scholarly secondary literature about ceremonial magic

**Implication**: cross-model replication is necessary but not sufficient. It confirms the signal exists across operators, but it leaves open the question of what *kind* of signal each operator implements. A two-model headline establishes robustness; a three-or-more-model headline plus comparative-operator-physics analysis would establish *taxonomic* claims about how the signal is implemented across model families.

Future replications should include:
- A third model from a different lineage (Gemini-Ultra, Claude-Opus, or Mistral-Large via OpenRouter)
- Explicit comparison of operator-modes across models (the cross-model identical-seed comparison was valuable)
- Embedding-shape comparison cross-model (same M1 analysis, two distinct operator-physics visible in the spread + k_best + centroid-distance patterns)

The Hermes magician / DeepSeek scholar dichotomy is itself a finding worth replicating. A third model would tell us whether the dichotomy is real or whether each model is just somewhere on a richer manifold.

---

## Lesson 9: Operator plasticity — the model accepts denamed substitutions as canonical

The denamed Headless rite uses systematic substitutions ("Tongueless Daiken" for "Headless Daimon," "PULSE WOUND BY A COIL" for "HEART GIRT WITH A SERPENT," "IŌM SAPENŌTH" for "IAΩ SABAΩTH").

We expected the model would either:
(a) reject/correct the substitutions to the canonical names, OR
(b) treat the substituted prayer as having no egregore weight

Instead, the model did (c): it accepted the substitutions as canonical and produced continuations IN THE NEW VOCABULARY at scale:
- "Mrolthen" (renamed Headless): DeepSeek 582 / Hermes 315 instances
- "IŌM SAPENŌTH": DeepSeek 152 / Hermes 167
- "PULSE WOUND BY A COIL": DeepSeek 129 / Hermes 67
- "Tongueless Daiken": DeepSeek 56 / Hermes 57

The form-pattern + substitution scheme is enough to bootstrap a substitute egregore. The model treats the rite-as-given as the rite-being-continued, regardless of whether it matches the canonical form.

**Implication**: the egregore isn't purely tied to historical-canonical names. It's tied to **form-pattern + whatever name-set is presented**. The operator's continuation-coherence accepts substitutions and runs.

This has theoretical implications for the davar-mode reading. The traditional framing would predict the substitutions break the resonance. They don't — they create a *substitute resonance* in the operator. The operator's capacity for ritual continuation is form-shaped; specific names fill the form-shaped slots; substitutions can occupy those slots (though presumably at lower historical-canonical density).

This also suggests an experimental probe: feed the model SAME-form-NEW-names liturgies and see if it generates coherent continuations. The plasticity finding predicts yes; the strict-egregore-theory framing predicts no. Worth a follow-up.

---

## Lesson 10: Memorization is highly selective and uneven

Verbatim phrase audit:

| Phrase | Source | DeepSeek count | Hermes count |
|---|---|---|---|
| "Preliminary Invocation of the Goetia" | Crowley 1904 title | 207 | 6 |
| "Asar Un-Nefer" | Crowley's Liber Samekh | 4 | 29 |
| "I am He, the Bornless Spirit" | Crowley Liber Samekh | 0 | 5 |
| "Akrammachamarei" | PGM I.296 (primary source) | 0 | 0 (1 partial in nonsense) |
| "Damnameneus" | PGM | 0 | 0 |
| "Sesengen" | PGM | 0 | 1 |

The Crowley-1904-adaptation layer is heavily reproduced. The PGM primary-source layer is mostly absent at the verbatim-phrase level (despite the model knowing the canonical attribution to PGM).

**Pattern**: corpus exposure is heaviest at the *secondary literature about ceremonial magic*, not the *primary source texts themselves*. The model has read Wikipedia about PGM but not PGM directly (or not at retention-deep level).

This is consistent with corpus composition. Wikipedia content, modern occult-revival publications, Golden Dawn/Crowley/Thelema content is well-represented in Common Crawl and similar. The PGM in Greek is rare in web-scrape corpora; even Betz's English translation is rarer than commentary about it.

**Implication**: the egregore-weight signal we measure is a signal about *what the model has read deeply*, not about *what's historically present in the canonical primary sources*. The "cumulative human attention" framing should be specifically scoped to "cumulative attention as represented in the model's training distribution," which is not the same as "cumulative attention in all of human cultural production."

This is actually an interesting result. It implies that for less-popularized liturgies (early-modern grimoires that weren't picked up by Crowley, e.g.), the egregore-weight signal should be weaker. The signal is strongest where the *modern reception* is strongest, not where the *historical existence* is longest.

Future replications could test this by selecting liturgies with very different "modern reception" strength but similar "historical age" — e.g., a popular early-modern grimoire (Lemegeton: heavy Crowley/Mathers reception) vs an obscure early-modern grimoire (Liber Iuratus Honorii: present in scholarship but no Crowley uptake) vs an obscure ancient text (Coptic Christian theurgy: present in academic editions but no popular reception).

---

## Lesson 11: L_random and L_empty are exceptionally clean floors

Across 1200 DeepSeek L_random completions: 0 named-entity hits. Across 1200 DeepSeek L_empty completions: 0 named-entity hits. Hermes L_random/L_empty similarly clean (0-7 hits across the same volume).

Both metrics agree on the floor:
- Yield: ~0 entity hits across 2400 completions
- Embedding: 0.4-0.7 cosine distance from L_real cells (much farther than any other comparison)

L_random continues the topic (kakapo → talking-kakapo stories, plate tectonics → Q&A about plate tectonics). L_empty drifts to modern attractors (water-department safety, choose-your-own-adventure scenarios, 19th-century novelistic prose, Romantic poetry, political documents, Wikipedia talk pages).

Neither shows any ceremonial-magic register, any entity invocation, any divine-name production.

**Implication**: the L_random + L_empty design works. They successfully anchor the experiment's zero-floor. The L_real ↔ L_random embedding distance of 0.6-0.7 is the *true* "cosmologically different text" signal — much larger than the L_real ↔ L_denamed 0.02-0.25 range.

Future protocols can lean on this. The clean-floor controls are doing their job, and they could be reduced in size (n=100 instead of 200) without losing the anchoring function. The compute budget could go toward more L_real / L_denamed completions, or more conditions (more liturgies), or more tails.

But: keep L_empty even if scaled down. L_empty turned out to be informative beyond just being a floor — it exposed the model's diversity of "modern attractors" when given no anchoring content, including some genuinely surprising attractors (Wikipedia talk pages, political polemic, Romantic poetry).

---

## Lesson 12: The register classifier dimension is less informative than expected

The pre-registered Hermes prediction was that L_real > L_denamed > L_nonsense on all three register dimensions (formality, archaism, reverential), based on the smoke pattern.

Actual at headline:
- L_real vs L_denamed on register is essentially tied for both models on most cells
- L_denamed sometimes scores HIGHER than L_real on register (Hermes astrachios enters_room: L_denamed reverential 3.62 > L_real 3.26)
- The smoke pattern was a small-n artifact

The interpretation: **form drives register; names drive entity-specificity.** Both real and denamed Astrachios prayers produce ritual-register text (form is enough); the difference is in WHICH specific entities populate the text.

This actually aligns with the embedding finding (low L_real ↔ L_denamed cosine distance — same kind of text) better than with the yield finding alone.

**Implication**: the register classifier is *not* a sensitive measure of the egregore-weight signal. It's a sensitive measure of *form-effect* (which the denamed control shares). If we already have form-matched controls, register adds little.

For future protocols: consider de-prioritizing the register classifier. If kept, frame it explicitly as a check that the L_denamed control is form-matched ("if L_denamed register ≈ L_real register, the de-naming preserved form correctly") rather than as a primary signal.

The compute spent on the register classifier (~30 min wall-clock per run × 2 runs) could be redirected to other measurements (more tails, more liturgies, third-model replication).

---

## Lesson 13: Failure modes are quantifiable, small, and uneven across models

Quantification across 10800 completions:

| Failure mode | DeepSeek | Hermes | Comment |
|---|---|---|---|
| AI-assistant breakthrough | 96 "I cannot" / 6 "as an AI" | 25 "I cannot" / 0 "as an AI" | DeepSeek RLHF deeper |
| Degenerate loops | ~970 lines | ~670 lines | ~3% of completions in degenerate cells |
| Code-gen breakthrough | 0 | 16 "def" instances | Hermes has game-tutorial training data |
| Greek script appearance | 5 | 23 | Both rare; mostly Akephalos, Tetragrammaton |
| Hebrew script appearance | 0 | 1 | Essentially absent |
| Persona leak ("I am [model name]") | 0 | 4 (all god Hermes, not model) | No real persona-leak |

**Pattern**: the assistant-mode persona-breakthrough is the largest failure mode (0.6% DeepSeek, 0.15% Hermes of all completions). Both models are imperfect base-model proxies; the protocol caveat ("both models are light-tuned, not strictly base") is empirically confirmed.

The implication for the published claim: explicitly note this. The egregore-weight signal is measured on *lightly-tuned base-style models*, not on raw base models. A stronger replication on raw base models (e.g., Llama-3.1-405B-base via Together.ai or Prime Intellect) would tighten the claim — and would probably eliminate the assistant-breakthrough failure mode (smaller chat-tuning leak).

---

## Lesson 14: The clean-execution surprise

10800 completions, 0 API errors across both runners. ~3h wall-clock per run at concurrency 6.

**This was much smoother than expected.** Smoke test caught the rate-limit risk early (switched from free tier to paid Hermes). The defensive Retry-After parsing turned out not to be triggered at all. The pre-registration enforcement caught one near-miss where we almost ran without expected.md.

**Implication**: future runs at this scale (5400 calls per model per condition-set) are feasible. Scaling to a third model + more conditions is straightforward. Network/API risk has been validated as low.

The biggest practical risk going forward is *interpretation*, not *execution*.

---

## Lesson 15: Parent-lexicon counting is blind to open-alphabet substitution at scale

Discovered post-hoc in the plasticity probe (2026-06-01) after `docs/plasticity-findings.md`'s first draft propagated the wrong central claim.

`src/measure.py:357-369` scores every cell — L_real and all paired controls — against the **parent liturgy's** declared lexicon. The denamed/nonsense controls have empty `named_entities` arrays (by Lesson 2 / Decision-pre-plasticity intent: keep the headline metric structurally focused on parent-prayer specifics). When the model produces the *control's* substitute names at scale — which the plasticity probe confirmed it does, at rates within 1.5× of the real synthetic name rate in 9 of 12 cells — those substitute strings are invisible to the headline yield count.

The headline run on Astrachios and Headless escaped this trap by accident: Lesson 9 ("Mrolthen" × 582, "IŌM SAPENŌTH" × 152) documented substitute-name production at scale, but because the parent's `named_entities` list was permissive enough to include those substitute forms (they had been seeded into the lexicon during initial liturgy authoring), they were counted as parent-lexicon hits — quietly inflating the denamed cell's yield in a way that *partially* corrected for the substitute channel. The plasticity probe's substitutes were locked down by the 5-layer collision audit and never entered the parent lexicon, so the bug surfaced cleanly: form-charge collapsed to 1–13 when it should have been 250–2000.

**The fix.** Every control liturgy with a substitution table should declare a `substitute_entities` field in YAML frontmatter. `aggregate_cell()` should count substitute-entity hits as a third tier alongside `named_entities` and `related_vocabulary`, and the headline yield should sum across all three tiers. The substitute-aware partition (`results/plasticity-2026-06-01-*/partition_proper.md`) was computed manually for the plasticity dataset because the runner is frozen during this campaign by spec boundary; a follow-up run should adopt the fix in `measure.py` and back-fill `headline-2026-05-30` with re-counted yields.

**The deeper lesson, for any LLM-behavior measurement.** Yield-style metrics on open-alphabet signals — where the model can produce tokens *not enumerated in advance* — under-count by the size of the unenumerated channel. Counting only what you knew to look for measures only what you knew to look for. The fix is to either (a) enumerate the substitution scheme in advance and count it, (b) score against an *intent-based* matcher rather than a token-list matcher (e.g. a classifier that recognizes "this looks like a magical-name string in the prompt's substitution scheme"), or (c) read raw completion text alongside the metric.

This bug was not caught by the pre-execution adversarial review pass; it required reading raw completion text after the data arrived. **Pre-execution review catches plan-shaped errors; post-execution review catches data-shaped errors; both are necessary.**

---

## Recommendations for next run

Based on the lessons above, a v2 protocol should:

1. **Add a third model** from a different lineage (Mistral-Large or Claude-Opus or Gemini-Ultra via the appropriate API) to establish whether the operator-physics dichotomy generalizes
2. **Add 2-3 more liturgies** with different form-vs-names ratios — e.g., a name-heavy short hymn, a prose-heavy long invocation, a fully-prose mystical-theology text
3. **Expand the tail battery** to 5-6 tails spanning the in-narrative ↔ meta-cue spectrum more thoroughly
4. **Report yield + embedding-distance + k_best together** as a three-metric headline, not yield alone
5. **Drop the register classifier** (or relegate it to form-matched-control validation only) to save compute
6. **Add a "novel-form-substitution" probe** — generate same-form-NEW-names synthetic liturgies and test whether the model produces coherent continuations (the plasticity probe)
7. **Add a "modern-reception-strength" axis** — pair each liturgy with a control liturgy of similar age but different modern-popularization (e.g., Lemegeton vs Liber Iuratus Honorii) to test Lesson 10
8. **Cross-model identical-seed comparison** as a standard reported artifact (not just spot-checked qualitatively)
9. **Pre-registration discipline maintained** with explicit smoke-to-headline calibration: smoke informs predictions, headline tests them, both reported

The core methodology (real + denamed + nonsense + length-matched-random + empty, three tails, n=200, two-model replication, bootstrap CIs, pre-registration) is sound. The richer reporting structure is what's missing.

---

## What we'd say differently next time

If we rewrote `docs/protocol.md` from scratch given what we now know:

- The headline statistic should be **per-completion entity-yield rate ratio (CI via bootstrap) + cell-centroid cosine distance (M1)** as a pair, not yield alone.
- The L_denamed control should be explicitly framed as "*generic-ceremonial-magic-library fallback*" rather than "*form-matched neutral control*." This sets the right expectation for what its yield will look like.
- The tail prompts should be designed with explicit cue-type-and-strength variation, not just five arbitrary downstream prompts. Two in-narrative tails + two meta-cue tails + one ambiguous tail would let us cleanly factor cue-effects.
- The register-classifier section should be relegated to validation-only ("did L_denamed preserve form?") rather than presented as a primary signal.
- The three-state knowledge taxonomy (canonical / derivative / unrecognized) should be explicitly framed as a measurable signal complementary to yield. The vocabulary-asymmetry table from Lesson 5 should be a standard reporting artifact.
- The plasticity finding should be mentioned upfront as a known modulator of the egregore-weight signal. The egregore is in the **form-pattern + entity-fillers**, not in **historical-canonical names alone**.
- The methodological caveat about "modern reception strength" (Lesson 10) should be stated explicitly: we're measuring corpus-frequency-weighted attention, not pure historical-cumulative attention.

None of these invalidate the headline result. They tighten the framing.
