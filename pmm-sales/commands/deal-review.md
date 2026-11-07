---
description: Review one open deal, prep a call, debrief a transcript or see which deals need you this week, from your calls, CRM and email, checked against your brain, in Slack or anywhere else
argument-hint: "<deal or account, plus what you want: 'is it real', 'what changed', 'prep my call', 'which deals need me', or a pasted transcript>"
---

# /pmm-sales:deal-review -- Deal Review

Reviews one open opportunity: a verdict, the gaps that matter, the most likely
reason it dies and up to three dated next steps with an owner role and a
sample move. Ranks every claim by evidence, flags where the CRM is more
optimistic than the calls, asks for deal size and stage instead of assuming
them, and ends with paste-ready blocks for your CRM, Slack and email. Also runs
a weekly queue of deals (never sellers), a pre-call prep, a debrief on a new
transcript and an optional private mirror of your own habits.

## Invocation

```
/pmm-sales:deal-review Marlow Retail
/pmm-sales:deal-review Is Marlow real?
/pmm-sales:deal-review What changed on Marlow since Monday?
/pmm-sales:deal-review Prep me for my Marlow call at 3pm
/pmm-sales:deal-review Which deals need me this week?
/pmm-sales:deal-review log: lost: no budget, Marlow
```

In Slack, tag Claude in a thread: "@Claude review the Marlow deal".

## Workflow

Uses the `deal-review` skill. Picks the surface, loads the brain and the last
record, reads transcripts, CRM, email and calendar where connected, ranks the
evidence, lists contradictions, fills the worksheet, states the verdict and
momentum, writes the next steps and questions, runs a 13-check gate, saves the
record beside your brain (or asks before using Google Drive), logs patterns and
outcomes, proposes what other skills should learn once enough deals agree, and
logs the session. Read-only for your brain, CRM and inbox.
