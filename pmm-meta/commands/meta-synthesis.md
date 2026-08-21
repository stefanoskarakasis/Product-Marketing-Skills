---
description: Detect cross-skill patterns and propose brain updates
argument-hint: "<optional: specific skills or timeframe to synthesize>"
---

# /pmm-meta:meta-synthesis -- Pattern Synthesis

Detect patterns across multiple skills' session logs and propose
updates to the shared brain — the mechanism that makes the whole system
compound over time instead of resetting every session.

## Invocation

```
/pmm-meta:meta-synthesis
/pmm-meta:meta-synthesis Focus on the last month of retro and pre-mortem
sessions
```

## Workflow

Uses the `meta-synthesis` skill. Reads recent session logs across
skills, looks for recurring signals, and proposes specific, named brain
updates for approval before writing anything.
