---
description: Kick off, interview for, draft, send for customer review or audit a B2B customer story in one fixed structure, with stats and named quotes checked
argument-hint: "<customer name, interview notes, or a finished story to audit>"
---

# /pmm-growth:customer-stories -- Customer Stories

Run a customer story from kickoff to customer approval in a fixed seven-block
structure. You pick the depth (short, standard, deep) and the angle; the skill
finds the tension, asks who does what instead of assuming, refuses to invent
evidence, and runs an 8-point gate before handing the draft over. Also writes
the internal brief, the interview questions, the customer review pack, and
audits a finished story.

## Invocation

```
/pmm-growth:customer-stories We want a story on Harbor & Pine. Start the kickoff
/pmm-growth:customer-stories I have a call with Harbor & Pine on Thursday
/pmm-growth:customer-stories Write a short story from these notes: [paste]
/pmm-growth:customer-stories Prepare the review pack for Harbor & Pine
/pmm-growth:customer-stories Audit this case study our agency sent: [paste]
```

## Workflow

Uses the `customer-stories` skill. Loads brain Sections 2, 3, 4 and 6 if
present, loads the story ledger and the story's stage, asks you for the names
and departments of the people involved (never assumes them), runs kickoff and
drafts the internal brief in the format you choose, picks Interview, Draft,
Review pack or Audit from what you paste, builds a packet of stats and quotes with every missing field
flagged, asks you to choose depth, proposes two or three angles with their
tension, drafts in the fixed structure with placeholders for any gap, runs
the 8-check gate on its own draft, saves the packet with its stage and next action to
`/context/customer-stories.md`, offers to hand confirmed claims to
`proof-points`, and closes with a session log to `/context/skill-sessions.md`.

## Commands

- `/kickoff` — the six kickoff questions and the internal brief
- `/interview` — the question list for a customer call
- `/draft` — packet, depth, angle and draft from notes
- `/review-pack` — cover note, checklist and asset list for the customer
- `/audit` — gate check and ranked fixes for a finished story
