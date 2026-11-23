---
description: Get the state of your open pipeline or your team's: what changed, the deals that need a move this week, the CRM fields to fix and a draft DM for each missing field, from your CRM or a CSV
argument-hint: "<optional: 'team', 'hygiene', 'forecast', 'since 16 Nov', or a question about the pipeline>"
---

# /pmm-sales:pipeline-digest -- Pipeline Digest

Reads the open deals of one seller or a whole team and gives you one digest in plain words: what changed since last week, which deals are quiet, slow or past due, the CRM fields to fix and up to five deals to act on, each with one action and one date. It lists deals, never sellers. A field it needs and cannot find becomes a question, and for each deal owner it drafts a DM that waits for your yes. It also prepares a forecast call. It reads your brain and writes none of it.

## Invocation

```
/pmm-sales:pipeline-digest
/pmm-sales:pipeline-digest team
/pmm-sales:pipeline-digest Which deals are stuck?
/pmm-sales:pipeline-digest hygiene
/pmm-sales:pipeline-digest Prep my forecast call
/pmm-sales:pipeline-digest since 16 Nov
/pmm-sales:pipeline-digest log: lost: no budget, Marlow
```

In Slack, tag Claude in a thread: "@Claude pipeline digest".

## Workflow

Uses the `pipeline-digest` skill. Picks the scope, loads the brain and the last digest, reads the open deals from your CRM or a CSV, runs the five checks, asks for any missing field instead of guessing it, ranks up to five deals, writes a card for Slack and a full digest, runs a 13-check gate, saves the digest beside your brain (or asks before using Google Drive), logs gaps and patterns, proposes what other skills should learn once enough deals agree, and logs the session. Read-only for your brain, CRM and inbox. Nothing is sent without a yes that names it. For one deal, use `deal-review`.
