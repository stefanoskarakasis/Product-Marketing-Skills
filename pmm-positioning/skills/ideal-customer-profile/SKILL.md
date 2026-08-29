---
name: ideal-customer-profile
version: 1.0.0
description: >
  Synthesizes research data — surveys, interviews, usage data, win/loss
  notes — into an Ideal Customer Profile across demographics, behaviors,
  Jobs to Be Done, and needs, then deepens brain Section 2 in place.
  Trigger with "build my ICP", "who is my ideal customer", "analyze our
  PMF survey", "define our target customer", or any request to identify,
  segment, or profile customers from research data.
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-08-27
---

# Ideal Customer Profile 

## How This Works

An ICP built from opinion is a guess with a template around it. This skill
builds one from evidence — survey responses, interview transcripts, usage
data, win/loss notes — synthesized across four layers: who they are
(demographics), how they decide (behaviors), what they're hiring your
product to do (Jobs to Be Done), and what's actually broken for them
(needs). It deepens your brain's existing Section 2 in place rather than
creating a second ICP file — one source of truth stays intact for every
downstream skill.

**Step 0** — Load brain Section 2 (current ICP, however thin) and any
guardrails from `/context/meta-patterns.md`.

**Step 1** — Gather and segment: collect available research, then identify
which customer cohort actually has the value — highest retention, fastest
time-to-value, best expansion — since that's who the profile should
describe, not just "whoever we have."

**Step 2** — Profile across the four layers: Demographics, Behaviors, JTBD,
Needs.

**Step 3** — Deepen brain Section 2 with the profile (on user confirmation).

**Step 4** — Learning Close: log the session to `/context/skill-sessions.md`.

---

## Trigger

- **When:** Defining or sharpening who you sell to from research data —
  PMF surveys, interview transcripts, usage analytics, win/loss notes — or
  when brain Section 2 is firmographic-only with no behavioral or JTBD
  layer.
- **Not for:** Choosing among several candidate segments once the ICP is
  profiled → `beachhead-segment`, run after. Turning a confirmed ICP into
  positioning or messaging → `positioning-messaging`, run after. Full
  brain build from zero → `product-marketing-context`, run first if no
  brain exists at all.
- **Example prompts:**
  - "Build my ICP from our PMF survey data"
  - "Here are 8 customer interviews — define our ideal customer"
  - "Who are our best-fit customers? I have usage and churn data."
  - "Our ICP is just company size and industry. Go deeper."

---

## Inputs

- **Args:** Research data — PMF survey responses, interview transcripts,
  usage or expansion data, win/loss notes, support tickets. If none is
  provided, ask for it; this skill synthesizes evidence, it doesn't
  generate a profile from assumption alone.
- **Defaults:** If brain Section 2 already has demographics but no
  behavioral, JTBD, or needs layer, treat this as additive — profile the
  missing layers, don't re-litigate settled firmographics.
- **Context keys:**
  - `/foundation/brain.md` — required. Section 2 (ICP).
  - `/context/meta-patterns.md` — optional; guardrails from prior sessions.
  - **Brain contract:** Reads Section 2. Writes Section 2 only — the four
    profile layers, appended on explicit confirmation. Never creates a
    separate ICP file.

---

## Pre-flight

- Load `/foundation/brain.md` Section 2 if it exists.
- Load `/context/meta-patterns.md` if present; surface any guardrail fired
  2+ times in prior ICP sessions.
- **Hard block:** brain entirely absent → stop, direct to
  `product-marketing-context` first. A thin Section 2 is not a block —
  that's what this skill exists to fix.
- **Soft block:** no research data provided and none referenced from
  brain → ask for it before profiling. A profile built on assumption
  alone should say so explicitly, not pass as evidence-based.

---

## Steps

### Step 0 — Load Context

Load brain Section 2 as it exists and any fired guardrails.

**Gate check:** brain absent → surface: *"Brain not found. Run
`product-marketing-context` first — even a thin Section 2 gives this
skill something real to build on."*

### Step 1 — Gather and Segment by Value

Ask what research is available if not already provided:
> "What do you have to work with? Survey responses, interview
> transcripts, usage data, win/loss notes, churn analysis — any of these
> work, and more than one is better."

If multiple customers or segments are represented in the data, identify
which cohort the profile should actually describe — the highest-value one,
not an average across everyone:

- Highest retention or lowest churn
- Fastest time-to-value
- Strongest expansion or upsell pattern
- Best reference or case-study potential

State which cohort you're profiling and why before moving to Step 2. A
profile that averages your best customers with your worst describes
nobody.

### Step 2 — Profile Across Four Layers

Every claim traces to a source. Mark anything without one `[A]`
(assumption) — same convention `beachhead-segment` uses. A profile that
hides its assumptions behind confident prose is more dangerous than one
that states them.

**Demographics** — who they are on paper:
company size, industry/vertical (specific — "SaaS" is not a vertical),
geography, job title and department, org structure and budget ownership.

**Behaviors** — how they decide and adopt:
how they discover and evaluate solutions, buying process and timeline,
solo decision vs. committee, technical adoption speed, tool-switching
frequency, peer influence.

**Jobs to Be Done** — what they're actually hiring the product to do:
- Functional job (the concrete outcome they need produced)
- Emotional job (how they want to feel afterward)
- Social job (how they want to be perceived by their team)
- What they're trying to stop doing or stop experiencing

**Needs and Pain Points** — what's actually broken:
specific pain points, current workarounds and their limits, cost or time
burden, available budget, competing priorities. Rank the top 3–5 by how
often they showed up in the source material, not by how compelling they
sound.

**Exit check — the One-Line Test:** can this compress into one sentence a
salesperson could use as a 10-second qualification filter?

> "[Company type] in [vertical] at [size], where [buyer role] needs to
> [functional job] because [top pain point]."

If it can't compress, a layer is still too vague — usually Behaviors or
JTBD. Return there before Step 3.

### Step 3 — Deepen Brain Section 2 (on Confirmation)

Show the exact addition before writing:
> "Adding to brain Section 2 — Demographics, Behaviors, Jobs to Be Done,
> and top Needs/Pain Points, built from [source data]. Existing content
> stays unchanged. Here's what I'll append: [show exact text]. Save this?"

Append to `/foundation/brain.md` Section 2 — do not replace existing
content, do not create a separate file:

```markdown
## Section 2: ICP Definition
[existing content unchanged]

### Behavioral & JTBD Profile (added via ideal-customer-profile, [date])
**Source:** [survey / interviews / usage data / win-loss — n=X if known]

**Behaviors:** [how they discover, decide, adopt]

**Jobs to Be Done:**
- Functional: [one sentence]
- Emotional: [one sentence]
- Social: [one sentence]

**Top Pain Points (ranked by frequency):**
1. [Pain — source]
2. [Pain — source]
3. [Pain — source]

### One-Line ICP Statement
[Company type] in [vertical] at [size], where [buyer role] needs to
[functional job] because [top pain point].
```

Never write without this explicit confirmation.

### Step 4 — Learning Close

Append one row to `/context/skill-sessions.md` (create with header row if
absent):

```yaml
skill: ideal-customer-profile
session_date: [YYYY-MM-DD]
pattern: [one falsifiable statement about this session, or "none"]
source: [surprised / wrong / missing / n.v.t.]
```

Write directly, no permission needed — separate from the brain write
above, which still requires explicit confirmation.

---

## Outputs

- **Files written:** `/foundation/brain.md` Section 2 — appended
  Demographics (if missing), Behaviors, JTBD, and ranked Pain Points
  (Step 3), only after explicit confirmation. `/context/skill-sessions.md`
  — one appended row per session (Step 4).
- **Chat output format:** Source and cohort stated → four-layer profile →
  One-Line ICP Statement → confirmation prompt for the brain write.
- **External side effects:** n.v.t.
- **Next skill:** After brain Section 2 is deepened, check
  `product-marketing-context/.claude-plugin/next-skill-map.md` for "After
  ideal-customer-profile" and surface that prompt. Do not auto-run — ask.

---

## Verification

- Cohort being profiled is stated and justified, not just "our customers."
- All four layers profiled: Demographics, Behaviors, JTBD, Needs.
- Every claim without a cited source flagged `[A]`.
- Pain points ranked by source frequency, not asserted importance.
- One-Line ICP Test passed before the brain write is proposed.
- Brain Section 2 write shown to the user and confirmed before it happens.
- Existing Section 2 content preserved, not overwritten.
- Session logged to `/context/skill-sessions.md`.

---

## Operating Rules

- **Deepen brain Section 2 — never fork a second ICP file.** Every
  brain-reading skill in this stack expects Section 2 to be the ICP.
- **Evidence over assertion.** Every claim without a cited source gets
  `[A]` and lowers confidence in the result.
- **Profile the highest-value cohort, not the average customer.** Averaging
  your best and worst accounts produces a profile that fits neither.
- **Rank pain points by frequency in the source data, not by how
  compelling they sound in the room.** The loudest pain isn't always the
  most common one.
- **The One-Line Test is mandatory.** If the ICP can't compress to a
  10-second qualification sentence, a layer is still too vague.
- **Never overwrite existing Section 2 content.** Append; don't replace
  unless the user explicitly asks to revise settled firmographics.
- **Brain write requires explicit confirmation. Never append silently.**

---

## Quality Gate

| Check | Standard | Pass = |
|---|---|---|
| Cohort stated and justified | Not "our customers" — a specific value-based segment | Yes |
| All 4 layers profiled | Demographics, Behaviors, JTBD, Needs all present | Yes |
| Assumption flags visible | Every unsourced claim marked `[A]` | Yes |
| Pain points ranked by frequency | Not asserted importance | Yes |
| One-Line ICP Test passed | Compresses to a single qualifying sentence | Yes |
| Existing content preserved | Firmographics untouched unless explicitly revised | Yes |
| Brain write confirmed | Exact addition shown and confirmed before writing | Yes |
| Learning Close ran | `/context/skill-sessions.md` has a new row | Yes |

---

## Do Not Use For

- **`product-marketing-context`** — full brain build from zero, or any
  section other than Section 2.
- **`beachhead-segment`** — choosing among multiple candidate segments once
  the ICP is profiled; run this skill first for real inputs.
- **`positioning-messaging`** — turning a confirmed ICP into a positioning
  statement or messaging hierarchy; run this skill first, then that one.
- n.v.t.
