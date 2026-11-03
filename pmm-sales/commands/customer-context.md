---
description: Get the current state of one customer account from your connected tools, checked against your brain, in Slack or anywhere else
argument-hint: "<customer name or domain, plus anything you want to know: 'before the renewal', 'what changed', 'is it at risk'>"
---

# /pmm-sales:customer-context -- Customer Context

Builds the current state of one existing customer: owner, renewal, open
opportunities, contacts and who has really replied, the latest calls and
threads, support and usage themes, and up to five evidenced flags. Checks the
customer against your brain (ICP fit, competitors, objections, claims you may
use) and, when an earlier brief exists, shows only what changed. In Slack it
answers in a short thread reply. Saves the brief to `/context/customers/`.

## Invocation

```
/pmm-sales:customer-context Northwind
/pmm-sales:customer-context Northwind before Thursday's renewal call
/pmm-sales:customer-context What changed at Northwind since last month?
/pmm-sales:customer-context Is Northwind at risk?
```

In Slack, tag Claude in a thread: "@Claude catch me up on Northwind".

## Workflow

Uses the `customer-context` skill. Picks the surface (Slack, chat, Cowork,
Claude Code or a scheduled run), loads the brain and the last brief, reads the
CRM, email, calls, docs, chat, support and usage you have connected, checks the
customer against the brain, flags what is missing or at risk, writes the brief
in the shape that fits where you are reading, runs a 12-check gate on its own
work, saves the record, proposes what other skills should learn once two
customers agree, and logs the session. Read-only for your brain, CRM and
inbox.
