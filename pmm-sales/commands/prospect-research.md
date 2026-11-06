---
description: Get the reason, angle and first question for reaching out to one company, from web search, your CRM and any enrichment, checked against your brain, in Slack or anywhere else
argument-hint: "<company name or domain, plus the role you will contact and anything you want to know: 'is there a reason now', 'what changed'>"
---

# /pmm-sales:prospect-research -- Prospect Research

Builds a brief on one company you do not sell to yet: the CRM status, up to five
dated signals that map to a pain in your brain, fit and timing as two separate
verdicts, and a hypothesis with an angle, a first question and a fallback.
Checks the company against your brain (ICP, anti-persona, approved proof) and,
when an earlier record exists, shows what changed or expired. In Slack it
answers in a short thread reply. Keeps EMEA data rules on when the account or
your team is in Europe. Saves the record to `/context/prospects/`. It never
writes outreach and never sends anything.

## Invocation

```
/pmm-sales:prospect-research Tidewell Foods
/pmm-sales:prospect-research Tidewell Foods, I'm an AE going to their Controller
/pmm-sales:prospect-research Is there a reason to contact Tidewell now?
/pmm-sales:prospect-research What changed at Tidewell since my last brief?
/pmm-sales:prospect-research log: meeting booked at Tidewell
```

In Slack, tag Claude in a thread: "@Claude research Tidewell Foods before I reach out".

## Workflow

Uses the `prospect-research` skill. Picks the surface (Slack, chat, Cowork,
Claude Code or a scheduled run), loads the brain and the last record, checks the
CRM first (customer, owned by a colleague, or net new), reads the web and any
connected company data or enrichment, keeps the signals that map to a pain you
solve, scores fit and timing, writes the hypothesis, angle, first question and
fallback, runs a 12-check gate on its own work, saves the record, logs patterns
and outcomes, proposes what other skills should learn once enough accounts
agree, and logs the session. Read-only for your brain, CRM and inbox.
