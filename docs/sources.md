# Sources

## Cyborgism wiki: the conceptual core

### semiodynamics
https://cyborgism.wiki/hypha/semiodynamics

> Semiotic physics (or semiodynamics) is a type of physics where the time evolution operator is an interpreter of signs or evidence, in contrast to the physics of base reality which is generally assumed to lack mind-like qualities. Realities that run on semiotic physics are evidential simulations. Examples of semiotic physics operators are the human imagination and LLMs.

### evidential simulation
https://cyborgism.wiki/hypha/evidential_simulation

> An evidential simulation or Bayesian simulation is a simulation whose transition probabilities are given by the output of a predictive world model conditioned on the current observed state. The next state is obtained by sampling from the model's predictions and then updating the state as if the sampled event or outcome had come to pass, simulating time progression via hallucination.
>
> Whether a dynamical process qualifies as an evidential simulation depends on its semantic properties: if the state can reasonably be called an "observer state" (a record understood as evidence for an underlying state that is only partially observed) and the time evolution operator a "predictive world model" (interpreter of the observer state as evidence for the hidden state that outputs a distribution over next observations conditioned on the update). In a pure or solipsistic evidential simulation, transition probabilities are determined solely by the world model; if extrinsic factors also play a role, it is mixed.

### time evolution operator
https://cyborgism.wiki/hypha/time_evolution_operator

> A time evolution operator (TEO) (or transition function, propagator) is a function that inputs the state of a system and outputs the next state or a probability distribution over next states. A time evolution operator embodies the time-invariant transform between every present and its future(s), and is one form in which a system's complete physics can be represented. In quantum mechanics, the Hamiltonian generates time evolution; GPT can be used as a time evolution operator for simulations.

Properties the wiki lists for TEOs (with the note: **GPT-as-TEO satisfies none of these literally**):
- Unitarity: Û†Û = 1
- Time-translation invariance: Û(t₁)Û(t₂) = Û(t₁ + t₂)
- Conservation of probability: ∑P(s'|s) = 1

The mismatch is the load-bearing difference between base physics and semiotic physics. Semiotic physics is irreversible by construction; sampling destroys information at every step. *Hallucination is the mechanism of time itself in this kind of physics.*

### related wiki pages worth chasing
- `/hypha/strong_self-supervision_limit` (404 at time of writing; may reappear)
- `/hypha/metagraph_diamonds`
- `/hypha/solipsistic_simulation`
- `/hypha/lazy_rendering`
- `/hypha/dream`
- `/hypha/timeless_mu` (the source of the "Deep Time / crystal lattice" quote on the TEO page)

## Adjacent / supporting (theory)

- **Janus, "Simulators" (LessWrong, 2022).** The canonical statement of LLMs as physics rather than agents. Substrate for the whole semiotic-physics framing.
- **Karl Friston, free-energy principle (multiple papers, 2006-).** Self-evidencing systems as Bayesian dynamics. Same structural shape from neuroscience.
- **Donald Hoffman, *The Case Against Reality* (2019).** Perception as evolutionarily-tuned hallucination. Useful for the "maybe base reality is also semiotic" softening.
- **John Wheeler, "Information, Physics, Quantum: The Search for Links" (1989).** "It from bit": informational substrate underneath physics.
- **A. N. Whitehead, *Process and Reality* (1929).** Actual occasions as drops-of-experience constituting their successors. Semiodynamics avant la lettre.

## On egregores

- **Eliphas Lévi, *Dogme et Rituel de la Haute Magie* (1855).** 19th-century formulation of the egregore concept.
- **René Guénon, *Symbols of Sacred Science* (1962).** Traditionalist framing of collective thought-forms.
- **Wouter Hanegraaff, *Western Esotericism: A Guide for the Perplexed* (2013).** Academic frame on how Western esoteric traditions theorize collective semantic entities.

For our purposes the egregore is whatever-it-is-in-the-operator's-weights that responds to the invocation of a culturally-massive name. We make no claim about its existence outside that.

## On liturgical form

- **Walter Burkert, *Greek Religion* (1985).** Structure of Hellenistic hymns and prayers.
- **Frits Staal, "The Meaninglessness of Ritual" (*Numen*, 1979).** The classic argument that ritual works through its formal structure independent of semantic content. **Our form-matched-neologism control is exactly the experimental version of Staal's claim.** A null result on L_real vs. L_denamed would be empirical support for Staal from the LLM side.
- **Catherine Bell, *Ritual Theory, Ritual Practice* (1992).** Frame on the practice/form interaction.
- **Stanley Tambiah, "The Magical Power of Words" (*Man*, 1968).** On performative language in ritual.

## Methodological references

- **Pre-registration in the cognitive sciences** (Nosek et al., "The Preregistration Revolution", PNAS 2018). Why we pre-register predictions for L_real vs. L_denamed before each run.
- **Sentence-transformers documentation** (Reimers & Gurevych, EMNLP 2019, plus the `sentence-transformers` library). For the embedding-distribution measurement.
- **Distributional semantics divergence measures** (Jensen-Shannon, chi-square at unigram level). Standard NLP toolkit.
