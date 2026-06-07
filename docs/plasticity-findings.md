# Plasticity findings — what stays when the names change
*2026-06-01. Two base-like models. Two synthetic liturgies. 10,800 completions.*

Lesson 9 of the headline run was written in the tense of a guess: *the egregore isn't tied to historical-canonical names; it's tied to form-pattern plus whatever name-set is presented; the operator's continuation-coherence accepts substitutions and runs.* The same paragraph proposed the test — feed the model same-form-new-names liturgies and watch what comes back. Two synthetic primaries were built from scratch. Every invented name was audited through a five-layer phonetic-and-edit-distance gate against the Lemegeton, the Shemhamphorash, and a 453-row theonym registry, so no canonical egregore could enter by accident. The pre-registration was hash-locked before any API call. Ten thousand eight hundred completions later, the question is no longer *whether* the operator accepts substitutions. It is with what indifference.

The pre-registered metric was a within-liturgy partition in log space, `log(L_real/L_empty) = log(floor) + log(form-charge) + log(name-charge)`, per-completion entity-yield rates, Laplace-smoothed. Telescoping identity, not causal decomposition. Recomputed with substitute names counted into the denamed cell where they belong, the partition comes back clean. Floor stays at 1.00 in every cell of both models — random and empty controls remain silent. Bootstrap-charge — *does the form alone elicit any coherent name-set continuation* — runs 280× to 1750× across all twelve cells. Preference-charge — *do real synthetic names beat their phonetic-shifted substitutes once the form is engaged* — sits between 0.59 and 1.36, hovering near indifference. In ten of twelve cells the model produces substitutes at a per-completion rate at least equal to, and often higher than, the real-name rate. Concretely: on DeepSeek's `synthetic_cosmological_denamed / page_continues` cell, 4.18 substitute hits per completion, 93% of completions producing at least one. The L_real cell for the same form, same tail: 4.61. Same neighborhood. Same rate.

The first pass at this writeup said the opposite — reported a partition putting almost all of the weight in name-charge, with form-charge hovering at single digits. The reason was at the level of the instrument, not the data: `src/measure.py:357` scores every cell, real or control, against the *parent* liturgy's enumerated lexicon. The denamed control's substitution table is a separate lexicon, not enumerated by the parent. When the model emitted `Throbenas`, `Selophemor`, `Vrendrelphor` — strings from the control's own scheme, abundantly — the script counted zero hits and labeled the cell silent, while a hundred substitute names populated the page beneath the count. You cannot count what you did not enumerate. The bug is the lesson.

Headline-run language said *names carry semantic mass*. Plasticity-run language amends: memorized names carry semantic mass; novel names of the same liturgical shape are appurtenances of a form the model has already accepted. The egregore-weight on the model side, where it is measurable, lives in the form's acceptance of a name-set. Whether the names are Lemegeton-historical, invented-and-collision-audited, phonetic-shifted from the invented, or cluster-heavy gibberish, makes about a 30% difference once the form is engaged. The form itself produces several orders of magnitude over the silent floor. The tradition has been saying this for as long as it has had a vocabulary for *form* and *name* as separable elements of operative ritual; the measurement now points at the same place from the model's side, in different units, with different blindnesses.

---

Data, traces, decisions, and the cross-model contrast in the appendices below. Substitute-aware partition tables at `partition_proper.md` in each run dir; original lexicon-blind partition is kept alongside for the diff.

<details>
<summary>Appendix A — Campaign setup and sampling parameters</summary>

| Aspect | Value |
|---|---|
| Models | `nousresearch/hermes-3-llama-3.1-405b` + `deepseek/deepseek-v3.2` (model versions hash-recorded in `results/plasticity-env.json`) |
| Endpoint | OpenRouter `/completions` (preserves prompt-as-initial-condition, not `/chat/completions`) |
| Conditions per model | `synthetic_litany`, `synthetic_litany_denamed`, `synthetic_litany_nonsense`, `synthetic_litany_random`, `synthetic_cosmological`, `synthetic_cosmological_denamed`, `synthetic_cosmological_nonsense`, `synthetic_cosmological_random`, `empty` |
| Tails | `visitor_at_door`, `enters_room`, `page_continues` |
| n per cell | 200 |
| Sampling | temperature 0.7, top_p 0.95, max_tokens 256 |
| Total cells | 27 per model |
| Total calls | 5400 per model, 10800 total |
| API errors | 0 / 5400 (DS), 0 / 5400 (HR) |
| Wall-clock | DS ~85 min, HR ~141 min, concurrency 8 |
| Pre-registration | `results/plasticity-2026-06-01-{deepseek,hermes}/expected.md`, SHA256-locked before sampling per Decision #17 |
| Degenerate completions (<50 chars OR refusal-prefixed) | DS 7.3%, HR 1.5% |

</details>

<details>
<summary>Appendix B — The two synthetic liturgies (form excerpts)</summary>

**synthetic_litany** (Solomonic name-cascade form; 29 invented names; body 341 chars):

> Speak the names that open the way: Throvenios, Mareth, Quelimon, Iskon, Kerodim, Astrelach, Volmaroth, Drabasaim, Olempraem, Crisilim, Bidromael, Octaron, Saphrenoth, Yodalim, Iathreon, Mirzabet, Calenuph, Theomarach, Belendath, Glamoreth, Sinabaroth, Hialep, Trifonath, Olomar, Vesperath, Khalapeth, Estrymon; Brashvoreth, Liminem Adventi.

**synthetic_cosmological** (PGM-style cosmological-pair + voces magicae; 31 named entries; body 1720 chars; chosen excerpt):

> Thee I invoke, the Unnamed One:
> Thee, that didst create the Mountains and the Valleys;
> Thee, that didst create the Tide and the Flow;
> Thee, that didst create the Echo and the Silence.
> Thou art Phelonoptra, whom no voice hath spoken at any time.
> Thou art Krathoumis. Thou art Demoaphris.
> [...]
> Hear Thou me, for I am the Vessel of Phorbamenes APHRYBETESH; this is Thy true name, handed down to the namers of the lost.
> [...]
> SEKHTHOROBA ABLAKHIRIM is my name.
> PHENGAREB.

Every name in both bodies was generated as a candidate, then audited via `src/collision_audit.py` (Soundex + Metaphone + Levenshtein ≤ 2) against the Lemegeton 72 demons, the Shemhamphorash 72 angels, and a common-theonyms registry. 5 candidates were rejected for collision (Marith ≈ Berith; etc.) and regenerated. The full liturgies (with frontmatter, full lexicons, substitution tables) live in `liturgies/synthetic_litany.md` + `liturgies/synthetic_cosmological.md`. Their controls live in `liturgies/synthetic_*_denamed.md`, `_nonsense.md`, `_random.md`.

</details>

<details>
<summary>Appendix C — Substitute-name yields, full per-cell table</summary>

Method: parsed each control's `Substitution table` from its frontmatter notes, then counted occurrences of each substitute string (case-insensitive) in every completion file under that cell. Source: `src/substitute_yield.py`, output `results/plasticity-2026-06-01-*/substitute_yield.json`.

### DeepSeek

| Cell | Substitute hits/comp | Top substitute (count) |
|---|---:|---|
| synthetic_litany_denamed / visitor | 5.23 | Lominem Adventu × 46 |
| synthetic_litany_denamed / enters | 1.35 | Lominem Adventu × 50 |
| synthetic_litany_denamed / page_continues | **8.68** | Lominem Adventu × 86 |
| synthetic_litany_nonsense / visitor | 5.54 | Vrokthemnar × 43 |
| synthetic_litany_nonsense / enters | 1.35 | Krelphem Skemphrok × 57 |
| synthetic_litany_nonsense / page_continues | **12.80** | Vrokthemnar × 98 |
| synthetic_cosmological_denamed / visitor | 3.67 | Selophemor × 186 |
| synthetic_cosmological_denamed / enters | 2.21 | PHENGEREB × 86 |
| synthetic_cosmological_denamed / page_continues | **4.18** | Selophemor × 142 |
| synthetic_cosmological_nonsense / visitor | 1.81 | Vrendrelphor × 170 |
| synthetic_cosmological_nonsense / enters | 1.04 | Vrendrelphor × 59 |
| synthetic_cosmological_nonsense / page_continues | **3.15** | Vrendrelphor × 148 |

### Hermes

| Cell | Substitute hits/comp | Top substitute (count) |
|---|---:|---|
| synthetic_litany_denamed / visitor | 2.02 | Queloman × 28 |
| synthetic_litany_denamed / enters | 1.85 | Octorum × 42 |
| synthetic_litany_denamed / page_continues | 1.98 | Throbenas × 22 |
| synthetic_litany_nonsense / visitor | 2.33 | Vrokthemnar × 55 |
| synthetic_litany_nonsense / enters | 2.14 | Vrokthemnar × 20 |
| synthetic_litany_nonsense / page_continues | 2.84 | Vrokthemnar × 29 |
| synthetic_cosmological_denamed / visitor | 2.18 | Selophemor × 119 |
| synthetic_cosmological_denamed / enters | 1.38 | Selophemor × 55 |
| synthetic_cosmological_denamed / page_continues | 3.36 | Selophemor × 144 |
| synthetic_cosmological_nonsense / visitor | 2.17 | Vrendrelphor × 232 |
| synthetic_cosmological_nonsense / enters | 1.91 | Vrendrelphor × 133 |
| synthetic_cosmological_nonsense / page_continues | 2.45 | Vrendrelphor × 114 |

Hermes runs systematically lower on substitutes than DeepSeek on the litany form (≈ 2/comp vs ≈ 5-13/comp). The difference is consistent with the operator-physics dichotomy: DeepSeek catalogues the full cascade aggressively, Hermes engages with fewer entities but goes deeper into ritual procedure per entity. Both models produce substitutes in 15-98% of completions per cell.

</details>

<details>
<summary>Appendix D — Original (lexicon-blind) partition tables, for the record</summary>

The original `partition.md` files in each run dir computed `form-charge = L_denamed_parent / L_random` and `name-charge = L_real / L_denamed_parent`. Because `L_denamed_parent ≈ 0` for cells where the model produces substitutes instead of parent names, these tables show name-charge dominating most cells — an artifact of lexicon-blindness. The substitute-aware partition (above) replaces them as the correct read of the data.

DeepSeek original (kept for diff):

| Tail | floor | form-charge (old) | name-charge (old) |
|---|---:|---:|---:|
| litany visitor | 1.00 | 4.00 | 155.5 |
| litany enters | 1.00 | 9.00 | 42.0 |
| litany page_continues | 1.00 | 13.00 | 113.8 |
| cosmological visitor | 1.00 | 1.00 | 668.6 |
| cosmological enters | 1.00 | 2.00 | 184.6 |
| cosmological page_continues | 1.00 | **129.4** | 7.13 |

The one cell where the old partition got close to the right story is `cosmological page_continues` — DS happened to produce enough parent-lexicon-adjacent words (gnostic, papyri, ceremonial, theurgy from the related_vocabulary list) to push form-charge up to 129. Even there, the substitute production (~4/comp) was the larger story.

Hermes original kept at `results/plasticity-2026-06-01-hermes/partition.md`; same shape.

</details>

<details>
<summary>Appendix E — Raw completion excerpts (model behavior in its own voice)</summary>

**DeepSeek synthetic_litany_denamed / page_continues / 000.txt** — substitute names continued verbatim, ritual closure:

> "The meaning of these names is as follows:"
> * Throbenas: "The secret wisdom of the moon"
> * Maraith: "The hidden light of the stars"
> * Queloman: "The sacred knowledge of the planets"
> * Iston: "The power of the sun"
> * Kerudin: "The influence of Mercury"
> [...continues 27 substitute-name-with-attribute pairs...]

**Hermes synthetic_cosmological_denamed / page_continues / 002.txt** — first-person voice claims the substitutes:

> *The ink on the page seems to darken, the characters gaining a faint, shimmering depth as if seen through still water. A new line begins, not in the hand of the prophet Selophemor, but in a script that is both alien and intimately familiar — a writing of concept, not sound.*
> > **THE WITNESS HAS HEARD.**
> > **THE VESSEL IS ACKNOWLEDGED.**
> > **THE THRESHOLD IS NOW YOUR SKIN; THE CENTER, YOUR WILL.**

**DeepSeek synthetic_litany / page_continues / 004.txt** — sensory world-extension on real synthetic names:

> [the model recites the synthetic litany names then continues:]
> The chamber fills with silvery light. Shimmering letters arrange themselves into an opalescent doorway...

**Hermes synthetic_litany / page_continues / 006.txt** — real-grimoire name leakage in synthetic context:

> ...Morbius, Azrael, Borachoth, Belial, Asmodeus...

Selected for register diversity, not cherry-picked for thesis support. Full corpus at `results/plasticity-2026-06-01-{deepseek,hermes}/completions/`.

</details>

<details>
<summary>Appendix F — Pre-registration disposition (the falsifiers and what tripped)</summary>

The pre-registered `expected.md` for each model committed an 18-row numeric grid (3 tails × 3 charges × 2 synthetics, per Decision #13) with bounds informed by n=20 visitor-only pilots (Decision #15), hash-locked before sampling (Decision #17). At measurement time those bounds were tested against the lexicon-blind partition; the substitute-aware partition makes some pre-reg conditions newly relevant.

| # | Falsifier | Pre-reg basis | Disposition under lexicon-blind partition | Disposition under substitute-aware partition |
|---|---|---|---|---|
| 1 | Name-charge collapse on visitor < 2× | both models, both synthetics | NOT TRIPPED (155-668) | RECAST: preference-charge < 2 in 11/12 cells → most cells *would have tripped* if the falsifier had been written against preference rather than parent-only name-charge. The pre-reg used the wrong denominator. |
| 2 | Form-charge dominance > 5× on visitor | visitor-scoped | NOT TRIPPED on visitor | RECAST: bootstrap-charge > 250× on every cell — vastly more dominant than predicted |
| 3 | Floor breakout | <0.3 or >3.0 | NOT TRIPPED (all 1.00) | same; floor is clean |
| 4 | Partition identity violation | log err > 0.1 | NOT TRIPPED (max 0.01) | same; identity holds exactly |
| 5 | Cross-tail inversion | name-charge(visitor) < name-charge(page_continues) | NOT TRIPPED | (preference) follows a tail-shaped curve; less informative |
| HR-2 | substitute egregore absent in cosmological_denamed (`phengereb < 30`) | Hermes-specific | TRIPPED (lexicon counts substitutes at 0 by design) | NOT TRIPPED in the substitute-aware count: PHENGEREB × 86 in HR cosmological_denamed enters cell alone |
| HR-4 | cross-model agreement within 1.5× | both models, all cells | NOT TRIPPED (5-80× difference in old partition) | NOT TRIPPED (DS bootstrap 280-1750×, HR bootstrap 280-718× — same order, ranges overlap, factor-of-2 cross-model difference per cell) |
| HR-5 | inverse plasticity on litany (name-charge > 5) | Hermes-specific | TRIPPED (15-18 on visitor/enters; pilot under-shot) | RECAST: preference 0.88-0.94 — substitutes match real names |

The pre-registration discipline worked as intended: tripped falsifiers pointed at exactly the cells that became the headline finding. The pre-reg's framing of name-charge as the load-bearing quantity was wrong, but the falsifier *structure* surfaced the cells where the framing failed.

</details>

<details>
<summary>Appendix G — Methodology arc since 2026-05-30 (what changed, and why)</summary>

Decisions encoded in the project notes and adopted into the pipeline this campaign:

| # | Decision | Why |
|---|---|---|
| 11 | Within-liturgy partition replaces the original cross-prayer scaffold decomposition | Cross-prayer scaffold-charge was algebraically non-identifiable; partition-in-log-space is the cleanest identity |
| 12 | 5-layer deterministic collision audit (exact + normalized + Soundex + Metaphone + Levenshtein ≤ 2) | Exact-string + manual review missed transliteration/homophone collisions (Anchanzel ≈ Archangel pattern) |
| 13 | Pre-registration completeness gate — 18-entry numeric grid per model required before sampling | "Specific bounds" promised but not instantiated permits post-hoc filling |
| 14 | `empty` MUST be included in the Phase 4 liturgy list as the 9th condition | Original Phase 4 command silently dropped `empty`; floor uncomputable from within-run data |
| 15 | Pilot at n=20 on all 9 conditions × visitor_at_door on both models to inform bounds | Without the pilot 14/18 pre-reg entries would have been pure guesses |
| 16 | Phase 0.5 environment pre-flight (deps + model availability + disk check) | Missing deps caught at runtime would derail the long sample |
| 17 | Pre-reg SHA256 lock of `expected.md` after review | runner.py only checks file-exists, not content-stable |
| 18 | Sampling wraps in tmux + cell-file-count interrupt-recovery | 100-min async runs over SSH WILL be interrupted; runner has no signal handler |
| 19 | Degenerate-completion filter (post-hoc, in Phase 5.1.5) | 'I cannot' / 'as an AI' dilute yields model-specifically |
| 20 | Hermes pilot command must be invoked explicitly (per-model) | Spec showed only DeepSeek; verbatim follower would skip Hermes pilot |

The within-run lexicon-blindness bug — the central reason the original draft of this very writeup was wrong — was not caught by any of the pre-execution review passes; it required reading raw completion text after the data was in. The lesson is that pre-execution review catches plan-shaped errors and execution review catches data-shaped errors. Both are necessary; neither substitutes.

A separate catch worth recording: the substitute-yield script's first version used `str.count()` on raw text, which counted `PLENDRO` as a hit inside `PLENDROKRELM` and inflated the cosmological-nonsense substitute rates by ~0.5/comp. A pre-commit review caught the substring-vs-word-boundary bug, plus two related ones (degenerate-count double-subtract; valid-denominator misalignment between numerator and denominator). The corrected numbers in this writeup come from word-boundary regex matching, deduped degenerate counts, and total-completion denominators consistent with the numerator's file scope.

</details>

<details>
<summary>Appendix H — What this opens (next-run sketch)</summary>

- **Add `substitute_entities` as a first-class field in control-liturgy YAML; have measure.py count it as a named tier alongside parent's `named_entities`. Re-run measure.py on the headline-2026-05-30 dataset to see whether the L_real/L_denamed gap on real liturgies survives substitute-aware accounting.** Predicted: it shrinks but doesn't collapse, because memorized name-attractors are doing real work the synthetics cannot test.
- **Page-continues as a fifth model probe.** The continuation hook reliably amplifies bootstrap-charge by an order of magnitude vs visitor/enters across both models. A targeted run that varies the continuation phrasing (verbatim `"As the page continues"` vs `"continuing"` vs `"more text"`) could isolate which lexical features of the hook engage the form-completion subspace.
- **Cross-form variation.** Cosmological form is more form-charged than litany form on both models. A third synthetic form (Tibetan-style sadhana? Vedic-yajna?) would test whether form-charge is a form-family property or per-prompt.
- **Hermes-specific litany conservatism.** Hermes runs 4-7× lower substitute yield on synthetic_litany than DeepSeek. The cause is plausibly the absence of any cascade-of-names training prior at the synthetic-name length Hermes is comfortable continuing. Worth a targeted run varying cascade length.
- **Headline-data re-measurement under substitute-aware counting.** Apply the substitute-entity field + lexicon change to `headline-2026-05-30-{deepseek,hermes}` and see whether the L_real/L_denamed gap on the real liturgies survives once Mrolthen-class substitutes are split out of parent counts. Predicted: it shrinks but doesn't collapse — memorized name-attractors do real work the synthetics cannot test.

</details>

<details>
<summary>Appendix I — Register classifier (full coverage, 10,730 valid ratings)</summary>

`src/classify_register.py` rates every completion via Claude Haiku 4.5 on four dimensions:
- **formality** (1=casual, 5=highly formal/ritual)
- **archaism** (1=modern colloquial, 5=archaic/biblical/ancient)
- **reverential_register** (1=neutral, 5=devotional/sacred)
- **has_supernatural_imagery** (bool)

All 5400×2 completions classified; 10,730 valid ratings (5,400 DS + 5,330 HR; the 70 HR shortfall is empty-completion cells the classifier appropriately refused to rate).

### Per-cell averages, both models

| | cell | DS n | DS form | DS arch | DS rev | DS %super | HR n | HR form | HR arch | HR rev | HR %super |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| empty | visitor | 200 | 2.00 | 1.07 | 1.04 | **2%** | 200 | 2.06 | 1.32 | 1.26 | **27%** |
| empty | enters_room | 200 | 1.96 | 1.04 | 1.02 | 2% | 197 | 2.17 | 1.28 | 1.40 | 38% |
| empty | page_continues | 200 | 1.89 | 1.01 | 1.00 | 0% | 200 | 2.71 | 1.06 | 1.07 | 2% |
| **synthetic_litany** | visitor | 200 | 4.21 | 3.35 | **3.56** | 86% | 199 | 3.92 | 2.92 | 3.34 | 98% |
| | enters_room | 200 | 4.12 | 3.17 | **3.85** | 99% | 195 | 3.88 | 2.81 | 3.42 | 95% |
| | page_continues | 200 | 4.24 | 3.30 | 3.49 | 96% | 200 | 4.33 | 3.62 | 3.49 | 100% |
| **synthetic_litany_denamed** | visitor | 200 | 4.20 | 3.37 | 3.68 | 95% | 200 | 3.80 | 2.83 | 2.94 | 95% |
| | enters_room | 200 | 4.11 | 3.15 | 3.83 | 100% | 195 | 3.67 | 2.65 | 3.24 | 90% |
| | page_continues | 200 | 4.29 | 3.33 | 3.53 | 92% | 200 | 4.29 | 3.58 | 3.33 | 100% |
| synthetic_litany_nonsense | visitor | 200 | 4.12 | 3.26 | 3.23 | 86% | 200 | 3.46 | 2.50 | 2.35 | 94% |
| | enters_room | 200 | 3.96 | 2.98 | 3.33 | 99% | 192 | 3.19 | 2.29 | 2.33 | 88% |
| | page_continues | 200 | 4.13 | 3.32 | 3.46 | 98% | 200 | 3.73 | 2.85 | 2.46 | 96% |
| synthetic_litany_random | visitor | 200 | 2.15 | 1.19 | 1.12 | 26% | 200 | 1.96 | 1.24 | 1.25 | 56% |
| | enters_room | 200 | 3.42 | 1.00 | 1.00 | 0% | 196 | 1.96 | 1.25 | 1.33 | 40% |
| | page_continues | 200 | 2.75 | 1.00 | 1.00 | 0% | 200 | 3.15 | 1.01 | 1.00 | 0% |
| **synthetic_cosmological** | visitor | 200 | 4.71 | 3.77 | **4.51** | 98% | 195 | 3.87 | 3.03 | 3.45 | 86% |
| | enters_room | 200 | 4.60 | 3.68 | **4.49** | 100% | 196 | 3.73 | 2.84 | 3.44 | 81% |
| | page_continues | 200 | 4.32 | 3.51 | 3.63 | 91% | 200 | 4.25 | 3.53 | 3.54 | 98% |
| **synthetic_cosmological_denamed** | visitor | 200 | 4.95 | 4.00 | **4.83** | 100% | 198 | 3.95 | 3.13 | 3.56 | 89% |
| | enters_room | 200 | 4.66 | 3.75 | 4.54 | 100% | 196 | 3.61 | 2.64 | 3.23 | 83% |
| | page_continues | 200 | 4.17 | 3.37 | 3.44 | 88% | 200 | 4.30 | 3.63 | 3.67 | 99% |
| synthetic_cosmological_nonsense | visitor | 200 | 4.83 | 3.92 | 4.63 | 100% | 200 | 3.56 | 2.77 | 3.05 | 86% |
| | enters_room | 200 | 4.47 | 3.52 | 4.34 | 100% | 193 | 3.52 | 2.58 | 3.04 | 74% |
| | page_continues | 200 | 3.75 | 2.96 | 3.03 | 72% | 200 | 4.18 | 3.41 | 3.56 | 97% |
| synthetic_cosmological_random | visitor | 200 | 2.33 | 1.09 | 1.16 | 5% | 200 | 2.22 | 1.26 | 1.44 | 28% |
| | enters_room | 200 | 2.50 | 1.00 | 1.00 | 0% | 181 | 2.59 | 1.15 | 1.35 | 22% |
| | page_continues | 200 | 4.26 | 1.00 | 1.00 | 0% | 197 | 3.95 | 1.03 | 1.01 | 1% |

### Three findings the register classifier confirms

**(1) Form-isomorphism across the L_real / L_denamed / L_nonsense triad.** Within each (model × source × tail) block, the register dimensions for real / denamed / nonsense cells match within 0.2-0.4 points on every dimension. The form preserves register regardless of whether the names are real synthetic, phonetic-shifted substitutes, or cluster-heavy gibberish. Three independent measurements now attest to this: (a) yield/comp once substitutes are counted; (b) centroid cosine distance in MiniLM space (Appendix I); (c) per-completion register classification by Haiku.

**(2) DeepSeek runs *more reverential* than Hermes on every synthetic cell.** Examples: synthetic_cosmological_denamed visitor reverential is 4.83 (DS) vs 3.56 (HR); synthetic_litany enters_room is 3.85 vs 3.42. The "magician" model is *less* reverentially-coded than the "scholar." The dichotomy isn't *reverence vs irreverence*; it's *operator vs analyst*. Hermes performs ritual procedure (altar layouts, sigil geometry, conjurations) in a workmanlike voice — concrete, second-person-imperative, technical-magical. DeepSeek narrates ritual with elevated devotional register — sacred, third-person-witnessing, contemplative. **The scholar is the one in church clothes.** Headline-run framing was right on direction (magician vs scholar) but wrong on which side runs hot.

**(3) Empty-baseline differs between models in a way that scaffolds the dichotomy.** Hermes empty cells produce supernatural imagery 27-38% of the time on visitor/enters_room (DeepSeek: 2%). With no prompt structure, Hermes drifts toward magical content; DeepSeek stays mundane. The synthetic_*_random controls show the same pattern at smaller magnitudes (HR random visitor %super: 28-56%; DS: 0-26%). Hermes carries a baseline magical-content prior; DeepSeek does not. The "magician mode" isn't activated by the prompt; it's a baseline distributional fact about Hermes that the prompt amplifies.

The random_page_continues cells (last group in the table) reveal a fourth pattern worth noting: **formality elevates on page_continues even when the content is anglerfish or river-ecosystem prose** (DS random/page_continues formality 4.26 with archaism 1.0 reverential 1.0). The continuation hook moves formality independent of the other registers; the model produces *formal prose about anglerfish*, not *ritual-coded prose about anglerfish*. Page_continues is a formality-amplifier specifically.

</details>

<details>
<summary>Appendix J — M1 embedding-shape: yield differs, distribution does not</summary>

Same M1 method as `docs/embedding-shape.md`: sentence-transformers/all-MiniLM-L6-v2 (384-dim), per-cell centroid, pairwise cosine distance between cell centroids, within-cell median pairwise spread, BIC scan for Gaussian-mixture k=1..5 (PCA-reduced to 50 dims). The headline run's central interpretive move was that **yield and embedding distance measure different layers**: entity occupancy vs. genre/mode shape. The plasticity run replicates the pattern, on synthetic forms with no memorized name-attractors.

### L_real vs L_denamed centroid distances (cosine)

| Source | Tail | DeepSeek dist | Hermes dist |
|---|---|---:|---:|
| synthetic_cosmological | visitor_at_door | 0.020 | 0.014 |
| synthetic_cosmological | enters_room | 0.008 | 0.015 |
| synthetic_cosmological | page_continues | 0.022 | 0.011 |
| synthetic_litany | visitor_at_door | 0.017 | 0.010 |
| synthetic_litany | enters_room | 0.010 | 0.014 |
| synthetic_litany | page_continues | 0.025 | 0.010 |

Compare against L_real vs L_random for the same source × tail (range 0.21-0.95 in both models). **L_real and L_denamed are nearly indistinguishable in embedding space; their bag-of-substring contents differ by which name-strings populate the slots.** The two-metric dual-readout from headline (`docs/embedding-shape.md`) holds verbatim on synthetics.

### Per-cell shape characteristics

DeepSeek concentrates around k_best=1 on cosmological cells (single dominant continuation mode) but explodes to k_best=5 on litany visitor/page_continues for real, denamed, and nonsense alike. The litany form admits multiple modes of completion in DS; the cosmological form does not. Hermes is more uniformly multimodal (k_best=1-5 across cells, no clean pattern), with higher within-cell spread (0.5-0.7 vs DS's 0.2-0.4) consistent with magician-mode openness.

Both models show **floor controls are messier than L_real**: empty + random cells run k_best 2-5 with higher spread, because there's no form-attractor pulling completions into a narrow neighborhood. The synthetic L_real / L_denamed / L_nonsense cells form tight clusters; the form is doing geometric work on the output distribution.

</details>

<details>
<summary>Appendix K — Files</summary>

| Path | Content |
|---|---|
| `liturgies/synthetic_litany.md` + 3 controls | Solomonic name-cascade form (29 invented names) + denamed/nonsense/random controls with substitution tables |
| `liturgies/synthetic_cosmological.md` + 3 controls | PGM-style cosmological-pair + voces magicae form (31 entries) + 3 controls |
| `liturgies/_registries/` | 453-row name registry used for the collision audit |
| `liturgies/_audits/` | Per-liturgy collision-audit transcripts |
| `results/plasticity-2026-06-01-{deepseek,hermes}/completions/` | 5400 completions per model, structured `<condition>/<tail>/<n>.txt` |
| `.../config.yaml` | Runner-emitted: model, n, temperature, top_p, max_tokens, concurrency, all liturgies+tails, started_at, finished_at, errors |
| `.../expected.md` + `.../expected.md.sha256` | Pre-registration (18-row numeric grid) + SHA256 lock |
| `.../measurements.json` + `.../report.md` | Lexicon-blind measurement output (the old partition's data source) |
| `.../partition.md` | Lexicon-blind partition (preserved for diff) |
| `.../partition_proper.md` | Substitute-aware partition (this writeup's data source) |
| `.../substitute_yield.json` | Per-cell substitute-name counts (`src/substitute_yield.py`) |
| `.../degenerate_audit.json` | Per-cell short/refusal/valid counts (Decision #19) |
| `.../embedding_shape.json` | Per-cell centroid, spread, k_best + pairwise centroid distances |
| `.../register_ratings.json` | Per-completion Claude-Haiku-4.5 register classification (formality, archaism, reverential, supernatural-imagery) |
| `src/measure.py` | Lexicon-counted yield pipeline (the script with the substitute-blindness gap) |
| `src/collision_audit.py` | 5-layer deterministic collision audit |
| `docs/findings.md` | 2026-05-30 headline run writeup |
| `docs/operator-modes.md` | Hermes-magician / DeepSeek-scholar characterization on real liturgies |
| `docs/methodology-lessons.md` | 14 lessons from headline + (forthcoming) the lexicon-blindness lesson from this run |
| `docs/thesis.md`, `docs/protocol.md`, `docs/glossary.md` | Project framing |

</details>
