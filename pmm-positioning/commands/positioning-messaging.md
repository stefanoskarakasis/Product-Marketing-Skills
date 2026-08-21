---
description: Build or audit positioning statements, messaging, and related output
argument-hint: "<what you need — a positioning statement, messaging audit, deck, sales cards, or homepage copy>"
---

# /pmm-positioning:positioning-messaging -- Positioning & Messaging

Build or audit positioning using the full Dunford sequence. Supports
five output modes — say what you need and the right mode runs
automatically:

- A new positioning statement and messaging hierarchy → **build**
- A score and rewrite queue for existing messaging → **audit**
- An internal positioning deck → **fletch**
- Sales persona cards and a competitive response guide → **sales-enablement**
- Production-ready homepage copy → **homepage**

## Invocation

```
/pmm-positioning:positioning-messaging Build positioning for our new tier
/pmm-positioning:positioning-messaging Audit our current homepage copy
/pmm-positioning:positioning-messaging I need sales cards for this competitor
```

## Workflow

Uses the `positioning-messaging` skill. Detects which of the five modes
fits the request, refuses to run without a named primary persona and at
least three alternatives (including status quo), and blocks output
until a 7-point self-verification gate passes.
