---
description: Get a point of view and a 7-stage call plan for a discovery call: give it the prospect company and the title of who you are meeting, in Slack or anywhere else
argument-hint: "<prospect company and buyer title, plus optional minutes or notes: 'VP Finance at Tidewell Foods, 30 min', 'next call with Tidewell', or a pasted transcript>"
---

# /pmm-sales:discovery-call-prep -- Discovery Call Prep

Researches the account, builds a ranked point of view with one lead hypothesis and a fallback, and returns an opener, the questions to ask at each of seven stages sized to your call length, what good looks like, where you are different in the buyer's words and a fast-disqualify line. Reads your brain for your company, ICP, proof and rivals. Also preps follow-up discovery calls and calls on open deals, grades each plan from the outcome, and learns which signals and questions work. Read-only for your brain, CRM and inbox. Nothing is sent to a buyer.

## Invocation

```
/pmm-sales:discovery-call-prep VP Finance at Tidewell Foods
/pmm-sales:discovery-call-prep Head of RevOps at Northbeam, 45 min
/pmm-sales:discovery-call-prep Next call with Tidewell
/pmm-sales:discovery-call-prep Prep my call with Marlow at 3pm
/pmm-sales:discovery-call-prep log: confirmed
/pmm-sales:discovery-call-prep setup
```

In Slack, tag Claude in a thread: "@Claude prep my discovery call with the VP Finance at Tidewell Foods".

## Workflow

Uses the `discovery-call-prep` skill. Checks the CRM and calendar, reads the prospect record or researches lightly, reads what the sibling skills have learned, ranks the point of view, writes the plan, runs a 14-check gate, saves the plan beside your brain (or asks before using Google Drive), ends Slack on one plain question, grades the plan from the outcome, proposes what other skills should learn once enough plans agree, and logs the session.
