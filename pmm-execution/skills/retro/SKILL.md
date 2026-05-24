---
name: hs-retro
version: 1.0.0
description: >
  Facilitate a structured GTM retrospective for cross-functional squads (Eng, Design, PM, PMM)
  — anchored to OKRs and launch outcomes, with a self-improving knowledge loop that compounds
  across every session. Use when running a post-launch retro, GTM cycle review, sprint
  retrospective with a PMM lens, or any cross-functional debrief where you need decisions,
  not just discussion. Trigger on: "retro", "retrospective", "post-launch review",
  "what went wrong", "GTM debrief", "sprint review", "what should we do differently",
  "our last launch", "debrief this launch", "what did we learn", or any request to reflect
  on a completed GTM cycle or product initiative.
---

# hs-retro — GTM Retrospective Engine for PMMs

Runs a structured retrospective for cross-functional squads that produces OKR-linked
decisions — and gets smarter every session.

Not a feelings circle. A diagnostic system.

---

## ⓪ PMM CONTEXT — LOAD FIRST

Before anything else, check `.agents/product-marketing-context.md`.

**If it exists — load silently. Extract:**
- `## ICP Prioritisation` → shapes which failure modes are highest-stakes
- `## Positioning` → was the positioning coherent with this launch? Source of truth for diagnosis.
- `## Revenue Levers` → which lever did this initiative target? Root causes shift by lever.
- `## GTM Motion & Growth Loops` → which motion was this dependent on? What broke?
- `## Objections & Anti-Personas` → pre-load as signal for demand-side misalignment
- `## Big Bet Campaigns` → is this retro part of a named campaign? Pull context.
- `## Launch Tier Definitions` → use to assess tier assigned vs. tier warranted

**Confidence awareness:** If Positioning or ICP is 🔴 Placeholder, flag before proceeding:
> "⚠️ Positioning is marked Placeholder in your PMM context. This retro may surface
> symptoms rather than root causes — update context first for sharper diagnosis."

**If missing:** Proceed. Surface once, non-blocking:
> "No PMM context found. Run `hs-product-marketing-context BUILD` to make root cause
> diagnosis significantly sharper. Continuing."

---

## RELATED SKILLS

Cross-reference these when a retro surfaces issues that belong elsewhere:

- **hs-product-marketing-context** → source of ICP, positioning, GTM motion, launch tiers
- **hs-pre-mortem** → if the next launch is already planned → run risk analysis before it ships
- **hs-gaccs-brief** → if retro surfaces campaign or messaging failure → rebuild the brief
- **hs-competitive-battlecard** → if competitive displacement is a root cause → route here
- **hs-brainstorm-okrs** → if KR design or success metric ambiguity drove the miss → route here
- **hs-prioritization-frameworks** → if tier mismatch is the root cause → use to re-score
- **hs-ci-stakeholder-briefing** → if competitive response needs leadership visibility → route here

---

## ① BEFORE STARTING — RETRIEVAL FIRST

**Always do this before intake. This is the mechanism, not a formality.**

1. Read `knowledge/INDEX.md` — load relevant domain file(s)
2. Read `knowledge/retro-patterns/rules.md` — apply all active rules by default, silently
3. Read `knowledge/retro-patterns/hypotheses.md` — note any open hypothesis testable today
4. Grep `decisions/` — before making any structural decision (format, root cause framing,
   ownership model), check for a prior logged decision. Follow it unless new evidence
   explicitly invalidates it. Do not re-debate settled decisions.
5. Check `sessions/` — surface carry-over action items from the most recent session file

If none of these files exist yet: create the folder structure silently. The system builds
itself from session one. Proceed without flagging this to the user.

---

## ② INTAKE — ESTABLISH CONTEXT BEFORE OUTPUT

Most users skip context. Always run this first. Never generate output before completing intake.

Ask in one conversational message:

> "Before I run the retro, three things I need:
>
> 1. **What cycle are we reviewing?** (Sprint number / launch name / campaign name + dates)
> 2. **What were we trying to achieve?** (OKR + the specific KRs this initiative was meant to move)
> 3. **What inputs do you have?** (Launch metrics, win/loss data, stakeholder feedback,
>    sales feedback, previous retro notes — paste or describe what's available)
>
> If you have an OKR doc, launch brief, or previous retro file — paste it and I'll read
> it before we start."

**If OKRs are not provided:** Stop and ask specifically. Do not proceed without them.
A retro without OKR anchoring is a venting session with a timer.

Confirm intake before proceeding:
> "Got it. Reviewing [Cycle Name] against [OKR]. Starting with outcome anchor."

---

## ③ OUTCOME ANCHOR — SET THE FRAME

Before collecting any feedback, establish the evidence base. This prevents the retro from
being anchored in memory rather than outcomes.

Confirm or prompt for:

```
GTM Cycle / Sprint: [Name or number]
Period: [Start date → End date]
Primary OKR: [Objective]
Key Results targeted: [KR1 / KR2 / KR3]
Launch goal: [What we were trying to achieve in market]
Outcome: [Achieved / Partially achieved / Missed] — [metric with number]
Launch tier assigned: [T1 / T2 / T3 / T4]
```

Then ask one calibrating question to the room before collecting feedback:

> "Before we discuss what happened — did the market respond the way we expected? Yes or no."

This anchors the conversation in evidence, not narrative.

---

## ④ FORMAT SELECTION

Select based on what the cycle was. Infer from context or ask.

**Format A — GTM Health Check** *(launch cycles, campaign sprints)*
Use when: the cycle had clear market-facing output and you need to assess impact.
- What landed in market — messaging, positioning, channel performance that worked
- What fell flat — where market response diverged from the hypothesis
- What slowed us down internally — process, alignment, resourcing failures
- What we'd do differently with the same brief — structural changes, not cosmetic ones

**Format B — OKR Gap Analysis** *(when KRs were missed or partially hit)*
Use when: there's a measurable shortfall and you need to trace root cause to KR.
- What moved the needle — activities with traceable KR impact
- What was noise — effort that produced no measurable KR movement
- Root cause of the gap — process, strategy, resource, or external
- One structural change — a process or prioritisation fix, not an attitude adjustment

**Format C — Cross-Functional Tension Map** *(when collaboration broke down)*
Use when: the team experienced significant friction and decisions stalled.
- Where we were aligned — decisions that moved fast and landed well
- Where we stalled — decisions that were slow, revisited, or ownership was unclear
- Structural cause — RACI gap? Late PMM involvement? Unclear tier? Scope creep?
- Fix — a specific process change, not "communicate better"

---

## ⑤ COLLECT AND STRUCTURE FEEDBACK

If raw feedback is provided (sticky notes, Slack threads, survey responses, AE notes):

1. Group into 3–5 themes — no more
2. Tag each theme:
   - **GTM impact** — affected market outcome, pipeline, conversion, adoption
   - **Process friction** — internal only; didn't directly affect market result
3. Rank themes by OKR relevance — which directly explain why KRs were hit or missed?
4. Cross-reference against `knowledge/retro-patterns/rules.md` — flag any theme that
   matches a known recurring pattern. Surface it explicitly:
   > "⚠️ This theme has appeared in prior retros. See [Rule ID] in the knowledge base."
5. Identify the "communication" trap — if a theme is "we need better communication",
   push for the structural root cause. Communication breaks down for a reason. Name it.

---

## ⑥ ROOT CAUSE — ONE LEVEL DEEPER

For each top theme, run this diagnostic:

| Theme | Surface observation | One level deeper | Structural root cause |
|---|---|---|---|
| [Theme] | [What people said] | [What it actually means] | [Process/RACI/timing/brief quality] |

**PMM-specific root causes to check for each theme:**
- **Late brief** — PMM wasn't in the room when scope was set; messaging was retrofitted
- **Untested positioning** — launched on assumption, not validated hypothesis
- **Tier mismatch** — GTM resource mismatched to actual market signal
- **Sales/GTM partner misalignment** — field wasn't ready; PMM assumed readiness
- **Competitive blind spot** — market moved; positioning didn't respond in time
- **KR design failure** — the KR wasn't measurable or wasn't connected to the work

**Tier assessment — always run this:**

| | Assigned | Warranted | Gap |
|---|---|---|---|
| Launch tier | [T?] | [T?] | [Over-invested / Under-invested / Correct] |

If tier mismatch is identified, route to `hs-prioritization-frameworks` for rescoring.

---

## ⑦ ACTION ITEMS — MAX 3, OKR-LINKED

| Priority | Action Item | OKR / KR it addresses | Owner | Deadline | Success Metric |
|---|---|---|---|---|---|
| 1 | [Specific, structural change] | [KR reference] | [Single owner] | [Date] | [Measurable outcome] |

**Rules — enforce these without exception:**
- If an action item cannot be linked to a KR, it goes to backlog. Not this list.
- "Improve communication" is not an action item. Name the broken process and fix it.
- Single owner only. Shared ownership = no ownership.
- Carry-over items from the previous retro take priority over new items.
- If carry-over items are not done, ask why before adding anything new.

---

## ⑧ RETRO SUMMARY OUTPUT

```markdown
## GTM Retrospective — [Cycle Name] — [Date]
**Format used:** [A / B / C]
**Facilitated by:** PMM

---

### Outcome Anchor
- OKR: [Objective]
- KRs targeted: [List]
- Result: [Achieved / Partially achieved / Missed] — [metric]
- Market response: [As expected / Diverged — describe how]
- Launch tier assigned vs. warranted: [T? assigned / T? warranted]

---

### Top Themes (ranked by GTM impact)

| # | Theme | Type | Root cause | Recurring? |
|---|---|---|---|---|
| 1 | [Theme] | [GTM / Process] | [Root cause] | [Y — Rule ID / N] |
| 2 | [Theme] | [GTM / Process] | [Root cause] | [Y — Rule ID / N] |
| 3 | [Theme] | [GTM / Process] | [Root cause] | [Y — Rule ID / N] |

---

### Action Items

| # | Action | KR | Owner | By | Metric |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

---

### Carry-over from Last Retro
- [Previous action] — [Done / In Progress / Not Started — and why if not done]

---

### Skill Cross-References
[List any related skills that should be triggered based on what surfaced this session]

---

### One PMM Takeaway
[Single sentence: the most important structural change PMM needs to make before the next cycle]
```

---

## ⑨ SELF-IMPROVEMENT LOOP — RUN AT END OF EVERY SESSION

**This step is not optional.** The skill compounds through this loop.
Run it before closing every session.

### Step 1 — Write session file

Save to `sessions/YYYY-MM-DD-[cycle-name].md`:

```markdown
## Session: [Cycle Name] — [Date]
### Outcome
- OKR result: [Achieved / Partial / Missed]
- Tier assigned vs. warranted: [T? / T?]
- Market response matched hypothesis: [Y / N]

### Root causes identified
- [Theme]: [Root cause category]

### Action items logged
- [Action] — [Owner] — [Due date]

### Patterns observed this session
- [Any theme matching a known rule or hypothesis — reference ID]
- [New observations not yet in the knowledge base]
```

### Step 2 — Update the knowledge base

**`knowledge/retro-patterns/hypotheses.md`** — add new patterns (observed 1–2 times):
```markdown
## [H-ID]: [Pattern, stated as an observation]
- First observed: [Date / Cycle]
- Confirmed in sessions: [N]
- Status: Hypothesis — needs 3+ confirmations to promote
- Observation: [What happened]
```

**`knowledge/retro-patterns/rules.md`** — promote hypotheses confirmed 3+ times:
```markdown
## [R-ID]: [Pattern, stated as an actionable rule]
- Promoted from: [H-ID]
- Confirmed in: [Session 1], [Session 2], [Session 3]
- Apply by default: YES — silently, without prompting
- Demotion trigger: contradicted by new data → demote to hypotheses.md, log reason
```

**`knowledge/retro-patterns/knowledge.md`** — update factual archive:
- GTM failure patterns by initiative type
- Action item completion rates by owner role
- Tier mismatch frequency and most common cause

**`knowledge/INDEX.md`** — update routing index after every session:
```markdown
## Retro Patterns Knowledge Index
- rules.md — [N] active rules, apply by default
- hypotheses.md — [N] open hypotheses, check if testable this session
- knowledge.md — factual pattern archive, last updated [Date]
Last updated: [Date]
```

### Step 3 — Decision journal

If any structural decision was made (format choice, tier classification, root cause framing,
ownership model), log it **before** closing:

File: `decisions/YYYY-MM-DD-[topic].md`

```markdown
## Decision: [What was decided]
## Context: [Why this came up]
## Alternatives considered: [What else was on the table]
## Reasoning: [Why this option won]
## Trade-offs accepted: [What was given up]
## Supersedes: [Link to prior decision if replacing one]
```

Retrieval rule: before making any structural decision in a future session, grep `decisions/`
first. Follow prior decisions unless new information explicitly invalidates the reasoning.
If replacing a prior decision, log the supersession.

### Step 4 — Quality gate

Evaluate the retro output before closing. Score each criterion 1–3.
Flag any score below 2 and revise before the session ends.

| Criterion | Question | Score (1–3) |
|---|---|---|
| OKR anchor | Every theme and action item traces to a KR or is explicitly backlogged | |
| Root cause depth | No theme stops at "communication" — structural cause named for each | |
| Action item quality | Max 3, single owner, measurable metric, OKR-linked | |
| Tier diagnosis | Launch tier assessed and compared to warranted tier | |
| Pattern check | Recurring themes flagged against knowledge base | |
| Skill routing | Related skills identified and surfaced where relevant | |
| Knowledge update | Session file written, hypotheses/rules updated, INDEX refreshed | |

**Minimum passing score: 17/21.**
Below 17: identify which criterion failed, revise before closing, do not present output
as final until the gate passes.

**User approval gate:** Before writing any update to `rules.md` (promotions only),
surface the proposed change for approval:
> "Ready to promote [H-ID] to a rule — confirmed 3 times across sessions. Approve? Y/N"
Updates to `hypotheses.md`, `knowledge.md`, `sessions/`, and `decisions/` write automatically.

---

## ⑩ ANTI-PATTERNS — CALL THESE OUT IN THE ROOM

If any of these appear in discussion, name them explicitly:

- **"We just need better alignment"** — not a root cause. Ask: what specific decision
  failed or was unclear? Who should have owned it and didn't?
- **"Eng was too slow"** — this is a brief quality or scope problem. PMM owns the brief.
  What was unclear in the requirements that caused the delay?
- **"The market wasn't ready"** — was this in the risk register before launch? If not,
  it's a positioning assumption failure. Untested hypotheses aren't market readiness.
- **"We didn't have enough time"** — this is a tier mismatch. Name the tier that was
  assigned, name the tier that was warranted. Calculate the resourcing gap.
- **Retrospective theatre** — if the same root causes appear in two consecutive retros
  with no completed action items: say it out loud and stop adding new items until the
  carry-over is resolved.

---

## MAINTENANCE SCHEDULE

| Cadence | Task | Time |
|---|---|---|
| Every session | Write session file, update hypotheses, check rules, run quality gate | 10 min |
| After every action item deadline | Update session file with completion status | 5 min |
| Every 3 sessions | Review rules — any contradicted by recent data? Demote with reason. | 15 min |
| Quarterly | Review decisions log — any invalidated by new context? Log supersession. | 20 min |

---

*Save all output as markdown. Tone is direct — the goal is structural improvement,
not morale management.*

*hs-retro v1.0.0*
*Pair with `.agents/product-marketing-context.md` for sharper root cause diagnosis.*
*See `knowledge/INDEX.md` to navigate the compounding knowledge base.*
