---
description: Show the freshness board for your competitor profiles — what is stale, changed or unproven
argument-hint: "<none>"
---

# /pmm-competitive-intelligence:profile-status -- Profile Status

Prints one table for your roster: last profile date, stale lines, oldest line, what changed and open proof items, with a single next action.

## Invocation

```
/pmm-competitive-intelligence:profile-status
/pmm-competitive-intelligence:profile-status What's stale?
```

## Workflow

Uses the `competitive-profile` skill in `status` mode. Reads only; saves a status record and logs the session. In Slack the board is posted as bullets, and the weekly run posts it to your board channel.
