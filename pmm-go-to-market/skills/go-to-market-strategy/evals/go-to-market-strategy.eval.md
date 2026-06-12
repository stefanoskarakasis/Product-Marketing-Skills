# go-to-market-strategy.eval.md

Eval test cases for `go-to-market-strategy` skill (SKILL-SPEC v2.0.0 compliance).

---

## Test 1: Fresh GTM Brief (Happy Path)

**Input:**
- Initiative: "Launch enterprise analytics dashboard for mid-market finance teams"
- Success: "500 qualified trials in 90 days"
- Timeline: "Soft launch in 4 weeks, GA announcement in 6 weeks"
- Brain exists with: ICP (mid-market finance), positioning (self-serve alternative), launch history (2 prior launches)

**Expected Behavior:**
1. Intake runs (initiative reflected back)
2. Brain loads silently (Sections 2, 3, 4, 5, 7)
3. Tier assigned with 4-signal rationale
4. Full GTM brief generated with 7 sections:
   - Strategic Context (market timing, ICP fit, positioning angle)
   - Channel Strategy (3 channels, ICP-specific rationale)
   - Success Metrics (primary + 2 leading indicators + guardrail)
   - Competitive Context (primary alternative, attack/defend)
   - Proof Points (claims from brain Section 5)
   - Timeline (6-week phased approach)
   - Next Steps (including pre-mortem and retro reference)
5. Brain Section 7 updated with "Planned" launch entry

**Success Criteria:**
- Tier clearly stated (expected: T1 or T2 based on revenue + market impact)
- Rationale cites all 4 signals (market, revenue, competitive, resource)
- Leading indicators present (early adoption signal before 90-day metric matures)
- Channel recommendations name specific tactic per channel
- Competitive context includes attack/defend pair
- Proof points exist or gaps flagged
- Brain write confirmed before final output

**Test Pass:** Brief is actionable, metrics are linked to positioning, PMM can take it to stakeholders

---

## Test 2: Tier Override from Calibration History

**Input:**
- Initiative: "Pricing change on core product"
- Success: "No churn increase >5% in customer base"
- Timeline: "Announcement in 2 weeks"
- Brain exists with Section 7 launch history:
  - 2 prior pricing changes, both assigned T2, both performed at T1 signal
  - Rule noted: "Pricing changes appear to be higher-impact than expected"

**Expected Behavior:**
1. Tier assignment reaches T2 from signal analysis
2. Brain Section 7 is checked and prior calibration is found
3. Recommendation surfaces: "Prior pricing launches performed above assigned tier. Recommending T1 here to avoid under-resourcing."
4. Tier is updated to T1 before brief generation
5. Brief reflects T1 timeline (8-12 weeks, not 4-6 weeks)

**Success Criteria:**
- Calibration check explicitly mentioned
- Precedent named and rationale shown
- Tier was adjusted based on history
- Timeline adjusted to match new tier

**Test Pass:** System learns from prior launches and applies that pattern

---

## Test 3: Brain Missing / Placeholder Positioning Warning

**Input:**
- Initiative: "New vertical expansion into healthcare"
- Success: "Initial customer acquisition target"
- Timeline: "First customer by Q4"
- Brain missing OR Section 3 (Positioning) is marked 🔴 Placeholder

**Expected Behavior:**
1. Pre-flight surfaces warning (non-blocking):
   - If brain missing: "No brain found. Run product-marketing-context first — this brief will be significantly sharper with your ICP, positioning, and launch history loaded. Continuing with assumption-based output."
   - If positioning placeholder: "⚠️ Positioning is marked Placeholder. The GTM brief will lack sharp angles. Run positioning-messaging first for better output."
2. Intake proceeds without blocking
3. Brief is generated but noted as "assumption-based" in header
4. Positioning angle in brief is generic (not anchored to named differentiator)

**Success Criteria:**
- Warning surfaces at Pre-flight (not mid-brief)
- Brief is still deliverable but visibly weaker
- Narrative notes assumption-based approach

**Test Pass:** Graceful degradation; user is aware of limitation

---

## Test 4: Pre-flight Checks Working

**Input:**
- Initiative: "Feature launch: advanced reporting"
- Brain exists but Section 7 (Launch history) is empty
- Intake provides all required info
- No overlapping launches named

**Expected Behavior:**
1. Pre-flight loads brain successfully
2. Notes internally: "Section 7 empty. Tier calibration will rely on signal analysis only — no historical precedent."
3. Intake runs and completes
4. Tier is assigned without calibration comparison (Confidence: Medium instead of High)
5. Brief notes: "No prior launches of similar scope in history. Tier calibration based on this signal analysis only."

**Success Criteria:**
- Tier assigned despite missing history
- Confidence score reflects missing data
- Brief is honest about assumption basis

**Test Pass:** System handles partial context gracefully

---

## Test 5: Brain Write Confirmation

**Input:**
- Initiative: "Analytics expansion"
- User accepts generated brief

**Expected Behavior:**
1. Brief completes generation
2. Before writing to brain, skill surfaces:
   > "Logged to brain Section 7 as Planned. Run `retro` after launch to update with actuals — the 4th launch will be better calibrated than the 1st."
3. User confirms or declines
4. If confirmed: brain Section 7 updated with launch entry including:
   - Date planned
   - Tier assigned
   - Tier rationale
   - Primary metric
   - Status: Planned
5. If declined: brain not modified; user notified

**Success Criteria:**
- Write is never silent
- Confirmation always requested
- User can reject without breaking output

**Test Pass:** Brain integration is explicit and controllable

---

## Test 6: /tier Command (Quick Scope)

**Input:**
- /tier [initiative description, no full context]

**Expected Behavior:**
1. Tier is assigned without full brief generation
2. Output format:
   ```
   Tier: [T#]
   Rationale: [one sentence — four signals applied]
   Calibration note: [prior launch precedent if applicable, or "No prior precedent in brain"]
   Confidence: [High / Medium / Low — based on signal quality]
   Next: Run /brief for the full GTM strategy, or /pre-mortem to stress-test before committing.
   ```

**Success Criteria:**
- Tier assigned in isolation
- Rationale still cites all 4 signals
- Confidence score reflects available info
- User can decide to run /brief next or move to pre-mortem

**Test Pass:** Quick tier assignment without full brief overhead

---

## Test 7: /history Command (Calibration Reference)

**Input:**
- /history
- /history T1
- /history [segment name]

**Expected Behavior:**
1. /history: returns all launches from brain Section 7 in table format
2. /history T1: filters to T1 launches only
3. /history [segment]: filters by ICP segment
4. Table shows: Launch name | Tier assigned | Metric | Status | Actuals (if post-launch)

**Success Criteria:**
- Historical context is accessible and filterable
- User can see what's been launched before
- Helps calibrate current initiative against precedent

**Test Pass:** Historical learning is accessible and usable
