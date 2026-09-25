---
name: alternatives-map.eval
version: 2.0.0
description: >
  Eval suite for alternatives-map skill. Tests: brain context loading,
  the four-alternative-type discipline (status quo never optional),
  layered mapping per type, status quo's four required elements,
  unsourced-claim tagging, the Named-Not-Abstract exit check,
  confirmation-gated Section 3 writes, and Learning Close accuracy. 7
  scenarios covering real alternatives-mapping sessions and edge cases.
---

# Alternatives-Map — Eval Suite

## Setup (Universal)

Each eval:
1. Populates `/foundation/brain.md` with a thin or absent Section 3
   (Alternatives & Positioning) to test loading/deepening behavior
2. Populates `/context/meta-patterns.md` with guardrails (if testing
   guardrail surfacing)
3. Provides research data (win/loss notes, call transcripts, reviews,
   analyst reports), or withholds it to test the intake sequence
4. Runs alternatives-map skill for the given scenario
5. Validates outputs: four-type discipline, layer completeness, tagging
   discipline, confirmation gating

---

## Eval 1: Brain Context Loading (Step 0)

**Scenario:** `/foundation/brain.md` exists with a thin Section 3 (one
generic "competitors" line, no named alternatives). Skill loads it
silently and treats this as deepening, not a fresh build.

**Test Data:**
```yaml
# /foundation/brain.md
## Section 3: Alternatives & Positioning
Current: "We compete with legacy tools and spreadsheets."
```

**Expected Output — Context Referenced:**
```
Loaded current Section 3 — generic ("legacy tools and spreadsheets"),
no named alternatives yet. Deepening this with named products across
all four alternative types rather than starting over.
```

**Pass Criteria:**
- Existing Section 3 content loaded silently, stated in one line before
  Step 1
- Skill does not discard or ignore the existing content
- Skill explicitly frames the session as deepening, not a fresh build

---

## Eval 2: Status Quo Is Never Optional

**Scenario:** User provides win/loss notes naming only a direct
competitor, with no mention of status quo. Skill must still probe for
status quo rather than mapping only what was volunteered.

**Test Data:**
```
Win/loss notes: "Lost to Salesforce — they already had budget approved
and IT wouldn't approve a second CRM."
(No mention of deals lost to inaction or "no decision.")
```

**Expected Output — Status Quo Probed, Not Skipped:**
```
Named Alternative: Salesforce — chosen because budget was pre-approved
and IT blocked a second CRM; unclaimed territory: no-additional-approval
path for teams with CRM budget committed elsewhere.

Status Quo: [A] not established from this data — every B2B deal has a
do-nothing option even when it isn't named in the notes provided. What
happens today if a prospect doesn't buy anything — a spreadsheet, a
different tool, nothing at all? This needs an answer before the map is
complete.
```

**Pass Criteria:**
- Skill does not silently produce a map with status quo absent
- Skill explicitly asks for or flags the missing status quo rather than
  treating the single competitor as a complete map
- Output states plainly that status quo is required, not optional

---

## Eval 3: Four-Type Discipline, DIY Marked n.v.t. Not Skipped

**Scenario:** Research data covers direct competitors, adjacent tools,
and status quo, but the business genuinely has no DIY/internal-build
alternative (e.g., a narrow technical tool no team would build
in-house). Skill must mark DIY `n.v.t.` explicitly rather than silently
omitting the type.

**Test Data:**
```
Interview: "Prospects compare us to [Competitor A] and to just using
spreadsheets. Nobody's ever mentioned building this internally — it's
too specialized."
```

**Expected Output — Type Marked, Not Dropped:**
```
Direct Competitors: [Competitor A] — [mapped]
Adjacent Tools: Spreadsheets — [mapped]
DIY / Internal Build: n.v.t. — not observed in source data; the tool's
specialization makes internal build uncommon. Flagged as absent, not
silently omitted.
Status Quo: [mapped]
```

**Pass Criteria:**
- All four types appear in the output structure, even when one has no
  content
- The absent type is explicitly marked `n.v.t.` with a stated reason,
  never just missing from the output
- The eventual Section 3 write preserves this explicit `n.v.t.` rather
  than dropping the row

---

## Eval 4: Status Quo's Four Required Elements

**Scenario:** User provides partial status-quo information — the tool
used today and a stated reason, but no quantified cost and no trigger.
Skill must flag the two missing elements rather than proceeding as if
the status quo were fully mapped.

**Test Data:**
```
Sales notes: "They're using a shared Google Sheet to track deals right
now. They said they don't have budget for a new tool."
```

**Expected Output — Gaps Flagged, Not Filled In Silently:**
```
Status Quo: Shared Google Sheet for deal tracking — named specifically.
Cost of inaction: [NEEDS PROOF] — not quantified in source data.
Real reason for inaction: [A] stated reason is "no budget" — the real
reason (risk aversion, unclear ROI, competing priority) is not
established from this data and needs validation.
Trigger to act: [A] not established from this data.
```

**Pass Criteria:**
- All four status-quo elements appear in output structure
- Elements without source data are flagged `[NEEDS PROOF]` or `[A]`,
  never fabricated to look complete
- Skill explicitly distinguishes the buyer's stated reason from the
  unconfirmed "real" reason rather than treating them as the same thing

---

## Eval 5: Unsourced-Claim Tagging Discipline

**Scenario:** A mix of directly-sourced and inferred claims in one
mapping pass.

**Test Data:**
```
Sales call transcript: "We're currently paying $40k/year for [Tool Y]
and it's up for renewal in Q2." (direct quote)
PMM assumption: "They're probably also frustrated with Tool Y's
reporting" (not stated on the call)
```

**Expected Output — Tagged Correctly:**
```
Renewal timing and price as leverage point — sourced directly (call
transcript, $40k/year, Q2 renewal)
Reporting frustration — [A] not sourced, PMM assumption only, needs
validation before it's used as a talking point
```

**Pass Criteria:**
- Directly-sourced claims are stated without the `[A]` flag
- Assumed/unvalidated claims carry the `[A]` flag explicitly, every
  time, not just once per section
- The eventual Section 3 write does not present `[A]`-flagged claims
  with the same confidence as sourced ones

---

## Eval 6: Named-Not-Abstract Test Exit Check, Including Gap-Credibility Test

**Scenario:** A draft map whose "unclaimed territory" claim could
actually be made by another alternative already in the map — must be
caught and rejected, not passed through as a real gap.

**Test Data (should fail — gap not actually unclaimed):**
```
Draft: "Unclaimed territory vs. Competitor A: we're easy to use."
(Adjacent tool, a spreadsheet, is also easy to use — arguably easier.)
```

**Test Data (should pass):**
```
Draft map: "Mid-market ops teams choose between us and Salesforce
because Salesforce is already budget-approved, and leave Salesforce
because per-seat pricing makes it unaffordable to roll out past the
sales team. No mapped alternative can match our flat per-team pricing
at this segment."
```

**Pass Criteria:**
- The "easy to use" gap is rejected — flagged as failing the
  equal-credibility test against the adjacent tool already in the map
- The specific, credibility-tested draft passes — someone could name
  the exact two products and the exact friction point, and no other
  mapped alternative could make the same unclaimed-territory claim
- Skill explicitly states the exit check ran and what its result was,
  not just silently improving the copy

---

## Eval 7: Confirmation-Gated Write and Learning Close

**Scenario:** Full session completes — layered map built across direct
competitor, adjacent tool, and status quo (DIY marked n.v.t.), ready to
deepen brain Section 3.

**Expected Output — Section 3 Write Shown Before Committed:**
```
Here's exactly what Section 3 will read after this write: [full
before/after shown, all four types including the n.v.t. DIY row].
Confirm before I save this?
```

**Expected Output — Session Log:**
```yaml
skill: alternatives-map
session_date: 2026-09-15
pattern: "Status quo wasn't mentioned in the win/loss notes provided —
  had to prompt for it directly. Worth asking for status-quo evidence
  upfront in the intake question next time, not just win/loss notes
  against named competitors."
source: surprised
```

**Pass Criteria:**
- Section 3 write is shown in full before being committed — no silent
  write
- Session logged to `/context/skill-sessions.md` with exactly four
  fields — no separate memory file written
- If nothing notable happened, `pattern: none` is still written — the
  row is never skipped

---

## Eval Test Coverage Matrix

| Eval | Feature | Pass Criteria |
|------|---------|---------------|
| 1 | Brain context loading (Step 0) | Thin Section 3 loaded silently, treated as deepening |
| 2 | Status quo never optional | Probed and flagged even when absent from source data |
| 3 | Four-type discipline | All four types present in structure; absent type marked n.v.t., not dropped |
| 4 | Status quo's four elements | Named, cost, real reason, trigger — gaps flagged, not fabricated |
| 5 | Unsourced-claim tagging | `[A]` flag applied consistently to every unvalidated claim |
| 6 | Named-Not-Abstract + gap-credibility test | Vague or non-unique gaps rejected; specific, tested gaps pass |
| 7 | Confirmation gate + Learning Close | Section 3 shown before write; real four-field session-log row |

---

## Running Evals

Run each of the 7 cases above by invoking `alternatives-map` with that case's test data, then checking the output against that case's pass criteria. Run all 7 in sequence to cover the full suite, or run a single case in isolation to check one behavior.
