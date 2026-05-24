---
name: hs-product-requirement-doc
description: >
  Builds, guides, and co-writes a complete HubSpot Product Requirements Document (PRD) with an embedded Solution Story.
  Use this skill whenever a user mentions PRD, product requirements, solution story, feature spec, GTM brief, launch plan,
  product brief, user stories, feature rollout, announcement level, or asks for help writing up a product idea, feature,
  or initiative. Also trigger when a PM or PMM asks how to structure a product document, align on messaging, define
  success metrics, or plan a feature launch — even if they don't use the word "PRD". This skill produces two tangible
  outputs: (1) a standalone Solution Story for PMM-led communications, and (2) a full collaborative PRD for PM + PMM.
metadata:
  version: "2.0.0"
  updated: "2026-03-18"
---

# HS Product Requirements Doc — Skill

A guided workflow for Product Managers and Product Marketing Managers to co-create a
complete PRD with an embedded Solution Story. Produces two outputs in one document.

**On startup:** Read `knowledge/INDEX.md` first. Load only the subfolder(s) relevant
to the current task. Do not load everything at once.

---

## ⓪ PMM CONTEXT — LOAD FIRST

Before intake, check `.agents/product-marketing-context.md`.

**If it exists — load silently:**
- `## Product Strategy Canvas` → Vision, Trade-offs, and Key Metrics as anchors
- `## ICP Prioritisation` → pre-fill target customer section
- `## Buyer Committee Personas` → inform stakeholder mapping in the PRD
- `## Positioning` → sharpen Solution Story framing
- `## Revenue Levers` → confirm feature aligns to priority lever

**Confidence awareness:** If Product Strategy Canvas is 🔴, flag:
> "Product Strategy is marked Placeholder — the PRD may lack strategic grounding. Update context first?"

**If missing:** Proceed. Surface once:
> "Run `hs-product-marketing-context BUILD` first — PRDs without strategy context miss the 'why now'. Continuing."

## RELATED SKILLS
Cross-reference these skills when building PRDs:
- **hs-brainstorm-okrs** → feature PRDs should align with quarterly project OKRs
- **hs-gaccs-brief** → PRD Solution Story feeds directly into the launch campaign brief
- **experiment-doc-builder** → risky assumptions in the PRD → suggest an experiment doc

---
## Outputs

| # | Output | Primary Owner | When to share it |
|---|--------|--------------|-----------------|
| 1 | **Solution Story** | PMM | Before engineering kicks off — aligns team on the 'why' |
| 2 | **Full PRD** | PM + PMM | Throughout discovery, design, and launch |

---

## Workflow

### Step 1 — Identify where the user is starting from

When this skill triggers, first ask:

> "Are you starting from scratch, or do you already have some notes / a brief / an existing doc I should work from?"

- If **scratch** → run the intake interview (Step 2)
- If **existing content** → read it, extract what's already answered, then ask only for gaps (Step 2, targeted)
- If **a specific section only** → jump directly to that section and generate it

Before running intake, check `knowledge/false-beliefs/catalog.md` — if the user's
framing contains a known weak pattern (vague problem statement, missing success metric,
announcement level mismatch), surface it immediately rather than letting it persist into
the document.

---

### Step 2 — Intake interview

Ask these questions **conversationally**, not all at once. Group them into two rounds.

**Round 1 — Core info (ask these together):**
1. What is the feature or initiative name?
2. Who is the target customer / user persona?
3. What problem does it solve? (Even a rough answer is fine — we'll sharpen it.)
4. What's the one outcome you most want to achieve?

**Round 2 — Depth (ask after Round 1 is answered):**
5. What evidence do you have that the problem is real? (data, quotes, tickets)
6. Who is on the team? (PM, PMM, Design, Engineering Lead)
7. What's the rough timeline or key dates?
8. Is there an experiment / A/B test planned, or is this a direct rollout?
9. What announcement level is this? (P1 Major / P2 Notable / P3 Improvement / P4 Minor)

If the user says "just get started" or seems impatient, use what you have and fill gaps
with clearly labelled placeholders. Never block on perfect information.

Consult `knowledge/craft/patterns.md` before generating — confirmed patterns about what
makes problem statements, pitches, and user stories land should inform every section.

---

### Step 3 — Generate Output 1: Solution Story

Once Round 1 is complete, generate the Solution Story first. This is the PMM-led
narrative that anchors the full PRD.

#### Solution Story structure

```
## Solution Story — [Feature Name]

### Feature Identity
- Feature Name: [name]
- Tagline (1–2 words): [tagline]
- Short Value Description: [one sentence — what it does and why it matters]
- Announcement Level: [P1 / P2 / P3 / P4 + one-line rationale]

### The One-Paragraph Pitch
[4–6 sentences. Open with what's broken about existing solutions. Explain what
this product does differently. Close with the key customer benefit. Confident,
clear, slightly opinionated. No jargon.]

### Press Paragraph
[3–4 sentence press-ready version, or N/A if same as above]

### Customer Proof Points
1. [Insight] — [supporting quote or data] (Source: [X])
2. [Insight] — [supporting quote or data] (Source: [X])
3. [Insight] — [supporting quote or data] (Source: [X], optional)
```

**Writing rules for the pitch:**
- Start with the broken status quo — don't open with "Introducing…"
- Name the pain specifically: who feels it, how often, what it costs them
- The solution sentence should feel inevitable given the problem
- End on the customer outcome, not the product feature
- Read it aloud — if it sounds like a press release, simplify it

---

### Step 4 — Generate Output 2: Full PRD

After the Solution Story is confirmed or accepted, generate the full PRD. Use the
structure below. Every section should either be filled with real content from the
intake or clearly marked `[TO FILL — hint about what goes here]`.

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

Pull from Output 1. Paste tagline, value description, and pitch here so engineers and
stakeholders see the 'why' before reading requirements.

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

Key dates: Discovery → Design sign-off → Engineering kickoff → Alpha → Beta → GA →
Post-launch review

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

### Step 5 — Collaboration checkpoints

Surface these moments explicitly when generating the PRD. Insert a clearly labelled
`🤝 PM + PMM checkpoint` comment at:

1. **After §01** — before filling §02–§04: "Run a 30-min kick-off sync. PM confirms
   the pitch is technically accurate. PMM flags messaging risks from early constraints."
2. **After §04 user stories** — before engineering kickoff: "PMM reviews P0 stories.
   Can you build launch messaging from these alone? Any gaps vs what's been promised
   to customers?"
3. **At §07 launch plan** — when scope is finalised: "GTM handoff meeting. PM brings
   final scope + experiment design. PMM brings draft copy + sales enablement. Align on
   go/no-go criteria."

---

### Step 6 — Output format

- Default output: **clean markdown**, structured for copy-paste into Google Docs or Notion
- If the user asks for a `.docx` file, refer to the `docx` skill
- Always produce **both outputs** (Solution Story first, then Full PRD) in the same
  response unless the user asks for one specifically
- Label every placeholder clearly: `[TO FILL — e.g. paste customer quote here]`
- Never leave a section silently blank — either fill it or explain what's needed

---

## Writing Principles

**Problem statements** — be specific. "New users churn" is weak. "New users who signed
up via organic search churn at 42% on Day 2 when their first feed session shows zero
content matching their stated interests" is strong.

**Pitches** — open with the broken status quo, not "Introducing X". The problem should
feel so obvious that the solution feels inevitable.

**User stories** — write the benefit as a real outcome, not a restatement of the
feature. "So that I can see topics" is weak. "So that my feed feels relevant from the
moment I sign up" is strong.

**Metrics** — one output metric, two to three inputs with causal logic. If you can't
explain why moving an input will move the output, it's the wrong input.

**Non-goals** — these are not a dump of "things we won't do forever." They are a
specific, time-bounded list of what's out of scope for this release and why.

---

## Learning Mode

Run this at the end of any session where a full PRD or Solution Story was produced,
a section was significantly revised, or the user corrected the output. Never mid-task.
Only at natural close.

**Step 1 — Pattern check**
Did this session surface evidence for or against anything in
`knowledge/hypotheses/active.md`? If yes: update the relevant hypothesis with a
one-line evidence note and current signal strength.

**Step 2 — Knowledge update**
Did a confirmed pattern emerge (3+ consistent data points)?
If yes: propose adding it to `knowledge/craft/patterns.md`.
Did a belief get killed by data or repeated correction?
If yes: propose moving it to `knowledge/false-beliefs/catalog.md` with a note on
what was observed — including which section triggered it.

**Step 3 — Session log**
Ask once: "Log this session? [yes/no]"
If yes: append a 3-line summary to `knowledge/sessions/log.md`:
- What was produced (PRD, Solution Story, specific section, or full doc)
- What was accepted without revision / what got rewritten or pushed back
- One pattern to watch

Do not pad. Three lines only.

---

## Self-Improvement Trigger

If you notice a pattern across three or more sessions that contradicts a current
instruction in this SKILL.md, surface it explicitly before the session closes:

> "Observation: [what I'm seeing across sessions].
> This conflicts with: [current instruction].
> Suggested update: [proposed change].
> Approve?"

Do not silently adapt. Surface it so the human decides.

---

## Reference

For sample prompts, filled-in examples, and PM + PMM collaboration scripts, refer the
user to: **hs_prd_sample_prompts.md**
