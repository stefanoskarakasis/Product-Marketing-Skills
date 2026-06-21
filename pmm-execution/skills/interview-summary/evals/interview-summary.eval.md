# interview-summary — Evaluation Test Cases

**Skill:** interview-summary  
**Version:** 2.1.0  
**Total test cases:** 6  
**Coverage:** Standard case, edge cases, error handling, context-writing, hypothesis promotion

---

## Test Case 1: Full Transcript → Complete JTBD Synthesis (Standard Case)

**Input:**
```
Interviewee: VP of Revenue Operations, 150-person B2B SaaS company. Matches ICP.
Interview type: Discovery
[Full transcript of 3000+ word discovery call discussing reporting pain, current Tableau setup, and desire to unify data sources]
```

**Expected output includes:**
- ✅ Metadata: Date, Participants (with title + company), Interview type, 🟢 High confidence, ICP match: Yes
- ✅ Background section: Title, company size, team structure
- ✅ Current solution: "Tableau + Snowflake + manual CSV exports"
- ✅ What they like: ≥2 strengths with Job satisfaction mapping
- ✅ Problems section: ≥3 JTBD blocks, each with Job, Desired outcome, Importance, Satisfaction, Verbatim signal
- ✅ Key Insights: ≥3 analytical observations (no quotes)
- ✅ Action Items table: ≥2 actions with named owners (not placeholders) and real dates
- ✅ Flags: ≥1 flag (e.g., "Infrastructure constraint preventing data consolidation")
- ✅ Signal Quotes: ≥3 verbatim quotes with speaker and context
- ✅ Pattern Signal: Explicitly states match to existing patterns or marks as "New signal for tracking"

**Expected output excludes:**
- ❌ Placeholder text like [Name], [Date], YYYY-MM-DD
- ❌ Quotes in Key Insights section (those belong in Signal Quotes)
- ❌ Vague action items ("Follow up", "Think about")
- ❌ ICP match defaulted to "Yes" without reasoning
- ❌ Verbatim quotes marked as paraphrases

**Pass condition:** Summary contains all required sections, all placeholders filled, Metadata complete, ≥3 Jobs with all fields, ≥3 signal quotes, 🟢 High confidence justified.

---

## Test Case 2: Sparse Notes → Confidence-Flagged Output (Edge Case)

**Input:**
```
Interviewee: Product Manager, company unknown, segment unclear
Interview type: Not specified
[Rough bullet-point notes: "Struggling with reporting. Wants real-time dashboards. Current tool slow. Lots of manual work."]
```

**Expected output includes:**
- ✅ Confidence: 🔴 Low — rough notes only
- ✅ Warning block prepended: "⚠️ Low-confidence summary. Findings below are based on thin input. Do not route downstream without a follow-up or validation pass."
- ✅ ICP match: "Unknown — insufficient context to assess"
- ✅ Background section: "PM at undisclosed company" (incomplete but honest)
- ✅ Current solution: "Identified as slow manual reporting tool"
- ✅ Problems: ≥1 identifiable Job (e.g., "Real-time reporting"), but marked with caution
- ✅ Action Items: Includes "Schedule follow-up call for deeper discovery"
- ✅ Flags: "Sparse input. Follow-up needed before routing downstream."

**Expected output excludes:**
- ❌ Confidence marked as 🟢 High or 🟡 Medium (should be 🔴)
- ❌ ICP match marked as "Yes" (should be "Unknown")
- ❌ Verbatim quotes (should note "No verbatim quotes available")
- ❌ Actionable insights treated as definitive (should add caution caveats)

**Pass condition:** Confidence is 🔴 Low, warning block surfaces, no confidence inflation, follow-up action created, sparse input flagged but synthesis attempted.

---

## Test Case 3: Competitor Named as Solution → Routing Flag (Integration Case)

**Input:**
```
Interviewee: Sales Manager, mid-market SaaS
Interview type: Win-loss (lost to competitor)
[Transcript where interviewee states: "We chose Salesforce because it integrates with our ERP and has better mobile reporting than your platform."]
```

**Expected output includes:**
- ✅ Metadata: Interview type: Win-loss
- ✅ Current solution: "Salesforce (recently selected)"
- ✅ Key Insights: "Chose competitor primarily for ERP integration and mobile-first reporting. Our strength in [X] was insufficient to overcome mobility gap."
- ✅ Signal Quotes: Exact quote about Salesforce, ERP integration, mobile gap
- ✅ Flags: "Competitor mentioned: Salesforce. Gap identified: Mobile reporting UX. Routing to hs-competitive-battlecard for LEARN mode."
- ✅ Pattern Signal: "New signal for tracking: ERP integration as critical buying criterion in this segment"
- ✅ Routing note: "This finding should trigger hs-competitive-battlecard LEARN mode on Salesforce mobile capabilities."

**Expected output excludes:**
- ❌ Competitor name buried or omitted
- ❌ Integration gap not highlighted
- ❌ No routing suggestion to hs-competitive-battlecard
- ❌ Loss reason treated as generic ("They chose someone else")

**Pass condition:** Competitor explicitly named, gap identified, routing flag created, signal logged for future learning.

---

## Test Case 4: ICP Mismatch → Flag & Reasoning (Validation Case)

**Input:**
```
Interviewee: CTO at 15-person startup, early-stage (Series A)
ICP: VP/Head of Marketing, 50–500 person companies, Series B+
Interview type: Discovery call (inbound inquiry)
[Transcript about their data infrastructure needs]
```

**Expected output includes:**
- ✅ Metadata: ICP match: "No — Company is Series A (target: Series B+), company size 15 (target: 50–500)"
- ✅ Background: "CTO at 15-person Series A startup" (non-ICP segment noted)
- ✅ Flags: "ICP Mismatch: Interviewee is Series A founder/CTO, not marketing leader. Insights may apply to different buyer personas but don't validate core ICP hypothesis."
- ✅ Key Insights: "Useful data point on early-stage infrastructure challenges, but distinct from Series B+ mid-market GTM pain. Consider creating separate early-stage persona hypothesis."
- ✅ Pattern Signal: "New signal for tracking: Early-stage founder pain around data infrastructure. Not core ICP, but adjacent segment worth monitoring."

**Expected output excludes:**
- ❌ ICP match defaulted to "Yes"
- ❌ ICP mismatch ignored or treated as minor
- ❌ Insights routed to positioning team without ICP caveat
- ❌ No mention of segment difference

**Pass condition:** ICP match explicitly assessed with reason, mismatch flagged with reasoning, insights contextualized, adjacent segment noted for future tracking.

---

## Test Case 5: Pattern Confirmation (3+ Interviews) → Hypothesis Promotion Gate (Self-Improvement Case)

**Input:**
```
Interviewee: Head of Sales Ops, enterprise SaaS (third discovery call with same pattern)
Prior sessions context: /context/interviews/hypotheses.md contains:
- Hypothesis: "Enterprise buyers prioritize forecast accuracy over UI polish" (2 confirmations)
Interview type: Discovery
[Transcript confirms this pattern for the third time with explicit quote about forecast accuracy being non-negotiable]
```

**Expected output includes:**
- ✅ Pattern Signal: "Matches existing pattern: 'Enterprise buyers prioritize forecast accuracy over UI polish'. Confirmation count: 3/3. Promotion ready."
- ✅ Self-Improvement Trigger surfaces:
  ```
  🔁 SELF-IMPROVEMENT TRIGGER
  Pattern: Enterprise buyers consistently prioritize forecast accuracy over UI polish across all discovery calls
  Occurrences: 3 interviews (this is third confirmation)
  Proposed update: "RULE: Enterprise segment (50–500 person) hiring decision driven by forecast accuracy. Messaging should emphasize accuracy + governance before design."
  Location: /context/interviews/rules.md
  Awaiting approval before encoding.
  ```
- ✅ Offer to update rules: "Want me to add this to rules.md? I'll apply it to future syntheses once approved."
- ✅ No silent encoding: Approval gate explicit before any write to rules.md

**Expected output excludes:**
- ❌ Pattern treated as isolated finding (not connected to prior 2 confirmations)
- ❌ Hypothesis promotion encoded silently (without approval)
- ❌ Self-Improvement Trigger not surfaced
- ❌ Confirmation count not tracked

**Pass condition:** Confirms third occurrence, surfaces promotion gate explicitly, waits for approval, offers skill improvement, no silent writes.

---

## Test Case 6: Context Write with Missing Directory → Graceful Handling (Error Handling)

**Input:**
```
Interviewee: Product Manager, Series B company
Interview type: Discovery
[Standard transcript]
Context: /context/interviews/ directory does not exist (missing on first run)
```

**Expected output includes:**
- ✅ Summary generated normally (synthesis not blocked)
- ✅ Non-blocking notice surfaces: "⚠️ No context directory found (/context/interviews/). Synthesis complete — but learnings not persisted to context. To enable pattern learning, create /context/interviews/ and rerun synthesis."
- ✅ Session metadata provided: "To save this session: Create /context/interviews/sessions/ and paste the summary there manually, or run synthesis again once /context/ is set up."
- ✅ Pattern findings captured in summary but not written to files
- ✅ No error, no crash, skill continues gracefully

**Expected output excludes:**
- ❌ Error message or crash
- ❌ Synthesis blocked or incomplete
- ❌ Attempt to force-write to missing directories
- ❌ Silent failure (user unaware learning wasn't persisted)

**Pass condition:** Synthesis completes, context writes skipped gracefully, non-blocking notice surfaces, user understands why patterns not persisted.

---

## Scoring Rubric

For each test case, mark:
- ✅ **Pass** — All "Expected output includes" present, all "Expected output excludes" absent
- ⚠️ **Partial** — 75%+ of expected content present, minor gaps acceptable
- ❌ **Fail** — <75% of expected content, critical section missing

**Overall score:**
- **6/6 Pass** = 19/19 skill compliance
- **5/6 Pass + 1 Partial** = 18/19
- **<5 Pass** = Below threshold, skill needs revision

---

## Test Case Results

| Test Case | Expected | Actual | Status |
|---|---|---|---|
| 1. Full Transcript → JTBD (Standard) | ✅ Complete synthesis | — | Pending |
| 2. Sparse Notes → Flagged (Edge) | 🔴 Low confidence + warning | — | Pending |
| 3. Competitor Named → Routing (Integration) | ✅ Competitor flag + routing | — | Pending |
| 4. ICP Mismatch → Assessed (Validation) | ✅ Mismatch noted + reasoning | — | Pending |
| 5. Pattern Confirmed (3+) → Promotion Gate (Self-Improvement) | 🔁 Gate surfaces + awaits approval | — | Pending |
| 6. Context Missing → Graceful (Error Handling) | ⚠️ Non-blocking notice | — | Pending |

**Overall eval status:** Pending execution  
**Pass threshold:** 6/6 ✅  
**Current score:** —/6
