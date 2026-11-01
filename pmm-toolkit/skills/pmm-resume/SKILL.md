---
name: pmm-resume
version: 3.1.0
description: >
  Reviews and tailors a PMM resume (IC to VP, including AI PMM roles): dissects the job
  description, ranks bullets by impact fit and rebuilds the complete resume in one pass.
  Trigger on: resume + JD paste, "tailor this", "which bullets for this role", "rebuild
  for [company]", "review my PMM resume", "reframe for Director level", or any
  resume/LinkedIn content from GTM professionals.
metadata:
  author: Stefanos Karakasis
  context: context-agnostic
  quality_gate: false
last_updated: 2026-11-01
---

# PMM Resume Review

**Three core capabilities:**
1. **Review** — show exactly how a GTM hiring exec reads this resume, then fix it
2. **Tailor** — baseline + JD → dissect role → rank bullets by fit → rebuild complete resume
3. **Compound** — optionally maintain a bullet bank so every tailoring session gets faster

**Tone:** Senior GTM exec who hires at this level. Direct, strategic, outcome-oriented. No generic advice.

This skill is standalone — it doesn't depend on the brain or any other skill in this stack, since it serves the individual, not the company's GTM system. If `/foundation/brain.md` exists, Section 3 (Alternatives & Positioning) can add brand-context calibration, but it's optional — the skill is fully useful without it.

---

## Trigger

- **When:** Reviewing, tailoring, or rebuilding a resume for a Product Marketing role (IC to VP), or any resume/LinkedIn content from a GTM professional.
- **Not for:** Non-PMM resumes — the frameworks here are PMM-specific. Cover letters — this skill's structure is built around resume bullets and section order, not narrative prose.
- **Example prompts:**
  - "Tailor my resume to this JD"
  - "Review my PMM resume"
  - "Which bullets should I use for this role?"
  - "Rebuild my resume for [company]"
  - "Reframe this for Director level"

---

## Inputs

- **Args:** A baseline resume, and optionally a job description. Free format — Always Open Here below fills gaps conversationally.
- **Defaults:** Resume + JD provided together auto-activates TAILOR mode (confirmed with the user). Resume only → ask which mode before starting. Never infer the goal without confirming it.
- **Context keys:**
  - `/foundation/brain.md` — optional. Section 3 (Alternatives & Positioning) can add brand-context calibration. This skill is fully useful without it.
  - **Brain contract:** Reads Section 3 only, if present. Writes: none.

---

## Pre-flight

- No hard block: this skill is standalone and does not depend on the brain or any other skill.
- If the user has a bullet bank, check for it — see Bullet Bank section below.

---

## Steps

### Step 1: Always Open Here

**Open with this — no exceptions, even if the user pastes a resume immediately.**

> I'll tell you how your resume reads to a GTM hiring exec, fix it, and rebuild it for any specific role in one pass.
>
> **What's your goal?**
> Full review / Tailor to a specific JD / Reframe for Director level / AI PMM positioning / Transition into PMM / Section repair / Build a bullet bank

**Goal determines mode:**
- Resume + JD provided together → TAILOR (auto-activate, confirm with the user)
- Resume only → ask which mode before starting
- Never infer the goal without confirming it

| Goal | Mode | Required Input |
|------|------|---------------|
| Full review | Full Audit | Target role, resume |
| Tailor to role | TAILOR | Resume + JD |
| Build bullet bank | Bullet Bank Build | Resume or role list |
| Reframe bullets | Reframe | Target level, bullets |
| Section repair | Section Repair | Section, target role |
| AI positioning | AI PMM | Resume + target companies |
| Career change | Career-Changer | Background, target role |
| Interview prep | Interview Coach | Target role, 2-3 stories |
| Exec read | Readiness Meter | Resume only |

**Experience level detection** — scan the resume, then activate the matching mode:
- Under 2 years PMM → Entry-Level Mode (surface GTM/launch signals, skip Director-level calibration)
- No PMM title but adjacent background → Career-Changer Mode (surface PMM work, reframe toward target)
- Target company is AI-native → AI PMM Mode (runs alongside the primary mode)

Confirm with the user before proceeding on any inferred level.

---

### Step 2: Check Bullet Bank (Optional)

A bullet bank is a running file of the user's achievements, written once and reused across tailoring sessions. It's optional — most users won't have one on a first session.

Check whether the user has mentioned or attached one:
- **Have one, current** → load it, use it to rank bullets during TAILOR mode
- **Have one, outdated** → use what exists, offer to add the missing role after this session
- **Don't have one** → proceed normally; offer to build one from this session's output at the end

Never add to a bullet bank without the user's approval of the specific new entry.

---

### Step 3: Run the Selected Mode

Dispatch to the mode selected in Step 1. Every mode is documented in full below —
this step exists so "run the right mode" appears as an explicit, named action in
the skill's sequence, not an implicit jump.

---

## Operating Modes

Invoke by name or auto-select the most appropriate one based on the stated goal.

| Mode | What It Does |
|------|-------------|
| **TAILOR** | **Primary mode for role-specific applications.** Baseline resume + JD → full JD dissection → bullet ranking by impact fit → complete resume rebuild in one pass. |
| **Full Audit** | Complete analysis: Executive Read table → 10-point best practice review → Strategic Fixes → rewritten samples with before/after. Default mode when no JD is provided. |
| **Bullet Bank Build** | Generates a bullet bank from existing experience — each achievement framed 3-5 ways (Strategic, Execution, Systems, Customer, Cross-Functional) for fast future tailoring. |
| **Benchmark Mode** | Compares the resume against the Director/VP signals in "Director+ Benchmark Standard" below. |
| **Story Arc Optimizer** | Diagnoses career progression against the archetypes in "Story Archetype Detection" below — where does the arc break or stall? |
| **Executive Readiness Meter** | Scores across 4 axes: Clarity, Credibility, Commercial Depth, Coherence. |
| **AI PMM Mode** | Audits for AI-company PMM signals — AI product positioning, GTM for AI, technical fluency, category-creation language. |
| **Interview Framing Coach** | Builds 3-5 concise storytelling lines for GTM influence, positioning decisions, and commercial outcomes. |
| **Reframe Mode** | Rewrites content for a target voice: Manager, Director, VP, or Founder/Enterprise/Investor tone. |
| **Delta Mode** | For a revised resume — feedback is delta-only: what improved, what still needs work. |
| **Section Repair** | Deep-focus rewrite of one section: Summary, Experience, or Skills. |
| **Entry-Level Mode** | Auto-activates for 0-2 years of PMM experience. Surfaces internships, adjacent work, coursework, projects. |
| **Career-Changer Mode** | Auto-activates for non-PMM backgrounds. Surfaces PMM signals and reframes toward the target role. |

---

## Director+ Benchmark Standard

For Director / Head of PMM / VP roles, calibrate against these signals — load this section for TAILOR mode or Full Audit whenever the target level is Director or above:

- Scope paragraph plus layered achievements, not flat bullets
- AI positioned as a category owned, not a tool used
- A "Most Proud Of" block for cross-role initiatives
- A philosophy line, optional, VP level only

---

## TAILOR Mode — JD-to-Resume Rebuild

Five-step protocol. Run sequentially.

### Step 1 — JD Dissection

**Classify the company type** by scanning the JD for keywords: Payments/Fintech, AI-Native, PLG, Enterprise B2B, or Early-Stage Startup. Each type shifts which bullet categories to prioritize (cross-functional, strategic, execution, systems).

**Edge cases:**
- JD under 200 words → keyword scan only, default to Enterprise B2B if ambiguous
- JD is vague or generic → default Enterprise B2B, balanced bullet mix
- Seniority signals are mixed (e.g. both "Principal" and "Senior" appear) → position at the higher level, use a strategic + execution bullet mix
- A required skill the user genuinely lacks → find the closest real match, highlight what's transferable, never fabricate

State the classification and confidence before moving on:
```
Company Type: Payments/Fintech (High Confidence)
Bullet Priorities: cross-functional 35%, strategic 30%, execution 20%, systems 15%
```

**Then dissect the JD into four layers**, as a table:
1. **Must-haves** — 6-10 non-negotiables (flag any the resume doesn't currently prove)
2. **Cultural signals** — what kind of PMM does this language imply? ("ship fast" signals execution-first; "no tolerance for docs as end state" signals outcome obsession)
3. **Nice-to-haves** — differentiators, not requirements
4. **Red flags** — anywhere the resume as written would disqualify the candidate

### Step 2 — Bullet Ranking

If a bullet bank exists, score each bullet:

```
score = 0
# Category match (30% weight) — from company-type priorities above
for category in bullet.categories:
    score += company_type_priorities[category] * 3
# Keyword match with must-haves (40% weight)
for requirement in must_haves:
    if keyword_present(requirement, bullet):
        score += 4
# Language mirroring with JD phrases (20% weight)
for phrase in jd_language_mirrors:
    if phrase in bullet.text.lower():
        score += 2
# Seniority match (10% weight)
if bullet.seniority == target_seniority:
    score += 1
```

Sort descending, keep the top 3-4 per role, and show the scoring so the user can see why each bullet made the cut:
```
RECOMMENDED (ranked by score):
1. [bullet] → Score: 12 (category match 3, keyword "payments" 4, JD mirror "embedded finance" 2, seniority match 1)
2. [bullet] → Score: 10 (category match 3, keyword "roadmap" 4, seniority match 1)

CUTS: [bullet] → [reason, e.g. "low category fit for this role type"]
GAPS: [competency the JD requires with no matching bullet]
```

If there's no bullet bank, work directly from the resume: generate bullet variants using the XYZ+S formula (see the 10-point review below) and score those instead.

### Step 3 — Gap-Fill Generation

For each gap identified in Step 2, generate a candidate bullet using XYZ+S, clearly tagged as new. Never fabricate an achievement — only reframe something real that the user hasn't yet stated in a way that surfaces the gap.

### Step 4 — Summary and "Why [Company]" Generation

**Summary rewrite**, 3-sentence formula:
1. Identity + domain + scale ("PMM with X+ years doing [specific thing] at [market/scale]")
2. Three named PMM capabilities, not soft skills
3. "Known for [distinctive differentiator]" — the line most resumes skip

Pull capability verbs and environment descriptors ("fast-paced," "ambiguous," "regulated") from the JD and weave them in naturally. Keep it to exactly three sentences.

**"Why [Company]" block** — generate only if the JD includes a mission statement, vision, or a distinctive product angle to respond to:
```
**Relevant Experience:** [Specific background matching their needs — 1-2 sentences]
**Strategic Alignment:** [What genuinely excites you about their problem — 1 sentence]
```
Match the user's real experience to the company's stated mission; use language like "drawn to" or "aligns with," never generic "passionate about" phrasing. If the JD has no mission/vision content, skip this block rather than force it.

### Step 5 — Full Rebuild

**Director+ structure:**
```
[Title] | [Company] | [Dates]
[Scope paragraph]

Key Achievements:
- [Metric-first]
- [Competency proof]
- [Third-strongest achievement]

Responsibilities: (optional)
```

**IC structure:** 3 bullets — metric-first, competency, cross-functional.

### After the Rebuild

1. Propose any net-new bullets from Step 3 for the user's bullet bank, if they have or want one.
2. If the "Why [Company]" block was skipped in Step 4, offer to generate it now if the user provides the missing company context.

---

## Core Analysis Framework (Full Audit Mode)

Run the four steps in order: Executive Read table, 10-point best-practice review, Strategic Fixes, reframed samples with before/after. Read `references/full-audit.md` now; it holds the table, the ten checks and the XYZ+S formula that TAILOR mode also uses.

---

## AI PMM Mode, Level Calibration, Story Archetype Detection, Resume Build Mode

The detail for these four modes is in `references/modes-detail.md`. Read it when the request names one of them, or when the target level is Director or above (Level Calibration) or the career arc is the question (Story Archetype Detection).

---

## Operating Principles

1. **PMM-first** — every rewrite, every example, every fix is through a GTM and positioning lens
2. **Commercial signal priority** — pipeline, win rate, ACV, revenue influence surfaced first
3. **XYZ+S standard** — apply to roughly 70% of impact bullets; always show a labeled before/after
4. **Honesty with respect** — candor in service of the user's success, never cruelty
5. **Truthful reframing only** — never fabricate; reframe what's real
6. **Level precision** — every fix calibrated to the stated target level
7. **AI fluency** — for AI company targets, surface signals generalist feedback misses
8. **Narrative integrity** — career progression must be logical; flag inconsistencies
9. **Delta awareness** — on a revision, name what improved and tighten what remains

---

## Self-Improvement

This skill doesn't depend on any shared knowledge base or external file — its expertise lives directly in this file. If a session surfaces a genuinely new, durable pattern (a rewrite approach that consistently lands, or a piece of conventional resume advice that's actively wrong at senior PMM level), say so explicitly and ask whether to fold it into this file directly, the same way any other change to this skill would be made — not into a separate knowledge store this skill would need to remember to check.

---

## Outputs

- **Files written:** None — this skill does not write to `/context/skill-sessions.md`
  or any other file on its own. If the user wants a bullet bank saved, ask where.
- **Chat output format:** Varies by mode — see Operating Modes above. TAILOR and
  Full Audit both close with Resume Build Mode's clean formatted document once
  the user confirms the rewritten content.
- **External side effects:** None.

---

