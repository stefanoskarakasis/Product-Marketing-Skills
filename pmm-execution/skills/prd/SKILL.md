---
name: prd
version: 2.4.0
description: >
  Guides Product Managers and Product Marketing Managers to co-create complete Product Requirements Documents with embedded Solution Stories.
  Reads brain context (positioning, ICP, Revenue Levers) to anchor PRDs in strategy.
  Outputs: structured Solution Story for GTM communications + full PRD for execution alignment.

metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-08-21
---

# PRD — Skill

Guides Product Managers and Product Marketing Managers to co-create complete Product Requirements Documents with embedded Solution Stories. Reads your brain for strategic context.

---

## How It Works

````
┌─────────────────────────────────────────────────────────────────┐
│                  PRODUCT REQUIREMENT DOC                         │
├─────────────────────────────────────────────────────────────────┤
│  STEP 0: Load Brain Context (pre-flight)                        │
│  ✓ Positioning (Section 3) → Solution Story framing             │
│  ✓ ICP (Section 2) → Target customer pre-fill                   │
│  ✓ Revenue Levers (Section 5) → Feature alignment check         │
│  ✓ Buyer Personas (Section 4) → Stakeholder mapping             │
├─────────────────────────────────────────────────────────────────┤
│  STEPS 1-6: Intake → Solution Story → Full PRD → Collaboration  │
│  ✓ Conversational intake (role detection)                        │
│  ✓ Solution Story generation (PMM-first)                        │
│  ✓ Full PRD structure (10 sections, 2 owners)                   │
│  ✓ PM + PMM checkpoints (collaboration gates)                   │
│  ✓ Output format (markdown, copy-paste ready)                   │
└─────────────────────────────────────────────────────────────────┘
````

---

## Trigger

- **When:** User mentions PRD, product requirements, solution story, feature spec, GTM brief, launch plan, product brief, user stories, feature rollout, announcement level, or asks for help structuring a product document.
- **Not for:** Strategic planning (use `go-to-market-strategy`), OKR design (use `pmm-okrs`), competitive analysis (no dedicated skill yet).
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
  - `/foundation/brain.md` — recommended. Sections 2 (ICP), 3 (Positioning), 4 (Personas), 5 (Revenue Levers)
  - `/context/meta-patterns.md` — optional; recurring patterns the user has logged from prior PRDs

---

## Pre-flight

- Load `/foundation/brain.md` if exists. Extract Positioning (§3), ICP (§2), Personas (§4), Revenue Levers (§5) for context.
  - If Positioning is 🔴 (Placeholder): surface "Your positioning is a draft — Solution Story may lack messaging grounding. Update brain first?"
  - If ICP missing: "Complete Section 2 (ICP Definition) of your brain via product-marketing-context first — target customer clarity sharpens PRDs."

- If `/context/meta-patterns.md` exists in the user's workspace, check for guardrails they've logged that apply to PRD writing. Skip silently if it doesn't exist.

**Quality gates before intake:**
- If user has zero positioning context: surface "Consider setting positioning first — PRD reads more sharply when anchored to a 'why now' narrative."
- If user is PM-only (no PMM): offer "PMM perspective is valuable here — best to co-author."

---

## Steps

### Step 1: Identify Starting Point

Ask conversationally:

> "Are you starting from scratch, or do you have existing notes, a brief, or an earlier doc I should work from?"

- If **scratch** → run intake interview (Step 2)
- If **existing content** → read it, extract what's answered, ask only for gaps
- If **specific section only** → jump to that section

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

### Step 3: Generate Output 1: Solution Story

Once Round 1 is complete, generate the Solution Story first. This anchors the full PRD.

#### Solution Story structure

````
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
````

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

If a pattern worth remembering surfaces this session — a recurring gap in problem
statements, a metric that consistently gets missed — name it and ask the user
where, if anywhere, they'd like it noted. This skill does not write to any file
on its own.

---

## Writing Principles

**Problem statements** — be specific. "New users churn" is weak. "New users who signed up via organic search churn at 42% on Day 2 when their first feed session shows zero content matching their stated interests" is strong.

**Pitches** — open with the broken status quo, not "Introducing X". The problem should feel so obvious the solution feels inevitable.

**User stories** — write the benefit as a real outcome, not a restatement of the feature. "So that I can see topics" is weak. "So that my feed feels relevant from the moment I sign up" is strong.

**Metrics** — one output metric, two to three inputs with causal logic. If you can't explain why moving an input will move the output, it's the wrong input.

**Non-goals** — not a dump of "things we won't do forever." A specific, time-bounded list of what's out of scope for this release and why.

---

## Verification

- Guardrails checked if `/context/meta-patterns.md` exists
- Brain context loaded and referenced (Step 0) — positioning, ICP, personas inform intake
- Role and document scope clarified (Step 1)
- Intake interview conducted conversationally (Step 2)
- Solution Story generated with writing rules applied (Step 3)
- Full PRD structured with all sections (Step 4)
- PM + PMM checkpoints surfaced (Step 5)
- Output format matches spec (Step 6)

---

## Do Not Use For

- **Strategic planning** — use `go-to-market-strategy`
- **OKR design** — use `pmm-okrs`
- **Competitive analysis** — no dedicated skill yet
- **Launch messaging** — use `gaccs-brief` after PRD is locked
- **Positioning** — use `positioning-messaging` if core positioning undefined

---

## Related Skills

- **pmm-okrs** → PRD OKR alignment
- **gaccs-brief** → GTM messaging from PRD Solution Story
- **experiment-doc** → Risky assumptions in PRD → suggest experiment
- **go-to-market-strategy** → Launch tier assignment
- **pre-mortem** → Risk analysis on PRD scope
