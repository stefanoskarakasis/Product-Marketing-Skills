---
description: Build a long-form, sourced deep-dive on one competitor for a named decision, with deal evidence, reviews, head-to-head per offering and where they win
argument-hint: "<competitor, plus the decision it supports: pricing change, RFP, strategy call, roadmap bet>"
---

# /pmm-competitive-intelligence:competitor-deep-dive -- Competitor Deep-Dive

Builds the long, sourced view of one competitor that sits behind a decision:
what they sell and what it costs, recent moves, deal evidence, what reviewers
say, a head-to-head against each of your offerings, and where they genuinely
win. Tests what your brain believes against fresh evidence. Saves the record
to `/context/deep-dives/` and, if you confirm, appends field notes to brain
Section 3.

## Invocation

```
/pmm-competitive-intelligence:competitor-deep-dive Deep-dive on [competitor]
/pmm-competitive-intelligence:competitor-deep-dive [Competitor] for our pricing review, audience is the exec team
/pmm-competitive-intelligence:competitor-deep-dive What do users really say about [competitor]?
/pmm-competitive-intelligence:competitor-deep-dive Refresh the [competitor] deep-dive
```

## Workflow

Uses the `competitor-deep-dive` skill. Loads the brain (or asks four quick
questions and holds the answers for the session), checks which deal and
pricing tools are connected and asks once whether to connect, paste or skip,
names its sources, checks your forbidden claims and prohibited items before
writing a line, builds the document, runs a 14-check gate on its own work,
saves the record, offers a brain note for you to confirm, and logs the
session.
