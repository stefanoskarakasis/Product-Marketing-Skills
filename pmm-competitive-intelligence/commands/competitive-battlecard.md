---
description: Build a one-page competitor battlecard for a live deal — tailored to role, motion, buyer persona and stage
argument-hint: "<competitor, plus anything you know: your role, the buyer, the stage, what they said>"
---

# /pmm-competitive-intelligence:competitive-battlecard -- Competitive Battlecard

Builds one page a seller can skim in 60 seconds before a call and quote
during it: a win condition, what to say first, a five-row snapshot, the
questions to ask, replies to what the buyer will say, when to lean in and
when to walk away, and the proof you are allowed to use. Saves the card to
`/context/battlecards/` and, if you confirm, appends field notes to brain
Section 3.

## Invocation

```
/pmm-competitive-intelligence:competitive-battlecard Battlecard for [competitor]
/pmm-competitive-intelligence:competitive-battlecard [Competitor] is the incumbent, I am an AE talking to their CFO in evaluation
/pmm-competitive-intelligence:competitive-battlecard They say we are more expensive. What do I say?
/pmm-competitive-intelligence:competitive-battlecard Refresh the [competitor] card
/pmm-competitive-intelligence:competitive-battlecard Set of cards for my roster
/pmm-competitive-intelligence:competitive-battlecard We lost to [competitor]; the price reply did not land
```

## Workflow

Uses the `competitive-battlecard` skill. Loads the brain (or asks five quick
questions and holds the answers for the session), asks once for the deal
context and the delivery format (Google Doc or HTML), names its sources,
checks your forbidden claims and prohibited items before writing a line,
builds the card, runs a 12-check gate on its own work, saves the record,
offers a brain note for you to confirm, and logs the session. Each card shows
the competitor's roster tier and a re-check date. "Set of cards" lists your
saved cards by tier and rebuilds nothing. Telling it how a deal ended adds one
row to an outcome log; two or more outcomes appear on the next card.
