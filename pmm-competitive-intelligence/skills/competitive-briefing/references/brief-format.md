# Brief Format

Reference for `competitive-briefing`. Read it when building the brief, rendering it for Slack, saving the record or setting up the weekly task.

## Contents

1. Budgets and marks
2. The brief (fixed order)
3. Audience variants
4. The quiet-week brief
5. The Held list and the status
6. Sources and the Assumed line
7. Slack rendering
8. The saved record
9. The weekly task

---

## 1. Budgets and marks

| Audience | Body words (target / ceiling) | Move rows |
|---|---|---|
| CEO and board | about 350 / 500 | 3 |
| CRO and revenue | about 450 / 650 | 5 |
| Product leadership | about 450 / 650 | 5 |
| Whole company | about 250 / 350 | 3 |

Body words are counted from the verdict to the end of the Held list. Tables' header cells, Sources, the footer and the handling line are not counted. Cells: 20 words or fewer. Tables are capped by rows, not words.

**Confidence marks** (each row carries one; the key sits under the table it explains):

| Mark | Word | Meaning |
|---|---|---|
| 🟢 | High | Primary source, retrieved or saved with its date, no conflict |
| 🟡 | Medium | One non-primary source, or an inference stated in the "why it matters" |
| ⚪ | Low | Stale (past the window), single weak source or unverified |

**Emoji legend (use no others):** 🧭 Decision · 🔍 What moved · 🚦 This call · ⚠️ Held · 🟢 🟡 ⚪ confidence. Status and results are words, not emoji: "HOLD", "Cleared", "Correct", "Wrong", "Open".

## 2. The brief (fixed order)

Header lines come first, then the sections in this order. One stacked column. Table header cells are bold. Block names are headings.

```markdown
# Competitive Briefing

**[Company] · [period, e.g. 19 to 26 Oct 2026] · [Audience] · [n] competitors**

*[Handling line.]*
**Status: HOLD. [n] items to clear before this goes out** (section 7)
(or, only when the Held list is empty and the user named a verifier: **Status: Cleared. Verified by [name], [date]**)

---

## The call

**[Verdict: what changed, what it puts at risk in €, what we recommend, by when. Two sentences at most.]**

---

## 1. 🧭 Decision

**[The decision as a question.]**

| | **A. [Option]** | **B. [Option]** *(recommended)* |
|---|---|---|
| **Cost** | | |
| **We'd need to believe** | | |
| **Evidence for it** | [source IDs] | [source IDs] |
| **Risk** | | |

**Confidence in [B]: [High / Medium / Low].** [One line on why.]
**This changes if:** [one observable trigger]
**Owner:** [role] · **Decide by:** [date]

(No decision needed: one line, "No decision needed this week: [reason]". No recommendation: "No recommendation yet: [what would make one possible]".)

---

## 2. Still open from earlier briefs

| **Decision asked** | **Owner** | **Open for** |
|---|---|---|

(Or "Nothing open.")

---

## 3. 🔍 What moved (ranked by exposure)

| **Competitor** | **Move** | **Why it matters** | **Confidence** | **Source** |
|---|---|---|---|---|

🟢 **High:** primary source, dated · 🟡 **Medium:** one non-primary source or an inference · ⚪ **Low:** stale or unverified

---

## 4. Don't react to

- **[Move and why no action is needed]** *([source ID])*
- **Quiet this cycle:** [competitors with no change, one line]

---

## 5. Last call graded

**[Correct / Wrong / Open].** [The call, its check-in date, the evidence with source ID.] **Record: [x of y]** (or "n=[n], too early to rate"; or "No earlier call.")

## 6. 🚦 This call

**[One falsifiable prediction.]** Check-in: [date]. Based on [source IDs].

---

## 7. ⚠️ Held

| **Item** | **Blocks** | **To clear** |
|---|---|---|

(Or "Nothing held.")

---

## Sources

[See section 6 of this file.]
```

Rules:

- **The call** is written last. It states the risk in € only when a dated `~~CRM` figure or paste supports it; otherwise "not quantified".
- **Options** name what we would need to believe. A cell about our side is a permitted or approved claim, or "seller-reported, n=[n]".
- **Still open** is built from `_decisions.md`: every decision with an `asked` row and no `made` or `dropped` row, with its age in weeks. A decision open 3 weeks or more is marked in the Open-for cell: "[n] weeks, overdue".
- **What moved** is ranked by open pipeline € when known, else by `roster_position`. A move without a commercial implication is trivia and is cut.
- **Don't react to** is for moves that are real but need no action. It saves the reader from inventing work.
- **Last call graded** is evidence-only: a saved record or a retrieved page, never recall.
- **This call** must be settled by a named record or page. If it cannot be, rewrite it until it can.

## 3. Audience variants

The audience changes emphasis and length, never the evidence rules.

| Audience | Lead with | Adds | Drops |
|---|---|---|---|
| CEO and board | Position, risk in €, the decision | None | Seller detail, long product notes |
| CRO and revenue | Win and loss, pricing, open-deal exposure | A **Deals** block after What moved: the outcomes since the last brief (won, lost, no decision, reason, source), up to 5 rows; the card to use for each competitor | Hiring detail |
| Product leadership | Product and roadmap moves, hiring, packaging | A line per move on the capability it implies | € figures unless asked |
| Whole company | What changed and what we do about it | One line on what to say if a customer asks | Deal data, € figures, internal tags, the Decision options table (keep the decision as one line) |

The whole-company version never carries deal data or € figures. Its handling line is "Internal use."

## 4. The quiet-week brief

Used when nothing crossed the bar (SKILL.md Step 3). Keep the header, the handling line and the status, then:

```markdown
## The call
**Nothing crossed the bar this week.** [One line: what was checked and found unchanged, with the newest source date.]

## 2. Still open from earlier briefs
[table or "Nothing open."]

## 6. 🚦 This call
[the call carried or a new one]

## 7. ⚠️ Held
[table or "Nothing held."]

## Sources
```

Sections 1, 3, 4 and 5 are left out in a quiet week, except that an earlier call due for grading is still graded under section 5.

## 5. The Held list and the status

An item goes on the Held list when it cannot be cleared by the brief itself:

- a figure with no export date, or older than 14 days;
- a claim with a single non-primary source that the verdict or the decision relies on;
- a profile or brain section past its freshness window that feeds a row;
- an item excluded by the collection-method check, named;
- a line removed by Section 6 `forbidden_claims` or Section 8 `prohibited`, naming the entry.

Each row says what it blocks (the verdict, the decision, a move row) and how to clear it.

**Status.** `HOLD. [n] items to clear before this goes out` while the Held list is not empty or no verifier is named. `Cleared. Verified by [name], [date]` only when the list is empty and the user gave the name. Without a verifier the line reads `HOLD. No verifier named`.

## 6. Sources and the Assumed line

One section, two small tables, no more than one line of prose.

```markdown
## Sources

**Public**

| **ID** | **Source** | **Retrieved** | **Source date** |
|---|---|---|---|
| S1 | [page or record] · `[URL if retrieved or saved]` | [date] | [date] |

**Internal**

| **ID** | **Source** | **Supplied** |
|---|---|---|
| I1 | [outcome log, CRM export, paste] | [date] |

*Assumed: [audience], [currency], [pipeline source]. Verified by: [name, date] or "not yet verified". Full record: `/context/briefings/[file].md`*
```

Every source ID cited above must appear here; a row not cited is removed. A record read (profile, card, signal) is listed as a source with its path and as-of date. A URL appears only if it was retrieved this run or is in a saved record; otherwise "link pending".

## 7. Slack rendering

Used in a thread or channel. About 150 words, ceiling 200. Bullets, no table, no headers beyond bold labels. Source wording in place of IDs (the page and its date). The saved path is the last line.

```
*Competitive briefing · week of [date]* · Status: [HOLD (n) / Cleared]
*The call:* [verdict, two sentences]
🧭 *Decision by [date]:* [question]. Recommend [B]: [why, one line]. Changes if: [trigger]. Owner: [role].
🔍 *What moved*
• [Competitor]: [move] ([confidence word], [source and date]). [Why it matters.]
• ...
*Don't react to:* [one line]
🚦 *Last call:* [Correct / Wrong / Open]. [x of y]. *This call:* [prediction], check-in [date].
⚠️ *Held:* [item, what it blocks]
_Full brief saved at [path]_
```

## 8. The saved record

`/context/briefings/YYYY-MM-DD-<audience-slug>.md`. Never overwritten; a rebuilt brief gets a new file.

```markdown
---
type: briefing
audience: [audience]
period: [YYYY-MM-DD to YYYY-MM-DD]
built: [YYYY-MM-DD]
status: HOLD | Cleared
verified_by: [name or none]
currency: [EUR]
roster: [competitor, roster_position; ...]
previous: [previous file name or "none"]
---

[The brief, exactly as delivered.]

## Evidence log

| id | claim | tag | source | as_of | conflict |
|---|---|---|---|---|---|
| C-1 | [one atomic claim] | [tag from card-format.md] | [file, URL or title] | [YYYY-MM-DD] | [none / what] |

## Method

- Records read: [paths and as-of dates]
- Connectors: [category: tool, pulled date, or "not connected" / "pasted"]
- Checked against: Section 6 `forbidden_claims`, Section 8 `prohibited`, collection method. Result: [none found / what was removed]
- Evidence floor: [what satisfied it]
- Not done: [what was not researched or supplied]

## Distribution

- Status and what clears it: [held items]
- Hand-offs: [decision to owner role; stale lines to `competitive-profile` refresh]
```

## 9. The weekly task

The brief is weekly by default. Schedule it after the profile refresh, so it reads fresh records. Paste into a scheduled task:

> Every Monday at 9:00, use the competitive-briefing skill. My brain is in [folder]. Audience is [CEO and board]; currency is euro. Read the newest profile for each roster competitor in /context/competitor-profiles/, the last 7 days of /context/signals/, /context/battlecards/_outcomes.md and /context/briefings/. Build the brief, grade the last call, list open decisions, and save the record and ledger rows. Post it to [channel]. Do not re-read stale pages, do not change the brain, do not ask questions, and put anything that needs my yes in the Held list.

A scheduled run uses the defaults, states them in the Assumed line and cannot clear its own Held list: the status stays HOLD until a person names a verifier.
