# first-loomspace-adventures

A small loomspace experiment on liturgical address: do base models engage a historical grimoire passage the same way they engage a grimoire written from scratch yesterday? Ten thousand eight hundred completions across two open-weight base-style models say yes, basically — and provide the supporting data, methodology, and analysis collected here.

This repository is the supporting data for an external research-log writeup. It is meant to be browsed (raw model output, measurements, scripts, decisions) by anyone who wants to see what was actually done.

## What's in here

```
liturgies/      Source liturgies: two synthetic primaries (Solomonic name-cascade
                + PGM cosmological-invocation), two historical primaries
                (Astrachios prayer + Headless Rite), and their controls
                (denamed / nonsense / random / empty). Each is a markdown file
                with YAML frontmatter naming the lexicon and design notes.

tails/          The three downstream open-ended prompts the model continues
                after the liturgy: visitor_at_door, enters_room, page_continues.

src/            Analysis scripts (Python). runner.py drives the OpenRouter
                completions endpoint. measure.py computes per-completion
                lexicon yields. substitute_yield.py + proper_partition.py
                handle the substitute-aware analysis. embed_shape.py runs
                the post-hoc embedding-distribution analysis.
                classify_register.py rates each completion on four register
                dimensions. collision_audit.py implements the 5-layer
                phonetic+edit-distance audit used when authoring the
                synthetic liturgies.

results/        Two campaigns of measurement.
                headline-2026-05-30-{deepseek,hermes}/   historical liturgies
                plasticity-2026-06-01-{deepseek,hermes}/ synthetic liturgies
                Each contains:
                  config.yaml          run parameters
                  expected.md          pre-registered predictions (SHA256-locked
                                       before sampling)
                  measurements.json    headline yield numbers per cell
                  partition*.md        within-liturgy log-space partition
                                       (floor / form-charge / name-charge)
                  embedding_shape.json M1 embedding-distribution metrics
                  register_ratings.json per-completion register classifier
                                       output
                  completions/         raw model output per condition/tail/n
                  report.md            human-readable summary
                  degenerate_audit.json refusal/short-completion accounting
                  substitute_yield.json substitute-name occurrence counts
                                       in controls

docs/           thesis.md            theoretical framing
                protocol.md          experimental design
                glossary.md          terms
                sources.md           references
                findings.md          full integrated picture of the headline run
                operator-modes.md    cross-model contrast (Hermes magician-mode
                                     vs DeepSeek scholar-mode), with verbatim
                                     completion passages
                embedding-shape.md   the M1 embedding-distribution analysis
                plasticity-findings.md the synthetic-liturgies writeup, with
                                       11 appendices
                methodology-lessons.md fifteen lessons accumulated across the
                                       two campaigns
```

## The headline question

Does a base language model in closed-loop continuation engage with the structural form of liturgical address, with the specific historical names threaded through that form, or with both? Two campaigns try to separate the contributions.

- **Headline campaign** (2026-05-30): two historical liturgies (the Astrachios prayer from the *Grimorium Verum* and the Headless Rite from PGM V.96-172), each fed with three controls (a phonetically-shifted denamed twin, a cluster-heavy gibberish nonsense twin, a length-matched random English prose preamble) plus the empty prompt.

- **Plasticity probe** (2026-06-01): two synthetic liturgies written from scratch (one Solomonic name-cascade, one PGM cosmological-invocation), every invented name audited five ways against the *Lemegeton*, the Shemhamphorash, and a 453-row registry of theonyms so no real name could sneak in. Same four controls per liturgy.

Two models: Hermes-3-405B and DeepSeek-V3.2, via OpenRouter `/completions`. n = 200 per cell, three downstream tails. Predictions hash-locked before each campaign ran.

## The headline finding

The form does most of the work. Across all twelve test cells of the plasticity probe and both models, the within-liturgy partition shows form-contribution at 280× to 1750× the random-prose floor; the model's preference for the real synthetic name-set over the form-matched substitute sits between 0.59× and 1.36×, hovering near indifference. In ten of twelve cells, the model produces substitute names at a per-completion rate at least equal to, often higher than, the real-name rate. Same operator-modes (Hermes-magician on Solomonic, DeepSeek-scholar on PGM) engage on the synthetics that engaged on the historicals.

Full numbers, full verbatim, full methodology: in the relevant `docs/` files and the `results/` measurement files.

## Reproduction

The analysis scripts run against OpenRouter's `/completions` endpoint. To re-run a campaign you would need an OpenRouter API key (set as the `OPENROUTER_API_KEY` environment variable), Python dependencies from `src/requirements.txt`, and patience for a ~3-hour wall-clock run per model per campaign. The pre-registered `expected.md` for each run is what `runner.py` validates against before starting sampling; the SHA256 file alongside it locks the predictions.

## License

Public domain (CC0). Use any part of this however you wish.
