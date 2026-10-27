# Learning Loop

Reference for `industry-newsletter`. Three small append-only files, plus the config, make each issue learn from the one before it. Read this file in Step 3 (closing the loop), when adding a call, and when deciding whether feedback justifies a change.

## Contents

1. The files
2. The call ledger
3. The watchlist
4. Reader feedback and when it may change the issue
5. What the next issue does with each
6. What this is not

---

## 1. The files

All live in `/context/industry-newsletter/`. Every file is append-only: a row is never edited or deleted; a change of state is a new row with the same `id`. Create each with its header row if it does not exist. If a file cannot be written, show the rows and say they were not saved.

| File | Holds | Written by |
|---|---|---|
| `_config.md` | Category, regions, owner team, audience, roles, frequency, platform, roster source, Slack channel, internal inputs | Step 2, as dated blocks (the newest block wins) |
| `_ledger.md` | Calls the newsletter made and how they turned out | Step 3 and Step 9 |
| `_watchlist.md` | Signals not yet strong enough to report, with the trigger that would promote them | Step 3 and Step 9 |
| `_feedback.md` | Explicit reader signals about the issue itself | Step 3 |

The newsletter reads, and never writes, `/context/briefings/_ledger.md`, `/context/briefings/_decisions.md` and `/context/battlecards/_outcomes.md`. Its ids (`N-`, `W-`, `B-`) never collide with theirs.

## 2. The call ledger

```markdown
| id | date | event | issue | competitor | call | check_in | outcome | evidence |
|---|---|---|---|---|---|---|---|---|
| N-001 | 2026-10-20 | called | 6 | [name or "category"] | [one falsifiable claim] | 2026-11-20 | open | [page or record that will settle it] |
| N-001 | 2026-11-24 | graded | 6 | [same] | [same call] | 2026-11-20 | correct | [link and date] |
```

- **Falsifiable.** An observable event that either happens or does not: "Paystream will publish a usage-based tier on its pricing page by 20 Dec", not "pricing pressure will build".
- **Settled by something that exists.** Name the page or record. If nothing could settle it, rewrite it.
- **Check-in 30 to 60 days out.** Shorter is noise, longer is never graded.
- **One per issue.** Ids run N-001, N-002; the next id is the highest plus one.
- **Own calls only.** A competitor's announced plan is evidence, not a call. A call about a competitor that `competitive-briefing` already made in `/context/briefings/_ledger.md` is not repeated; the issue points to it.
- **Grading.** Due when the check-in date has passed with no later `graded` row. `correct`: it happened by the date, shown by a saved record or a page retrieved this run. `wrong`: the date passed and the page or record shows it did not. `partial`: say which part. `open`: the date has not passed, or the evidence cannot be read this run (never guess; the item goes on the Held list). A call more than 60 days past its check-in with no evidence is graded `wrong` with the evidence cell "no evidence by [date]".
- **Showing the record.** "x of y", where y counts `correct`, `wrong` and `partial` and x counts `correct`; add "(1 partial)" when there is one. Show it only once 3 calls are graded. Below that: "n=2, too early to rate". Never a percentage.

## 3. The watchlist

A signal not yet strong enough to report is not dropped. It waits here with the trigger that would promote it.

```markdown
| id | date | event | item | why | trigger | source | issues_open |
|---|---|---|---|---|---|---|---|
| W-001 | 2026-10-13 | opened | [e.g. "Brightfold hiring 6 partner managers"] | [why it could matter] | [observable event that promotes it] | [link] | 1 |
| W-001 | 2026-10-27 | promoted | [same] | | [met: partner directory page lists 4 new integrators] | [link] | 3 |
```

- **Events:** `opened`, `kept`, `promoted`, `dropped`.
- A `🟡` or `⚠️` item that is interesting but unconfirmed goes here instead of into the issue.
- A held claim whose only gap is a missing link is not on the watchlist; it is on the Held list.
- **Promotion.** If the trigger was met in this period's research, the item enters the issue at the mark its new evidence earns, and a `promoted` row is appended.
- **Age.** `issues_open` counts issues, not days. At 4 with no movement, the issue asks once: "Drop W-00N or keep it for another four issues?" Only the user closes it.
- **Cap.** At most 7 open items. At the cap, the oldest gets the drop question before a new one is added.
- The pricing watch's "Watch next week" line is drawn from the watchlist. Other items stay in the file and the chat summary; the document does not carry a watchlist block.

## 4. Reader feedback and when it may change the issue

The weakest evidence in the loop is also the easiest to over-read. Email and Slack give almost no clean engagement data, and a reaction from an unknown reader tells you nothing about which section to change. So only explicit, attributable signals count.

```markdown
| id | date | issue | channel | role | signal | section | note |
|---|---|---|---|---|---|---|---|
| B-001 | 2026-10-24 | 6 | slack | RevOps | too long | Competitor Watch | [10 words or fewer] |
```

- `signal`: `useful`, `not useful`, `too long`, `too short`, `missing`, `wrong`.
- **Counts:** a reply that names a signal and a section, or one signal on the whole issue. **Does not count:** a reaction alone, a forward, an open, silence.
- **Threshold for a proposal:** the same signal about the same section from at least **three different roles** across at least **two issues**. One loud reader is not a trend.
- **What a proposal may change:** a row cap down or up by one, the order of Sources & References rows, whether Industry Changes is shown in a quiet week, a role added or dropped from `_config.md`. It appears in the chat summary, not in the document, as "Proposed change: [change]. Behind it: [signal, n roles, n issues]. Reply yes to apply." Applied only after the user says yes, then written to `_config.md` as a dated block.
- **What it may never change:** the headings and their order, the Pricing / Packaging watch, the Calls, the actions, the handling line, the evidence rules. Feedback tunes how much space a block gets, never whether the discipline holds.
- **A `wrong` signal is not feedback, it is a correction.** It goes on the held list in the chat for the next issue with the claim it disputes, and is checked against the source before anything else.

## 5. What the next issue does with each

| Store | Where it shows up next issue |
|---|---|
| `_ledger.md` | "Last issue's call" in the Calls table, with the record once 3 calls are graded |
| `_watchlist.md` | The pricing watch's "Watch next week" line, and the first search targets in Step 4 |
| `_feedback.md` | A proposed change in the chat summary, only when section 4's threshold is met |

The issue shows the last call and, after three graded calls, the record; the files hold the rest. Do not narrate the history.

## 6. What this is not

- Not a forecast model. A call is one observable claim, not a probability.
- Not a scorecard of people. Respondents are roles.
- Not an engagement dashboard. There is no open rate, no reaction count and no percentage anywhere.
- Not a CRM. Nothing is written to any external tool, and deal data never enters these files.
- Not a reason to change a past issue. Records are never edited; a later fact goes in a later row.
