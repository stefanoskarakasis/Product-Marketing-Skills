---
description: Map the buying committee, then build alternatives-anchored messaging personas
argument-hint: "<segment or deal context — research data if you have it, otherwise just describe the buyer>"
---

# /pmm-positioning:buyer-personas -- Buyer Personas

Map who's actually in the room for a B2B purchase — Economic Buyer,
Champion, Technical Evaluator, End User, Procurement — before building a
single message. Produces a Buying Committee Map and Dunford-structured
persona cards ready to hand to `positioning-messaging`.

## Invocation

```
/pmm-positioning:buyer-personas Map our buying committee for enterprise deals
/pmm-positioning:buyer-personas Here are 4 call transcripts — build our personas
/pmm-positioning:buyer-personas Our deals keep stalling in legal, who's involved?
```

## Workflow

Uses the `buyer-personas` skill. Loads brain ICP and alternatives if
present, gathers research data or runs a 5-question intake if none is
provided, maps the committee by behavior rather than title, applies a
quality gate (at least one Economic Buyer and Champion, named
alternatives present), then builds one persona card per role needing
differentiated messaging. Hands off directly to `positioning-messaging`
with the primary persona and any still-unvalidated claims flagged.
