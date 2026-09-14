---
description: Define a North Star Metric and capped scorecard, or audit an existing metrics list for sprawl and vanity metrics
argument-hint: "<business context, or just say 'help me define what to measure'>"
---

# /pmm-growth:pmm-metrics -- PMM Metrics

Classify the business game, define a North Star Metric validated against
7 criteria, name 3-5 Input Metrics with a stated causal link and owner,
then build a capped scorecard (8-16 metrics) across Financial, Customer,
Product & GTM, and Process & Growth. Rejects revenue-shaped North Star
candidates and flags vanity metrics nobody can move.

## Invocation

```
/pmm-growth:pmm-metrics Help me define our North Star metric
/pmm-growth:pmm-metrics Build a scorecard for leadership reporting
/pmm-growth:pmm-metrics Our metrics list has 25 things and nobody updates it
```

## Workflow

Uses the `pmm-metrics` skill. Loads brain Sections 1/2 if present,
classifies the business game (Attention/Transaction/Productivity),
proposes and validates a North Star Metric against all 7 criteria
(rejecting revenue-shaped candidates by name), defines 3-5 Input Metrics
each with a causal link and named owner, builds a capped scorecard with
targets/weights/cadence, runs a sprawl and vanity-metric self-check, then
delivers the result in chat — this skill writes no output file, and
closes with a session log to `/context/skill-sessions.md`.

## Commands

- `/classify` — business game classification only
- `/north-star` — business game + NSM + Input Metrics, skip the scorecard
- `/scorecard` — scorecard only, assuming NSM/Input Metrics are already set
- `/audit` — pressure-test an existing metrics list for sprawl and vanity metrics
