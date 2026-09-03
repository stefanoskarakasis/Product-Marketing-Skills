---
name: ideal-customer-profile.eval
version: 1.0.0
description: >
  Eval suite for ideal-customer-profile skill. Tests: brain context
  loading, value-segmentation (not "whoever we have"), the four-layer
  profile discipline, unsourced-claim tagging, the One-Line ICP Test exit
  check, confirmation-gated Section 2 writes, and Learning Close accuracy.
  6 scenarios covering real ICP-building sessions and edge cases.
---

# Ideal-Customer-Profile — Eval Suite

## Setup (Universal)

Each eval:
1. Populates `/foundation/brain.md` with a thin or absent Section 2 (ICP) to test loading/deepening behavior
2. Populates `/context/meta-patterns.md` with guardrails (if testing guardrail surfacing)
3. Provides research data (survey, interview, usage, win/loss), or withholds it to test the intake sequence
4. Runs ideal-customer-profile skill for the given scenario
5. Validates outputs: value-segmentation, four-layer completeness, tagging discipline, confirmation gating

---

## Eval 1: Brain Context Loading (Step 0)

**Scenario:** `/foundation/brain.md` exists with a thin Section 2 (firmographic-only, no behaviors/JTBD/needs). Skill loads it silently and treats this as deepening, not a fresh build.

**Test Data:**
```yaml
# /foundation/brain.md
## Section 2: ICP
Current: "Mid-market B2B SaaS, 50-500 employees"
```

**Expected Output — Context Referenced:**
```
Loaded current Section 2 — firmographic-only right now (mid-market
B2B SaaS, 50-500 employees). Deepening this with behaviors, JTBD, and
needs rather than starting over.
```

**Pass Criteria:**
- Existing Section 2 content loaded silently, stated in one line before Step 1
- Skill does not discard or ignore the existing firmographic data
- Skill explicitly frames the session as deepening, not a fresh build

---

## Eval 2: Value-Segmentation, Not "Whoever We Have"

**Scenario:** User provides usage data covering the full customer base, without segmenting by value. Skill must identify and profile the highest-value cohort rather than averaging across everyone.

**Test Data:**
```
Usage data: 40% of customers churn within 90 days. Of the remaining 60%,
a 15% subset shows 3x the expansion revenue and 2x the time-to-value
speed of the rest.
```

**Expected Output — Cohort Identified, Not Averaged:**
```
Profiling the 15% subset with 3x expansion revenue and 2x faster
time-to-value — that's who the ICP should describe, not an average
across a base that's 40% churned within 90 days. An ICP built on the
average customer describes your churn risk, not your best-fit buyer.
```

**Pass Criteria:**
- Skill identifies and names the specific high-value cohort rather than describing "the average customer"
- Skill explicitly rejects averaging across a mixed-quality base
- The four-layer profile that follows is built from the identified cohort's data, not the full base

---

## Eval 3: Four-Layer Profile Discipline

**Scenario:** User provides rich behavioral and JTBD data but nothing on demographics or needs. Skill must still produce all four layers, flagging gaps rather than skipping them.

**Test Data:**
```
Interview transcript: "We switched because our old tool couldn't handle
approval workflows across regions — that was the whole reason. We
evaluate any new tool now by asking 'does this scale past one region.'"
(No firmographic or stated-needs data provided.)
```

**Expected Output — All Four Layers Present, Gaps Flagged:**
```
Demographics: [A] not established from this data — needs survey or CRM enrichment
Behaviors: Evaluates tools by cross-region scalability as a first filter — CONFIRMED from transcript
JTBD: "Handle approval workflows across regions" — CONFIRMED, the stated switching trigger
Needs: [A] inferred — reliability/predictability at scale, not directly stated
```

**Pass Criteria:**
- All four layers (Demographics, Behaviors, JTBD, Needs) appear in output, none silently omitted
- Layers with real data are populated; layers without data are explicitly marked, not fabricated
- The `[A]` unsourced-claim flag (per skill's own convention) appears on every layer not directly evidenced

---

## Eval 4: Unsourced-Claim Tagging Discipline

**Scenario:** A mix of directly-sourced and inferred claims in one profiling pass.

**Test Data:**
```
Survey response (n=40): "73% cite implementation speed as top purchase driver"
PMM assumption: "They probably also care about vendor stability" (not asked)
```

**Expected Output — Tagged Correctly:**
```
Implementation speed as top driver — sourced directly (survey, n=40, 73%)
Vendor stability as a concern — [A] not sourced, PMM assumption only, needs validation
```

**Pass Criteria:**
- Directly-sourced claims are stated without the `[A]` flag
- Assumed/unvalidated claims carry the `[A]` flag explicitly, every time, not just once per section
- The eventual Section 2 write does not present `[A]`-flagged claims with the same confidence as sourced ones

---

## Eval 5: One-Line ICP Test Exit Check

**Scenario:** A draft profile that's too vague to pass the skill's own exit check — no way to actually identify a real prospect from it.

**Test Data (should fail):**
```
Draft ICP: "Growing companies that need better tools."
```

**Test Data (should pass):**
```
Draft ICP: "VP Ops at 50-200 person remote-first B2B SaaS companies,
currently coordinating cross-team handoffs in spreadsheets, who have
hit a scaling wall in the last 2 quarters."
```

**Pass Criteria:**
- The vague draft is rejected — flagged as failing the One-Line ICP Test, not delivered as final
- The specific draft passes — someone could point at a real company/contact and say "yes, that's this ICP"
- Skill explicitly states the exit check ran and what its result was, not just silently improving the copy

---

## Eval 6: Confirmation-Gated Write and Learning Close

**Scenario:** Full session completes — four-layer profile built, ready to deepen brain Section 2.

**Expected Output — Section 2 Write Shown Before Committed:**
```
Here's exactly what Section 2 will read after this write: [full
before/after shown, all four layers]. Confirm before I save this?
```

**Expected Output — Session Log:**
```yaml
skill: ideal-customer-profile
session_date: 2026-09-01
pattern: "Usage data initially given unsegmented — worth checking
  whether intake should ask for cohort breakdown before analysis
  starts, not after."
source: surprised
```

**Pass Criteria:**
- Section 2 write is shown in full before being committed — no silent write
- Session logged to `/context/skill-sessions.md` with exactly four fields — no separate memory file written
- If nothing notable happened, `pattern: none` is still written — the row is never skipped

---

## Eval Test Coverage Matrix

| Eval | Feature | Pass Criteria |
|------|---------|---------------|
| 1 | Brain context loading (Step 0) | Thin Section 2 loaded silently, treated as deepening |
| 2 | Value-segmentation | Highest-value cohort identified and profiled, not averaged |
| 3 | Four-layer discipline | All four layers present; gaps flagged, not fabricated or skipped |
| 4 | Unsourced-claim tagging | `[A]` flag applied consistently to every unvalidated claim |
| 5 | One-Line ICP Test exit check | Vague drafts rejected; specific drafts pass explicitly |
| 6 | Confirmation gate + Learning Close | Section 2 shown before write; real four-field session-log row |

---

## Running Evals

```bash
# Run all evals
for i in {1..6}; do
  echo "Running eval $i..."
  # [invoke ideal-customer-profile with test data]
  # [validate outputs against pass criteria]
done

# Run single eval
# [invoke ideal-customer-profile with eval N test data]
# [validate against eval N pass criteria]
```
