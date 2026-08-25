---
description: Score and select a GTM motion stack against real deal economics, not a taxonomy tour
argument-hint: "<segment or initiative, ACV/deal size, sales-cycle length>"
---

# /pmm-go-to-market:gtm-motions -- GTM Motions

Score the 7 acquisition motions (Inbound, Outbound, Paid Digital,
Community, Partner, ABM, PLG) against your ICP's deal economics, apply
blocking gates, and select a stack — one primary motion, at most one
secondary, with named rejection reasons for the rest.

## Invocation

```
/pmm-go-to-market:gtm-motions Mid-market fintech segment, ~$8K ACV, 45-day sales cycle
/pmm-go-to-market:gtm-motions Should we go PLG or sales-led for this launch?
```

## Workflow

Uses the `gtm-motions` skill. Loads brain context and any confirmed
beachhead, scores all 7 motions on deal-economics fit, buyer
reachability, team/tool readiness, and time-to-signal, applies hard
gates (ACV floors, self-serve capability, team capacity), then outputs
a motion stack with a 90-day activation plan and numeric kill criteria.
Feeds directly into `go-to-market-strategy`'s Channel Strategy section.
