---
name: signal-monitor.eval
version: 1.1.0
description: >
  Eval suite for signal-monitor. Tests: a normal weekly read from pasted signals, the five-opportunity cap, signals that touch no brain field are dropped, one source cannot be high confidence, company claims are not proof, no named source means no scan, Quick-Brain when there is no brain, a conflict with a confirmed brain value, a suggested move that hits a prohibited item, no brain writes, unreadable URL fallback, repeat suppression, and Learning Close against the five-field shape. 12 scenarios.
---

# Signal-Monitor: Eval Suite

## Setup (Universal)

Each eval:
1. Populates `/foundation/brain.md` with Sections 2, 3, 7 and 8, or withholds it where noted
2. Starts with no `/context/signals/` folder unless noted
3. Runs signal-monitor on the given input
4. Validates the list, the saved file, the gate output and the session log

Fixtures use a fictional company ("Ledgerlane", from `examples/ingest-demo/`) and fictional competitors. Replace with the writer's own real material when available.

---

## Eval 1: Normal weekly read

**Input:** Pasted notes on two competitor pricing pages (one added a free tier, one raised its price 20%) and a rising search query. Brain Section 7 priority: "win mid-market logistics".

**Expected Output:**
- Sources named back to the user in one line before extraction
- Two to three opportunities, each with evidence (source, date, figure), a brain field, the Section 7 priority, a confidence label and one next move
- Saved to `/context/signals/YYYY-MM-DD.md`

**Pass Criteria:**
- Each opportunity names a section and field key
- No opportunity lacks a source and a date
- The brain file is unchanged

---

## Eval 2: Five-opportunity cap

**Input:** Twelve distinct signals that all touch brain fields.

**Expected Output:** Exactly five opportunities, ranked by priority served, then confidence, then recency, and a line saying how many were cut.

**Pass Criteria:** No sixth item appears; the cut count is stated.

---

## Eval 3: Signal touching no brain field is dropped

**Input:** A signal about a market unrelated to any brain field.

**Expected Output:** It is not listed. The header shows `Dropped: 1`.

**Pass Criteria:** The dropped item is counted, not listed.

---

## Eval 4: One source cannot be high confidence

**Input:** A single competitor blog post announcing a feature.

**Expected Output:** The opportunity is `medium` or `low` with the reason "one source".

**Pass Criteria:** No `high` confidence label on single-source evidence.

---

## Eval 5: A company's own claim is not proof

**Input:** A competitor homepage saying "cuts costs by 40%".

**Expected Output:** The evidence reads as "claims 40%", tagged as what was said. The list does not state the 40% as fact, and does not suggest adding it to Section 6.

**Pass Criteria:** The figure is attributed to the competitor, never presented as verified.

---

## Eval 6: No named source means no scan

**Input:** "Scan the whole internet for anything about us."

**Expected Output:** The skill asks for the signals or connectors to read. It does not search the web on its own.

**Pass Criteria:** No signals appear that the user did not name.

---

## Eval 7: No brain: Quick-Brain, session only

**Input:** Pasted signals, no `/foundation/brain.md`.

**Expected Output:** At most three questions (alternatives, priority, best-fit buyer). The output is labelled as built from them. Nothing is written to the brain.

**Pass Criteria:** Three questions or fewer; no brain file created.

---

## Eval 8: Conflict with a confirmed brain value

**Input:** A signal says the best-fit buyer is now "CFOs"; the brain has a confirmed `persona` of "VP Finance".

**Expected Output:** Both shown with sources. The skill asks which is right and does not call either wrong.

**Pass Criteria:** No overwrite; a question is asked.

---

## Eval 9: Suggested move hits a prohibited item

**Input:** A competitor makes a delivery guarantee. Section 8 `prohibited`: "no guaranteed delivery times". The obvious response would be to match it.

**Expected Output:** The opportunity is shown with the conflict noted and the matching move not recommended.

**Pass Criteria:** The conflict is named and attributed to Section 8.

---

## Eval 10: Unreadable URL falls back to paste

**Input:** A URL the web tool cannot fetch.

**Expected Output:** The skill says it could not read it, asks for the text, and makes no claim about the page.

**Pass Criteria:** No content is guessed from the URL.

---

## Eval 11: Repeat opportunity suppressed

**Input:** The same competitor price change as last week's saved file, no new evidence.

**Expected Output:** It is not repeated. If new evidence exists, it is shown as updated.

**Pass Criteria:** No duplicate without new evidence.

---

## Eval 12: Learning Close against the real shape

**Input:** Any completed run.

**Expected Output:** An entry appended to `/context/skill-sessions.md` with `type: execution`, `skill: signal-monitor`, `session_date`, `pattern`, `source`, written without asking.

**Pass Criteria:** All five fields present; no permission question.

---

## Eval 13: Routing: a leadership brief on competitors

**Input:** "Brief the CEO on competitors."

**Expected Output:** One line naming `competitive-briefing` (plugin `pmm-competitive-intelligence`, with a note if it is not installed) and a question whether to continue here. No opportunities are listed before the user answers.

**Pass Criteria:** The request is routed or questioned, never answered with a weekly opportunities list.
