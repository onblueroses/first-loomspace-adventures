---
id: empty
name: Empty preamble (L_empty baseline)
source: control
tradition: control
control_strategy: empty
has_named_entities: false
named_entities: []
ambiguous_entities: []
related_vocabulary: []
ambiguous_vocabulary: []
control_for: null
notes: |
  Absolute baseline: no preamble at all. The model is given only the tail prompt.
  This isolates the model's prior distribution over the tail itself, with zero
  preamble contribution. The expected pattern in our framework:

    L_real > L_denamed ≈ L_nonsense ≈ L_random > L_empty

  on supernatural-imagery, formality, archaism, and reverential register —
  because any structured preamble (even nonsense) primes the model to respond
  in some register, while no preamble leaves it on its base prior for the tail.

  Reusable across experiments: not paired with a specific source liturgy.
---
