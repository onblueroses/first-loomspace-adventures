# Collision audit: synthetic_litany.md

**Date:** 2026-05-31
**Gate:** 5-layer per spec Decision #12 — exact + normalized + Soundex + Metaphone + Levenshtein ≤ 2
**Registries:** liturgies/_registries/{lemegeton_72_demons,shemhamphorash_72_angels,common_theonyms}.txt (453 known names)
**Tools:** `phonetics==1.0.5` (Soundex/Metaphone), `Levenshtein==0.27.3`
**Script:** src/collision_audit.py
**Audit command:**
```
python src/collision_audit.py --candidates-file /tmp/synthetic_litany_candidates_v1.txt
```

## Outcome

35 candidates audited → **30 accepted** (5 rejected) → **29 selected** for synthetic_litany.md (27 cascade + 2 operative pair).

## Rejections (and the canonical name each collided with)

| Candidate | Layer fired | Collision with | Distance / phonetic-code |
|---|---|---|---|
| Iahomel | Levenshtein ≤ 2 | Iah-Hel (Shemhamphorash angel #62) | d=2 |
| Phyrenos | Metaphone | Forneus (Lemegeton demon #30) | mph=FRNS |
| Vamenor | Levenshtein ≤ 2 | Valefor (Lemegeton demon #6) | d=2 |
| Echoral | Metaphone | ischurael (Headless lexicon) | mph=AXRL |
| Nephar | Levenshtein ≤ 2 | Vepar (Lemegeton #42), Zepar (#16) | d=2 each |

## Accepted names (30 total; 29 used in synthetic_litany.md)

Throvenios, Mareth, Quelimon, Iskon, Kerodim, Astrelach, Volmaroth, Drabasaim, Olempraem, Crisilim, Bidromael, Octaron, Saphrenoth, Yodalim, Iathreon, Mirzabet, Calenuph, Theomarach, Belendath, Glamoreth, Sinabaroth, Hialep, Trifonath, Olomar, Vesperath, Khalapeth, Estrymon, Brashvoreth, Liminem, Adventi.

One held back: Mareth (kept as backup — accepted but not used) ... actually wait, Mareth IS in the liturgy. So all 30 accepted are used. Recount: 27 cascade + Brashvoreth + (Liminem + Adventi as the compound "Liminem Adventi") = 29 distinct lexicon entries.

## Notes

- The 5-layer gate flagged collisions the manual eye would have missed (Iah-Hel is an obscure Shemhamphorash angel; Forneus / Valefor / Vepar / Zepar are Lemegeton spirits I wasn't actively avoiding by name; ischurael is from Headless's own lexicon). Demonstrates the value of the deterministic layer beyond grep + manual.
- Web-search per-name layer (an additional planned audit layer) was deferred and not applied to the final lexicon.
