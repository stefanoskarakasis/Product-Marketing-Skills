---
description: Score and rank initiatives using a GTM-native prioritization framework
argument-hint: "<list of initiatives to score>"
---

# /pmm-execution:prioritize -- Prioritization

Score and rank a set of initiatives using whichever prioritization
framework fits the decision — RICE, ICE, and seven other GTM-specific
frameworks.

## Invocation

```
/pmm-execution:prioritize Rank these 5 Q3 launch candidates
/pmm-execution:prioritize Should this be a T1 or T2 launch?
```

## Workflow

Uses the `prioritization-frameworks` skill. Recommends the right
framework for the decision type, walks through scoring each initiative,
and produces a ranked list with the reasoning shown for each score.
