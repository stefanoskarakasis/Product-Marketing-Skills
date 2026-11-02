---
description: Build a "you vs a named rival" or "best alternatives to X" page from your brain and competitor records, with a sourced claims ledger behind every row
argument-hint: "<page type and rival, e.g. vs Northgate AP, alternatives to Paystream, switch from Brightfold, or refresh>"
---

# /pmm-competitive-intelligence:comparison-page-brief -- Comparison Page Brief

Works out how you really stack up against a named rival, then builds the
page: a vs page, an alternatives page (one rival or a ranked list) or a
switch page. Every row sits in a claims ledger with a source, a date and an
expiry, so the page can be refreshed instead of rewritten. One dataset
renders the public page and the sales-sent version. It says where you lose,
holds the page when the rival's pricing and features cannot be sourced,
saves to `/context/comparisons/` and never writes the brain. Nothing is
published or sent.

## Invocation

```
/pmm-competitive-intelligence:comparison-page-brief Build our vs page against Northgate AP
/pmm-competitive-intelligence:comparison-page-brief Write a best alternatives to Paystream page
/pmm-competitive-intelligence:comparison-page-brief Switch page for Brightfold users
/pmm-competitive-intelligence:comparison-page-brief Sales-sent version for the Northgate deal
/pmm-competitive-intelligence:comparison-page-brief Refresh the Northgate vs page, pricing changed
```

## Workflow

Uses the `comparison-page-brief` skill. Loads the brain (or asks five quick
questions and holds the answers for the session), reads the rival's records
and up to five roster rivals, and states the cost of the run before it
reads anything. It builds a Field Map with a coverage score and checks the
named-rival floor, judges the stack-up in three lenses (head-to-head, field
position, switching reality), builds the claims ledger, writes the page from
the template for its type, lints it, runs an 11-check gate and saves the
records. Ask for the Figma handoff and it adds a text spec.
