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
8. Slack settings file
9. Draft file
10. Unanswered log
11. Weekly Slack run prompt

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

Saved as `/context/competitor-profiles/<competitor-slug>-YYYY-MM-DD-HHMM.md`. Never overwrite; the newest file by date and then time is current, so two approvals on one day never collide. Records written before v1.14.0 keep their date-only names and still sort correctly.

```markdown
---
competitor: [name]
slug: [competitor-slug]
status: draft            # draft | approved
approved_by: none        # role of the approver, set only when status is approved
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

## 8. Slack settings file

Saved as `/context/competitor-profiles/_slack.md`. Written only at `setup` (or `review`), after you confirm the exact text. A scheduled run never writes it.

```markdown
---
approvers: [Slack handle and role of each person who may approve a change, e.g. "@dana (PMM lead)"]
field_channel: [channel the weekly run sweeps for competitor intel, or "none"]
board_channel: [channel the weekly board is posted to, or "none"]
---
```

Approvers are named by Slack handle because a reply in a thread shows a handle, not a role. Handles are the only personal data kept, and only here. Without this file, Slack drafts are saved but never applied, and the thread is told to run `setup`.

## 9. Draft file

Saved as `/context/competitor-profiles/drafts/<competitor-slug>-YYYY-MM-DD-HHMM.md`, one per proposed change. A draft is a working file: its `status` line may be updated. Profile records are never overwritten.

```markdown
---
competitor: [name]
slug: [competitor-slug]
line: [profile section and line]
status: open            # open | approved | rejected | expired
opened: [YYYY-MM-DD HH:MM]
reports: [n]
---
Now: [old value] (as of [date])
New: [new value]
Sources: [tag · permalink or URL · date], one per report. Roles only, no names.
Thread: [permalink]
Decision: [approved / rejected / expired · approver role · date]
```

An open draft older than 7 days becomes `expired`.

## 10. Unanswered log

Append-only. `/context/competitor-profiles/_unanswered.md`, one row per question with no sourced answer or about a competitor that is not on the roster.

```markdown
| Date | Competitor | Type | What was missing | Reaction |
|---|---|---|---|---|
| [YYYY-MM-DD] | [name or "not profiled"] | [pricing / launch / win-loss / objection / other] | [the source that would have answered it] | [none / thumbs down] |
```

The weekly board shows the five most common rows. A competitor that appears three times is a candidate for `roster`.

## 11. Weekly Slack run prompt

For a Claude in Slack routine or any scheduled task. Replace the bracketed parts.

> Every Monday at 8:00, use the competitive-profile skill in refresh, status and sweep mode. My brain is in [folder]. Read /context/competitor-profiles/_slack.md for the approvers, the field channel and the board channel. Re-read only the profile lines past their window. Sweep the field channel for the last 7 days and save each new item as an open draft; do not change any profile. Mark drafts open for more than 7 days as expired. Post the freshness board, "Waiting for [approver]" (open drafts) and the five most common unanswered questions to the board channel, as bullets and not a table. Do not change the brain, do not ask questions, and list anything that needs my yes under "Waiting for you".
