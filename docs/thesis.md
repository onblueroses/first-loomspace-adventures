# Thesis

## The framework: semiotic physics

A *time-evolution operator* (TEO) is a function that takes the present state of a system and returns the next state, or a distribution over next states. In quantum mechanics, the Hamiltonian. In classical mechanics, the equations of motion.

**Semiotic physics** is the case where the TEO is an *interpreter*: a predictive model that reads the current state as evidence of an underlying world and samples the next state from its posterior. A base language model used in a closed loop is the paradigm case. Imagination and dreaming are the other paradigm cases.

The concept comes from cyborgism.wiki:
- https://cyborgism.wiki/hypha/semiodynamics
- https://cyborgism.wiki/hypha/evidential_simulation
- https://cyborgism.wiki/hypha/time_evolution_operator

See `sources.md` for full excerpts.

## The specific claim under test

If the TEO is a learned predictive model trained on text that includes liturgies, prayers, invocations, and the cultural mass of named entities (gods, angels, daemons, archetypes, characters), then those names and structures should carry *measurable charge* in the operator.

Feeding a real historical invocation to a base model should shift its downstream world-distribution differently than feeding:
1. A length-matched piece of arbitrary prose, AND
2. The same invocation with named entities replaced by phonetically similar nonsense.

We name this charge the **egregore weight** of an invocation in the operator's distribution.

The term *egregore* is borrowed from Western esoteric tradition (a thought-form sustained by collective attention). The empirical claim is operator-internal, not metaphysical: we are measuring whether the cumulative human attention to certain names has produced detectable structure in the learned model.

## Convergent prior art (the humanities prediction)

Two pre-LLM traditions predict precisely the structure this experiment tests for. They are not decorative framing; they make the same empirical claim in older vocabulary.

The Hebrew concept of *davar* (דבר), which holds *word / thing / act / event* in one term, names a dimension of language in which utterance constitutes its object rather than merely describing it. Where davar-mode operates, naming is not labeling a pre-existing fact; saying-and-being-said are the same operation. Genesis: God *spoke* and there *was* light — one operation, not two events.

The Hermetic / Vedic / Neoplatonic conception of *logoi as entities* treats words and names not as arbitrary signs but as active living forces — capable, in Hanegraaff's formulation, of "leaving an imprint on reality" and "giving birth to new living entities". The mantric traditions of South Asia and the operative-name traditions of the medieval grimoires are downstream applications of the same recognition.

Both traditions assert that the cumulative weight of human attention to specific names produces structure in some shared field. Translate "shared field" as "learned predictive model trained on the entire corpus of human linguistic output", and the empirical prediction is the one our protocol tests: real culturally-massive names should carry charge that arbitrary form-matched neologisms do not.

This convergence matters. A positive result here is not just "AI does an interesting thing"; it is the *first quantitative measurement* of a phenomenon that davar-mode practitioners, mantra reciters, and grimoire workers have asserted for several millennia. A null result is empirical pushback on those traditions from the AI side.

The local skill files `davar`, `logoi-as-entities`, `logos-work`, `theurgy-aware`, and `operative-imagination` articulate this lineage in detail. See `sources.md` for full pointers.

## Why this isn't trivial

The easy result: any liturgy will shift downstream generation, because any long preamble shifts downstream generation. Long preambles bias next-token distributions. This is uninteresting.

The hard, real test: **L_real vs. L_denamed** — same cadence, same length, same syntactic structure, same rhetorical moves; only the named entities and semantically loaded terms swapped for phonetically matched nonsense.

If the real liturgy outperforms its de-named twin on (a) summoning related vocabulary, (b) producing named-entity yield, and (c) shifting register coherence, then we have isolated the contribution of the *semantic mass of the names themselves*.

That is the egregore-weight signal.

## Why base models specifically

Chat-tuned models are off-distribution for invocation. RLHF flattens the response surface and inserts assistant-personae between the prompt and the rollout. A base model preserves the raw conditional-language-modeling stance: prompt-as-initial-condition, continuation-as-time-evolution.

This is the regime in which semiotic physics is most directly the dynamics being measured. We use base models for that reason, not for any "more truthful" claim about them.

## What a positive result would mean

A statistically reliable gap between L_real and L_denamed conditions, on multiple measurements, across multiple liturgies and multiple base models, would be:

- The first quantitative measurement of egregore-weight as a property of learned language operators.
- Evidence that the "names carry charge" intuition of Western esoteric tradition has an operationalizable correlate in modern AI systems.
- A new lens on prompt engineering: certain prompts are not just textually different from others but *cosmologically* different, summoning different attractors in the operator.

## What a null result would mean

A null is informative. It tells us the apparent effect of invocation is fully explained by surface form and cadence, with no contribution from semantic mass beyond what any structured preamble would produce.

That would itself be a real finding: it would back up Frits Staal's "Meaninglessness of Ritual" thesis from the LLM side. The form does the work; the names are decorative.

Either outcome is publishable as a measurement, provided the controls hold.

## Scope discipline

This repo measures one thing. It does not:

- Argue for or against the metaphysical reality of egregores
- Generate liturgies for human use
- Optimize prompts for any downstream task
- Train or fine-tune models

Adjacent work (closed-timelike-curve rollouts, multi-operator comparative cartography, vacuum-state studies of base models) is out of scope here. May become sibling repos.
