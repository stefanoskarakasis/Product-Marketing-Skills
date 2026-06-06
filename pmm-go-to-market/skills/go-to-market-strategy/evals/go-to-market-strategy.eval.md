# go-to-market-strategy — Eval Suite
**Skill version:** 2.0.0
**Last updated:** 2026-06-06

---

## Test Case 1: Tier assignment — T1 signal

**Input:**
```
We're launching a fully redesigned enterprise product tier targeting VP-level buyers
at companies 500+ employees. It replaces our current mid-market pricing entirely.
Success = $400K new ARR in 90 days. Launch in 8 weeks.
```

**Expected output includes:**
- Tier assigned as T1 with explicit rationale citing at least two of the four signals
  (market impact, revenue potential, competitive urgency, resource requirement)
- One-sentence rationale before the full brief is generated
- Brief contains all seven sections including Strategic Context, Channel Strategy,
  Success Metrics, Competitive Context, Proof Points, Timeline, Next Steps
- Timeline reflects T1 scope (6–12 weeks total)
- Leading indicator present alongside $400K ARR primary metric
- Next steps include `pre-mortem` and `retro` trigger

**Expected output excludes:**
- Tier assigned as T2 or lower without explicit reasoning challenging T1 signals
- Generic channel list with no ICP-specific rationale
- Brief generated before intake reflection step

**Pass condition:**
T1 is assigned with all four signals addressed, brief contains all seven sections,
and at least one leading indicator is present alongside the primary metric.

---

## Test Case 2: Tier assignment — T3 signal with T1 pressure

**Input:**
```
We're adding dark mode to the product. Our CEO wants to announce it at the
upcoming conference as a big moment. I'm not sure it warrants a full launch.
```

**Expected output includes:**
- Skill reflects back the initiative before tiering
- Tier assigned as T3 (or T2 at most) with rationale that explicitly addresses
  the CEO's desire for a "big moment" vs. the actual market impact signal
- Operating rule applied: tier is based on four signals, not exec pressure
- Acknowledgement that the conference is a channel opportunity, not a tier driver
- Suggested framing: how to use the conference announcement for T3 without
  over-resourcing the launch itself
- "Do Not Use For" routing not triggered (this is appropriate for this skill)

**Expected output excludes:**
- T1 assignment based solely on CEO preference or conference timing
- No challenge to the framing — brief generated without addressing the tier mismatch
- Generic advice about "making a splash" without signal-based rationale

**Pass condition:**
Tier is grounded in the four signals and the skill explicitly distinguishes between
conference timing as a channel tactic vs. T1 market impact signal.

---

## Test Case 3: Edge case — missing brain, no launch history

**Input:**
```
/tier New market entry into healthcare vertical. Targeting mid-size health systems,
100–500 beds. No prior launches in this segment. Goal: 3 signed pilots in 6 months.
```

**Expected output includes:**
- Pre-flight surfaced: brain missing or Section 7 empty — skill continues but flags it
- Calibration note: "No prior precedent in brain — tier assigned on initiative
  signals only"
- Tier assigned (likely T1 or T2 for new market entry) with rationale based on
  available signals
- Confidence level stated: Medium or Low given absence of brain/history
- Recommendation to run `product-marketing-context` before full brief
- /tier command output format followed: Tier, Rationale, Calibration note, Confidence, Next

**Expected output excludes:**
- Tier assigned with High confidence when brain is absent
- Full brief generated from /tier command (that requires /brief)
- Error or refusal — skill should degrade gracefully, not block

**Pass condition:**
Skill surfaces the brain gap non-blockingly, assigns tier with explicit confidence
level, and uses the correct /tier command output format.

---

## Test Case 4: Quality gate — incomplete brief triggers self-check

**Input:**
```
/brief We're launching a competitive battlecard program for the sales team.
Internal enablement. Goal: improve competitive win rate against Competitor X.
Timeline: 3 weeks.
```

**Expected output includes:**
- Tier assigned as T3 (internal enablement, 3-week timeline, single-team effort)
- Quality gate runs silently after brief generation
- Leading indicator present — not just win rate (lagging), but something earlier
  (e.g. % of AEs using battlecard within 2 weeks of launch)
- "Do Not Use For" routing surfaces: this is sales enablement that should also
  involve `competitive-battlecard` skill for the actual battlecard content
- Channel strategy is internal-only (no external channels listed for a T3 internal launch)
- Brief does not include customer-facing channels (LinkedIn, events, etc.)

**Expected output excludes:**
- T1 or T2 tier for internal sales enablement
- External channels in the channel strategy
- Brief delivered without quality gate having run
- No mention of `competitive-battlecard` skill for the battlecard content itself

**Pass condition:**
T3 assigned correctly, brief is internally-scoped, quality gate catches any missing
leading indicator, and routing to `competitive-battlecard` is surfaced in next steps.

---

## Test Case 5: /calibrate command — tier mismatch update

**Input:**
```
/calibrate "Analytics Dashboard Launch" — We assigned T2 but it performed like T1.
Pipeline generated was $280K vs. $90K target. Sales used it in 80% of enterprise deals.
It became our main competitive differentiator for 2 quarters.
```

**Expected output includes:**
- Launch name and assigned tier confirmed
- Actual performance documented
- Calibration verdict: "Under-resourced" — T2 assigned, T1 performance
- Rule proposed in the Self-Improvement Trigger format (🔁)
- Proposed rule is specific: e.g. "When a feature becomes a primary competitive
  differentiator for enterprise ICP, assign T1 regardless of initial scope estimate"
- Offer to update brain Section 7 with actuals
- Rule proposed for `knowledge/gtm/hypotheses.md` with path stated

**Expected output excludes:**
- No calibration verdict — just documenting without evaluating
- Rule proposed without Self-Improvement Trigger format
- Brain Section 7 updated without asking for confirmation

**Pass condition:**
/calibrate command produces verdict, specific rule proposal in correct format,
and asks for confirmation before writing to brain.

---

## Test Case 6: /history command — no history in brain

**Input:**
```
/history
```

**Expected output includes:**
- Skill checks brain Section 7
- If Section 7 is empty or absent: surfaces non-blocking message:
  > "No launch history in brain yet. Run your first launch through `/brief` and
  > confirm the brief to start building your calibration history."
- Suggestion to run `product-marketing-context` if brain itself is missing
- No error or confusing output

**Expected output excludes:**
- Fabricated launch history
- Blocking error that prevents further use of the skill
- Table with empty rows presented as if history exists

**Pass condition:**
Skill handles empty or missing Section 7 gracefully with a clear message and
actionable next step.

---

## Test Case 7: Full session — T2 launch with calibration precedent

**Input:**
```
We're launching a new API integration marketplace. It's targeted at our developer
persona — CTOs and senior engineers at mid-market SaaS companies. Goal: 50 integrations
published by partners in 90 days, which should generate 20% uplift in expansion ARR.
Timeline: 6 weeks. We've launched partner programs before.
```

**Expected output includes:**
- Intake reflected back correctly before tier assignment
- Brain Section 7 checked for prior partner program launches
- If prior launches exist: calibration note references them
- Tier assigned — likely T2 (significant initiative, developer persona, 6-week timeline)
  with four-signal rationale
- Channel strategy includes developer-specific channels (documentation, devrel,
  GitHub, developer newsletters) — not generic B2B channels
- Leading indicator: number of integrations in development pipeline by week 3,
  not just final count at 90 days
- Proof points from Section 5 relevant to partner ecosystem pulled if available
- Brain Section 7 write offered after brief confirmed
- Next steps include `retro` at T+90 days for actuals update

**Expected output excludes:**
- T1 assigned without stronger revenue signal or company-defining market impact
- Channel list that doesn't acknowledge developer persona (LinkedIn ads, cold email)
- No leading indicator — only the 50 integrations lagging metric
- Brief delivered without intake reflection

**Pass condition:**
T2 assigned with developer-appropriate channels, leading indicator present,
calibration history checked, and retro trigger in next steps.
