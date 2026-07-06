---
name: go-to-market-strategy
version: 2.2.0
description: >
  Assigns launch tier (T1–T4) using four-signal framework and generates complete GTM brief with positioning angles, channel strategy, success metrics, and competitive context; reads brain (ICP, positioning, competitive, proof points, launch history) and guardrails from prior launches; writes to brain Section 7; logs session data to /context/skill-sessions.md for meta-synthesis pattern detection and compounds learnings over time.
---

# Go-to-Market-Strategy — Skill

## How This Works

Assigns a launch tier and generates a complete GTM strategy brief grounded in your brain and sharper with every launch. Not a template-filler. A strategic thinking partner that interrogates scope before recommending resource investment.

The skill runs in 7 steps:

**Step 0** — Load brain context (ICP, positioning, competitive landscape, proof points, launch history) and guardrails from `/context/meta-patterns.md` (e.g., "T2 launches with <0.5 launch readiness score have underperformed 80% of the time").

**Step 1** — Intake: Initiative name, success metric (90 days), timeline.

**Step 2** — Load brain silently (Sections 2, 3, 4, 5, 7).

**Step 3** — Apply four-signal tier assignment (market impact, revenue potential, competitive urgency, resource requirement).

**Step 4** — Generate full GTM brief (7 sections: strategic context, channels, metrics, competitive, proof points, timeline, next steps).

**Step 5** — Update brain Section 7 with new launch entry (on user confirmation).

**Step 6** — Output markdown brief, copy-paste ready.

**Step 7** — Log session to `/context/skill-sessions.md` with quality score, tier assigned, signals applied, confidence, guardrails triggered, brain updates proposed.

---

## Step 0 — Pre-Flight: Load Context & Surface Guardrails

Before intake, load:
- **Brain context** (Sections 2, 3, 4, 5, 7): ICP, positioning, competitive landscape, proof points, launch history — these anchor all tier signals
- **Guardrails** from `/context/meta-patterns.md`: If a pattern fired 2+ times in prior GTM briefs (e.g., "T2 launches with launch readiness <0.5 fail," "Product launches without proof points slip 3+ weeks"), surface it now

**Surface guardrails like this:**

```
🔁 PATTERN FROM PRIOR GTM BRIEFS

I've seen [pattern description] in 2+ prior sessions.
Examples: [specific launches or outcomes]

Quick check: Does this apply to your initiative?
- If YES → We'll watch for this during brief generation
- If NO → Let's flag it if it emerges
```

You can skip a guardrail if you disagree, but you'll see it first.

**Gate check — block if brain is missing:**
If `/foundation/brain.md` is absent or Section 2 (ICP) is empty, block and surface:
> "Brain not found. Run `product-marketing-context` first. GTM strategy without ICP and positioning produces generic output, not defensible strategy."

---

## Step 1 — Intake (Conversational, One Round)

Ask in one message. Never generate brief before this is complete.

> "Before I assign a tier and build the brief, three things I need:
>
> 1. **What's the initiative?** (Product, feature, pricing change, new segment, market expansion — one sentence)
>
> 2. **What does success look like in 90 days?** Specific metric with a number.
>
> 3. **Timeline?** Launch date or rough window."

Reflect back in 2 sentences:
> "Got it. We're launching [X] for [segment] with a goal of [metric] by [date]. Let me check the brain and assign a tier."

---

## Step 2 — Load Brain Context

Load silently. Extract Sections 2, 3, 4, 5, 7. Do not narrate.

If launch history (Section 7) shows a tier calibration mismatch (T2 that performed like T1, or T1 that underdelivered), surface as calibration note before assigning tier.

---

## Step 3 — Assign Tier

Apply all four signals before assigning. Single signal does not override others.

| Signal | T1 | T2 | T3 | T4 |
|---|---|---|---|---|
| **Market impact** | New category or primary segment | Major new segment or significant feature | Existing segment, incremental feature | Internal only, maintenance |
| **Revenue potential** | Materially moves ARR/NRR | Meaningful pipeline contribution | Conversion or retention support | Minimal or indirect |
| **Competitive urgency** | Closes gap or creates advantage | Responds to or anticipates competitor | No immediate pressure | n/a |
| **Resource requirement** | All teams, full budget, exec visibility | 2–4 teams, dedicated PMM, targeted budget | PMM + one team, standard budget | Minimal, no external comms |

**Tier definitions:**
- **T1** — Company bet. 6–12 weeks. All channels. Full exec alignment.
- **T2** — Major initiative. 2–4 weeks. Targeted GTM. Dedicated PMM.
- **T3** — Routine launch. 1 week. Focused enablement. Limited external comms.
- **T4** — Minimal lift. Internal or beta only. Changelog or in-product only.

**Calibration check:** Before confirming tier, check Section 7. If similar initiative was under- or over-resourced, adjust and name precedent:
> "Based on [prior launch], similar scope was assigned T2 but performed at T1. Recommending T1 here to avoid under-resourcing."

Output tier with one-sentence rationale before generating brief:
> `[T#] — [one sentence why, grounded in the four signals]`

---

## Step 4 — Generate Full GTM Brief

Generate only after tier is assigned. Structure (7 sections):

```markdown
## GTM Brief — [Initiative Name]
**Tier:** [T1 / T2 / T3 / T4]
**Rationale:** [one sentence — four signals applied]
**Launch date:** [date or range]
**DRI:** [name]
**Success metric:** [specific number + timeframe]

### Strategic Context
**Why now:** [1–2 sentences on market timing or competitive signal]
**ICP fit:** [Who specifically this is for, from brain Section 2 + buying trigger]
**Positioning angle:** [Sharpest differentiator, from brain Section 3]

### Channel Strategy
| Channel | Why | Tactic | Owner |
|---|---|---|---|
| [Primary] | [Specific reason tied to ICP] | [Concrete tactic] | [Function] |
| [Secondary] | [Specific reason] | [Concrete tactic] | [Function] |

### Success Metrics
| Metric | Type | Target | Timeframe | Measurement |
|---|---|---|---|---|
| [Primary] | Lagging | [number] | [date] | [where] |
| [Leading indicator 1] | Leading | [number] | [earlier date] | [where] |
| [Leading indicator 2] | Leading | [number] | [earlier date] | [where] |

### Competitive Context
**Primary alternative:** [From brain Section 4]
**Defensive angle:** [What you say when they bring it up]
**Attack angle:** [Specific gap the alternative has]

### Proof Points
- [Claim + metric or quote]
- [Claim + metric or quote]

⚠️ [If missing proof points: flag]

### Timeline
| Week | Milestone | Owner |
|---|---|---|
| -4 to -2 | Pre-launch prep | PMM |
| -1 | Launch readiness check | PMM + Sales |
| 0 | Launch day | All |
| +2 | First signal check | PMM |
| +12 | Retro trigger | PMM |

### Next Steps
1. Confirm tier and brief with [stakeholder] by [date]
2. Run positioning-messaging to sharpen angles
3. Run pre-mortem to stress-test
4. Run stakeholder-maps for internal alignment
5. After launch, run retro → updates brain Section 7
```

---

## Step 5 — Update Brain Section 7 (on Confirmation)

After brief confirmed by user:
> "Logging to brain Section 7 as Planned. Run retro after launch to update with actuals."

Write to `/foundation/brain.md` Section 7:
```markdown
## Launch: [Initiative Name]
- **Date planned:** [launch date]
- **Tier assigned:** [T#]
- **Tier rationale:** [one sentence]
- **Primary metric:** [metric + target]
- **Status:** Planned
- **Actuals:** [Updated after retro]
```

---

## Step 6 — Post-Session Logging

Log to `/context/skill-sessions.md` with YAML metadata:

```yaml
skill: go-to-market-strategy
session_date: [YYYY-MM-DD]
decision_type: [new brief / tier calibration / launch audit]
initiative_name: [Name]
initiative_type: [product launch / feature / pricing change / segment entry / market expansion]
quality_score: [0-100]
tier_assigned: [T1/T2/T3/T4]
tier_rationale: [one-sentence rationale]
four_signals:
  - "Market impact: [score reasoning]"
  - "Revenue potential: [score reasoning]"
  - "Competitive urgency: [score reasoning]"
  - "Resource requirement: [score reasoning]"
confidence_score: [🟢 / 🟡 / 🔴]
launch_readiness_score: [0-1.0, if calibration mode]
guardrails_triggered:
  - "[Pattern name if surfaced]"
brain_context_loaded: true
brain_sections_referenced:
  - "ICP (Section 2)"
  - "Positioning (Section 3)"
  - "Competitive (Section 4)"
  - "Proof points (Section 5)"
  - "Launch history (Section 7)"
brain_updates_proposed:
  - "[Emerging pattern or meta-learning, if any]"
calibration_note: "[Prior launch precedent if applicable]"
leading_indicators_count: [count]
proof_point_gaps: [count, if any]
brain_write_executed: [true/false]
success_metric: [metric + target]
output_path: "[Where brief was saved]"
```

**Quality score:** 90+ = All four signals applied, proof points present, leading indicators clear. 70+ = Most signals applied, some gaps in proof points. <70 = Major gaps in reasoning.

---

## Operating Rules

- **Load brain before intake.** ICP and launch history change what tier is appropriate.
- **First-run blocks without brain.** Missing brain triggers onboarding, not a warning.
- **All four tier signals must be applied.** Revenue alone does not make something T1.
- **Tier rationale mandatory.** One-sentence grounded reason required. "It feels big" is not a rationale.
- **Leading indicators required.** Every brief has ≥1 leading indicator + primary metric.
- **Channel recommendations ICP-specific.** Every channel tied to ICP + motion type, not generic.
- **Calibration history checked.** Before confirming tier, check Section 7 for precedent.
- **Brain write requires explicit confirmation.** Ask before writing to Section 7.
- **Proof point gaps must be flagged.** If brief requires unverified claim, surface before launch.

---

## Quality Gate

| Check | Pass = |
|---|---|
| Four signals applied | All signals reasoned through before tier assigned |
| Brain loaded | Sections 2, 3, 4, 5, 7 extracted before brief |
| Intake complete | Initiative reflected back and confirmed |
| Leading indicator present | ≥1 leading indicator + primary metric |
| Channel specificity | Every channel has ICP-specific reason |
| Competitive context | Primary alternative + attack/defend angles |
| Proof point check | Missing proof points flagged if brief requires them |
| Timeline present | Tier-appropriate timeline with milestones |
| Next steps include retro | Retro named as post-launch trigger |
| Brain write confirmed | User accepted before writing Section 7 |

---

## Self-Improvement Loop

Each session logs to `/context/skill-sessions.md` with:
- Tier assigned and four signals reasoning
- Launch readiness calibration (if auditing)
- Guardrails triggered and usefulness
- Proof point gaps discovered
- Brain updates proposed

Monthly, meta-synthesis reads logs and detects patterns:
- "T2 launches with <0.5 readiness have underperformed" → Guardrail surfaces next time
- "Tier calibration drift: we systematically over-assign T1" → Recommend recalibration
- "Proof point gaps in positioning cause messaging rework" → Alert positioning skill

Patterns feed back into guardrail injection (Step 0) and brain updates (Section 7).

---

## Do Not Use For

- **workflow-orchestrator** — for chaining multiple skills end-to-end
- **positioning-messaging** — for messaging work (use after this skill)
- **pre-mortem** — for risk analysis (use after this skill)
- **retro** — for post-launch review (run after)

