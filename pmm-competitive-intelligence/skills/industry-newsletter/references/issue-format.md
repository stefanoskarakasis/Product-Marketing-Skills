# Issue Format

Reference for `industry-newsletter`. Read it when building an issue, choosing the platform rendering, saving the record or setting up the weekly task. The layout is locked: the sections, their headings and their order never change.

## Contents

1. Budgets and row caps
2. Readability rules
3. Marks and the scoring rubric
4. The issue (fixed order)
5. Platform renderings (Google Doc, email, Slack)
6. Roles
7. The quiet-week issue
8. The Held list (chat only)
9. Sources & References
10. The saved record
11. The weekly task

---

## 1. Budgets and row caps

| Block | Cap |
|---|---|
| Body words (Google Doc, email), "This week in one sentence" to the actions | about 900 / ceiling 1,200 |
| Slack post | about 220 words, ceiling 250 |
| Table cells | 25 words or fewer |
| Competitor Watch | up to 5 competitors, each with its own numbered table; **3 to 5 product or platform updates in total** (a pricing, channel, customer-proof or hiring row is added only when it changed and does not count toward the 3 to 5) |
| Industry Changes | up to 3 rows, of which at most 2 are a procurement, security or regulatory trend, or an early signal |
| Pipeline impact | 5 rows in total across Now, Next, Later |
| Pricing / Packaging watch | one status line plus what to watch next week, always |
| Actions | 5 |
| Sources & References | every link the issue cites, nothing else; at least 3 rows carry a priority or read time |

Fewer than 3 verifiable product updates: show only those and state the count. A block with nothing to report says so in one line; it is never padded.

## 2. Readability rules

The reader may be a CEO, a sales lead or a colleague in Finance. They find the same thing in the same place every week.

- **Heading levels carry the hierarchy.** H1 is the title. H2 is a section. H3 is a competitor (numbered). H4 is a small label inside a section. Never skip a level.
- **Competitor names are H3 headings, numbered** (`### 1 · Northgate AP`), in roster order, so a reader can scan the page by name and say "see competitor 2".
- **Each section has its heading, then a one-line italic purpose.**
- **Same column order in every competitor table:** Update, Impact · Horizon, Confidence, Pipeline implication, Source.
- **Bold is for labels and the one insight per competitor that changes behavior.** Nothing else.
- **A line that must stand alone is its own paragraph**, with a blank line around it. Single line breaks collapse in a Google Doc, an email and a Slack post.
- **One emoji per section header.** Labels keep their own (💰 ❓ 🎯 ✅ 🧩 📡 🔮) and the marks are 🔵 🟡 ⚠️. Use no others.
- **No toggles, no columns, no HTML.** They do not survive Doc, email or Slack.
- **Plain words.** Spell out an acronym once.

## 3. Marks and the scoring rubric

Each update, industry change and competitor row carries one mark with its score. The score comes from the rubric.

| Mark | Meaning | Score | Rule |
|---|---|---|---|
| 🔵 Verbatim | The source says it | 5 | Primary source (newsroom, changelog, filing, regulator), retrieved this run, dated in the period |
| 🔵 Verbatim | The source says it | 4 | Primary source in a saved record, inside its freshness window |
| 🟡 Inferred | We read it from the source | 3 | One credible non-primary source (trade press, analyst), or an inference stated in "why it matters" |
| 🟡 Inferred | A signal, not a plan | 2 | Job posting, partner directory or app-store changelog |
| ⚠️ Uncertain | Weak or ambiguous | 1 | Executive post uncorroborated, single weak or stale source, or contested. State the limit in one short phrase |

**Impact (1 to 5):** how much it changes a live deal for the audience. 5 = changes price, packaging or the buying process now; 3 = changes how a rival is framed; 1 = background. **Horizon:** Now (this quarter's deals), Next (next quarter), Later. Shown together as `5/5 · Now`.

A hiring or partner signal never scores above 2. **Internal inputs are not marks:** a lead from Gong, Slack, Klue, Drive or a saved CI record becomes a claim only when a public page confirms it, and then carries that page's mark (`inputs.md`).

## 4. The issue (fixed order)

````markdown
# Industry Newsletter · Issue [N] · Week [WW]

**[Region(s) presented] · Owned by [team that owns the content]**

*Internal use. No deal data.*

#### This week in one sentence

[One decisive sentence: the highest-impact shift.]

#### Why this matters

[One or two lines: why leadership should care now.]

## 🚀 Competitor Watch

*Product and platform changes by competitor. [n] tracked, [n] changed.*

### 1 · [Competitor]

| **Update** | **Impact · Horizon** | **Confidence** | **Pipeline implication** | **Source** |
|---|---|---|---|---|
| **[Product or platform change]** | [1-5]/5 · [Now/Next/Later] | [mark] [score]/5 | [One sentence, deal-level.] | [Source](url) |
| [Pricing / channel / customer proof / hiring row, only if changed] | … | … | … | … |

🧩 **Enablement note:** [Objection likely to rise, in quotes.] [One or two sentences of talk track.]

### 2 · [Competitor]

…

### [n] · [Competitor with no verifiable change]

No verifiable change as of [date].

## 📊 Industry Changes

*Outside the competitor set, but it could affect pipeline*

| **Change** | **Impact · Horizon** | **Confidence** | **Pipeline implication** | **Source** |
|---|---|---|---|---|
| **[Headline]** ([regulatory / early signal, if so]) | … | … | … | [Source](url) |

## 💬 Decisions & Actions

#### ❓ Decision question

[One question tied to the top move.] **Owner:** [role] · **Decide by:** [date]

#### 🎯 Pipeline impact

| **When** | **What to expect** |
|---|---|
| **Now** | … |
| **Next** | … |
| **Later** | … |

#### 💰 Pricing / Packaging watch

[Status across all competitors in one line: the change, or "No verifiable change found across [n] competitors".] **Watch next week:** [page or event, with link].

#### 🔮 Calls

| **Last issue's call** | **This issue's call** |
|---|---|
| **[Correct / Wrong / Partial / Open].** [The call, one line, with the evidence link.] | [One falsifiable prediction.] Settled by [page or record]; check-in [date]. |

#### ✅ This week's GTM actions

| **#** | **Action** | **Owner** | **By** |
|---|---|---|---|
| 1 | [Action tied to a competitor number or I-number] | [role] | [day] |

*Was this useful? Reply with one word (useful, too long, missing, wrong) and the section.*

## 🔗 Sources & References

*Every link this issue relies on, plus what to save or forward*

| **ID** | **Source** | **Retrieved** | **Source date** | **Priority / read time** |
|---|---|---|---|---|
| S1 | [page or record] · `[URL]` | [date] | [date] | [High / Med / Low, or minutes] |
````

Rules:

- **Title:** `Industry Newsletter · Issue N · Week WW`, WW the ISO week of the issue date.
- **The header line** shows the regions the issue covers and the team that owns the content, nothing else. Category, frequency, audience and the subject line live in `_config.md` and the email cover.
- **Written last:** "This week in one sentence" and "Why this matters" come from the finished body.
- **A competitor table row** needs a link, a mark with its score, an impact and horizon, and a one-sentence pipeline implication. A row without a pipeline implication a seller could use is cut.
- **Bold** the single most decision-relevant update per competitor. The Enablement note appears only for a competitor with an update.
- **Competitors are numbered 1 to n in roster order**; industry changes are I1, I2. Actions cite the number: `1`, `2 · I1`.
- **The pricing watch** rolls the pricing facts across competitors into one status. It repeats no row.
- **Calls:** "Last issue's call" is one line with its evidence link, or "First issue. Nothing to grade yet." The record shown as "x of y" appears only after 3 graded calls, and then in the same cell. The call must be settled by a named page or record.
- **Sources & References** is last. Priority or read time marks what to save or forward; every cited link appears once; a row nothing cites is removed.
- **Not in the document:** a status line, a "Forward to" line, a "Since last issue" block, field questions, a paste-ready snippet, a Held list, a footer. Held items are shown in chat (section 8).

## 5. Platform renderings

The platform is asked once before the first build (SKILL.md Step 2) and saved in `_config.md` as `platform`. A scheduled run reads the saved value and never asks. One primary format per issue.

| Platform | What it produces |
|---|---|
| **Google Doc** (default) | The template above, with 5-column competitor tables. Markdown headings and tables that paste into a Doc as H1/H2/H3/H4 and real tables. Two-line email cover when it will be sent: the email subject (`[Category] \| [headline, 8 words or fewer] \| Week [WW]`) and one line saying who should read which section |
| **Email** | The same sections and order, but each competitor table has **4 columns**: Update, Impact · Horizon · Confidence (together, `5/5 · Now · 🔵 5/5`), Pipeline implication, Source. The email subject goes above the body. No heading shorter than H3 relies on size alone: labels are bold |
| **Slack** | A single post, no tables, no headings, about 220 words, written as below. The full issue is linked last; if no Doc exists the post says "Full issue: saved at `[path]`" |

### Slack post

```text
*Industry Newsletter · Issue [N] · Week [WW]*
[Region(s)] · Owned by [team]

*This week:* [one sentence]

*1 · [Competitor]*
• [Update] · Impact [n]/5 · [Horizon] · [mark] [score]/5 · <[url]|[Source]>
  [Pipeline implication, only where it is the point]
🧩 [Objection in quotes.] [One-line talk track.]

*2 · [Competitor]*
• …

*[n] · [Competitor]:* no verifiable change.

*Industry:* [headline] · Impact [n]/5 · [Horizon] · [mark] [score]/5 · <[url]|[Source]>

*Decision ([role], by [date]):* [question]

*Actions*
1. [Action] · [role] · [day]

*Pricing watch:* [status line]. Next week: [page].
*Last call:* [Correct / Wrong / Open]. *This call:* [one line]
*Full issue + sources:* <[link]|Google Doc>
```

- A Slack post carries every claim's own link, so sources stay one click away; the Sources table lives in the full issue.
- If the post exceeds 250 words, drop the lowest-impact update per competitor, then the Enablement notes for competitors scoring under 3, then stop.
- Replies in the thread that name a section are logged as feedback (`learning-loop.md`); reactions alone are not logged.
- A scheduled run posts only to the channel its prompt names.

Other formats (Word, PDF, slides, Notion, a public edition) are not built in this version: say so and offer the Google Doc.

## 6. Roles

Roles tag every action's owner and the decision's owner. Defaults: **Product, Sales, RevOps, PMM, Pricing.** Optional additions from `_config.md`: CS, Marketing, Partnerships, Finance, Exec. Never a person's name. A role that owns nothing over a four-issue span gets one question: "Drop it from the list?"

| Role | Typically owns |
|---|---|
| Product | roadmap or packaging response; API and platform gaps |
| Sales | talk tracks, objections, deal strategy |
| RevOps | CRM fields, routing, reporting, renewals data |
| PMM | messaging, battlecards, positioning, profile refresh |
| Pricing | price and packaging response, discount guardrails |

## 7. The quiet-week issue

Used when nothing crossed the bar (SKILL.md Step 5). Keep the title, the header line and the handling line, then:

````markdown
#### This week in one sentence

Nothing crossed the bar this week: [one line on what was checked and the newest source date].

## 🚀 Competitor Watch

*[n] verifiable updates this week.*

[The one or two updates found, in the competitor tables, or "No verifiable change: [competitors], as of [date]".]

## 💬 Decisions & Actions

[Decision, or "No decision needed this week: [reason]"; Pipeline impact (may read "No change"); Pricing / Packaging watch; Calls; actions (may be fewer)]

## 🔗 Sources & References
````

Industry Changes is left out unless something qualified. The pricing watch and the call are not optional.

## 8. The Held list (chat only)

Items the issue cannot clear are **not** in the document. After the issue, the chat lists them so the owner can decide before forwarding. An item is held when:

- a claim has no URL retrieved this run ("link pending");
- a claim has a single non-primary source and the one-sentence verdict or the decision relies on it;
- a lead from Gong, Slack, Klue, Drive or a saved record that no public page confirms yet, when the issue leans on it;
- a profile or brain section past its freshness window feeds a row;
- an item was excluded by the collection-method check, named;
- a line was removed by Section 6 `forbidden_claims` or Section 8 `prohibited`, naming the entry;
- a public page contradicts a Klue card or saved profile ("card says X; page says Y; CI owner to update").

Each line says what it blocks and how to clear it. A held claim stays out of the body. The skill never states that anyone reviewed the issue.

## 9. Sources & References

One table at the very end, one line of prose before it. Columns: ID, Source, Retrieved, Source date, Priority / read time. Every link cited above appears once. A saved CI record read (profile, card, deep-dive, signal) is listed with its path and as-of date. A URL appears only if it was retrieved this run or is in a saved record. What was assumed (audience, period, roster source) and which internal inputs were read go in the chat summary and the saved record, not in the document.

## 10. The saved record

`/context/industry-newsletter/YYYY-MM-DD-issue-NNN.md`. Never overwritten; a rebuilt issue gets a new file.

```markdown
---
type: industry-newsletter
issue: [N]
week: [WW]
category: [category]
regions: [regions]
owner_team: [team]
audience: [audience]
platform: google-doc | email | slack
period: [YYYY-MM-DD to YYYY-MM-DD]
built: [YYYY-MM-DD]
roster: [competitor, roster_position; ...]
previous: [previous file name or "none"]
---

[The issue, exactly as delivered.]

## Evidence log

| id | claim | mark | score | source | as_of | conflict |
|---|---|---|---|---|---|---|
| E-1 | [one atomic claim] | [🔵/🟡/⚠️] | [1-5] | [URL or record] | [YYYY-MM-DD] | [none / what] |

## Inputs

| input | kind | what it gave | used for |
|---|---|---|---|
| [path or connector category: tool] | [CI record / connector / paste] | [lead, objection theme, count] | [which block, or "lead only, not confirmed"] |

## Method

- Assumed: [audience], [period], [roster source]
- Records read: [paths and as-of dates]
- Pages retrieved: [count, by competitor and category]
- Connectors: [category: tool, pulled date, or "not connected" / "pasted"]
- Checked against: Section 6 `forbidden_claims`, Section 8 `prohibited`, collection method. Result: [none found / what was removed]
- Loop: [call graded, watchlist rolled, feedback rows read]
- Not done: [what was not researched or supplied]

## Held

- [Item, what it blocks, how to clear it] (or "none")
```

## 11. The weekly task

Schedule it after the profile refresh, so it reads fresh records. Paste into a scheduled task:

> Every Monday at 8:00, use the industry-newsletter skill. My config, including the platform, is in /context/industry-newsletter/_config.md. Read the newest profile for each roster competitor, the cards and deep-dives, the last 7 days of /context/signals/ and the stores in /context/industry-newsletter/. Check the connected Slack channel, Gong themes, Klue cards and Drive folder I named. Grade the last call, roll the watchlist, research the period, build the issue in the saved platform format and save the record. Post to [channel] if the platform is Slack. Do not change the brain, do not apply any proposed change, do not ask questions, and list anything that needs my yes as held.

A scheduled run uses the saved config and the defaults and cannot clear its own held items: it lists them in its summary and leaves them out of the issue.
