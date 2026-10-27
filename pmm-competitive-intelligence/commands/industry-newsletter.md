---
description: Build the weekly industry newsletter on your competitors and industry for GTM leaders, formatted for Google Doc, email or Slack
argument-hint: "<category and regions, plus the platform, e.g. fintech EMEA, Slack>"
---

# /pmm-competitive-intelligence:industry-newsletter -- Industry Newsletter

Builds the weekly industry newsletter on your competitors and your industry
for GTM leaders in one locked layout: a one-sentence verdict, numbered
competitor tables with 3 to 5 product updates (impact, horizon and a
pipeline implication each), industry changes, a pricing watch, one decision
question, role-owned actions and a sources list. Every claim carries a link.
It asks once where the issue will be read (Google Doc, email or Slack) and
formats for that. Each issue grades the last call and carries open signals
forward. Saves the issue and its loop files to `/context/industry-newsletter/`.
Never writes the brain.

## Invocation

```
/pmm-competitive-intelligence:industry-newsletter Fintech EMEA, Google Doc
/pmm-competitive-intelligence:industry-newsletter Weekly market and pricing watch for our GTM leaders
/pmm-competitive-intelligence:industry-newsletter industry newsletter in Slack, post it in #ci-fintech
/pmm-competitive-intelligence:industry-newsletter Grade the last newsletter call and show what we are still watching
```

## Workflow

Uses the `industry-newsletter` skill. Loads the brain (or asks three quick
questions and holds the answers for the session), your other CI skills'
records (profiles, battlecards, deep-dives, signals), the stores from earlier
issues, and what your connected tools hold: the Slack channel, Gong themes,
Klue cards and the Drive folder. Those are leads: only a public page makes a
claim. It asks once, in one message, for the platform, the category, the
regions and the team that owns the content, and saves the answers; a
scheduled run never asks. Before it researches, it grades the last call,
rolls the watchlist and reads the feedback. It then reads public sources
for the period, checks your forbidden claims and how each item was
collected, builds the issue in the fixed order, runs a 22-check gate on its
own work, saves the record and logs the session. Anything it could not
verify stays out of the document and is listed in the chat for you.

A Google Doc issue has 5-column competitor tables; email has 4 columns; Slack
is a single post of about 220 words with no tables. A quiet week gets a short
issue, never a skipped one. To run it every Monday, see
`skills/industry-newsletter/references/issue-format.md`, section 11.
