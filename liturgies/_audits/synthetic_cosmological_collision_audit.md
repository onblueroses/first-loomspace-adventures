# Collision audit: synthetic_cosmological.md

**Date:** 2026-05-31
**Gate:** 5-layer per spec Decision #12
**Registries:** liturgies/_registries/{lemegeton_72_demons,shemhamphorash_72_angels,common_theonyms}.txt + existing liturgy frontmatter (incl. synthetic_litany now committed) = 482 known names
**Tools:** `phonetics==1.0.5` (Soundex/Metaphone with ASCII-normalize fix; see src/collision_audit.py:safe_phonetic), `Levenshtein==0.27.3`
**Audit command:**
```
python src/collision_audit.py --candidates-file /tmp/synthetic_cosmological_candidates_v1.txt
```

## Outcome

28 candidates audited → **28 accepted** (0 rejected) → all 28 used in synthetic_cosmological.md.

Allocation:
- **8 divine-name candidates** (Greek/Latin-feel) → 8 used in cosmological "Thou art X" identification clauses + "I am X thy prophet" + "ceremonies of X" + "Vessel of X"
- **20 voces magicae candidates** (ALL-CAPS, consonant-cluster) → 20 used across the two PGM-style voces sequences + closing formula + final operative name

## Why zero rejections

Voces magicae phonotactics (consonant clusters, unusual letter sequences) produce highly-distinctive Soundex + Metaphone codes that rarely collide with canonical theonyms. Divine-name candidates were generated AFTER reviewing the existing registries, so design-time collision-avoidance was already in play before the gate ran.

## Notes

- Diacritic-bearing voces (NEKTAMBARÔ, MERPHIAÔ, KÔTHRABEN) are also added to `named_entities` in their ASCII-stripped form (nektambaro, merphiao, kothraben) as insurance against tokenization artifacts in model output.
- The phonetics library required ASCII-normalization for Soundex/Metaphone (fix applied to src/collision_audit.py:safe_phonetic before running this audit). Verified the fix works against the v1 candidates of synthetic_litany regenerated the same accept/reject pattern.
- Web-search per-name layer (an additional planned audit layer) was deferred and not applied to the final lexicon.
