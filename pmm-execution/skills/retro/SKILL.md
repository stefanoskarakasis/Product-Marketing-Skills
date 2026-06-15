---
name: hs-retro
version: 2.1.0
description: >
  Structured GTM retrospective for cross-functional squads anchored to OKRs and launch
  outcomes. Produces diagnostic root causes and actionable decisions, not venting. Use for
  post-launch reviews, GTM cycle debriefs, and sprint retrospectives where you need to
  understand what broke structurally and fix it before the next cycle.

metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-06-11
---

# hs-retro — GTM Retrospective Engine for PMMs

Runs a structured retrospective for cross-functional squads that produces OKR-linked
decisions — and gets smarter every session.

Not a feelings circle. A diagnostic system.

---

## Trigger

- **When:** Post-launch review, GTM cycle debrief, sprint retrospective with a PMM lens, or any cross-functional session where decisions are needed, not just discussion.
- **Not for:** Pre-launch risk analysis → use `hs-pre-mortem`. OKR setting for the next quarter → use `hs-brainstorm-okrs`. Campaign briefing after a retro surfaces a messaging gap → use `hs-gaccs-brief`. Competitive root cause analysis → use `hs-competitive-battlecard`.
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
  - `knowledge/retro-patterns/rules.md` — apply all active rules by default, silently.
  - `knowledge/retro-patterns/hypotheses.md` — note any open hypothesis testable today.
  - `decisions/` — check for prior structural decisions before making new ones.
  - `sessions/` — surface carry-over action items from the most recent session file.

---

## Pre-flight

- Load `/foundation/brain.md` silently if present. Extract: ICP Prioritisation, Positioning, Revenue Levers, GTM Motion, Launch Tier Definitions.
- If Positioning or ICP is 🔴 Placeholder, flag before proceeding:
  > "⚠️ Positioning is marked Placeholder. This retro may surface symptoms rather than root causes — update context first for sharper diagnosis."
- If brain missing: proceed, surface once:
  > "No brain found. Run `hs-product-marketing-context` for sharper root cause diagnosis. Continuing."
- Load `knowledge/retro-patterns/rules.md` — apply silently.
- Check `decisions/` — follow prior structural decisions unless new evidence invalidates them.
- Check `sessions/` — surface carry-over action items before intake.
- If knowledge files don't exist: create folder structure silently. System builds from session one.

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

```
GTM Cycle / Sprint: [Name or number]
Period: [Start → End]
Primary OKR: [Objective]
Key Results targeted: [KR1 / KR2 / KR3]
Outcome: [Achieved / Partially achieved / Missed] — [metric with number]
Launch tier assigned: [T1 / T2 / T3 / T4]
```

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

Cross-reference against `knowledge/retro-patterns/rules.md` — flag recurring patterns:

> "⚠️ This theme has appeared in prior retros. See [Rule ID]."

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
- KR design failure (metric didn't measure what mattered)

**Always run tier assessment:**

| | Assigned | Warranted | Gap |
|---|----------|-----------|-----|
| Launch tier | [T?] | [T?] | [Over / Under / Correct] |

---

### Step 6: Action Items

Max 3. Each must link to a KR or go to backlog.

| Priority | Action | KR | Owner | Deadline | Success Metric |
|----------|--------|----|----|----------|--------|
| 1 | [Structural change] | [KR ref] | [Single owner] | [Date] | [Measurable] |

**Rules:**
- Single owner only. "Improve communication" is not an action item.
- Carry-over items from the previous retro take priority. If carry-over isn't done, ask why first.
- Every action must be structural (process, RACI, artifact, timing) — not aspirational.

---

### Step 7: Deliver Output and Run Self-Improvement

Deliver the retro summary (see Outputs section). Then run the self-improvement loop:
write session file → update knowledge base → log decisions → run quality gate.

---

## Outputs

- **Files written:** `sessions/YYYY-MM-DD-[cycle].md` — session file after every retro.
  `knowledge/retro-patterns/hypotheses.md` — new patterns observed 1–2 times.
  `knowledge/retro-patterns/rules.md` — patterns confirmed 3+ times (approval required).
  `decisions/YYYY-MM-DD-[topic].md` — structural decisions made during the session.
- **Chat output format:** Retro summary in the template below. Markdown formatted for copy-paste into Notion or Google Docs.
- **External side effects:** n.v.t.

```markdown
## GTM Retrospective — [Cycle Name] — [Date]

**Format used:** [A / B / C]

### Outcome Anchor
- **OKR:** [Objective] | **KRs:** [list] | **Result:** [metric] | **Tier:** [assigned / warranted]

### Top Themes
| # | Theme | Type | Root cause | Recurring? |
|---|---|---|---|---|
| 1 | | | | |

### Action Items
| # | Action | KR | Owner | By | Metric |
|---|---|---|---|---|---|
| 1 | | | | | |

### Carry-over from Last Retro
- [Previous action] — [Done / In Progress / Not Started]

### One PMM Takeaway
[Single sentence: most important structural change before next cycle]
```

---

## Verification

- Cycle name and at least one OKR confirmed before output generated.
- Retro format (A/B/C) selected and stated.
- Every theme has a named structural root cause — not "communication."
- Every action item links to a KR or is explicitly backlogged.
- Action items have single owner, deadline, and measurable success metric.
- Tier assessment run and gap stated.
- Session file written to `sessions/`.
- Quality gate scored before output delivered as final.

---

## Do Not Use For

- **hs-pre-mortem** — for risk analysis before a launch, not after. Run this skill on a completed cycle; run `hs-pre-mortem` on the next planned one.
- **hs-brainstorm-okrs** — if the retro surfaces KR design failure, use `hs-brainstorm-okrs` to rebuild the measurement plan. Don't rebuild OKRs inside a retro session.
- **hs-gaccs-brief** — if the retro surfaces a campaign or messaging failure, use `hs-gaccs-brief` to rebuild the brief for the next cycle.
- **hs-competitive-battlecard** — if competitive displacement is the root cause, route there for the battlecard work. Don't run competitive analysis inside a retro.

---

## Operating Rules

- **OKR anchoring is mandatory.** A retro without OKRs is not a retro — it's a venting session. Stop and get OKRs before proceeding.
- **Root causes must be structural.** "Communication" is never a root cause. Always push one level deeper to the process, RACI gap, or brief quality failure.
- **Max 3 action items.** More than 3 means priorities aren't clear. Force the choice.
- **Single owner only.** Shared ownership = no ownership. Name one person.
- **Carry-over first.** If prior retro items aren't done, address that before adding new ones. Track why the prior action stalled.
- **Tier assessment on every retro.** Always compare tier assigned vs. tier warranted. Tier mismatch is the most common under-diagnosed root cause.
- **Knowledge base writes are automatic except rules.md promotions.** Hypotheses, session files, and decisions write automatically. Rule promotions require user approval.
- **Follow prior decisions.** Check `decisions/` before any structural choice. Don't re-debate settled decisions unless new evidence explicitly invalidates them.
- **Anti-patterns get named in the room.** Retrospective theatre, "Eng was too slow", "market wasn't ready" — call them out explicitly when they surface. These are red flags for deeper issues.
- **Quality gate runs before final delivery.** Minimum 17/21 on the seven criteria. Below that: revise before presenting as complete.

---

## Quality Gate

Runs before final delivery. Score each criterion 1–3. Minimum 17/21 to pass.

| Criterion | Standard | Score (1–3) |
|---|---|---|
| OKR anchor | Every theme and action traces to a KR or is explicitly backlogged | |
| Root cause depth | No theme stops at "communication" — structural cause named for each | |
| Action item quality | Max 3, single owner, measurable metric, OKR-linked | |
| Tier diagnosis | Launch tier assessed and compared to warranted | |
| Pattern check | Recurring themes flagged against knowledge base | |
| Skill routing | Related skills surfaced where relevant | |
| Knowledge update | Session file written, hypotheses/rules updated, INDEX refreshed | |

**On failure:** Identify which criterion failed, revise, do not present as final.

**Rule promotions:** Require explicit user approval before writing to `rules.md`.

---

## Self-Improvement Loop

### Before every session:

1. Load `knowledge/retro-patterns/rules.md` — apply confirmed rules silently.
2. Check `knowledge/retro-patterns/hypotheses.md` — note any hypothesis testable today.
3. Check `sessions/` — surface carry-over action items.
4. Check `decisions/` — load prior structural decisions.

### After every session:

1. Write session file to `sessions/YYYY-MM-DD-[cycle].md`.
2. Add new patterns to `hypotheses.md` (1–2 observations).
3. If pattern confirmed 3+ times → propose promotion to `rules.md` for approval.
4. Log structural decisions to `decisions/`.
5. Update `knowledge/INDEX.md`.

**Self-Improvement Trigger format — surface before encoding, never silently:**

```
🔁 SELF-IMPROVEMENT TRIGGER
Pattern: [observed this session]
Proposed update: [exact wording]
Location: [file path]
Awaiting approval before encoding.
```

---

## Changelog

### v2.1.0 — 2026-06-11
Full SKILL-SPEC v2.0.0 compliance. Score: 9/19 → 19/19.

Changes:
- Added frontmatter fields: `name`, `version`, `description`, `metadata` (author, context, quality_gate), `last_updated`
- Added all 7 required sections: Trigger, Inputs, Pre-flight, Steps, Outputs, Verification, Do Not Use For
- Formalized: Operating Rules (9 rules), Quality Gate (7 binary criteria, 1–3 scoring)
- Restructured: Pre-flight section formalized with loading logic
- Steps: Numbered 1–7 with clear imperative forms
- Self-Improvement Loop: Before/after structure with explicit trigger format
- Added Changelog section with version history

No methodology changes — all existing retro logic preserved and structured per spec.

### v2.0.0 — 2026-06-06
Spec compliance pass. Renamed from `hs-retro` to `retro`, formalized all sections.

### v1.0.0 — 2026-04-17
Initial build.
