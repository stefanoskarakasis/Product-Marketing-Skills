# Prediction Ledger and Decision Log

Reference for `competitive-briefing`. Two small append-only files make the brief worth reading week after week: one tracks whether the calls were right, the other whether the decisions got made. Read this file when grading a call, adding a call, or building "Still open".

## Contents

1. The two files
2. Calls: format and rules
3. Grading
4. Decisions: format and rules
5. Showing the record
6. What this is not

---

## 1. The two files

| File | Holds | Written by |
|---|---|---|
| `/context/briefings/_ledger.md` | Calls the brief made and how they turned out | `competitive-briefing`, Step 8 |
| `/context/briefings/_decisions.md` | Decisions the brief asked for and what became of them | `competitive-briefing`, Step 8; a closure only on the user's word or a listed approver's reply |

Both are append-only. A row is never edited or deleted; a change of state is a new row with the same `id`. Create each file with its header row if it does not exist. If a file cannot be written, show the rows and say they were not saved.

## 2. Calls: format and rules

```markdown
| id | date | event | competitor | call | check_in | outcome | evidence |
|---|---|---|---|---|---|---|---|
| P-001 | 2026-10-12 | called | [name] | [one falsifiable claim] | 2026-11-12 | open | [record or page that will settle it] |
| P-001 | 2026-10-26 | graded | [name] | [same call] | 2026-11-12 | correct | [source and date] |
```

Rules for a call:

- **Falsifiable.** An observable event that either happens or does not: "Paystream will reinstate a trial or demo path by 10 Dec", not "Paystream will struggle".
- **Settled by something that exists.** Name the page or record that will show it (a pricing page, the changelog, the outcome log). If nothing could settle it, rewrite it.
- **Check-in 30 to 60 days out.** Shorter is noise, longer is never graded.
- **One per brief.** A second call in the same brief is a second brief's job.
- **Ids** run P-001, P-002 and so on; the next id is the highest plus one.
- **Own calls only.** A competitor's announced plan is evidence, not a call.

## 3. Grading

At the start of each run, every `called` row with no later `graded` row whose `check_in` is on or before today is due.

| Outcome | When |
|---|---|
| `correct` | The event happened by the check-in date, shown by a saved record or a page retrieved this run |
| `wrong` | The check-in date passed and the page or record shows it did not happen |
| `partial` | Part of the claim happened; say which part in the evidence cell |
| `open` | The check-in date has not passed, or the evidence cannot be read this run (never guess) |

A call is graded only on evidence, never recalled. If the settling page cannot be fetched, the outcome stays `open` and the item goes on the Held list. A call more than 60 days past its check-in with no evidence is graded `wrong` with the evidence cell "no evidence by [date]".

## 4. Decisions: format and rules

```markdown
| id | date | event | decision | owner | decide_by | outcome |
|---|---|---|---|---|---|---|
| D-001 | 2026-09-28 | asked | [the decision as a question] | [role] | 2026-10-14 | open |
| D-001 | 2026-11-03 | made | [same decision] | [role] | 2026-10-14 | [the choice in 20 words or fewer] |
```

Events: `asked`, `made`, `dropped`, `moved` (a new decide-by date, with the reason in the outcome cell).

- **One row when a brief asks.** A decision already open is not asked again; it appears under "Still open" and the Decision block only if it is still the one on the table.
- **A decision closes only on a person's word.** The user says it was made or dropped, or a listed approver replies in the thread. A reply from anyone else is quoted back and not applied.
- **Roles only.** The owner is a role. Never a name.
- **Age.** "Open for" is whole weeks since the first `asked` row. Three weeks or more is shown as overdue in "Still open" whether or not the decide-by date has passed.
- **Never carry a decision that no one owns.** If the owner role is unknown, ask once; if still unknown, the decision goes on the Held list as "no owner".

## 5. Showing the record

- **Hit rate:** "x of y", where y counts calls graded `correct`, `wrong` or `partial` and x counts `correct`; add "(1 partial)" when there is one. Show it only once 3 calls are graded. Below that: "n=2, too early to rate". Never a percentage.
- **No earlier call:** "No earlier call." The first brief says so and makes the first call.
- **Still open:** every decision with an `asked` row and no `made` or `dropped`, oldest first, with its age.
- **Do not narrate the history.** The brief shows the last call and the running record; the files hold the rest.

## 6. What this is not

- Not a forecast model. A call is one observable claim, not a probability.
- Not a scorecard of people. Owners are roles.
- Not a CRM or project tracker. Nothing is written to any external tool.
- Not a reason to change a past brief. Records are never edited; a later fact goes in a later row.
