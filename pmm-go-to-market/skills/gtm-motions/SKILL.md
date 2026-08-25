---
name: gtm-motions
version: 1.0.0
description: >
  Scores your GTM motion stack (Inbound, Outbound, Paid, Community, Partner, ABM, PLG)
  against ICP deal economics with blocking gates, then selects one primary and at most
  one secondary motion. Trigger with "which GTM motions should we use", "inbound vs
  outbound", "PLG vs sales-led", or any request to select or sequence acquisition channels.
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-08-25
---

# GTM Motions

## Overview

Scores the 7 acquisition motions against your ICP's deal economics and
forces a stack decision — one primary motion, at most one secondary,
with a named rejection reason for every motion not selected. A motion
mix picked because it "sounds right" is a budget guess with a launch
attached to it; this skill replaces that guess with gates and scores.

---

## Trigger

- **When:** Choosing which acquisition motion(s) to invest in for a launch, a segment, or a company-wide GTM model.
- **Not for:** Launch tier + full GTM brief → `go-to-market-strategy` (this skill feeds its Channel Strategy section). Choosing the target segment → `beachhead-segment`, run first. Messaging within a chosen motion → `positioning-messaging`, run after.
- **Example prompts:**
  - "Which GTM motions should we use for this launch?"
  - "Inbound vs outbound — which is right for us?"
  - "Should this be PLG or sales-led?"

---

## Inputs

- **Args:** Initiative/segment, ACV band, target sales-cycle length, current motion if any. Free format — Step 1 fills gaps conversationally.
- **Defaults:** If ACV and sales-cycle length are both unknown, block scoring and ask for a rough band first — motion fit runs on deal economics, not preference.
- **Context keys:**
  - `/foundation/brain.md` — required. Sections 2 (ICP), 3 (Positioning), 4 (Competitive).
  - `/context/meta-patterns.md` — optional; guardrails from prior motion decisions.
  - **Brain contract:** Reads Sections 2, 3, 4. Writes: none.

---

## Pre-flight

- Load `/foundation/brain.md` Sections 2, 3, 4 if present — see Step 0.
- Load `/context/meta-patterns.md` if present; surface any guardrail fired 2+ times.
- **Hard block:** brain absent or Section 2 (ICP) empty → stop, direct to `product-marketing-context` first.

---

## Steps

### Step 0 — Load Context & Surface Guardrails

Load brain Sections 2–4, the confirmed beachhead if `beachhead-segment`
already wrote one, and any guardrail from `/context/meta-patterns.md`
that has fired 2+ times.

**Gate check:** if brain is absent or Section 2 is empty, block and surface:
> "Brain not found. Run `product-marketing-context` first — motion fit is scored against ICP deal size, buyer type, and self-serve capability."

### Step 1 — Intake (One Round)

Ask in one message, never score before it's answered:
> "1. Segment or initiative? (uses confirmed beachhead if one exists)
> 2. ACV / deal size band?
> 3. Target sales-cycle length?
> 4. Current motion, if any — working or not?"

Reflect back in one sentence, then score.

### Step 2 — Score Each Motion

Score all 7 motions — Inbound, Outbound, Paid Digital, Community,
Partner, ABM, PLG — on 4 signals, 1–5 each (five-point, not ten, to
force real spread):

| Signal | What it measures |
|---|---|
| **Deal economics fit** | Does ACV/sales-cycle match what this motion is built to close? |
| **Buyer reachability** | Does this ICP actually gather, search, or get sold to in this channel? |
| **Team/tool readiness** | Do you have — or can get in 30 days — what this motion needs to run credibly? |
| **Time-to-signal** | Weeks or quarters until you know it's working? |

Score against real bands, not gut feel: Outbound needs $10K+ ACV to
clear cost-per-meeting; ABM needs $25K+ to clear cost-per-account; PLG
needs sub-$10K ACV or a self-serve entry tier; Partner needs $5K+ to
absorb revenue share. Inbound and Community work at any ACV but compound
slowly; Paid compresses fast below ~$1K ACV without a self-serve close.

### Step 3 — Apply Blocking Gates

A motion that fails its gate is excluded regardless of score — never
average a gate failure away.

- **ABM:** ACV < $25K → exclude.
- **PLG:** no self-serve signup/trial (none planned in 90 days) → exclude.
- **Outbound:** no dedicated SDR/BDR capacity → exclude as primary (secondary still allowed if a founder/PMM runs it part-time — flag the constraint).
- **Readiness floor:** any motion scoring 1/5 on Team/tool readiness is excluded from primary consideration.

State every gate fired and what it excluded before Step 4.

### Step 4 — Select the Stack

Sum each surviving motion's 4 scores (max 20), rank them.

- **Primary** — highest-scoring survivor. Gets the majority of the plan and budget.
- **Secondary (max 1)** — only if within 3 points of primary AND funnel-distinct from it (e.g. PLG + Community for expansion, not PLG + Paid fighting the same top-of-funnel).
- **Rejected** — one sentence each: gate failure, or lowest-scoring signal and why it matters here.

```markdown
## Motion Stack — [Initiative/Segment]
**Primary:** [Motion] — [score]/20 — [why]
**Secondary:** [Motion or "None"] — [score]/20 — [why]
### Rejected
- **[Motion]** — [gate or signal reason]
### Sequencing
[If one motion should precede another, say so and why.]
```

### Step 5 — 90-Day Activation Plan

Selected motion(s) only — a plan covering rejected motions signals the
rejection wasn't real.

```markdown
### 90-Day Activation — [Primary Motion]
| Weeks | Milestone | Owner | Leading indicator |
|---|---|---|---|
| 1–2 | [Foundation work] | [Function] | n.v.t. |
| 3–6 | [First execution wave] | [Function] | [Earliest signal] |
| 7–10 | [Iterate on signal] | [Function] | [Signal] |
| 11–13 | [Scale or cut] | [Function] | [Decision metric] |
**Kill criteria:** [Number, by week 13, below which this motion is cut.]
```

If a secondary was selected, repeat at roughly half scope.

### Step 6 — Learning Close

Append one row to `/context/skill-sessions.md` (create with header row if absent):

```yaml
skill: gtm-motions
session_date: [YYYY-MM-DD]
pattern: [one falsifiable statement about this session, or "none"]
source: [surprised / wrong / missing / n.v.t.]
```

Write directly, no permission needed. Not a brain write — still needs
separate confirmation if the user wants the stack saved elsewhere.

---

## Outputs

- **Files written:** `/context/skill-sessions.md` — one row per session. n.v.t. otherwise; no brain write. Stack goes into `go-to-market-strategy`'s brief if the user wants it saved.
- **Chat output format:** Motion Stack block, then 90-Day Activation table(s) — always together.
- **External side effects:** n.v.t.

## Verification

- All 7 motions scored on all 4 signals before any gate applied.
- Every fired gate named with what it excluded.
- Exactly one primary; ≤1 secondary; every rejection has a stated reason.
- 90-day plan covers only selected motion(s) and includes a numeric kill criterion.

## Do Not Use For

- **`go-to-market-strategy`** — tier assignment and full GTM brief. Run this skill first for real Channel Strategy backing.
- **`beachhead-segment`** — segment selection. Run before this skill if no beachhead is confirmed.
- **`positioning-messaging`** — messaging within a chosen motion.
- n.v.t.

---

## Operating Rules

- **Score all 7 before gating.** A motion excluded pre-score gets a guess dressed as a gate.
- **Deal-economics gates are hard.** ACV < $25K blocks ABM regardless of other scores; no self-serve blocks PLG regardless of enthusiasm. Override only on explicit user request, stated back before proceeding.
- **Max one secondary.** A 4-motion "portfolio" at partial resourcing funds nothing enough to produce a signal.
- **Every rejection gets one sentence.** Silence invites relitigating later with no anchor.
- **The 90-day plan always carries a numeric kill criterion.** Milestones alone are a calendar, not a plan.
- **Never write the stack to `/foundation/brain.md`.** Motion choice is initiative-specific and can legitimately change per launch — writing it as a brain fact would drift the brain every time a new motion is tried.

## Quality Gate

| Check | Standard | Pass = |
|---|---|---|
| All 7 motions scored | Every motion scored on all 4 signals before Step 3 | Yes |
| Gates applied explicitly | Every fired gate named with excluded motion(s) | Yes |
| Single primary, ≤1 secondary | Exactly one primary; secondary only if within 3 pts and funnel-distinct | Yes |
| Every rejection has a reason | No motion in "Rejected" without a named cause | Yes |
| Kill criterion present | 90-day plan states a numeric cut threshold | Yes |
| Learning Close ran | `/context/skill-sessions.md` has a new row for this session | Yes |
