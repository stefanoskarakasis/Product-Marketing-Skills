---
description: Check which five competitors really show up in your deals and propose a swap, never forcing one
argument-hint: "<optional: 'last quarter' or a CRM name>"
---

# /pmm-competitive-intelligence:competitor-roster -- Competitor Roster

Counts competitor appearances in your deals over the last 90 days (CRM competitor field, or your own list) and proposes promoting or demoting competitors. The roster stays at five, and nothing changes until you confirm.

## Invocation

```
/pmm-competitive-intelligence:competitor-roster
/pmm-competitive-intelligence:competitor-roster Review my roster against last quarter's deals
```

## Workflow

Uses the `competitive-profile` skill in `roster` mode (v2). Shows the cost of each swap (a new profile to build, an old one frozen at its last date). Without a connected CRM the count is marked as recollection.
