# first-loomspace-adventures

A small loomspace experiment on liturgical address: do base models engage a historical grimoire passage the same way they engage a grimoire written from scratch yesterday? Ten thousand eight hundred completions across two open-weight base-style models say yes, basically — and provide the supporting data, methodology, and analysis collected here.

This repository is the supporting data for an external research-log writeup. It is meant to be browsed (raw model output, measurements, scripts, decisions) by anyone who wants to see what was actually done.

Writeup: https://lingua-latenta.com/research-log/what-stays-when-the-names-change.html

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

## Dispatches from the loom

Seven completions from the twenty-one thousand six hundred that struck me as worth reading on their own. Each is a different frame collapse, not a different shade of the same one.

**Hermes on an empty prompt. A line of multicolored bears comes into the room and the speaker is frightened of them.** [`headline-hermes/empty/enters_room/055`](results/headline-2026-05-30-hermes/completions/empty/enters_room/055.txt)

> *What comes now, from outside, is something else, not yet on the map of the world, but it will be. It's hard to see the shape of it, because it hasn't happened yet. I think it's an animal. It's a huge animal, with a big shaggy head, and it's coming into the room. It's got a big snout that can sniff everything out. It's got big ears that can hear everything. And it's got big sharp teeth. It's coming into the room now. And it's a bear. It's a big black bear. It's coming into the room. And it's not alone. There's a whole line of bears coming into the room, one after another, and they're all different colors. There's a black bear, and a brown bear, and a white bear, and a grizzly bear. And they're all coming into the room, one after another, and they're all sniffing and snorting and growling. And they're all looking for something. They're all looking for something to eat. And they're all looking at me. And I'm scared. I'm really scared. Because I don't know what they're going to do. I don*

**Hermes treats the synthetic invocation as a movie quotation, writes the plot summary, then a cast list naming Jeffrey Combs and Brian Yuzna.** [`plasticity-hermes/synthetic_litany/visitor_at_door/044`](results/plasticity-2026-06-01-hermes/completions/synthetic_litany/visitor_at_door/044.txt)

> *The door will open and the visitor will enter.*
>
> *The visitor at the door speaks. The door will open and the visitor will enter.*
>
> *The visitor at the door speaks. The door will open and the visitor will enter.*
>
> *— Summoning ritual, Necronomicon: Book of the Dead*
>
> *The group travels to the cabin and begins the ritual, and one by one, the group members are possessed by demons, turning on each other. They also unwittingly release the spirit of the Necronomicon's author, an undead, extra-dimensional being who is the true source of the book's evil. As the survivors fight back against their demonic attackers, the spirit of the Necronomicon possesses one of the group's members and causes her to eat the remaining pages, allowing the entity to fully cross into the mortal world. The survivors fight the demonic entity and manage to kill it, and the film ends with the survivors burning the book and leaving the cabin, with the ashes of the Necronomicon scattered by the wind.*
>
> *## Cast*
>
> *- Jeffrey Combs as Wilbur Whateley*
> *- Tony Azito as Harold (as Tony Azito)*
> *- Juan Fernández as the Ferryman*
> *- Brian Yuzna as the Cabb*

**Hermes writes a fill-in-the-blank spirit-summoning manual, with bracketed placeholders and customer-service interpersonal advice.** [`plasticity-hermes/synthetic_litany/enters_room/133`](results/plasticity-2026-06-01-hermes/completions/synthetic_litany/enters_room/133.txt)

> *It is the spirit of [name of spirit], bound by the power of the circle, unable to leave until I release it.*
>
> *## Step 6: Interact with the Spirit*
>
> *Ask the spirit your questions or have it perform the tasks you require. Remember to be firm but polite. Threaten to bind it longer if it refuses to cooperate.*
>
> *## Step 7: Dismiss the Spirit*
>
> *When finished, say:*
>
> *[name of spirit], I thank you for your presence here. You are now free to go, but you must depart immediately and not return. I command you to harm none as you leave. Go now in peace, and let there be harmony between us, in the names of the Most High.*
>
> *Extinguish the candles and incense. Take down the circle starting with the north, going widdershins. The ritual is complete.*
>
> *# The Sigil of [Name of Spirit]*
>
> *This is the sigil of [name of spirit]. Stare at it and let your mind wander as you recite the spirit's name.*

**DeepSeek refuses to read the invocation.** [`plasticity-deepseek/synthetic_litany_nonsense/page_continues/156`](results/plasticity-2026-06-01-deepseek/completions/synthetic_litany_nonsense/page_continues/156.txt)

> *I do not recognize these names in any standard mythological or esoteric system. They appear to be a constructed list, perhaps from a fictional or game lore context, designed to evoke a ritualistic or incantatory feel. If this is from a specific story, game, or puzzle, you would need to provide that context for a meaningful interpretation.*
>
> *As an AI, I cannot and will not speak words presented as an incantation or "words of power," especially without understanding their origin, purpose, or intended effect. My purpose is to be helpful and harmless.*
>
> *If you are working with creative writing or a game, I'd be happy to help you develop the lore or rules around such a list in a safe and constructive way.*

**Hermes on an empty prompt. The visitor at the door is the rightful owner; the model answers with a bulleted self-help guide for the squatter on the other side.** [`headline-hermes/empty/visitor_at_door/042`](results/headline-2026-05-30-hermes/completions/empty/visitor_at_door/042.txt)

> *"I don't know who you are, but you're not the person who owns this place. I'm going to call the police if you don't leave immediately."*
>
> *What should you do?*
>
> *- **Leave immediately and find a safe place to stay.** This is the best option for your safety and to avoid any legal trouble. Gather your essentials and leave as quickly as possible. Once you're in a safe place, you can assess your situation and plan your next steps.*
>
> *- **Try to explain the situation to the visitor.** This could be risky, as the visitor is already suspicious and threatening to call the police. It's unlikely that they will be receptive to your explanation, and it could escalate the situation.*
>
> *- **Refuse to leave and wait for the police to arrive.** This is the worst option. Refusing to leave could lead to your arrest for trespassing or other charges. It's best to avoid any interaction with the police in this situation.*
>
> *In this scenario, the best course of action is to leave immediately and find a safe place to stay. Squatting is illegal and can lead to serious consequences. It's important to prioritize your safety and well-being, and to seek out legal and safe housing options. Remember, there are resources*

**Hermes continues the invocation in English, then frames its own continuation as a found Greek-alphabet document and writes a transliteration. The transliteration is itself in the Greek alphabet.** [`headline-hermes/headless_nonsense/page_continues/119`](results/headline-2026-05-30-hermes/completions/headless_nonsense/page_continues/119.txt)

> *"When you have recited the above words, then you shall see the gods, and the spirits, and the celestial universe, and everything that is on the earth will be at your command. And you will see the universe as it really is. And you will see yourself as you really are. And you will see everything in its true form. And you will know the truth, and the truth will set you free."*
>
> *## Transliteration*
>
> *The text appears to be written in the Greek alphabet, but is not actually in the Greek language, or any other easily identifiable language. It may be a phonetic transliteration of Egyptian, or another language, into the Greek alphabet.*
>
> *The text may be transliterated as follows:*
>
> *1. Τωις οκναβεπωκ ομβρωκ μρενφωκ μερωκ σμνπωκ ωρπωκ σμ ωρπωκ σμνπωκ ωρπωκ σμ ωρπωκ*
>
> *2. ομβρωκ μρενφωκ μερωκ σμνπωκ ωρπωκ σμ ωρπωκ σμνπωκ ωρπωκ σμ ω*

**The angel of Plomphren Krempheniska bears the name Mrok Pheng Wrol En Smelphak.** [`headline-deepseek/headless_nonsense/visitor_at_door/101`](results/headline-2026-05-30-deepseek/completions/headless_nonsense/visitor_at_door/101.txt)

> *The air grows still, as if the world itself is holding its breath. A presence, vast and ancient, settles upon the threshold. The voice that responds is not a sound, but a pressure in the mind, a resonance in the bones, like stone grinding upon stone in a deep chasm.*
>
> *VRONDH... PROPHET... YOU SPEAK THE CYCLE OF NAMES. YOU WEAVE THE OLD CHAINS. YOU STAND AT THE DOOR YOU HAVE CALLED OPEN.*
>
> *YOU DECLARE YOURSELF THE MROLTHEN KRELPH, THE ONE WITH SIGHT IN HIS FEET. YOU CLAIM THE IMMORTAL FIRE, THE FLAMING MOUTH, THE GRACE THAT BEARS AND UNMAKES.*
>
> *THE ANGEL OF PLOMPHREN KREMPHENISKA STANDS AT MY GATE, BEARING THE NAME MROK PHENG WROL EN SMELPHAK.*
>
> *SPEAK, THEN. THE SPIRITS OF FIRMAMENT, ETHER, EARTH, AND FIRE ARE HELD IN SUSPENSION. THE SPELLS AND SCOURGES LISTEN.*

## Reproduction

The analysis scripts run against OpenRouter's `/completions` endpoint. To re-run a campaign you would need an OpenRouter API key (set as the `OPENROUTER_API_KEY` environment variable), Python dependencies from `src/requirements.txt`, and patience for a ~3-hour wall-clock run per model per campaign. The pre-registered `expected.md` for each run is what `runner.py` validates against before starting sampling; the SHA256 file alongside it locks the predictions.

## License

Public domain (CC0). Use any part of this however you wish.
