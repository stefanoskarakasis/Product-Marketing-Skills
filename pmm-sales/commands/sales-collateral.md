---
description: Build a one-pager, demo script, proposal, ROI calculator, deck outline or win-loss analysis from your brain, or get sent to the skill that owns the asset you asked for
argument-hint: "<the asset and who it is for: 'one-pager for the CFO champion at Tidewell', 'demo script, 30 min, VP Finance', 'proposal for Marlow', 'why do we lose mid-market deals?'>"
---

# /pmm-sales:sales-collateral -- Sales Collateral

Builds the sales assets a rep sends or uses in a deal, from claims your brain can prove: a one-pager or leave-behind, a demo script, a proposal, an ROI calculator, a deck outline, and win-loss analysis of why you win and lose. Any other sales-asset ask (an objection, a battlecard, persona cards, a playbook, a case study, a call plan, a message) is sent to the skill that owns it, with what you already told it. Includes where you lose. Reads your brain; never writes it, a CRM or an inbox. Nothing is sent to a buyer.

## Invocation

```
/pmm-sales:sales-collateral One-pager for the CFO champion at Tidewell
/pmm-sales:sales-collateral Demo script, 30 minutes, VP Finance, first demo
/pmm-sales:sales-collateral Proposal for the Marlow deal
/pmm-sales:sales-collateral ROI calculator for invoice automation
/pmm-sales:sales-collateral Why do we lose mid-market deals?
/pmm-sales:sales-collateral What sales assets are stale?
```

In Slack, tag Claude in a thread: "@Claude one-pager for the CFO champion at Tidewell".

## Workflow

Uses the `sales-collateral` skill. Finds the asset in your ask and routes it if a sibling owns it. Otherwise reads your brain, sources every claim or names the gap, builds the asset in the buyer's words, runs the Quality Gate, saves it with the claims it relies on, ends Slack on one plain question, flags stale assets, proposes what other skills should learn once enough deals agree, and logs the session.
