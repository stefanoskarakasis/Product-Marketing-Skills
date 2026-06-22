---
name: prioritization-frameworks
version: 2.0.0
description: >
  Selects and applies the right prioritization framework (9 frameworks: Opportunity Score, ICE, RICE, Eisenhower, Impact vs Effort, Risk vs Reward, Kano, Weighted Decision Matrix, MoSCoW) with PMM interpretation layer and GTM launch tier output (T1–T4). Reads brain context (ICP, positioning, revenue levers) and guardrails from prior scoring sessions. Logs framework selection, tier assignments, and scoring confidence to /context/skill-sessions.md for meta-synthesis pattern detection and compounds learnings over time.
---

# Prioritization-Frameworks — Skill

## How This Works

Prioritization frameworks are decision tools, not prescriptions. Your job is to pick the right one for the question, apply it with integrity, and translate the output into a tier recommendation (T1–T4) that drives GTM resource allocation.

The skill runs in 6 core steps:

**Step 0** — Load brain context (ICP, positioning, revenue levers) and guardrails from `/context/meta-patterns.md` (e.g., "frameworks without customer confidence >7 have led to 3 T1 overstatements").

**Step 1** — Intake: Understand what you're deciding (launch tier? roadmap backlog? strategic choice?) and what signals you have.

**Step 2** — Framework selection: Based on decision type and available data, recommend the right framework(s).

**Step 3** — Scoring: Run the framework, surface Confidence weaknesses, apply Quality Gates.

**Step 4** — Tier translation: Convert framework output to T1–T4 with one-sentence rationale.

**Step 5** — Audit & recommendation: Pressure-test the tier assignment; deliver go/no-go on tier or recommend additional validation.

**Step 6** — Output: Tier assignment card + scoring table + next step.

**Step 7** — Log session to `/context/skill-sessions.md` with quality score, framework selected, tier assigned, confidence scores, guardrails triggered, and brain updates proposed.

---

## Step 0 — Pre-Flight: Load Context & Surface Guardrails

Before intake, load:
- **Brain context** (Sections 2, 3, 5): ICP, positioning, revenue levers — these anchor how you interpret "Opportunity" and "Impact"
- **Guardrails** from `/context/meta-patterns.md`: If a pattern fired 2+ times in prior scoring sessions (e.g., "RICE without customer data inflates Confidence," "Frameworks applied by committees lose rigor"), surface it now

**Surface guardrails like this:**

```
🔁 PATTERN FROM PRIOR SCORING SESSIONS

I've seen [pattern description] in 2 prior sessions.
Examples: [specific initiatives or decision types]

Quick check: Are you aware of this in your current context?
- If YES → We'll build it into the scoring
- If NO → Let's flag it as we score
```

You can skip a guardrail if you disagree, but you'll see it first.

---

## Step 1 — Intake (Conversational, One Round)

Ask 5 questions, grouped into one conversational block:

1. **What are you deciding?** — Tier a single launch? Prioritize a backlog? Choose between two strategies?
2. **How many initiatives are you comparing?** — One? Three? Twenty?
3. **What signals do you have?** — Customer research? Win/loss data? Internal confidence scores? Nothing yet?
4. **What's your timeline?** — Do you need a decision today, or do you have time to gather more data?
5. **Who's the audience for the output?** — Is this for your own roadmap, or do you need to defend it to leadership?

Adjust depth based on user input. If they're detailed, you have rich context. If they're vague, offer to use a lightweight framework and iterate.

---

## Step 2 — Framework Selection

Based on intake, recommend the right framework. Here's the selection logic:

| Decision Type | Recommended Framework | Why |
|---|---|---|
| Prioritizing customer problems before roadmap | Opportunity Score | Surfaces unmet needs; upper-left quadrant is your target |
| Triaging a launch backlog quickly | ICE | Balances value, confidence, cost; Confidence is your sanity check |
| Building a case for leadership | RICE | Separates Reach from Impact; forces addressable segment clarity |
| New market entry or pricing risk | Risk vs Reward + Confidence | High uncertainty demands explicit Risk mapping |
| Workshop with cross-functional group | Impact vs Effort first, then RICE | Rapid rough sort, then rigorous scoring |
| Launch messaging hierarchy | Kano → feed to value-prop-statements | Must-be vs Attractive vs Delighter |
| Multi-criteria with competing stakeholders | Weighted Decision Matrix | Legitimizes competing priorities; outputs tier-adjacent |
| Scoping deliverables within a tier | MoSCoW | Must-Have / Should-Have / Could-Have |
| Personal launch sprint workload | Eisenhower | Urgency vs Importance; not a strategic framework |

---

## Step 3 — Scoring

Run the selected framework(s).

### Core Frameworks (Formulas & PMM Interpretation)

**Opportunity Score**
```
Score = Importance × (1 − Satisfaction)
Plot: Importance (y-axis) vs Satisfaction (x-axis)
Target: Upper-left quadrant (high importance, low satisfaction)
```
PMM use: Identifies the problems you solve best vs. competitors. If a problem scores high but you don't own it, that's a positioning gap.

**ICE Framework**
```
I = Opportunity Score × Number of customers
C = Confidence (1–10)
E = Ease of implementation (1–10)
Score = I × C × E
```
PMM use: Confidence is your integrity check. If ≥7 without customer evidence, flag it. Low Confidence drags a strong Impact to T3.

**RICE Framework**
```
R = Reach (customers affected)
I = Impact (opportunity score)
C = Confidence (0–100%)
E = Effort (person-months)
Score = (R × I × C) / E
```
PMM use: Reach forces you to define your addressable segment explicitly. This is where PMMs should lead the conversation.

**Risk vs Reward Matrix**
```
Plot: Reward (y-axis) vs Risk (x-axis)
High Reward / Low Risk = T1 candidate
High Reward / High Risk = T2 or T3 with explicit Confidence thresholds
```
PMM use: Essential for pricing, new market entry, positioning pivots. Pull win/loss data to sharpen Risk input.

**Kano Model**
```
Classify: Must-be (table stakes) / Performance (differentiator) / Attractive (delighter)
Messaging priority: Attractive > Performance >> Must-be
```
PMM use: Don't lead launch messaging with Must-be features — they're assumed. Lead with Attractive.

**Weighted Decision Matrix**
```
Assign weights to criteria (must sum to 100)
Score each option 1–10 on each criterion
Weighted score = sum(weight × score)
Build GTM variables (pipeline impact, segment fit, competitive urgency) directly into weights
```
PMM use: Build in cross-functional but GTM-native. Output should be tier-adjacent.

**MoSCoW**
```
Must Have (60% max)
Should Have (20%)
Could Have (15%)
Won't Have (5%)
```
PMM use: Set hard caps before you start. Use to scope launch deliverables within a tier, not to assign the tier.

### Quality Gates (Run After Scoring)

Before delivering any tier recommendation, validate:

1. **Signal integrity** — Is the tier based on evidence or assumption? If no customer data supports the Opportunity Score, flag it.
2. **Confidence honesty** — Confidence ≥7 without customer evidence? That's inflation. Call it out.
3. **Framework fit** — Is the right framework being used? Applying Eisenhower to a launch decision is wrong, not suboptimal.
4. **Tier consistency** — Does the output align with go-to-market-strategy tier criteria?
5. **Actionability** — Does the output tell the PMM what to do next, specifically?

If any gate fails, flag it with an ADVERSARIAL CALLOUT and rewrite before delivering.

---

## Step 4 — Tier Translation

Convert framework output to a T1–T4 tier with one-sentence rationale.

| Tier | Signal | GTM Motion |
|------|--------|-----------|
| **T1** | High Opportunity, large segment, high Confidence, strong strategic fit, competitive urgency | Full GTM. All channels, all teams, exec visibility. |
| **T2** | Strong signal on 2–3 dimensions but not all — real opportunity, limited reach or confidence | Significant launch. Targeted GTM. Not all hands on deck. |
| **T3** | Moderate signal — validated problem, narrow reach, low confidence, or high effort | Soft launch. Focused enablement. Limited external noise. |
| **T4** | Low scores across the board or too early to validate | Internal only, beta, or deprioritize. No GTM investment yet. |

**Output format:** `[T#] — [one sentence why]. Confidence: [C/10]. Next step: [specific action].`

Example: `T2 — Strong customer pain signal in upper-left Opportunity quadrant, but Confidence limited to 6/10 (thin win/loss data). Next step: Run 3 customer conversations to validate pricing elasticity.`

---

## Step 5 — Audit & Pressure-Test

After assigning tier, ask:

1. **Does the framework fit the decision type?** (If not, rerun with different framework)
2. **Is Confidence honestly assessed?** (If ≥7 without evidence, lower it)
3. **Would you bet GTM resources on this tier, or does it need more validation first?**

If pressure-test reveals the tier was inflated, recommend a validation step before full GTM motion. State it clearly.

---

## Step 6 — Output Structure

Deliver three artifacts:

**Artifact 1: Tier Assignment Card (1 page)**
```
Initiative: [Name]
Framework: [RICE / ICE / Other]
Tier: [T1–T4]
Rationale: [One sentence]
Confidence: [#/10]
Key signals: [3 strongest data points]
Next step: [Specific action]
```

**Artifact 2: Scoring Table (1 page)**
```
| Component | Score | Source | Confidence |
|-----------|-------|--------|------------|
| Opportunity | [#] | [Customer research / Internal] | [🟢 🟡 🔴] |
| Reach | [#] | [Segment size / ICP alignment] | [🟢 🟡 🔴] |
| Confidence | [%] | [Win/loss data / Assumption] | [🟢 🟡 🔴] |
| [Other] | [#] | [Source] | [🟢 🟡 🔴] |
```

**Artifact 3: Tier Rationale (2-3 sentences)**
```
Why this tier. What would move it up. What validation is needed before committing GTM resources.
```

---

## Step 7 — Post-Session Logging

Log to `/context/skill-sessions.md` with this YAML metadata:

```yaml
skill: prioritization-frameworks
session_date: [YYYY-MM-DD]
decision_type: [tier / backlog / strategic choice]
initiatives_scored: [count]
framework_selected: [RICE / ICE / Opportunity Score / Risk vs Reward / Kano / Weighted Matrix / MoSCoW]
frameworks_used: [list if multiple]
quality_score: [0-100, where 90+ = all gates passed, Confidence <7 on weak signals]
tier_assignments:
  - initiative: [Name]
    tier: [T1/T2/T3/T4]
    confidence: [#/10]
guardrails_triggered:
  - "[Pattern name if surfaced]"
brain_context_loaded: true
brain_sections_referenced:
  - "ICP (Section 2)"
  - "Positioning (Section 3)"
  - "Revenue Levers (Section 5)"
brain_updates_proposed:
  - "[Emerging pattern or meta-learning, if any]"
confidence_inflation_detected: [true/false, count if true]
gate_failures: [count of Quality Gate failures caught and fixed]
validation_recommended: [true/false, for which tiers/initiatives]
recommendation: "[Proceed with tier / Recommend validation sprint / Recommend re-score]"
output_path: "[Where the tier assignment cards were saved]"
```

**Quality score:** 90+ = All frameworks applied with integrity, Confidence ≥7 backed by evidence, all gates passed. 70+ = Most gates passed, some Confidence slightly inflated. <70 = Multiple gate failures or low data quality.

---

## Operating Rules

- **Load brain context first.** ICP and revenue levers shape how you interpret "Opportunity" and "Reach."
- **Confidence is your integrity check.** ≥7 without evidence = inflation. Call it.
- **Framework fit matters.** Wrong tool = wrong answer. Eisenhower is not a launch decision tool.
- **Quality Gates are not optional.** Run them before delivering any tier.
- **Tier without rationale is incomplete.** Always output one-sentence reasoning + next step.
- **Guardrails surface at Step 0.** If a pattern applies to your decision, you'll see it.
- **Customer evidence > assumption.** If you can't cite a source for Confidence, lower it.
- **Validation before GTM investment.** If a tier is uncertain, recommend validation sprint first.

---

## Self-Improvement Loop

Each session logs to `/context/skill-sessions.md` with:
- Framework selected and why
- Confidence scores and whether they held up
- Tier assignments and whether they were validated later
- Quality Gates passed/failed

Monthly, meta-synthesis reads these logs and detects patterns:
- "RICE without customer data inflates Confidence by 2 points on average" → Guardrail surfaces next time
- "T1 assignments with Confidence <7 lead to GTM churn 60% of the time" → Recommend validation before full motion
- "Eisenhower applied to launch decisions has 0% accuracy vs. RICE" → Update framework selection guide

These patterns feed back into guardrail injection (Step 0) and brain updates (Section 5: Revenue Levers, Section 7: Meta-Learnings).

