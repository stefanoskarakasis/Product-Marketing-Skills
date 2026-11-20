---
description: Paste a discovery call you already ran and get it scored across the seven stages, replayed and coached, in Slack or anywhere else
argument-hint: "<a pasted transcript, a file, or 'my call with Tidewell'; optional buyer title and call number>"
---

# /pmm-sales:discovery-call-scoring -- Discovery Call Scoring

Scores a finished discovery call across the seven stages, names the pattern, replays the moments that cost you and gives two to four moves with the words to say. Compares against your call plan when one exists and shows your trend across calls. Private to you: it never goes to a manager. Reads your brain; never writes it, a CRM or an inbox. Nothing is sent to a buyer.

## Invocation

```
/pmm-sales:discovery-call-scoring [paste transcript]
/pmm-sales:discovery-call-scoring My call with Tidewell
/pmm-sales:discovery-call-scoring Am I getting better?
```

In Slack, tag Claude in a thread and paste the transcript: "@Claude score this discovery call".

## Workflow

Uses the `discovery-call-scoring` skill. Reads the transcript, the plan and your earlier reviews, scores seven stages, names the pattern, finds the moments that cost you, writes the card or full review, runs the Quality Gate, saves your own file, ends Slack on one plain question, proposes what other skills should learn once enough reviews agree, and logs the session.
