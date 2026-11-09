# Update Format

Reference for `weekly-competitive-updates`. Read it in Step 5 (quiet week), Step 9 (build) and Step 11 (the weekly task).

## Contents

1. Header and the fixed order
2. The template
3. Section rules
4. The quiet-week update
5. Threat levels and continuity
6. The weekly task
7. Emoji legend

---

## 1. Header and the fixed order

Eight sections, in this order, no exceptions. One stacked column. Sections 6 and 8 appear only when they have content; sections 1 to 5 and 7 appear in every non-quiet update.

1. Header
2. Executive Summary
3. Recommended Leadership Decisions (always directly after the summary, as one block)
4. Key Takeaways
5. Threat Board
6. Watchlist: Next 30 Days
7. Competitor Deep Dives (Past Week)
8. Data Confidence & Gaps

## 2. The template

```markdown
# 📰 [Company] Weekly Competitive Update

**Skill:** weekly-competitive-updates · **As of:** [run date] · **Window covered:** [start date]–[run date] · **Prepared for:** [name, role, department, market] · **Audience:** C-suite

> 🌐 **Coverage:** [sources swept; what was not covered; which competitors have no items in the window; any assumption about the requester]
>
> 🧮 **Ordering:** By relevance to [Company] and magnitude. This is my read, not a scored output.

## 📌 Executive Summary

- **[DD Mon]** [headline of what changed, most material first]

## 🧭 Recommended Leadership Decisions

1. [Action.] [Rationale tied to this window's evidence.] *Leadership sign-off needed.* (only where it applies)

## 💡 Key Takeaways

1. **[claim]**
   - 📊 **Fact:** [sourced, dated data] ([source](url))
   - 💬 **Interpretation:** [what it means for [Company]]

## 🚦 Threat Board

| **Competitor** | **Threat** | **Change this week** |
|---|---|---|
| [name] | 🟠 ⬆️ | [change; continuity note] |

## 👀 Watchlist: Next 30 Days

- 📅 **Scheduled:** [item] ([source](url))
- 📡 **Weak signal:** [item] *(weak signal)*: [why it is not yet significant] ([source](url))

## 🔎 Competitor Deep Dives (Past Week)

### 🟠 [Competitor]

- **[DD Mon]** · [fact with its figures] · [source](url)
- 👉 *So what:* [one line, only where the implication is not obvious]

## 🧪 Data Confidence & Gaps

- ⚠️ [one line per flag]
```

## 3. Section rules

- **Executive Summary:** headline bullets only, each with its date. No recommended action here.
- **Decisions:** numbered, 2 to 4. No owners. Not carried from an earlier edition unless this week's evidence supports them.
- **Key Takeaways:** 2 to 4, exactly the structure above. Each links the data to a decision or a risk. No generic commentary.
- **Threat Board:** only competitors with a change in the window. Where a level changed since the last edition, say so in the Change column.
- **Watchlist:** scheduled items have a known or expected date inside 30 days. Weak signals are labelled and say why they are not yet significant. Omit the section if nothing material is on it. A line may say what closed since the last edition ("Resolved: [item] happened on 05 Nov").
- **Deep Dives:** one heading per competitor with news in the window, one flat list, most material first, no priority and context split. Use the same emoji as the Threat Board. Background and pre-window items do not belong here; they appear in the Watchlist or Key Takeaways only where they bear on a current decision.
- **Data Confidence & Gaps:** only if something needs flagging: conflicting figures, unverified claims, self-published company data, items excluded for date or source reasons, items removed by a Section 6 or 8 constraint, coverage gaps. One line each.

## 4. The quiet-week update

When no competitor has a qualifying item, do not pad. Build:

1. The header, with the Coverage line naming every competitor swept and every source blocked.
2. One line: "No competitor had a dated item inside the window."
3. The Watchlist, if any scheduled item remains.
4. Data Confidence & Gaps (always, because a quiet week is only trusted if the coverage is honest).

No Threat Board, decisions or takeaways. The threat ledger gets no new rows; the edition is still saved so the next run knows the window was covered.

## 5. Threat levels and continuity

| Level | Mark |
|---|---|
| High | 🔴 |
| Medium-High | 🟠 |
| Medium | 🟡 |
| Low-Medium | 🟢 |

Trend: ⬆️ rising, ⬇️ weakening, ➡️ stable.

- **Continuity:** read the last row for the competitor in `_threat-ledger.md`. If the level changed, write "Raised from Medium in the 02 Nov edition" (or "Lowered from"). If it did not, write nothing about it.
- **No prior row for a competitor:** "First edition for this competitor."
- **No ledger at all:** one line under the Threat Board: "Continuity is limited: no prior edition was available."
- The level is the analyst's read. It is never attributed to a data source, and it is not a score.

## 6. The weekly task

Each scheduled run starts a fresh session, so everything the next run needs is in `/context/weekly-updates/` or the Carry-forward Block. The run is self-contained: it re-runs the source sweep for the window, applies this format and delivers the update. It never asks a question and never runs setup.

Prompt to schedule, for example Monday morning:

```
Run the weekly competitive updates for [Company]. Markets: [list]. Prepared for: [name, role, department, market]. Post to #[channel].
```

Confirm the requester when you create the schedule: that confirmation is what lets a scheduled run use it (for 90 days). Run it by hand twice before trusting the schedule: confirm that the second run reads the first run's edition and shows continuity. Do not schedule it alongside `media-monitoring` on the same pages without telling the sweep to read this skill's items first; two schedules on one page double the effort.

## 7. Emoji legend

Use these and no others. They are part of the fixed layout, so they appear in every update.

| Where | Emoji |
|---|---|
| Title | 📰 |
| Section headings | 📌 Summary · 🧭 Decisions · 💡 Takeaways · 🚦 Threat Board · 👀 Watchlist · 🔎 Deep Dives · 🧪 Data Confidence & Gaps |
| Labels | 🌐 Coverage · 🧮 Ordering · 📊 Fact · 💬 Interpretation · 📅 Scheduled · 📡 Weak signal · 👉 So what |
| Threat level | 🔴 High · 🟠 Medium-High · 🟡 Medium · 🟢 Low-Medium |
| Trend | ⬆️ rising · ⬇️ weakening · ➡️ stable |
| Doubt | ⚠️ unclear date, unverified, self-published or link pending |

Status and results are words, not emoji. The quiet-week update uses the same title, 🌐 Coverage line and 🧪 Gaps heading.
