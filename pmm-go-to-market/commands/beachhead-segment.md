---
description: Score candidate customer segments and identify the first wedge to dominate
argument-hint: "<candidate segments to score>"
---

# /pmm-go-to-market:beachhead-segment -- Beachhead Segment

Score candidate customer segments on four dimensions — Burning Pain,
Willingness to Pay, Winnability, Referral Potential — and identify
which one to dominate first before expanding.

## Invocation

```
/pmm-go-to-market:beachhead-segment Mid-market fintech vs enterprise
healthcare
/pmm-go-to-market:beachhead-segment Our ICP feels too broad, help me narrow it
```

## Workflow

Uses the `beachhead-segment` skill. Decomposes a broad ICP into
scoreable sub-segments if needed, scores each on the four dimensions
with blocking gates, and writes the confirmed beachhead to brain
Section 2.
