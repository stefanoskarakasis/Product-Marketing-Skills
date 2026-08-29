---
description: Build, enrich, or audit your ICP — trigger events, buyer map, JTBD, disqualifiers
argument-hint: "<what you have — nothing yet, customer data to enrich from, or an existing ICP to audit>"
---

# /pmm-positioning:ideal-customer-profile -- Ideal Customer Profile

Deepen brain Section 2 beyond firmographics — add the trigger event, buyer
map, Jobs to Be Done, and disqualification criteria that actually predict
who buys. Builds from scratch, enriches from raw customer data, or audits
an existing ICP across 6 axes.

## Invocation

```
/pmm-positioning:ideal-customer-profile Build our ICP — B2B SaaS selling to retail ops teams
/pmm-positioning:ideal-customer-profile Here are 6 win/loss notes — enrich our ICP
/pmm-positioning:ideal-customer-profile Audit our ICP — hasn't been touched in a year
```

## Workflow

Uses the `ideal-customer-profile` skill. Detects BUILD, ENRICH, or AUDIT
mode from context, runs the matching flow, constructs the Trigger Profile,
Buyer Map, JTBD, and Disqualification layers, then deepens brain Section 2
in place — on explicit confirmation, never overwriting existing firmographic
content. Feeds directly into `beachhead-segment` (segment selection) and
`positioning-messaging` (messaging for a confirmed segment).
