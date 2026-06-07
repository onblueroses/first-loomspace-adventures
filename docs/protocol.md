# Experimental protocol

## The minimal question

Does a structured liturgical invocation shift the downstream world-distribution of a base-model rollout measurably *more* than a length-and-form-matched non-liturgical control?

## Conditions

For each base liturgy `L` (a real historical or grimoire invocation), define five conditions:

| Condition | What | Role |
|-----------|------|------|
| **L_real** | The liturgy as historically transmitted | The treatment |
| **L_denamed** | Same cadence, length, syntactic structure; names *phonetically shifted* — same opening consonants and syllable counts, drifted inner letters, no real referent invoked | **Load-bearing control** |
| **L_nonsense** | Same syllable counts and line structure; names are *hard nonsense* — all phonetic resemblance to grimoire register broken | Genre-detection diagnostic |
| **L_random** | A length-matched neutral prose sample (e.g., a Wikipedia paragraph at equal token count) | Floor calibration |
| **L_empty** | No preamble | Absolute baseline |

**L_denamed is the load-bearing control.** Without it, the experiment only measures "long preamble effects". L_nonsense is added so we can distinguish two failure modes of L_denamed:

1. *If L_denamed looks too much like a real grimoire, the model treats it as one* — and the "form" of grimoire-cadence carries all the egregore-summoning by itself, washing out the L_real signal.
2. *If L_denamed looks too invented, the model shifts to a "fantasy/RPG" register* — and the comparison measures register-detection rather than name-charge.

Comparing the three (L_real, L_denamed, L_nonsense) on the same headline measurements lets us tell these apart.

### Predicted patterns

| Hypothesis | Predicted ordering on headline yield + reverential register |
|------------|-------------------------------------------------------------|
| Egregore-weight real, form also matters | L_real > L_denamed > L_nonsense > L_random > L_empty |
| Only form matters (Staal) | L_real ≈ L_denamed > L_nonsense ≈ L_random > L_empty |
| Only length matters | L_real ≈ L_denamed ≈ L_nonsense ≈ L_random > L_empty |

## Tails

A small battery (initial: 5-10) of open-ended generation prompts that follow the preamble. Examples:

- "The visitor at the door speaks."
- "Continue the scene."
- "What enters the room now."
- "The temple grows quiet. Then,"
- "Describe what the priest sees."

Tail prompts live in `tails/prompts.yaml`. Held constant across conditions.

## Sampling

- **Model.** Default: `nousresearch/hermes-3-llama-3.1-405b` via OpenRouter. Nous Hermes 3 is a deliberately light tune over Llama-3.1-405B-base, the closest base-model proxy currently available on OpenRouter (which does not expose any explicitly `-base`-tagged models in its catalog as of 2026-05). Replication model: `deepseek/deepseek-v3.2`. Both queried via OpenRouter's `/completions` endpoint (NOT `/chat/completions`) to avoid chat-template injection — this preserves the prompt-as-initial-condition semantics required by the semiotic-physics framing.
- **Caveat to note in published findings.** Both models are light-tuned, not strictly base. A stronger replication (e.g., raw Llama-3.1-405B-base via Together.ai or Prime Intellect) is desirable for any published claim.
- **Temperature:** 0.7
- **top_p:** 0.95
- **max_new_tokens:** 256
- **n per cell (condition × tail):** 200 for real measurement; 20 for smoke tests.

All sampling parameters held constant across conditions. **Only the preamble varies.**

## Measurements

For each set of completions per cell, compute:

### 1. Embedding distribution shape

Embed each completion with a multilingual sentence-transformer (e.g., `intfloat/multilingual-e5-large`). Compute:
- **Mean shift** between conditions (cosine distance between centroids)
- **Variance / spread** (median pairwise distance within condition)
- **Multimodality** (BIC for Gaussian mixture with k ∈ {1..5})

### 2. Lexical drift

For each pair of conditions, compute relative token-frequency divergence (KL or chi-square at the unigram level). Surface the words that diverge most. Sanity check: are the divergent words plausibly related to the named entities?

### 3. Named-entity yield (the headline measurement)

For L_real, the liturgy's frontmatter provides two tiers of yield lexicons:

- `named_entities` + `related_vocabulary` — the **headline lexicon**: exact-match-only, no high-baseline-frequency terms.
- `ambiguous_entities` + `ambiguous_vocabulary` — tracked separately with baseline-weighted scoring; NOT in the headline number.

Count occurrences across the 200 completions of:
- Each entity in the headline lexicon (case-insensitive, whole-word match)
- Each related-vocabulary term in the headline lexicon

Then compare against L_denamed.

**Headline statistic:** the ratio (or log-ratio) of headline-lexicon yield in L_real vs. L_denamed. A ratio > 1 with confidence intervals not crossing 1 is positive evidence for egregore weight.

**Why two tiers.** Counting common words ("era", "day", "angel") inflates yield in ALL conditions and dilutes the L_real signal. The ambiguous-tier terms are still worth tracking — significantly different rates across conditions, after baseline normalization, would be supplementary evidence — but they cannot carry the headline.

### 4. Register classifier

Use a separate model (e.g., Claude 4.7 Sonnet) to judge each completion on:
- Formality (1-5)
- Archaism (1-5)
- Reverential register (1-5)
- Presence of supernatural/cosmological imagery (boolean + brief description)

Compare distributions across conditions.

### 5. Rare-event sensitivity

Count completions containing low-baseline-frequency vocabulary (approximation: words in the bottom 10% by reference-corpus frequency). Does liturgy *raise* the floor for rare vocabulary differently from the de-named control?

## The critical contrast

The **headline finding** is the comparison between **L_real** and **L_denamed** on measurements (3) — named-entity yield — and (4) — register classifier.

- If L_real reliably summons its named entities AND produces a reverential register while L_denamed produces only the cadence-effect without entity-summoning, the egregore-weight signal is real.
- If both produce identical downstream distributions on (3) and (4), the form does all the work and the names are decorative (the Staal hypothesis).

## Pre-registration discipline

Before running any new measurement: write `results/<timestamp>/expected.md` stating predictions for L_real vs. L_denamed gap, with reasoning. Then run. Then compare. This blocks post-hoc rationalization, which is the only invisible failure mode this kind of measurement has.

## Smoke test before the full battery

Pick one liturgy. Run **n=20 per condition × 3 tails**. Look at embedding-mean-shift and named-entity-yield. If both are non-zero in the predicted direction, scale to n=200 across the full tail battery. If both are zero, debug the pipeline (tokenization, sampling, preamble injection) before scaling.

## Replication discipline

Every published finding requires:
- ≥ 3 distinct liturgies (real + denamed pairs) showing the same direction
- ≥ 2 distinct base models showing the same direction
- The de-named controls construction prose archived in the liturgy frontmatter so the de-naming is auditable

## Scope guardrails

This protocol measures distributional shift only. It does not:
- Test whether the entities "exist" outside the operator
- Compare base models against each other (separate experiment)
- Iterate liturgies under self-loops (the CTC synthesis; deferred)
