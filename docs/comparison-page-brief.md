# Comparison page brief: build a vs or alternatives page you can defend

`comparison-page-brief` builds the page a buyer lands on when they search "you vs a rival" or "alternatives to a rival". It first works out how you really stack up, then writes only what it can source. This page covers who uses it, the five page types, what it needs, and how to keep the page fresh.

## Use it when

- Buyers search "[you] vs [rival]" or "[rival] alternative", and you have no page, or a stale one.
- A seller wants a comparison to send into a live deal (a sales-sent version).
- A rival changed its pricing and your page is now wrong.

Do not use it for a one-page seller card (`competitive-battlecard`), one question about one rival (`competitive-profile`) or a long write-up (`competitor-deep-dive`).

## Page types

| Type | Search intent | Result |
|---|---|---|
| `vs` | "[you] vs [rival]" | Verdict, table, who should choose which, switching |
| `alt-single` | "[rival] alternative" | Why people leave, how you answer, where the rival is still better |
| `alt-list` | "best [category] tools" | 7 entries (max 10), same template for every entry, yours included |
| `switch` | "migrate from [rival]" | What moves, what does not, sample run, undo |
| `sales-sent` | a live deal | Same ledger, labelled, never published |

## What it needs

- A brain with Sections 1 to 3 (and Section 6 for proof). Without it, five quick questions.
- The rival's profile, if you have one. Without it, fresh public pricing and feature pages.
- Optional: a keyword export, review ratings (pasted), win/loss notes.

If the rival's pricing and at least five features cannot be sourced, it holds the page or downgrades it. It will not guess.

## What you get

A page, plus a claims ledger (every row with a source, a date and an expiry), a stack-up, keyword targets, a plain-text twin of the page, a publish checklist, schema for facts that are on the page, and optionally a Figma text spec. Saved to `/context/comparisons/`.

## Keep it fresh

Pricing rows expire after 30 days, features after 90. Run `/pmm-competitive-intelligence:comparison-page-brief Refresh the [rival] vs page` and it re-reads only the expired rows and saves a new dated file. Pair it with `media-monitoring` so a rival's pricing change tells you the page is stale.

## What it will not do

- Publish, post or send anything.
- Write the brain.
- Add a rating schema without a real rating.
- Use a claim it cannot source, or hide where you lose. A page with no concession does not convert.
