---
name: prd
version: 2.3.0
description: >
  Guides Product Managers and Product Marketing Managers to co-create complete Product Requirements Documents with embedded Solution Stories.
  Reads brain context (positioning, ICP, Revenue Levers) to anchor PRDs in strategy. Logs session data for meta-synthesis pattern detection and compounds learnings over time.
  Outputs: structured Solution Story for GTM communications + full PRD for execution alignment.

metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
  logging_enabled: true
last_updated: 2026-06-21
---

# PRD — Skill

Guides Product Managers and Product Marketing Managers to co-create complete Product Requirements Documents with embedded Solution Stories. Reads your brain for strategic context, logs learnings for system-wide pattern detection.

---

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                  PRODUCT REQUIREMENT DOC                         │
├─────────────────────────────────────────────────────────────────┤
│  STEP 0: Load Brain Context (pre-flight)                        │
│  ✓ Positioning (Section 3) → Solution Story framing             │
│  ✓ ICP (Section 2) → Target customer pre-fill                   │
│  ✓ Revenue Levers (Section 5) → Feature alignment check         │
│  ✓ Buyer Personas (Section 4) → Stakeholder mapping             │
│  ✓ Meta-patterns (guardrails) → Flag recurring risks             │
├─────────────────────────────────────────────────────────────────┤
│  STEPS 1-6: Intake → Solution Story → Full PRD → Collaboration  │
│  ✓ Conversational intake (role detection)                        │
│  ✓ Solution Story generation (PMM-first)                        │
│  ✓ Full PRD structure (10 sections, 2 owners)                   │
│  ✓ PM + PMM checkpoints (collaboration gates)                   │
│  ✓ Output format (markdown, copy-paste ready)                   │
├─────────────────────────────────────────────────────────────────┤
│  STEP 7: Post-session Logging (for meta-synthesis)              │
│  ✓ Session metadata → /context/skill-sessions.md                │
│  ✓ Pattern detection → Quality scores, guardrails triggered     │
│  ✓ Brain updates proposed → Link to brain Section updates       │
│  ✓ Learnings log → Feeds into meta-synthesis monthly cycle      │
└─────────────────────────────────────────────────────────────────┘
```

---

## Trigger

- **When:** User mentions PRD, product requirements, solution story, feature spec, GTM brief, launch plan, product brief, user stories, feature rollout, announcement level, or asks for help structuring a product document.
- **Not for:** Strategic planning (use `go-to-market-strategy`), OKR design (use `hs-brainstorm-okrs`), competitive analysis (use `hs-competitive-battlecard`).
- **Example prompts:**
  - "Write a PRD for our new dashboard feature"
  - "Help me structure this product initiative"
  - "Create a solution story for our messaging team"
  - "I have some rough notes — turn them into a PRD"
  - "What should we include in the launch section?"

---

## Inputs

- **Args:** Feature/initiative name, optional existing notes or brief
- **Context keys:**
  - `/foundation/brain.md` — REQUIRED. Sections 2 (ICP), 3 (Positioning), 4 (Personas), 5 (Revenue Levers), 7 (Meta-Learnings)
  - `/context/meta-patterns.md` — REQUIRED. Guardrails from meta-synthesis (flags recurring risks)
  - `/context/skill-sessions.md` — OPTIONAL. Prior PRD sessions to detect patterns
  - `knowledge/false-beliefs/catalog.md` — OPTIONAL. Known weak patterns in problem statements
  - `knowledge/craft/patterns.md` — OPTIONAL. Confirmed patterns about what lands in pitches

**Brain contract:** Reads: Sections 2, 3, 4, 5, 7. Writes: Section 7 (if major learnings emerge). Reads guardrails, logs to `/context/skill-sessions.md`.

---

## Pre-flight

- Load `/foundation/brain.md` if exists. Extract Positioning (§3), ICP (§2), Personas (§4), Revenue Levers (§5) for context.
  - If Positioning is 🔴 (Placeholder): surface "Your positioning is a draft — Solution Story may lack messaging grounding. Update brain first?"
  - If ICP missing: "Run `/hs-icp` first — target customer clarity sharpens PRDs."
  
- Load `/context/meta-patterns.md` if exists. Check for guardrails that apply to PRD writing:
  - "Success metrics undefined in 2+ PRDs → Ask baseline + target upfront"
  - "Problem statements vague 3+ times → Pressure-test early"
  - "Missing rollback criteria → Flag before launch plan"
  
- Check `knowledge/false-beliefs/catalog.md` for patterns user might repeat (weak problem statements, vague benefits, missing metrics).

**Quality gates before intake:**
- If user has zero positioning context: surface "Consider setting positioning first — PRD reads more sharply when anchored to a 'why now' narrative."
- If user is PM-only (no PMM): offer "PMM perspective is valuable here — best to co-author."

---

## Steps

### Step 0: Surface Guardrails (NEW)

Before intake, check for patterns:

If `/context/meta-patterns.md` exists and contains PRD patterns:
```
🔁 PATTERN DETECTED FROM PRIOR PRDS

I've seen [specific weakness] in X prior PRDs this cycle.
Examples: "missing success metrics", "vague problem statements", "undefined rollback criteria"

Quick check: Do you have [specific requirement]?
- If YES → proceed to Step 1
- If NO → we'll fill this first
```

Surface guardrail only if pattern applies (2+ occurrences in prior 30 days).

### Step 1: Identify Starting Point

Ask conversationally:

> "Are you starting from scratch, or do you have existing notes, a brief, or an earlier doc I should work from?"

- If **scratch** → run intake interview (Step 2)
- If **existing content** → read it, extract what's answered, ask only for gaps
- If **specific section only** → jump to that section

Before running intake, check `knowledge/false-beliefs/catalog.md`. If user's framing contains a known weak pattern, surface it immediately:
> "Your framing: [weak pattern]. That's a common stumble — we see it when [example]. Better approach: [better framing]."

### Step 2: Intake Interview

Ask conversationally, grouped into two rounds.

**Round 1 — Core info (together):**
1. What is the feature or initiative name?
2. Who is the target customer / user persona? (Pre-filled from brain ICP if available)
3. What problem does it solve?
4. What's the one outcome you most want to achieve?

**Round 2 — Depth (after Round 1):**
5. What evidence do you have the problem is real? (data, quotes, tickets)
6. Who's on the team? (PM, PMM, Design, Engineering Lead)
7. Timeline or key dates?
8. Is there an experiment planned, or direct rollout?
9. What's the announcement level? (P1 Major / P2 Notable / P3 Improvement / P4 Minor)

If user seems impatient, use what you have and fill gaps with clearly labelled `[TO FILL — hint]` placeholders.

Consult `knowledge/craft/patterns.md` before generating — confirmed patterns about what makes problem statements and pitches land should inform every section.

### Step 3: Generate Output 1: Solution Story

Once Round 1 is complete, generate the Solution Story first. This anchors the full PRD.

#### Solution Story structure

```
## Solution Story — [Feature Name]

### Feature Identity
- Feature Name: [name]
- Tagline (1–2 words): [tagline]
- Short Value Description: [one sentence — what it does and why it matters]
- Announcement Level: [P1 / P2 / P3 / P4 + one-line rationale]

### The One-Paragraph Pitch
[4–6 sentences. Open with what's broken about the status quo. Explain what this product does differently. Close with customer benefit. Confident, clear, slightly opinionated. No jargon.]

### Press Paragraph
[3–4 sentence press-ready version, or N/A if same as above]

### Customer Proof Points
1. [Insight] — [supporting quote or data] (Source: [X])
2. [Insight] — [supporting quote or data] (Source: [X])
3. [Insight] — [supporting quote or data] (Source: [X], optional)
```

**Writing rules:**
- Start with the broken status quo — don't open with "Introducing…"
- Name the pain specifically: who feels it, how often, what it costs
- Solution sentence should feel inevitable given the problem
- End on customer outcome, not product feature
- Read aloud — if it sounds like a press release, simplify

### Step 4: Generate Output 2: Full PRD

After Solution Story is confirmed, generate the full PRD. Use structure below. Every section either filled with real content or marked `[TO FILL — hint]`.

#### Full PRD structure

---

**Document Header**
- Feature Name:
- Author:
- Date:
- Version: v1.0
- Status: Draft

---

**Section 00 — Team**

| Role | Name | Responsibility |
|------|------|---------------|
| Product Manager (PM) | | Owner |
| Product Marketing Manager (PMM) | | Owner |
| Design | | Contributor |
| Engineering Lead | | Contributor |
| Analytics | | Contributor |
| Stakeholder / Exec Sponsor | | Approver |

---

**Section 01 — Solution Story Summary** *(PMM)*

Pull from Output 1. Paste tagline, value description, and pitch so engineers see the 'why' before reading requirements.

---

**Section 02 — Problem & Background** *(PM + PMM)*

**2.1 Problem Statement**
- Who: [specific segment]
- Problem: [concrete, observable struggle]
- Evidence: [data, quotes, tickets — linked]
- Secondary Issues: [knock-on problems]

**2.2 Market Opportunity** *(PMM)*
- Market Size / TAM:
- Trend (why now):
- Competitor landscape:
- Our differentiation:

**2.3 User Personas** *(PMM)*
- Primary Persona: [name, role, top 3 frustrations, current workaround, JTBD]
- Secondary Persona: [if applicable]

---

**Section 03 — Goals & Success Metrics** *(PM)*

| Type | Metric | Baseline | Target | Timeframe |
|------|--------|----------|--------|-----------|
| Output (North Star) | | | | |
| Input 1 (Leading) | | | | |
| Input 2 (Leading) | | | | |
| Input 3 (Leading) | | | | |

**Non-Goals:**
- [What's out of scope and why]

**Strategic Alignment:**
- Company OKR / Goal:
- Synergies:
- Risk if not built:

---

**Section 04 — Requirements & User Stories** *(PM)*

**High-Level Solution** (2–3 sentences — what we're building and how it works)

**Milestones:**
- Phase 1 — MVP: [scope + date]
- Phase 2 — V2: [scope + date]
- Phase 3 — Future: [backlog ideas]

**User Stories:**

| Priority | User Story | Benefit |
|----------|-----------|---------|
| P0 Must Ship | As a [user], I want [capability]… | …so that [benefit] |
| P0 Must Ship | As a [user], I want [capability]… | …so that [benefit] |
| P1 Should Ship | As a [user], I want [capability]… | …so that [benefit] |
| P1 Should Ship | As a [user], I want [capability]… | …so that [benefit] |

**Open Questions:**
- [Question — @owner — due date]

---

**Section 05 — User Experience** *(PM + Design)*

- Figma / Prototype Link:
- Design Principles:
- Key UI Components:
- User Journey (entry → core flow → success state → edge cases):
- Accessibility standard (WCAG AA/AAA):

---

**Section 06 — Technical Requirements** *(Engineering Lead)*

- Tech Stack:
- System Architecture:
- Key Integrations / APIs:
- Security Considerations:
- Performance Benchmarks:
- Scalability Notes:

---

**Section 07 — Launch Plan** *(PMM + PM)*

**Experiment Design (if applicable):**
- Success Criteria:
- Eligibility:
- Test Group:
- Control Group:
- Split:
- Minimum Duration:

**Rollout Plan:**

| Phase | Audience | Duration | Watch Metric | Go / No-go Owner |
|-------|----------|----------|-------------|-----------------|
| 1 | Internal / Alpha (5%) | | | PM |
| 2 | Beta (25%) | | | PM + PMM |
| 3 | GA (100%) | Ongoing | | PM + PMM |

**Rollback Criteria:**
- Trigger Metric:
- Threshold:
- Decision Owner:
- Rollback Process:

**Go-to-Market** *(PMM)*:
- Messaging Headline:
- Target Channels:
- Key Dates:
- Sales Enablement:
- Support Documentation:

---

**Section 08 — Milestones & Risks** *(PM)*

Key dates: Discovery → Design sign-off → Engineering kickoff → Alpha → Beta → GA → Post-launch review

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| | High/Med/Low | High/Med/Low | |

---

**Section 09 — Sign-Off**

| Role | Name | Approval | Date |
|------|------|---------|------|
| PM | | | |
| PMM | | | |
| Design Lead | | | |
| Engineering Lead | | | |
| Exec Sponsor | | | |

---

### Step 5: Collaboration Checkpoints

Surface these moments explicitly. Insert `🤝 PM + PMM checkpoint` at:

1. **After §01** — before filling §02–§04: "Run a 30-min kick-off sync. PM confirms pitch is technically accurate. PMM flags messaging risks from early constraints."
2. **After §04 user stories** — before engineering kickoff: "PMM reviews P0 stories. Can you build launch messaging from these alone? Any gaps vs what's been promised?"
3. **At §07 launch plan** — when scope is final: "GTM handoff meeting. PM brings final scope + experiment design. PMM brings draft copy + sales enablement. Align on go/no-go."

### Step 6: Output Format

- Default: **clean markdown**, structured for copy-paste into Google Docs or Notion
- If user asks for `.docx`: refer to `docx` skill
- **Always produce both outputs** (Solution Story first, then Full PRD) unless user asks for one
- Label every placeholder: `[TO FILL — e.g. paste customer quote here]`
- Never leave a section silently blank — either fill it or explain what's needed

### Step 7: Post-Session Logging (NEW)

After every session where a full PRD or Solution Story was produced, log to `/context/skill-sessions.md`:

```yaml
skill: prd
session_date: 2026-06-21
feature_name: "Dashboard Analytics"
prd_sections_completed: 9
solution_story_generated: true
quality_score: 82
guardrails_triggered:
  - "Success metrics undefined" (addressed in intake)
  - "Missing rollback criteria" (flagged, user added)
brain_context_loaded: true
brain_sections_referenced:
  - "Positioning (Section 3)"
  - "ICP (Section 2)"
  - "Revenue Levers (Section 5)"
brain_updates_proposed:
  - "Section 7: New learning about announcement-level timing"
pm_pmm_collaboration: true
collaboration_checkpoints_surfaced: 3
output_path: "/artifacts/prd/dashboard-analytics-v1.0.md"
decision: "approved"
```

This data feeds into meta-synthesis monthly, which detects patterns:
- "Success metrics missing 3x → surface upfront in guardrail"
- "Problem statements vague 2x+ → pressure-test early in intake"
- "Missing rollback criteria 2x → add checklist"

Each pattern becomes a guardrail that future PRD sessions load at pre-flight (Step 0).

---

## Writing Principles

**Problem statements** — be specific. "New users churn" is weak. "New users who signed up via organic search churn at 42% on Day 2 when their first feed session shows zero content matching their stated interests" is strong.

**Pitches** — open with the broken status quo, not "Introducing X". The problem should feel so obvious the solution feels inevitable.

**User stories** — write the benefit as a real outcome, not a restatement of the feature. "So that I can see topics" is weak. "So that my feed feels relevant from the moment I sign up" is strong.

**Metrics** — one output metric, two to three inputs with causal logic. If you can't explain why moving an input will move the output, it's the wrong input.

**Non-goals** — not a dump of "things we won't do forever." A specific, time-bounded list of what's out of scope for this release and why.

---

## Verification

- Guardrails checked before intake (Step 0) — user warned of prior patterns
- Brain context loaded and referenced (Step 0) — positioning, ICP, personas inform intake
- Role and document scope clarified (Step 1)
- Intake interview conducted conversationally (Step 2)
- Solution Story generated with writing rules applied (Step 3)
- Full PRD structured with all sections (Step 4)
- PM + PMM checkpoints surfaced (Step 5)
- Output format matches spec (Step 6)
- Session logged with metadata (Step 7) — feeds meta-synthesis

---

## Do Not Use For

- **Strategic planning** — use `go-to-market-strategy`
- **OKR design** — use `hs-brainstorm-okrs`
- **Competitive analysis** — use `hs-competitive-battlecard`
- **Launch messaging** — use `hs-gaccs-brief` after PRD is locked
- **Positioning** — use `hs-positioning-messaging` if core positioning undefined

---

## Related Skills

- **hs-brainstorm-okrs** → PRD OKR alignment
- **hs-gaccs-brief** → GTM messaging from PRD Solution Story
- **experiment-doc-builder** → Risky assumptions in PRD → suggest experiment
- **go-to-market-strategy** → Launch tier assignment
- **hs-pre-mortem** → Risk analysis on PRD scope

---

## Self-Improvement Loop

### Before every session:
1. Load `/foundation/brain.md` → check Positioning (§3), ICP (§2), Personas (§4), Revenue (§5)
2. Load `/context/meta-patterns.md` → check guardrails matching this PRD context
3. Load `knowledge/false-beliefs/catalog.md` → know weak patterns to flag upfront
4. Check prior PRD sessions in `/context/skill-sessions.md` → detect recurring gaps

### After every session:
1. Log to `/context/skill-sessions.md` (Step 7) → Complete session metadata
2. Extract learnings: Which guardrails proved most useful? Which gaps appeared 2+ times?
3. Propose to `/context/meta-patterns.md`: Should we surface a new guardrail next time?
4. Update brain Section 7: Did this PRD surface new learnings about announcement timing, success metrics, or rollout patterns?

**Self-Improvement Trigger:**
```
🔁 PRD LEARNING
Most useful guardrail this cycle: [guardrail name]
New pattern emerging: [pattern]
Recommendation: [Add to meta-patterns if 2+ occurrences]
```

---

## Changelog

### v2.3.0 — 2026-06-21
Added full post-session logging + guardrail intake. Step 0 surfaces patterns from `/context/meta-patterns.md` before intake. Step 7 logs session data to `/context/skill-sessions.md` for meta-synthesis pattern detection. Brain context loading clarified. Quality gate updated to verify logging. Self-improvement loop integrated.

Changes from v2.2.0:
- Added Step 0: Surface guardrails before intake
- Updated Pre-flight: Load brain context + guardrails
- Added Step 7: Post-session logging to `/context/skill-sessions.md`
- Updated Inputs: Now reads `/context/meta-patterns.md`
- Updated Verification: Added guardrail + logging checks
- Updated Self-Improvement: Tied to meta-synthesis monthly cycle
- Version bump 2.2.0 → 2.3.0 (logging enabled)

### v2.2.0 — 2026-05-21
User-first rework. Conversational intake. Solution Story-first output. Collaboration checkpoints. Clean markdown output.

### v2.1.0 — 2026-03-18
Brain context integration. ICP pre-fill. Positioning anchor.

### v2.0.0 — 2026-02-01
Full rebuild to SKILL-SPEC v2.0.0. Structured intake. Solution Story + PRD dual output.

### v1.0.0 — [date]
Initial PRD workflow.
