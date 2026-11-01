---
description: Sweep your core competitors' public pages and get a one-screen brief with the fix for each item already drafted
argument-hint: "<setup, run the sweep, do N, status, or a competitor to add or swap>"
---

# /pmm-competitive-intelligence:media-monitoring -- Media Monitoring

Reads the public pages of your 3 to 5 core competitors, triages what
changed into at most three items that need you, and drafts the fix for each:
a battlecard patch, a note for the CRO, a re-test list. One person runs it
with a named backup; the team reads the Slack post and the Doc. Nothing is
changed or sent without your go. It says what it could not see, saves its
records to `/context/monitoring/` and never writes the brain.

## Invocation

```
/pmm-competitive-intelligence:media-monitoring Set up media monitoring for our five competitors
/pmm-competitive-intelligence:media-monitoring Run the weekly competitor sweep
/pmm-competitive-intelligence:media-monitoring do 1
/pmm-competitive-intelligence:media-monitoring Monitor status
/pmm-competitive-intelligence:media-monitoring We missed this: [competitor] changed its pricing page
/pmm-competitive-intelligence:media-monitoring Run the monthly review
```

## Workflow

Uses the `media-monitoring` skill. Loads the brain (or asks three quick
questions and holds the answers for the session), reads the watchlist, and
states the cost of the run before it reads anything. Setup asks five
questions, requires an executor and a named backup, and shows a channel
preflight. A sweep tries a connector, then built-in search, then a
logged-out browser, then asks for a paste, and records each step. It
triages by source tier, drafts an action card for each item that needs you,
checks last week's actions, builds the brief, runs a 13-check gate on its
own work and saves the records. `do N`, `go`, `edit`, `skip` and `post` act
on a card; only the executor or backup can approve.

A first run sets the baseline and says so. A quiet week gets a short
brief, not a skipped week. To run it every Monday, see
`skills/media-monitoring/references/setup.md`, section 6.
