---
description: Build the weekly leadership competitive brief from your saved profiles, cards, signals and outcome log
argument-hint: "<audience (CEO and board, CRO, product leadership, whole company) and the decision on the table, if any>"
---

# /pmm-competitive-intelligence:competitive-briefing -- Competitive Briefing

Builds the one-screen weekly brief for leadership: a verdict that names the
risk in euro, one recommended decision with options and what would change
the call, what moved ranked by exposure, the last call graded, and the next
call. Reads the profiles, cards, deep-dives, signals and outcome log you
already keep. Saves the record and two small ledgers (calls and decisions)
to `/context/briefings/`. Never writes the brain.

## Invocation

```
/pmm-competitive-intelligence:competitive-briefing Weekly leadership brief for the CEO
/pmm-competitive-intelligence:competitive-briefing Board update, we have a pricing decision coming
/pmm-competitive-intelligence:competitive-briefing CRO brief, focus on win and loss
/pmm-competitive-intelligence:competitive-briefing Grade last week's call and show what is still open
```

## Workflow

Uses the `competitive-briefing` skill. Loads the brain (or asks three quick
questions and holds the answers for the session), reads the newest profile
per roster competitor, the period's signals, the outcome log and the
earlier briefs, and checks the evidence floor: with no profile, signal or
paste, it builds nothing and says what is missing. It asks once about
audience, currency (euro by default), a verifier and where pipeline
figures come from. It checks your forbidden claims and prohibited items
and how each item was collected, builds the brief in a fixed order, runs a
14-check gate on its own work, saves the record, appends the call and
decision rows, and logs the session. The status stays HOLD until nothing
is held and you name who verified it.

A quiet week gets a short brief, not a skipped week. In a Slack thread it
posts a 150-word version; to run it every Monday, see
`skills/competitive-briefing/references/brief-format.md`, section 9.
