---
description: Set up your market and a roster of up to five competitors, each with a dated, sourced profile, or ask a question about one
argument-hint: "<optional: a competitor, 'setup', 'status', 'review', or a question about a competitor>"
---

# /pmm-competitive-intelligence:competitive-profile -- Competitive Profile

Confirms the market you play in, fixes a roster of five competitors from brain Section 3, builds a dated and sourced profile for each, and shows what is stale. Saves records to `/context/competitor-profiles/` and, if you confirm, appends a roster note to brain Section 3. Given a question about a named competitor, it answers from every CI record you hold, then deal data, then the public web, with dated sources (the same answer a teammate gets by tagging Claude in Slack).

## Invocation

```
/pmm-competitive-intelligence:competitive-profile Set up my competitive profiles
/pmm-competitive-intelligence:competitive-profile Who are my five key competitors, and what's stale?
/pmm-competitive-intelligence:competitive-profile Review the proposed brain note
/pmm-competitive-intelligence:competitive-profile What do we say against Stripe on pricing?
/pmm-competitive-intelligence:competitive-profile Update the profile: Stripe cut its entry plan to $19 per seat
```

## Workflow

Uses the `competitive-profile` skill. Loads the brain (or asks five quick questions), picks the mode, checks your own side against the market, builds or refreshes profiles with evidence tags and dates, runs an 8-check gate, saves the records, offers a brain note for you to confirm, proposes a weekly scheduled refresh once, and logs the session. Given a question, it runs in `ask` mode instead: it reads every CI record for the competitor, goes on to deal data and the public web only if it must, answers briefly with sources, and logs anything it could not answer.
