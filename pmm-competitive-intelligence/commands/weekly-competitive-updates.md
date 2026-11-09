---
description: Build the weekly C-suite competitor update from public sources, with this week's threat board compared to last week's
argument-hint: "<the company, markets and who the update is for, or 'run it'>"
---

# /pmm-competitive-intelligence:weekly-competitive-updates -- Weekly Competitive Updates

Sweeps the public sources for your competitors over the last 7 days and writes
the C-suite update in one fixed order: executive summary, recommended
decisions, data-backed takeaways with fact and interpretation kept apart, a
threat board, a 30-day watchlist and the dated detail per competitor. Every
item carries its date and an inline link. It saves each edition, so the
threat board shows what changed since last week. Public sources only; no
owners; never writes the brain.

## Invocation

```
/pmm-competitive-intelligence:weekly-competitive-updates Run the weekly competitive updates
/pmm-competitive-intelligence:weekly-competitive-updates Weekly competitor update for the C-suite, Germany only
/pmm-competitive-intelligence:weekly-competitive-updates Executive competitor news this week, for Sales
/pmm-competitive-intelligence:weekly-competitive-updates What changed since the last edition?
```

## Workflow

Uses the `weekly-competitive-updates` skill. Loads the brain (or asks a few
setup questions and holds the answers), reads your last edition, threat
ledger and open watchlist, and confirms who the update is prepared for. A
saved identity is shown for a one-line confirmation; it is never assumed.
States the cost of the run, checks your forbidden claims and prohibited
items, sweeps the window, keeps only dated items with a link retrieved this
run, and builds the update. A week with no news is a short update, not a
padded one. It runs a 14-check gate on its own work, saves the edition and
the ledger rows to `/context/weekly-updates/`, and logs the session.

To run it every Monday, see `skills/weekly-competitive-updates/references/update-format.md`, section 6.
