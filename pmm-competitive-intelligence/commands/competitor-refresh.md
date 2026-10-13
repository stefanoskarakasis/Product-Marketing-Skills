---
description: Refresh only the stale lines of one competitor profile or the whole roster, and leave unchanged lines with their original dates
argument-hint: "<optional: competitor name>"
---

# /pmm-competitive-intelligence:competitor-refresh -- Competitor Refresh

Compares each profile line with its freshness window (pricing 60 days, product and positioning 90, buyer 180) and re-reads only what is past due or named in a signal. Writes a new dated record and never overwrites the old one.

## Invocation

```
/pmm-competitive-intelligence:competitor-refresh
/pmm-competitive-intelligence:competitor-refresh Stripe
/pmm-competitive-intelligence:competitor-refresh Fold this week's signals into the profiles
```

## Workflow

Uses the `competitive-profile` skill in `refresh` mode (or `intake` when you name signals, battlecards or deal data). Delta only: unchanged lines are carried forward with their original date. Runs read-only for the brain. If you have not set up a schedule yet, it proposes one.
