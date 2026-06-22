---
name: pre-mortem
version: 2.3.0
description: >
  Identifies and pressure-tests failure modes for any strategic initiative (product launch, pricing change, GTM pivot, new market entry, feature rollout) by running a cross-functional risk exercise. Loads brain context (ICP, positioning, competitive landscape) and guardrails from prior pre-mortems; surfaces Tigers (deal-blocking risks) with owner-assigned action plans. Logs session data to /context/skill-sessions.md for meta-synthesis pattern detection and compounds learnings over time.
---

# Pre-Mortem — Skill

## How This Works

A pre-mortem flips the question from "what could go wrong?" to "imagine it's 3 months from now and this initiative failed spectacularly — what happened?" This reframes risk thinking: instead of abstract worries, you get concrete failure narratives grounded in your actual market, team, and competitive context. Your job is to facilitate, not fear-monger.

The skill runs in 7 steps:

**Step 0** — Load guardrails from `/context/meta-patterns.md` (e.g., "pricing changes without competitive posture cost 2 prior launches") and surface them before intake.

**Step 1** — Intake: Gather initiative name, scope, timeline, target customer, and announcement level. Brain-load ICP and positioning to ground discussion.

**Step 2** — Generate failure scenarios using a provocative frame: "It's 3 months out. Revenue missed, team demoralized, customers churned. Why?"

**Step 3** — Classify risks: Tigers (deal-blocking, immediate action needed), Paper Tigers (loud but manageable), Elephants (known risks, accepted trade-off).

**Step 4** — Tiger triage: For each Tiger, assign an owner, define the test or signal that proves it's real, and write the mitigation action plan.

**Step 5** — PMM recommendation: Is the go/no-go decision clear? If Tigers remain unmitigated, flag for leadership.

**Step 6** — Output structure: Deliver a one-page Tiger summary + 2-3 page full risk table + action register.

**Step 7** — Log session to `/context/skill-sessions.md` with quality score, guardrails triggered, risks materialized (if prior pre-mortem), and brain updates proposed.

---

## Step 0 — Pre-Flight: Load Context & Surface Guardrails

Before intake, load:
- **Brain context** (Sections 2, 3, 5): ICP, positioning, revenue levers — you'll reference these during risk generation
- **Guardrails** from `/context/meta-patterns.md`: If a pattern fired 2+ times in prior pre-mortems (e.g., "pricing without comp posture," "launch without sales alignment"), surface it now

**Surface guardrails like this:**

```
🔁 PATTERN FROM PRIOR PRE-MORTEMS

I've seen [pattern description] in 2 prior pre-mortems.
Examples: [specific initiative names]

Quick check: Are you aware of this risk? 
- If YES → We'll dig into it during Tiger triage
- If NO → Let's add it to our failure scenarios
```

You can skip a guardrail if you disagree, but you'll see it first.

---

## Step 1 — Intake (Conversational, One Round)

Ask 6 questions, grouped into one conversational block:

1. **Initiative name** — Feature, pricing change, market entry, GTM pivot, etc.
2. **What's the scope?** — Feature flag rollout? Full migration? Quiet rollout or announcement?
3. **Who's the target customer?** (or: Who does this affect most?) — Reference brain ICP if available
4. **Timeline** — When does it launch? Key milestones?
5. **Announcement level** — P1 major / P2 notable / P3 improvement / P4 minor?
6. **Team readiness** — Sales prepped? Docs done? Eng team confident?

Adjust depth based on user input. If they're verbose, you have rich context. If they're terse, offer to use placeholders and iterate.

---

## Step 2 — Failure Scenario Generation

**Frame it:** "Imagine it's 3 months from launch. Revenue is down 20%. Customer churn spiked. The team is frustrated. Walk me through what happened."

Generate 8–12 failure narratives across these categories. Use brain context (ICP pain points, competitive positioning) to make them specific, not generic:

**Market/Competitive:**
- Competitor launched first / launched better / undercut pricing
- Market shifted (buying behavior changed, macro headwind)
- Positioning didn't land; customers didn't understand why to switch

**Go-To-Market:**
- Sales team unprepared; didn't understand the value story
- Launch messaging missed the mark (wrong persona, wrong angle)
- Announcement didn't reach the right buyers
- Pricing felt out of market vs. competitive set

**Customer/Product:**
- Product quality issue (bugs, performance, UX friction)
- Adoption slower than expected; customers didn't see the value
- Integration failed; customers couldn't use it
- Promised timeline slipped; customers lost trust

**Internal/Execution:**
- Team alignment broke; marketing and product wanted different things
- Rollback decision took too long; damage was done
- Resources diverted mid-launch; team lost focus

---

## Step 3 — Risk Classification

For each failure scenario, place it in one of three buckets:

**Tigers** — Deal-blocking risks. If this happens, the launch fails.
- High likelihood + high impact
- Requires immediate action or decision to proceed
- Example: "Competitor undercuts 40%, we lose enterprise segment"

**Paper Tigers** — Loud but manageable. You can live with it.
- High likelihood but medium/low impact, OR
- Low likelihood but high-drama (very visible if it happens)
- Example: "Some customers confused by new UI" (ships with docs, improves over time)

**Elephants** — Known risks, accepted trade-off.
- You've decided to accept them as part of the launch
- Example: "We're launching without X feature because we're prioritizing Y"

**Classify in real time:** After each scenario, ask the user: "Tiger, Paper Tiger, or Elephant?"

---

## Step 4 — Tiger Triage

For each Tiger, define three things:

**1. Signal/Test** — What would prove this risk is real? (Not prevention, proof.)
- Example: "We'd see churn >15% in the first 30 days" or "Competitor would announce a price cut <5 days of our launch"
- Make it measurable and observable

**2. Owner** — Who owns mitigation? (Name + role required. Not "we." Not "TBD.")
- Example: "Sarah (VP Sales) owns sales alignment" not "Sales owns it"

**3. Action Plan** — What's the mitigation or rollback trigger?
- Mitigation: "Pre-brief sales 2 weeks before launch, run weekly competitive intel stand-ups"
- Rollback: "If churn >15% in first 30 days, pause feature for 2 weeks and iterate on UX"

Write this as a short narrative (3-4 sentences). Avoid bullet lists here — narrative forces clarity.

---

## Step 5 — PMM Recommendation

After Tiger triage, answer: **Can we go, or should we hold?**

**Go** — All Tigers have owners + action plans. You're confident the team understands the risks.

**Conditional Go** — Some Tigers exist, but you've decided they're worth the risk. State the condition explicitly.
- Example: "Go if we lock sales alignment by Friday. If not, hold."

**Hold** — Unmitigated Tigers remain. Leadership needs to make a conscious decision to accept them.
- Example: "We can't ship without testing Competitor Response Risk. That's a blocker."

State your recommendation in one paragraph. Be clear. Be direct.

---

## Step 6 — Output Structure

Deliver three artifacts:

**Artifact 1: Tiger Summary (1 page, one-pager format)**
```
Initiative: [Name]
Timeline: [Key dates]
Recommendation: [Go / Conditional Go / Hold]

Tigers (Deal-Blocking Risks):
1. [Tiger name] — Owner: [Name]. Signal: [measurable proof]. Action: [mitigation/rollback plan]
2. [Tiger name] — Owner: [Name]. Signal: [measurable proof]. Action: [mitigation/rollback plan]
3. [Tiger name] — Owner: [Name]. Signal: [measurable proof]. Action: [mitigation/rollback plan]
```

**Artifact 2: Full Risk Table (2-3 pages)**
```
| Risk Name | Category | Classification | Owner | Mitigation / Rollback |
|-----------|----------|-----------------|-------|----------------------|
| [Risk] | [Market/GTM/Product/Exec] | Tiger/Paper Tiger/Elephant | [Name] | [Action] |
| ... | ... | ... | ... | ... |
```

**Artifact 3: Action Register (1 page)**
```
Owner | Tiger | Signal | Action | Timeline | Status
[Name] | [Tiger name] | [Signal definition] | [Mitigation or rollback trigger] | [Date] | [Pending/Active]
```

---

## Step 7 — Post-Session Logging

Log to `/context/skill-sessions.md` with this YAML metadata:

```yaml
skill: pre-mortem
session_date: [YYYY-MM-DD]
initiative_name: [Name]
initiative_tier: [P1/P2/P3/P4]
quality_score: [0-100, where 90+ = Tigers have owners + measurable signals]
tigers_count: [Number of deal-blocking risks identified]
paper_tigers_count: [Number of manageable risks]
elephants_count: [Number of accepted trade-offs]
guardrails_triggered:
  - "[Pattern name if surfaced]"
brain_context_loaded: true
brain_sections_referenced:
  - "ICP (Section 2)"
  - "Positioning (Section 3)"
  - "[Other sections loaded]"
brain_updates_proposed:
  - "[Emerging pattern or meta-learning, if any]"
pre_mortem_accuracy: [If this is a follow-up, compare predicted vs. materialized risks — did the Tigers we ID'd actually happen?]
risks_materialized_count: [Number of predicted Tigers that actually occurred]
recommendation: "[Go / Conditional Go / Hold]"
decision: "[User decision: approved, holding, or conditional]"
output_path: "[Where the Tiger summary + risk table were saved]"
```

**Quality score:** 90+ = Tigers have owners, signals, and action plans. 70+ = Most Tigers defined but some actions vague. <70 = Risk analysis incomplete.

**Pre-mortem accuracy tracking:** If the user has run a prior pre-mortem and we're now reviewing whether the predicted risks materialized, log `risks_materialized_count` and compare against `tigers_count`. This feeds meta-synthesis pattern detection for calibration.

---

## Initiative Type Modifiers

Adjust intake and scenario generation by initiative type:

**Feature Launch:**
- Add: product quality, adoption friction, UX learning curve
- Less emphasis on: competitive response (unless adjacent feature exists)

**Pricing Change:**
- Add: customer reaction, competitive response, sales alignment
- Less emphasis on: product quality (existing product), adoption friction (change management, not feature friction)

**New Market Entry:**
- Add: market viability, competitive entry, sales infrastructure readiness
- Less emphasis on: product quality (assume product-market fit in existing market)

**GTM Pivot:**
- Add: sales team alignment, messaging clarity, channel readiness
- Less emphasis on: product (assume stable), market timing (known market)

---

## Rules of Engagement

**Surface Tigers first.** After classification, discuss Tigers before Paper Tigers — they're the ones with owners and action plans.

**Assume worst-case thinking.** Don't be optimistic. If you say "the team will figure it out," that's not a plan. Make it concrete.

**Owners are required.** Every Tiger gets a person's name and role. "Marketing owns it" is not an owner.

**Signals are measurable.** "We'd see low adoption" is vague. "We'd see <500 signups in the first week" is measurable.

**Action plans bridge risk to decision.** If you can't mitigate a Tiger, that's fine — but then you're saying "we're accepting this risk and here's how we'll respond if it happens."

---

## Self-Improvement Loop

This skill learns from prior pre-mortems. Each session logs to `/context/skill-sessions.md` with:
- Tigers identified
- Risks that actually materialized
- Guardrails that surfaced and proved useful

Monthly, meta-synthesis reads these logs and detects patterns:
- "Pricing changes without competitive posture have failed 3x" → Guardrail surfaces next time
- "Feature launches with <2-week sales prep have 80% Tiger materialization rate" → Recommend 3-week prep
- "Tigers with named owners have 70% mitigation success; Tigers without owners fail" → Emphasize owner assignment

These patterns feed back into guardrail injection (Step 0) and brain updates (Section 2: Anti-ICP, Section 5: Revenue Levers, Section 7: Meta-Learnings).

