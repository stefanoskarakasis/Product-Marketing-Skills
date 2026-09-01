---
name: retro
version: 1.4.0
description: >
  Structured GTM retrospective for cross-functional squads anchored to OKRs and launch
  outcomes. Produces diagnostic root causes and actionable decisions, not venting. Loads
  brain context and, when available, guardrails from prior sessions logged in the user's
  own workspace. Use for post-launch reviews, GTM cycle debriefs, and sprint
  retrospectives where you need to understand what broke structurally and fix it before
  the next cycle.

metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-08-24
---

# retro — GTM Retrospective Engine for PMMs

Runs a structured retrospective for cross-functional squads that produces OKR-linked
decisions. Not a feelings circle. A diagnostic system.

---

## Trigger

- **When:** Post-launch review, GTM cycle debrief, sprint retrospective with a PMM lens, or any cross-functional session where decisions are needed, not just discussion.
- **Not for:** Pre-launch risk analysis → use `pre-mortem`. OKR setting for the next quarter → use `pmm-okrs`. Campaign briefing after a retro surfaces a messaging gap → use `gaccs-brief`. Competitive root cause analysis → no dedicated skill yet.
- **Example prompts:**
  - "Run a retro on our Q2 product launch"
  - "We missed our pipeline KR — let's debrief"
  - "What went wrong with the enterprise campaign?"
  - "Facilitate our post-launch review for the analytics dashboard"
  - "Our last sprint ended badly — help us figure out why"

---

## Inputs

- **Args:** Cycle name or launch name (required). Free format — one sentence minimum.
- **Defaults:** If no cycle named, run intake before proceeding. Never generate a retro output without a named cycle and at least one OKR to anchor to.
- **Context keys:**
  - `/foundation/brain.md` — optional but recommended. Load ICP, Positioning, Revenue Levers, GTM Motion, Launch Tier Definitions silently if present.
  - `/context/meta-patterns.md` — optional; recurring patterns the user has logged from all skills.

---

## Pre-flight

Before anything else, check `/foundation/brain.md`.

**If it exists — load silently. Extract:**
- Section 2 (ICP Definition) → shapes which failure modes are highest-stakes
- Section 3 (Alternatives & Positioning) → was the positioning coherent with this launch? Source of truth for diagnosis.
- Section 5 (Market Context) → which market forces was this initiative riding on? Root causes shift by context.
- Section 6 (Proof Points Registry) → what proof was this launch meant to generate or rely on?

**Confidence awareness:** If Section 3 (Alternatives & Positioning) or Section 2 (ICP Definition) is 🔴 Placeholder, flag before proceeding:
> "⚠️ Positioning is marked Placeholder in your brain. This retro may surface
> symptoms rather than root causes — update the brain first for sharper diagnosis."

**If missing:** Proceed. Surface once, non-blocking:
> "No brain found. Run `product-marketing-context` to make root cause
> diagnosis significantly sharper. Continuing."

If `/context/meta-patterns.md` exists in the user's workspace, check it for guardrails
from prior retros they've logged there. If a pattern applies, surface it before intake:
> "🔁 I've seen [pattern] in prior retros you've logged. Did this show up again here?"

If that file doesn't exist, skip silently — it isn't required for the skill to run.

---

## Steps
### Step 1: Run Intake
Ask in one message. Never generate before OKRs are confirmed.
> "Before I run the retro, three things I need:
>
> 1. **What cycle are we reviewing?** (Sprint / launch name / campaign name + dates)
> 2. **What were we trying to achieve?** (OKR + specific KRs this initiative was meant to move)
> 3. **What inputs do you have?** (Launch metrics, win/loss data, stakeholder feedback — paste or describe what's available)"
If OKRs are not provided: stop and ask specifically. A retro without OKR anchoring is a venting session with a timer.
Confirm before proceeding:
> "Got it. Reviewing [Cycle Name] against [OKR]. Starting with outcome anchor."
---
### Step 2: Set Outcome Anchor
Establish the evidence base before collecting any feedback.
````
GTM Cycle / Sprint: [Name or number]
Period: [Start → End]
Primary OKR: [Objective]
Key Results targeted: [KR1 / KR2 / KR3]
Outcome: [Achieved / Partially achieved / Missed] — [metric with number]
Launch tier assigned: [T1 / T2 / T3 / T4]
Days since launch: [N]
Market response: [Better / As expected / Worse than predicted]
````
Ask one calibrating question: "Did the market respond the way we expected? Yes or no."
---
### Step 3: Select Format
Infer from context or ask.
| Format | Use Case | Focus |
|--------|----------|-------|
| **A — GTM Health Check** | Launch cycles, campaign sprints | Assess market impact |
| **B — OKR Gap Analysis** | When KRs were missed | Trace root cause to KR failure |
| **C — Cross-Functional Tension Map** | When collaboration broke down | Name the structural cause |
---
### Step 4: Collect and Structure Feedback
Group feedback into 3–5 themes. Tag each: GTM impact or Process friction. Rank by OKR relevance.

If `/context/meta-patterns.md` exists and a theme matches a pattern logged there, flag it:
> "⚠️ This theme has appeared in prior retros you've logged. See [pattern]."

**Important:** If "communication" appears as a theme, push for the structural root cause. Communication is never the real cause — it's a symptom.
---
### Step 5: Root Cause Diagnosis
For each top theme, build a diagnostic chain:
| Theme | Surface observation | One level deeper | Structural root cause |
|-------|-------------------|-----------------|----------------------|
| [Theme] | [What people said] | [What it means] | [Process/RACI/timing/brief quality] |
**PMM-specific root causes to check:**
- Late brief (positioning or messaging locked too close to launch)
- Untested positioning (claim validation gap)
- Tier mismatch (assigned T2, but market signals said T1 or T3)
- Sales misalignment (enablement gap or comp misalignment)
- Competitive blind spot (missed alternative or competitor move)
- Post-sales prep gap (support docs / training not ready)
- KR design failure (metric didn't measure what mattered)
- Champion alignment failure (champion wasn't aligned before go-live)

**Always run tier assessment:**
| | Assigned | Warranted | Gap |
|---|----------|-----------|-----|
| Launch tier | [T?] | [T?] | [Over / Under / Correct] |
---
### Step 6: Correlate with Pre-Mortem Predictions

If the user ran a `pre-mortem` before this launch and has it available, compare
predicted risks to what actually materialized:
- Which Tiger risks came true?
- Which risks didn't materialize (and why)?
- Which risks did we miss?

Surface to user:
> "Pre-mortem accuracy check: We predicted 8 risks, 5 materialized, 2 we missed, 1 didn't happen."

If no pre-mortem exists for this launch, skip this step — recommend running one for the next cycle instead.

---
### Step 7: Action Items
Max 3. Each must link to a KR or go to backlog.
| Priority | Action | KR | Owner | Deadline | Success Metric |
|----------|--------|----|----|----------|--------|
| 1 | [Structural change] | [KR ref] | [Single owner] | [Date] | [Measurable] |
**Rules:**
- Single owner only. "Improve communication" is not an action item.
- Carry-over items from the previous retro take priority, if the user has one to reference. If carry-over isn't done, ask why first.
- Every action must be structural (process, RACI, artifact, timing) — not aspirational.
---
### Step 8: Surface Learnings

If the retro surfaces a pattern worth remembering — a timeline assumption, a
recurring gap, a new anti-ICP signal — name it explicitly and ask the user if and
where they want it saved (their own notes, a brain-adjacent doc, or
`/context/meta-patterns.md` if they maintain one). This skill does not write to
any file on its own.

---
### Step 9: Deliver Output
Deliver the retro summary (see Outputs section).
---
### Step 10: Learning Close

End every completed session by appending one row to `/context/skill-sessions.md`
(create the file with a header row if it doesn't exist yet):

````yaml
skill: retro
session_date: [YYYY-MM-DD]
pattern: [one falsifiable statement about what happened this session, or "none"]
source: [surprised / wrong / missing / n.v.t.]
````

Write this row directly — do not ask the user for permission. This is a
separate, mechanical row from Step 8's Learnings to Remember, which is a
user-facing summary of what to carry forward, not a file write. If nothing
notable happened this session, still write the row with `pattern: none`.

---
## Outputs
- **Chat output format:** Retro summary in the template below. Markdown formatted for copy-paste into Notion or Google Docs.
- **Files written:** `/context/skill-sessions.md` — one appended row per
  session, per Step 10.
- **External side effects:** None beyond the session log above.

````markdown
## GTM Retrospective — [Cycle Name] — [Date]
**Format used:** [A / B / C]

### Outcome Anchor
- **OKR:** [Objective] | **KRs:** [list] | **Result:** [metric] | **Tier assigned / warranted:** [T2 / T2]

### Pre-Mortem Correlation (if applicable)
- **Predicted 8 risks, 5 materialized, 2 missed, 1 avoided**
- Tiger risks that materialized: [list]
- Tiger risks that didn't: [list]
- Pre-mortem accuracy: [67%]

### Top Themes
| # | Theme | Type | Root cause | Recurring? |
|---|---|---|---|---|
| 1 | | | | |

### Action Items
| # | Action | KR | Owner | By | Metric |
|---|---|---|---|---|---|
| 1 | | | | | |

### Learnings to Remember
- [Pattern worth carrying forward — ask user where to save it, if anywhere]

### Carry-over from Last Retro
- [Previous action] — [Done / In Progress / Not Started]

### One PMM Takeaway
[Single sentence: most important structural change before next cycle]
````
---
## Verification
- Guardrails checked before intake, if `/context/meta-patterns.md` exists.
- Cycle name and at least one OKR confirmed before output generated.
- Retro format (A/B/C) selected and stated.
- Every theme has a named structural root cause — not "communication."
- Every action item links to a KR or is explicitly backlogged.
- Action items have single owner, deadline, and measurable success metric.
- Tier assessment run and gap stated.
- Pre-mortem correlation checked if a prior pre-mortem is available.
- Learnings surfaced with the user, not written anywhere without asking.
- Session logged to `/context/skill-sessions.md` (Step 10), separate from Step 8's user-facing learnings.
---
## Do Not Use For
- **pre-mortem** — for risk analysis before a launch, not after. Run this skill on a completed cycle; run `pre-mortem` on the next planned one.
- **pmm-okrs** — if the retro surfaces KR design failure, use `pmm-okrs` to rebuild the measurement plan. Don't rebuild OKRs inside a retro session.
- **gaccs-brief** — if the retro surfaces a campaign or messaging failure, use `gaccs-brief` to rebuild the brief for the next cycle.
---
## Operating Rules
- **OKR anchoring is mandatory.** A retro without OKRs is not a retro — it's a venting session. Stop and get OKRs before proceeding.
- **Root causes must be structural.** "Communication" is never a root cause. Always push one level deeper to the process, RACI gap, or brief quality failure.
- **Max 3 action items.** More than 3 means priorities aren't clear. Force the choice.
- **Single owner only.** Shared ownership = no ownership. Name one person.
- **Carry-over first.** If prior retro items aren't done, address that before adding new ones. Track why the prior action stalled.
- **Tier assessment on every retro.** Always compare tier assigned vs. tier warranted. Tier mismatch is the most common under-diagnosed root cause.
- **Pre-mortem correlation when available.** Compare predicted risks to actual outcomes if the user has a pre-mortem for this launch.
- **Anti-patterns get named in the room.** Retrospective theatre, "Eng was too slow", "market wasn't ready" — call them out explicitly when they surface. These are red flags for deeper issues.
- **Quality gate runs before final delivery.** Minimum 12/15 on the criteria. Below that: revise before presenting as complete.
---
## Related Skills

Cross-reference these when a retro surfaces issues that belong elsewhere:

- **product-marketing-context** → source of ICP, positioning, and brain context
- **pre-mortem** → if the next launch is already planned → run risk analysis before it ships
- **gaccs-brief** → if retro surfaces campaign or messaging failure → rebuild the brief
- **pmm-okrs** → if KR design or success metric ambiguity drove the miss → route here
- **prioritization-frameworks** → If tier mismatch is identified, route to `prioritization-frameworks` for rescoring.

---

## Quality Gate
Runs before final delivery. Score each criterion 1–3. Minimum 12/15 to pass.
| Criterion | Standard | Score (1–3) |
|---|---|---|
| Guardrails surfaced | Patterns checked if `/context/meta-patterns.md` exists | |
| OKR anchor | Every theme and action traces to a KR or is explicitly backlogged | |
| Root cause depth | No theme stops at "communication" — structural cause named for each | |
| Action item quality | Max 3, single owner, measurable metric, OKR-linked | |
| Tier diagnosis | Launch tier assessed and compared to warranted | |
| Learning Close ran | `/context/skill-sessions.md` has a new row for this session | |

**On failure:** Identify which criterion failed, revise, do not present as final.
