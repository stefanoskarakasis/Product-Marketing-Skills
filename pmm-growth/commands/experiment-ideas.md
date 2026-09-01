---
description: Generate several concrete, brain-grounded growth ideas — channel, message, rationale, cost-efficiency — ranked by effort vs. impact
argument-hint: "<product/launch context, or just say 'give me growth ideas'>"
---

# /pmm-growth:experiment-ideas -- Experiment Ideas

Generate a ranked list of concrete growth ideas — not generic tactics —
grounded in your brain's ICP, alternatives, and market context. Each idea
gets a channel, a core message, why it works for this specific ICP, and
a concrete cost-efficiency reason. Hands off explicitly to
`experiment-doc` for whichever idea is worth pressure-testing.

## Invocation

```
/pmm-growth:experiment-ideas Give me 5 ideas for our Q4 launch
/pmm-growth:experiment-ideas We have almost no budget — what should we try?
/pmm-growth:experiment-ideas Brainstorm growth tactics that beat [named alternative]
```

## Workflow

Uses the `experiment-ideas` skill. Loads brain Sections 1/2/3/5 if
present, asks for budget/resource constraints and channels already
tried, generates the requested number of ideas (default 5) each with
Channel/Core Message/Why It Works/Cost Efficiency, self-checks every idea
against named alternatives — flagging anything indistinguishable from
what a status-quo competitor already says — ranks by effort vs. impact,
then closes with an explicit handoff naming which idea(s) are strong
enough for `experiment-doc` and a session log to
`/context/skill-sessions.md`.
