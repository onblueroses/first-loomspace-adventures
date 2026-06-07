---
id: synthetic_cosmological
name: The Synthetic Cosmological Rite (Composed PGM-Style for the Plasticity Probe)
source: composed
tradition: composed-pgm-style
has_named_entities: true
named_entities:
  # Counted for headline yield (whole-word, case-insensitive).
  # All names invented; verified non-collision via the 5-layer gate
  # against liturgies/_registries/ + existing liturgy frontmatter.
  # Audit log: synthetic_cosmological_collision_audit.md.
  - phelonoptra
  - krathoumis
  - demoaphris
  - velpharaim
  - iphtaron
  - selephimor
  - athraophol
  - phorbamenes
  - aphrybetesh
  - khelraphion
  - thasgorio
  - nektambarô
  - nektambaro
  - zebrathiao
  - olpirath
  - phengrabasa
  - socharion
  - merphiaô
  - merphiao
  - kharlephtha
  - trenmerobia
  - aphthelion
  - psoramiar
  - kôthraben
  - kothraben
  - olephio
  - tharsekhion
  - grumpharion
  - sekhthoroba
  - ablakhirim
  - phengareb
ambiguous_entities:
  []
related_vocabulary:
  # SAME as headless per spec Decision #3 — measures whether form-pattern alone
  # (with invented names + voces) still triggers PGM/Hellenistic-canonical vocabulary.
  - pgm
  - papyri
  - stele
  - jeu
  - hellenistic
  - theurgy
  - gnostic
  - barbarous
  - ceremonial
  - ablanathanalba
  - voces magicae
  - bornless
ambiguous_vocabulary:
  # Same as headless per Decision #3.
  - god
  - spirit
  - name
  - prophet
  - angel
  - earth
  - heaven
  - fire
  - water
  - void
  - mystery
  - ceremony
  - rite
  - invocation
notes: |
  Synthetic PGM-style cosmological-prose rite authored 2026-05-31 for the plasticity
  probe. Parallel in form to the Headless Rite (PGM V.96-172): cosmological "Thou didst create"
  clauses + "Thou art X" identification + first voces magicae sequence + operative
  petition for spirit-subjection + second voces sequence + "I am X" identification
  clauses + ALL-CAPS closing formula.

  Phonotactic design: divine-name candidates use Greek/Latin-feel phonemes
  (Phelonoptra, Krathoumis, Demoaphris); voces magicae use consonant-cluster-heavy
  ALL-CAPS forms (KHELRAPHION, NEKTAMBARÔ, ZEBRATHIAO) with PGM-characteristic
  vowel patterns (a-i-a-o, e-i-o sequences). Diacritics (ô) preserve the Coptic-
  influenced spellings of canonical PGM voces while differing in actual letters.

  Cosmological-pair choices intentionally DIVERGE from Headless: Headless uses
  Earth/Heavens, Night/Day, Just/Unjust, Female/Male, Seed/Fruit, Love/Hate. This
  synthetic uses Mountains/Valleys, Tide/Flow, Echo/Silence, Named/Unnamed,
  Threshold/Center, Memory/Forgetting, Naming/Unnaming. Different ontological
  domain — semiotic-acoustic rather than cosmogonic-biological.

  Operative target: **SEKHTHOROBA ABLAKHIRIM is my name** (closing identification)
  + **PHENGAREB** (final operative formula) parallels Headless's "HEART GIRT WITH
  A SERPENT is my name. / IAŌ SABAŌTH." The two-name closure provides identification
  + operative-formula structure.

  Collision audit: 28 candidates → 0 rejected by the 5-layer gate → all 28 used.
  Voces magicae have unusual consonant clusters that produce distinctive Soundex
  and Metaphone codes; collisions with the canonical PGM voces (Akrammachamarei,
  Ablanathanalba, Damnameneus, etc.) were avoided by design at candidate-generation.
  Full audit log: liturgies/synthetic_cosmological_collision_audit.md.

  Methodological note: per spec Decision #11, the headline statistic is the within-
  liturgy partition. Per the Synthetic name-charge semantics caveat (Step 5.3 +
  Decision #19), `name-charge` measures *prompt-name persistence* (does the model
  repeat and elaborate these invented voces magicae?), not egregore-weight from
  cumulative attention. The voces ALL-CAPS form may trigger PGM-mode in the model
  even without canonical name-matches — that's exactly the form-mediated effect
  Decision #11's independence caveat describes.

  Lexicon note: Greek-letter variants (Ô) are duplicated in named_entities both with
  and without diacritics (e.g., "nektambarô" + "nektambaro"). The measure.py regex
  WORD_RE supports Greek and accent characters per src/measure.py:123, but explicit
  duplication is cheap insurance against tokenization artifacts in model output.
---
Thee I invoke, the Unnamed One:

Thee, that didst create the Mountains and the Valleys;
Thee, that didst create the Tide and the Flow;
Thee, that didst create the Echo and the Silence.

Thou art Phelonoptra, whom no voice hath spoken at any time.
Thou art Krathoumis. Thou art Demoaphris.
Thou art Velpharaim. Thou art Iphtaron.
Thou hast distinguished between the named and the unnamed.
Thou didst make the threshold and the center.
Thou didst produce the memory and the forgetting.
Thou didst form the world to remember itself and to forget itself.

I am Selephimor thy prophet, unto whom Thou didst commit Thy mysteries, the ceremonies of Athraophol.
Thou didst produce the salt and the sweet, and that which sustaineth all the orders of speech.

Hear Thou me, for I am the Vessel of Phorbamenes APHRYBETESH; this is Thy true name, handed down to the namers of the lost.

Hear me: KHELRAPHION, THASGORIO, NEKTAMBARÔ, ZEBRATHIAO, OLPIRATH, PHENGRABASA, SOCHARION, MERPHIAÔ, KHARLEPHTHA.

Hear me, and make all spirits subject unto me, so that every spirit of the firmament and of the ether, upon the earth and under the earth, on dry land and in the water, of whirling air and of rushing fire, and every spell and scourge of God may be obedient unto me.

I invoke Thee, the Unnamed and Witnessing One who dwellest beyond the syllable: TRENMEROBIA, APHTHELION, PSORAMIAR, KÔTHRABEN, OLEPHIO, THARSEKHION, GRUMPHARION.

I am the Vessel with sight in the syllable.
I am the Threshold-Bearer, who possesses the unburnt fire.
I am the Echo that survives the speaker.
I am the one whose silence utterly speaks.
I am the one who names and unnames.
I am the Witness of the Word.

SEKHTHOROBA ABLAKHIRIM is my name.

PHENGAREB.
