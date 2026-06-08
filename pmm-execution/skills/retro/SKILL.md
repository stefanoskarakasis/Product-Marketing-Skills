---
name: retro
version: 2.0.0
description: >
  Facilitate a structured GTM retrospective for cross-functional squads (Eng, Design,
  PM, PMM) — anchored to OKRs and launch outcomes, with a self-improving knowledge
  loop that compounds across every session. Use when running a post-launch retro, GTM
  cycle review, sprint retrospective with a PMM lens, or any cross-functional debrief
  where you need decisions, not just discussion. Trigger on: "retro", "retrospective",
  "post-launch review", "what went wrong", "GTM debrief", "sprint review", "what should
  we do differently", "debrief this launch", "what did we learn", or any request to
  reflect on a completed GTM cycle or product initiative.

metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-06-06
---

# retro — GTM Retrospective Engine for PMMs

Runs a structured retrospective for cross-functional squads that produces OKR-linked
decisions — and gets smarter every session.

Not a feelings circle. A diagnostic system.

---

## Trigger

- **When:** Post-launch review, GTM cycle debrief, sprint retrospective with a PMM
  lens, or any cross-functional session where decisions are needed, not just discussion.
- **Not for:** Pre-launch risk analysis → use `pre-mortem`. OKR setting for the next
  quarter → use `pmm-okrs`. Campaign briefing after a retro surfaces a messaging gap
  → use `gaccs-brief`. Competitive root cause analysis → use `hs-competitive-battlecard`.
- **Example prompts:**
  - "Run a retro on our Q2 product launch"
  - "We missed our pipeline KR — let's debrief"
  - "What went wrong with the enterprise campaign?"
  - "Facilitate our post-launch review for the analytics dashboard"
  - "Our last sprint ended badly — help us figure out why"

---

## Inputs

- **Args:** Cycle name or launch name. Free format — one sentence minimum.
- **Defaults:** If no cycle named, run intake before proceeding. Never generate
  a retro output without a named cycle and at least one OKR to anchor to.
- **Context keys:**
  - `/foundation/brain.md` — optional but recommended. Load ICP, Positioning,
    Revenue Levers, GTM Motion, Launch Tier Definitions silently if present.
  - `knowledge/retro-patterns/rules.md` — apply all active rules by default, silently.
  - `knowledge/retro-patterns/hypotheses.md` — note any open hypothesis testable today.
  - `decisions/` — check for prior structural decisions before making new ones.
  - `sessions/` — surface carry-over action items from the most recent session file.

---

## Pre-flight

- Load `/foundation/brain.md` silently if present. Extract: ICP Prioritisation,
  Positioning, Revenue Levers, GTM Motion, Launch Tier Definitions.
- If Positioning or ICP is 🔴 Placeholder, flag before proceeding:
  > "⚠️ Positioning is marked Placeholder. This retro may surface symptoms rather
  > than root causes — update context first for sharper diagnosis."
- If brain missing: proceed, surface once:
  > "No brain found. Run `product-marketing-context` for sharper root cause diagnosis. Continuing."
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
> 3. **What inputs do you have?** (Launch metrics, win/loss data, stakeholder feedback —
>    paste or describe what's available)"

If OKRs are not provided: stop and ask specifically. A retro without OKR anchoring
is a venting session with a timer.

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

**Format A — GTM Health Check** — launch cycles, campaign sprints. Assess market impact.
**Format B — OKR Gap Analysis** — when KRs were missed. Trace root cause to KR.
**Format C — Cross-Functional Tension Map** — when collaboration broke down. Name the structural cause.

---

### Step 4: Collect and Structure Feedback

Group into 3–5 themes. Tag each: GTM impact or Process friction. Rank by OKR relevance.
Cross-reference against `knowledge/retro-patterns/rules.md` — flag recurring patterns:
> "⚠️ This theme has appeared in prior retros. See [Rule ID]."

If "communication" appears as a theme: push for the structural root cause. It's never
the real cause.

---

### Step 5: Root Cause Diagnosis

For each top theme:

| Theme | Surface observation | One level deeper | Structural root cause |
|---|---|---|---|
| [Theme] | [What people said] | [What it means] | [Process/RACI/timing/brief quality] |

PMM root causes to check: late brief, untested positioning, tier mismatch,
sales misalignment, competitive blind spot, KR design failure.

Tier assessment — always run:

| | Assigned | Warranted | Gap |
|---|---|---|---|
| Launch tier | [T?] | [T?] | [Over / Under / Correct] |

---

### Step 6: Action Items

Max 3. Each must link to a KR or go to backlog.

| Priority | Action | KR | Owner | Deadline | Success Metric |
|---|---|---|---|---|---|
| 1 | [Structural change] | [KR ref] | [Single owner] | [Date] | [Measurable] |

Rules: single owner only. "Improve communication" is not an action item. Carry-over
items from the previous retro take priority. If carry-over isn't done, ask why first.

---

### Step 7: Deliver Output and Run Self-Improvement

Deliver the retro summary (see Outputs). Then run the self-improvement loop:
write session file → update knowledge base → log decisions → run quality gate.

---

## Outputs

- **Files written:** `sessions/YYYY-MM-DD-[cycle].md` — session file after every retro.
  `knowledge/retro-patterns/hypotheses.md` — new patterns observed 1–2 times.
  `knowledge/retro-patterns/rules.md` — patterns confirmed 3+ times (approval required).
  `decisions/YYYY-MM-DD-[topic].md` — structural decisions made during the session.
- **Chat output format:** Retro summary in the template below. Markdown formatted for
  copy-paste into Notion or Google Docs.
- **External side effects:** n.v.t.

```markdown
## GTM Retrospective — [Cycle Name] — [Date]
**Format used:** [A / B / C]

### Outcome Anchor
- OKR: [Objective] | KRs: [list] | Result: [metric] | Tier: [assigned / warranted]

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

- **pre-mortem** — for risk analysis before a launch, not after. Run this skill
  on a completed cycle; run `pre-mortem` on the next planned one.
- **pmm-okrs** — if the retro surfaces KR design failure, use `pmm-okrs` to rebuild
  the measurement plan. Don't rebuild OKRs inside a retro session.
- **gaccs-brief** — if the retro surfaces a campaign or messaging failure, use
  `gaccs-brief` to rebuild the brief for the next cycle.
- **hs-competitive-battlecard** — if competitive displacement is the root cause,
  route there for the battlecard work. Don't run competitive analysis inside a retro.

---

## Operating Rules

- **OKR anchoring is mandatory.** A retro without OKRs is not a retro — it's a venting
  session. Stop and get OKRs before proceeding.
- **Root causes must be structural.** "Communication" is never a root cause. Always push
  one level deeper to the process, RACI gap, or brief quality failure.
- **Max 3 action items.** More than 3 means priorities aren't clear. Force the choice.
- **Single owner only.** Shared ownership = no ownership. Name one person.
- **Carry-over first.** If prior retro items aren't done, address that before adding new ones.
- **Tier assessment on every retro.** Always compare tier assigned vs. tier warranted.
  Tier mismatch is the most common under-diagnosed root cause.
- **Knowledge base writes are automatic except rules.md promotions.** Hypotheses,
  session files, and decisions write automatically. Rule promotions require user approval.
- **Follow prior decisions.** Check `decisions/` before any structural choice.
  Don't re-debate settled decisions unless new evidence explicitly invalidates them.
- **Anti-patterns get named in the room.** Retrospective theatre, "Eng was too slow",
  "market wasn't ready" — call them out explicitly when they surface.
- **Quality gate runs before final delivery.** Minimum 17/21 on the seven criteria.
  Below that: revise before presenting as complete.

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

Below 17: identify which criterion failed, revise, do not present as final.
Rule promotions require explicit user approval before writing to `rules.md`.

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

```
🔁 SELF-IMPROVEMENT TRIGGER
Pattern: [observed this session]
Proposed update: [exact wording]
Location: [file path]
Awaiting approval before encoding.
```

---

## Changelog

### v2.0.0 — 2026-06-06
Spec compliance pass against SKILL-SPEC v2.0.0. Score: 9/19 → 19/19.
- Fixed: `name` changed from `hs-retro` to `retro` to match directory.
- Added: `## Trigger`, `## Inputs`, `## Outputs`, `## Verification`, `## Do Not Use For`,
  `## Operating Rules` (10 rules), `## Quality Gate` (standalone section).
- Renamed: `## ⓪ PMM CONTEXT — LOAD FIRST` → `## Pre-flight`.
- Restructured: numbered circled sections converted to named `## Steps`.
- Consolidated: self-improvement loop restructured with before/after format and
  explicit trigger surface format.
- Trimmed: anti-patterns and maintenance schedule condensed into operating rules.

### v1.0.0 — 2026-04-17
Initial build.
