---
description: Pull proof points from decks/battlecards, register, verify, or audit the claims your messaging relies on — then deepen brain Section 6 argument-hint: "<paste a deck/battlecard, a claim to add or verify, or 'audit my proof points'>"
---

# /pmm-positioning:proof-points -- Proof Points

Govern the evidentiary foundation of every claim your GTM copy makes —
what's approved, what needs a source, and what's forbidden and why. Mines
claim candidates out of existing sales decks, battlecards, and case
studies, adds a new claim directly, checks one before it ships, or audits
the existing registry for gaps. Deepens brain Section 6 in place, on
confirmation.

## Invocation

```
/pmm-positioning:proof-points Pull proof points out of this battlecard: [paste]
/pmm-positioning:proof-points Add: 89% retention rate, from our Q4 earnings
/pmm-positioning:proof-points Can I say "industry-leading" in this deck?
/pmm-positioning:proof-points Audit our proof points — anything stale or unsourced?
```

## Workflow

Uses the `proof-points` skill. Loads brain Section 6 (current registry,
however thin) if present, classifies the request as Extract / Add / Verify
/ Audit. Extract mode mines claim-shaped statements out of pasted decks or
battlecards — every candidate starts flagged `[NEEDS PROOF]`, even if the
source material cites its own source, since decks go stale. Add mode
requires a source for a directly-supplied claim (unsourced claims are
flagged, never silently approved) and documented approval-to-use for
every named customer quote. Then deepens brain Section 6 with the result
— showing the exact before/after first, writing only on confirmation.
Closes with a session log to `/context/skill-sessions.md`.
