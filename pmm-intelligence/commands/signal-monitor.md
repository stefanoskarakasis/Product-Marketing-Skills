---
description: Turn this week's signals into at most five opportunities tied to your brain and your quarterly priorities
argument-hint: "<signals you name: competitor pages, pasted news, win/loss notes, or 'use my connectors'>"
---

# /pmm-intelligence:signal-monitor -- Signal Monitor

Takes the signals you name and returns at most five opportunities. Each
opportunity carries its evidence, the brain field it touches, the Section 7
priority it serves, a confidence label and one suggested next move. Saves the
list to `/context/signals/YYYY-MM-DD.md`. Read-only for your brain.

## Invocation

```
/pmm-intelligence:signal-monitor Here is what changed on two competitor pricing pages: [paste]
/pmm-intelligence:signal-monitor Use my connectors for this week's search and traffic shifts
/pmm-intelligence:signal-monitor Win/loss notes from the last 10 deals: [paste]
```

## Workflow

Uses the `signal-monitor` skill. Loads brain Sections 3, 7 and 2 if present
(or asks three quick questions and holds the answers for the session),
reads only the sources you name in this run, tags each signal with its source
and date, drops anything that touches no brain field, ranks what is left
against your Section 7 priorities, runs a 6-check gate on its own list, saves
the list, and logs the session.
