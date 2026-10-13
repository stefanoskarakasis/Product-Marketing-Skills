# Profile Format

Reference for `competitive-profile`. Read it when building a record, a board, a brain note or a scheduled-run prompt.

## Contents

1. Evidence tags
2. Freshness windows
3. Profile record
4. Roster and profile note (the only brain write)
5. Status record and freshness board
6. Scheduled-run prompts
7. Deal feedback line

---

## 1. Evidence tags

Tags follow `product-marketing-context/references/evidence-format.md`. Use the short form on every line.

| Tag | Meaning | Rank |
|---|---|---|
| `[B]` | Confirmed brain value | 0 |
| `[CRM]` / `[WL]` / `[CALL]` | Your deal data, win/loss interviews, recorded calls | 1-2 |
| `[CI]` | Your CI team's card or profile, read only | 3 |
| `[PUB]` | Public page about the competitor (site, pricing, release notes, newsroom) | 4 |
| `[3P]` | Third-party material (reviews, analysts, company data) | 4 |
| `[A]` | Chat or recollection, unsourced | 5 |

A fact older than 12 months drops one rank. A competitor's own claim is `[PUB]` and proves only that it said it.

## 2. Freshness windows

| Profile line | Window (days) | Why |
|---|---|---|
| Pricing and terms | 60 | Pricing pages change fastest |
| Product and packaging | 90 | Releases land monthly to quarterly |
| Positioning and axis | 90 | Homepage and campaign shifts |
| Recent moves (funding, hiring, leadership) | 90 | News ages out |
| Roster (who is on it) | 90 | Checked quarterly |
| Market and buyer, segments | 180 | Moves slowly |
| Where they win / lose | 180, or on a new loss reason | Needs n of 2 or more |

Past the window the line is marked `re-check`. These windows change only when you confirm a change proposed by `meta-synthesis`.

## 3. Profile record

Saved as `/context/competitor-profiles/<competitor-slug>-YYYY-MM-DD.md`. Never overwrite; the newest file is current.

```markdown
---
competitor: [name]
slug: [competitor-slug]
status: draft
roster_position: [1-5]
market: [category · market type · segment]
built: [YYYY-MM-DD]
previous: [previous file name or "none"]
---

# [Competitor]: profile

## Market and buyer
- Who they sell to: [text] [tag · as of YYYY-MM-DD]

## Product and packaging
- [text] [tag · as of]

## Pricing and terms
- [text] [tag · as of] (window 60 days)

## Positioning and axis
- Their claim: [text] [PUB · as of]
- The axis they compete on: [text] [tag · as of]

## Recent moves
- [YYYY-MM-DD] [text] [tag]

## Where they win
- [text] [tag · n of N, window] (or "no pattern yet, one data point: [note]")

## Where they lose
- [text] [tag · n of N] (or "no public evidence")

## Open questions for the field
- [weakness without a source, written as a question]

## Our side
- Shipped, permitted: [Section 1 / 6 items]
- Roadmap (never a capability): [items]
- [NEEDS PROOF]: [differentiator and the question that would expose it]

## Carried forward
- [lines not re-read this run, with original date]

## Sources
- [tag] [title or URL] · [date read]
```

## 4. Roster and profile note (the only brain write)

Shown as exact text, then written only on a yes. Appended under Section 3; existing text is never edited.

```markdown
### Competitor Roster and Profile Notes (competitive-profile, YYYY-MM-DD)
Roster (max 5): 1. [name] · 2. [name] · ...
- [competitor]: [dated fact or pattern] [tag · as of] (n of N)
- Conflict: map says [X], fresh evidence says [Y] [tag · as of]
```

At most five lines. Status quo and DIY stay in Section 3 as they are and are not profiled.

## 5. Status record and freshness board

Saved as `/context/competitor-profiles/_status-YYYY-MM-DD.md`.

```markdown
| Competitor | Profile | Stale lines | Oldest line | Changed since | Open |
|---|---|---|---|---|---|
| [name] | 🟢🟡🔴⚪ [date] | [n] | [line, age] | [one phrase] | [NEEDS PROOF count] |
```

🟢 current · 🟡 some lines stale · 🔴 pricing or product stale · ⚪ no profile yet. End with one next action.

Roster check (v2): competitor, deals in last 90 days, on roster, proposed move. Mark `[A]` if the count came from recollection.

## 6. Scheduled-run prompts

A scheduled run starts a fresh session, so name the brain folder and every source. Replace the bracketed parts.

**Weekly refresh**

> Create a scheduled task that runs every Monday at 8:00. Use the competitive-profile skill in refresh and status mode. My brain is in [folder]. Read Section 3 for the roster, the newest file per competitor in /context/competitor-profiles/, and /context/signals/. Re-read only lines past their window, using public pages for the five roster competitors and [named connectors]. Save new records and a status board in /context/competitor-profiles/. Do not change the brain, do not ask questions, and list anything that needs my yes under "Waiting for you".

**Quarterly roster check**

> Create a scheduled task that runs on the first Monday of each quarter at 8:00. Use competitive-profile in roster mode. My brain is in [folder]. Count competitor appearances in [CRM name] for the last 90 days, and save the proposed swaps in a status record. Do not change the brain or the roster.

## 7. Deal feedback line

After a deal, one line is enough, and it feeds `intake`:

`[competitor] · won/lost · reason in the buyer's words · stage · date`

One line is a note. The same reason twice within 180 days is a "where they win" proposal.
