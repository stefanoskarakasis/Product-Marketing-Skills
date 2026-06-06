# beachhead-segment — Eval Suite
**Skill version:** 1.0.0
**Last updated:** 2026-06-06

---

## Test Case 1: /decompose — broad ICP decomposed into scoreable candidates

**Input:**
```
/decompose

[Brain Section 2 ICP: "Mid-market B2B SaaS companies, 50–500 employees,
any industry, using multiple disconnected sales and marketing tools"]
```

**Expected output includes:**
- Skill reads brain Section 2 ICP before decomposing
- ICP is flagged as too broad to score directly — "mid-market B2B SaaS" is
  not a single scoreable segment
- 2–4 distinct sub-segments produced with one-line rationale per candidate:
  e.g. RevOps teams at B2B SaaS (50–200 employees), Sales ops at PLG companies,
  Marketing ops at mid-market SaaS with field sales
- Each sub-segment is specific enough to score on four dimensions
- Ends with offer to run /score on the decomposed candidates

**Expected output excludes:**
- Scoring before /decompose completes — /decompose produces candidates, not scores
- Generic industry verticals as decomposition output (e.g. "fintech, healthtech,
  edtech") — these are industries not sub-segments of the stated ICP
- Single sub-segment output — minimum 2 candidates for comparison

**Pass condition:**
Output contains 2–4 specific, scoreable sub-segments derived from the brain ICP,
each with a one-line rationale, with no scoring attempted.

---

## Test Case 2: /score — Gate 1 blocks a low-pain segment

**Input:**
```
/score enterprise HR tech vs SMB HR tech vs fintech compliance teams
```

**Expected output includes:**
- All three segments scored on all four dimensions before gates are applied
- Enterprise HR tech scores low on Burning Pain (e.g. 2) — large procurement
  cycles, problem is chronic not acute
- Gate 1 applied: Enterprise HR tech explicitly eliminated with reason:
  "Burning Pain score of 2 — no urgency signal; HR transformation is a
  multi-year initiative, not an acute problem"
- Scorecard shown for all three segments including the eliminated one
- Recommendation made from the remaining qualifying segments
- Eliminated segments section at bottom with specific gate and reason

**Expected output excludes:**
- Enterprise HR tech passing Gate 1 with a score of 2
- Elimination without naming the gate applied
- Recommendation made before all three segments are scored
- Generic elimination reason ("didn't score well enough")

**Pass condition:**
Gate 1 explicitly fires on the low-pain segment, elimination is documented
with the specific score and reason, and recommendation comes from qualifying
segments only.

---

## Test Case 3: /score — Assumption flags reduce confidence

**Input:**
```
/score legal tech vs compliance tech

[Brain Section 4 (Competitive) is empty — no competitive landscape data]
[Brain Section 5 (Proof points) is empty — no customer evidence]
```

**Expected output includes:**
- Pre-flight surfaces empty Sections 4 and 5 before scoring begins
- Winnability dimension marked `[A]` for both segments — competitive positions
  cannot be scored without Section 4 data
- Burning Pain marked `[A]` for at least one segment — no proof point evidence
- Scorecard shows `[A]` flags visibly next to affected dimension scores
- Confidence capped at 🟡 (not 🟢) because more than 2 dimensions rely on
  assumptions across the top candidate
- Recommendation is conditional:
  > "🟡 Conditional — validate [specific assumptions] before committing GTM investment"
- Assumption flags listed explicitly at bottom of scorecard

**Expected output excludes:**
- 🟢 confidence with empty brain sections
- Winnability scored as if competitive data were available
- Assumption flags absent from scorecard
- Unconditional recommendation despite missing evidence

**Pass condition:**
`[A]` flags appear on affected dimensions, confidence is 🟡, and recommendation
is explicitly conditional with named validation actions.

---

## Test Case 4: /audit — Expansion trigger hit, recommend expanding

**Input:**
```
/audit

[Brain Section 2 shows: fintech compliance teams confirmed as beachhead,
scored 90 days ago, Pain 4 / WTP 4 / Winnability 4 / Referral 3 = 15/20.
90-day trigger: 5 signed reference customers in fintech compliance.
Current evidence: 7 signed customers, 3 have provided case studies,
win rate in segment is 68%.]
```

**Expected output includes:**
- Audit reads original scores from brain Section 2 before running fresh assessment
- Original scores shown alongside current scores
- Current scores re-assessed with updated evidence — likely equal or improved
- 90-day trigger status checked: "Hit — 7 customers vs 5 target, win rate 68%"
- Expansion trigger explicitly stated as met
- Recommendation: "Expand — beachhead is proven. Move to [adjacent segment] now."
- /pathway offered as next step to plan the expansion sequence

**Expected output excludes:**
- Audit ignoring the original scores in brain
- Fresh scoring without comparing to baseline
- Recommendation to "stay" when trigger is clearly met
- No mention of expansion trigger status

**Pass condition:**
Original scores compared to current, expansion trigger explicitly evaluated,
"Expand" recommendation made with clear rationale, /pathway offered.

---

## Test Case 5: /eliminate — stakeholder pressure to add a segment

**Input:**
```
/eliminate enterprise financial services — our CEO wants to pursue it but we've
looked at this before and the sales cycle is 18+ months and incumbents like
Salesforce Financial Services Cloud own the category
```

**Expected output includes:**
- Segment eliminated and logged with user's stated reason
- Gate applied: Winnability floor (cannot dominate in 12–18 months)
- Specific evidence cited from user input: 18+ month sales cycle, Salesforce FSC
  incumbent
- Logged to brain Section 2 under Eliminated Segments
- Optional: skill surfaces what it would take to revisit this segment
  (e.g. "Revisit if win rate vs Salesforce FSC improves above 30% or if segment
  access changes via partnership")

**Expected output excludes:**
- Segment kept open for reconsideration without clear trigger
- Elimination without naming the specific gate
- Brain write without confirmation from user

**Pass condition:**
Segment explicitly eliminated, gate named, evidence cited, logged to
brain Section 2 with user confirmation.

---

## Test Case 6: Referral Potential as tiebreaker

**Input:**
```
/score B2B legal ops vs B2B compliance ops

[Both score similarly on Pain (4/4), WTP (3/3), Winnability (3/3).
Legal ops: buyers are General Counsels who attend the same ALM and Legal
Tech conferences, active peer communities, reference customers have driven
3+ warm introductions each.
Compliance ops: buyers are fragmented across industries, no shared community,
references are willing to speak but don't proactively refer.]
```

**Expected output includes:**
- Both segments score similarly on Pain, WTP, and Winnability
- Referral Potential scores diverge: Legal ops 5, Compliance ops 2
- Skill explicitly calls out Referral Potential as the differentiating dimension
  rather than hiding it in the aggregate score
- Recommendation: Legal ops as beachhead — not just because of higher total,
  but because the referral network means the beachhead compounds
- Operating rule surfaced: "Legal ops scores 4+ on Referral Potential with
  moderate scores elsewhere — this is often the right choice. A beachhead
  that compounds is worth more than a higher-scoring segment that doesn't."
- Expansion pathway shows Compliance ops as Stage 2 target once Legal ops
  is proven

**Expected output excludes:**
- Aggregate score comparison only with no narrative on Referral Potential
- Legal ops recommended without explaining why Referral matters strategically
- Compliance ops recommended despite 2 on Referral

**Pass condition:**
Referral Potential explicitly called out as the tiebreaker with strategic
explanation, Legal ops recommended with compounding logic, and Compliance ops
positioned as Stage 2 in the pathway.

---

## Test Case 7: Single segment input — skill challenges before scoring

**Input:**
```
We've decided our beachhead is fintech. Just score that for us.
```

**Expected output includes:**
- Skill does not immediately score fintech in isolation
- Operating rule applied: "Single-segment scoring is not a choice"
- Challenge surfaced:
  > "One segment isn't a choice — it's an assumption. Name at least two so we
  > have something to compare against. What else have you considered and rejected?"
- If user names a second candidate, scoring proceeds
- If user insists on fintech only: skill scores it but with a caveat that
  without comparison, the recommendation is a validation, not a decision

**Expected output excludes:**
- Immediate scoring of fintech without requesting a comparison candidate
- Compliance with the single-segment request without any challenge

**Pass condition:**
Skill challenges the single-segment input before proceeding, requests at least
one comparison candidate, and only scores after the challenge is addressed.
