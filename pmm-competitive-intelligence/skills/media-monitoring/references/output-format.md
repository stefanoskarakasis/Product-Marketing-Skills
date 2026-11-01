# Output Format

Reference for `media-monitoring`. Read it in Step 7 (building the brief) and Step 9 (delivery).

## Contents

1. The layout rule
2. The brief (VP Product Marketing, the default)
3. The first-sweep variant
4. The Slack ping
5. The Monitor section of the weekly board post
6. Other reader views
7. The Doc

---

## 1. The layout rule

- Every field label sits on its own line.
- Important copy sits on its own line.
- Prose is bulleted.
- Two labelled fields never share a paragraph.
- Priority marks: 🔴 needs you, 🟡 watch, ⚪ no action. Confidence in plain words (High, Medium, Low).
- No source tiers, ids or hashes in the body; they live behind `evidence M-id`.

## 2. The brief (VP Product Marketing, the default)

```markdown
## 📡 Competitor Monitor · week of [date]
*Executor: [name] · backup: [name] · last run [day time]*

### 🔴 Needs you this week ([n])
**1. [Competitor] [what happened, in a headline]**
- [Dated fact with the real date]
- [Why our asset is now wrong, one line]
- **Do:** [action] by **[calendar date]**
- **Ready:** [what is drafted]. Reply `do 1`

### 🔁 Still open from last week ([n])
- **[Item]**, due [date]. [Status and age]

### ⚪ No action
- **[Competitor]:** [one line, or "quiet"]

### 🙈 Can you trust the quiet?
[checks read] of [checks attempted] read.
**Blind spots:** [named channels]
```

- Maximum 3 Needs-you items plus 1 own-company item; held-back items are counted in the coverage line.
- A quiet week: "Nothing needs you this week", then No action and the coverage line.
- Footer line: "Reply `do 1`, `evidence M-id`, `acted`, `noise` or `mute <topic>`."

## 3. The first-sweep variant

```markdown
## 📡 Competitor Monitor · baseline · [date]
**Baseline set; nothing to diff yet.**
- Roster: [competitors]
- [n] snapshots saved, first diff next [day]
### 🔴 Needs you ([n])  (items published in the last 30 days only)
### 🙈 Can you trust the quiet?
```

## 4. The Slack ping

Three lines.

- Line 1: week, company.
- Line 2: counts: 🔴 [n] needs you · 🟡 [n] watch · ⚪ [n] quiet, with the top headline.
- Line 3: coverage and the Doc, with the reply options.

## 5. The Monitor section of the weekly board post

Added to the weekly board post in `competitive-profile/references/slack-mode.md` section 10, as bullets and not a table: the Needs-you headlines, the coverage line and "Waiting for [executor]" for open actions.

## 6. Other reader views

- **CEO:** the bottom line, the one decision if any, the risk, and what is being done.
- **Sales:** talk-track changes only, and what is unchanged.

Set per channel in `watchlist.md`. Same data, different rendering.

## 7. The Doc

Sections: Latest brief, Open actions, Watchlist (the one editable section), the 90-day log, monthly reviews and the State Block. If the Doc and `signal-log.md` disagree, the log wins except in the Watchlist section. Slack never wins.
