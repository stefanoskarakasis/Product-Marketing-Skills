---
description: Set up your market and a roster of up to five competitors, each with a dated, sourced profile
argument-hint: "<optional: a competitor, or 'setup', 'status', 'review'>"
---

# /pmm-competitive-intelligence:competitive-profile -- Competitive Profile

Confirms the market you play in, fixes a roster of five competitors from brain Section 3, builds a dated and sourced profile for each, and shows what is stale. Saves records to `/context/competitor-profiles/` and, if you confirm, appends a roster note to brain Section 3.

## Invocation

```
/pmm-competitive-intelligence:competitive-profile Set up my competitive profiles
/pmm-competitive-intelligence:competitive-profile Who are my five key competitors, and what's stale?
/pmm-competitive-intelligence:competitive-profile Review the proposed brain note
```

## Workflow

Uses the `competitive-profile` skill. Loads the brain (or asks five quick questions), picks the mode, checks your own side against the market, builds or refreshes profiles with evidence tags and dates, runs an 8-check gate, saves the records, offers a brain note for you to confirm, proposes a weekly scheduled refresh once, and logs the session.
