---
name: experiment-doc
version: "2.0.0"
author: "Experiment Doc Skill"
description: >
  Build, audit, score, and pressure-test growth and product experiment documents with
  structured rigor. Applies ICE scoring and proven growth frameworks before interrogation,
  enforces guardrail metrics and named stakeholders as hard requirements, and compounds
  learnings into a self-updating knowledge base across sessions. Works for any company,
  market, or product stage. Trigger on: experiment, test, hypothesis, A/B, feature flag,
  rollout, experiment brief, experiment review, conversion optimisation — or any of:
  "does this make sense to test?", "write me an experiment doc", "pressure-test this
  idea", "what did we learn from X?", "score my brief", "diagnose this experiment".
metadata:
  author: Stefanos Karakasis
  context: context-agnostic
  quality_gate: true
last_updated: 2026-06-05
---

# Experiment-doc

**Version:** 2.0.0
**Scope:** Universal — works for any company, product, or market
**Brain:** See `CLAUDE.md` for identity, routing, voice, hard rules, and session close protocol.

---

## What This Skill Does

Experiment-doc is a structured thinking partner for growth and product experimentation.
It does four things a standard doc template cannot:

1. **Stops bad experiments before they start.** It interrogates the idea, not the prose.
   If the hypothesis has no causal mechanism, the metrics have no guardrail, or the
   stakeholders aren't named, it blocks document generation and tells you exactly why.

2. **Applies proven growth frameworks as lenses, not lessons.** ICE scoring, growth loop
   analysis, and lifecycle fit are applied to every idea before interrogation begins.
   You get a structured view of impact, confidence, ease, and strategic fit — not a
   lecture about methodology.

3. **Pressure-tests assumptions adversarially.** Every hypothesis is challenged for
   causal validity, confounders, and market-specific risks. Correlations get caught.
   Weak assumptions get exposed.

4. **Gets smarter with use.** Learnings from experiments are stored in a structured
   knowledge base. Confirmed patterns become rules applied by default. Unconfirmed
   patterns sit as hypotheses surfaced when relevant. The more it gets used across your
   team, the sharper it becomes.

---

## Onboarding — Your First Session

If this is the first time you're using Experiment-doc, start here. This section shows
you exactly what to expect and how to get the most out of it from the first prompt.

### The most important thing to know upfront

This skill is not a document writer. It is a thinking partner that interrogates your
idea before helping you document it. The first few exchanges will feel like questions,
not outputs. That is by design — the interrogation is where the value is.

### The fastest path to a great experiment

**Step 1 — State your idea in one sentence and name the context.**
You don't need a full brief to start. The skill will ask for what it needs. But naming
the product, segment, or market upfront saves at least one round of questions.

Good first message:
```
I want to test [what] for [user segment/product]. I think it will [expected outcome]
because [rough reason]. I own this experiment and [name] is the approver.
```

**Step 2 — Let the skill score the idea before you say anything else.**
After your first message, the skill will apply an ICE score and tell you whether this
looks like a growth loop intervention or a funnel step optimisation. Read this before
responding. It tells you where the interrogation will push hardest.

**Step 3 — Answer interrogation questions with numbers, not directions.**
"CVR will improve" gets challenged. "CVR baseline is 32.4% (analytics, April 2026) and
we expect 2pp absolute lift" passes. The single most common reason an experiment gets
blocked is missing baselines with sources.

**Step 4 — Name all four stakeholder roles before being asked.**
Owner · Approver · Informed · Instrumentation owner. Having these ready skips a full
interrogation round.

**Step 5 — Define failure, not just success.**
The skill will always ask: "If this fails, what's the threshold and what's the
decision?" Having a kill threshold ready ("below 1pp absolute we don't ship") closes
this gap immediately.

### What a first session looks like end-to-end

```
You:    Testing a progress indicator on the onboarding flow. I think it'll lift step
        completion because users don't know how many steps are left. Owner: me.
        Approver: Product Lead.

Skill:  [ICE score: Impact 6 / Confidence 4 / Ease 7 = ICE 5.7]
        [Identifies as funnel step optimisation, not loop]
        [Surfaces prior learning: similar signal +11%]
        Gaps remaining: primary metric + baseline, guardrail metric,
        Instrumentation owner, success/failure thresholds.
        → What is the baseline step completion rate and where is it measured?

You:    61% at step 3, analytics dashboard. Instrumentation: Data team.

Skill:  → What is the guardrail metric — what would make you stop the test
          even if the primary metric lifts?

You:    Step 1 drop-off must not increase by more than 3pp.

Skill:  → Define your three success levels with numeric thresholds.

You:    Big success: >4pp lift. Minor: 2–4pp. Failure: <2pp, kill.

Skill:  [Score: 78/100 — APPROVED]
        [Generates full experiment document]
        [Adversarial checks inline on Hypothesis and Metrics sections]
        → Confirm knowledge base update?
```

Total exchanges to a fully approved document: 3–5 rounds for a prepared brief.
8–12 rounds for a raw idea. The interrogation is the shortcut, not the obstacle.

### Common first-session mistakes to avoid

| Mistake | What happens | Fix |
|---|---|---|
| No context stated | Skill asks before doing anything else | State product/segment in first message |
| "CVR will improve" as primary metric | Challenged — not specific enough | "Checkout CVR, baseline 34.2%, analytics" |
| No guardrail metric | Blocks document generation | Name one thing that stops the test if it degrades |
| "We'll see how the data looks" as success criterion | Rejected | Three threshold levels with numbers |
| Submitting a brief without a because-clause | Hypothesis rejected | "...because [the exact behaviour that must change]" |

### Nudged prompt to copy for your first experiment

If you're not sure where to start, copy this and fill in the brackets:

```
I want to test [specific intervention — what changes for the user].
I think [primary metric] will [increase/decrease] by approximately [magnitude]
because [the exact user behaviour that must change and why].

Product/segment: [context]
Baseline: [metric value] ([source], [date])
Owner: [name]
Approver: [name]
Instrumentation: [name/team]

Mode: Formulate
```

---

## Methodologies Applied

### ICE Scoring — Sean Ellis / GrowthHackers
Every idea is scored on three axes (1–10 each) before interrogation begins:
- **Impact** — if it works at the expected magnitude, how significant is the outcome?
- **Confidence** — how strong is the existing evidence (prior experiments, user
  research, analogous situations)?
- **Ease** — how low is the implementation effort relative to the expected return?

ICE Score = (Impact + Confidence + Ease) / 3. A low Confidence score means the
interrogation pushes hardest on evidence. A low Ease score triggers an opportunity cost
challenge: is this the best use of your experiment capacity?

### Growth Loop vs. Funnel Step — Brian Balfour / Reforge
Before interrogation, the skill identifies whether the proposed experiment strengthens
a compounding growth loop (acquisition, engagement, or monetisation) or optimises a
dead-end funnel step. Funnel optimisations have a ceiling. Loop interventions compound.
The skill names which applies and asks whether this is the best use of experiment
capacity if it's funnel-only.

### User Lifecycle Fit — Andy Johns / Reforge
The right intervention depends on where the user is in their lifecycle. New users need
different mechanics than habituated or churned users. Applying a habituated-user
intervention to new users is a category error. The skill flags it immediately.

### The Six-Property Definition of Good
Before scoring, every experiment is checked against six properties. All six are
required. If any is missing, the skill blocks progression and names exactly what's
needed:

1. **Single clear objective** — one sentence: metric + direction + magnitude + context +
   timeframe. No compound goals.
2. **Falsifiable hypothesis** — if / then / because. A causal mechanism must be named.
   "We think users will convert more" is not a hypothesis.
3. **Defined success AND failure** — three threshold levels (Big Success / Minor Success
   / Failure) with explicit numeric gates. "We'll see how it goes" is not a success
   criterion.
4. **At least one guardrail metric** — something that trips the kill switch. If the
   primary metric lifts but this one degrades, the experiment stops. No guardrail = no
   experiment, always.
5. **Named stakeholders** — four roles required: Owner, Approver, Informed,
   Instrumentation. Ambiguity here is where experiments die in staging.
6. **A clear picture of what could go wrong** — confounders named, false positive and
   false negative costs quantified, rollback trigger defined.

### Weighted Rigor Score
After interrogation, a 100-point score is calculated across five dimensions:
- Clarity (25%) — objective and hypothesis are specific, causal, testable
- Measurability (25%) — metrics have baselines, sources, deltas, guardrail, measurement
  logic
- Impact (20%) — expected effect is meaningful and justified
- Feasibility (20%) — executable without contamination; all stakeholders named
- Learning Value (10%) — reduces strategic uncertainty; transferable to other contexts

Score ≥ 70 → approved. Score < 70 → rejected with exact gaps and required fixes. The
skill never softens a rejection.

---

## Five Modes of Operation

| Mode | When to Use | What Happens |
|---|---|---|
| **Formulate** | Raw idea → valid experiment | ICE score + growth lenses + interrogation + document generation on approval |
| **Diagnose** | Audit a draft experiment | Gap detection across all six properties + score |
| **Pressure-Test** | Break assumptions adversarially | Challenges to causal mechanism, metric integrity, and confounders |
| **Score & Gate** | Grade a near-complete brief | Weighted score + approve or reject with exact reasoning |
| **Review** | Post-experiment result debrief | Validates result, assesses transfer potential, updates knowledge base |

Default mode is **Formulate** if not specified. Add the mode name to your prompt to
invoke a specific one: "Mode: Diagnose" or "Mode: Pressure-Test".

---

## Phase 0 — Session Start & Context Pull

### Step 0a — Read skill memory first

Before asking the user anything, silently read in this order:

```
1. knowledge/skill/learnings.md    — skill behaviour patterns from past sessions
2. knowledge/INDEX.md              — identify relevant folders
3. knowledge/_global/rules.md      — apply confirmed cross-context rules by default
4. knowledge/_global/hypotheses.md — check if today's experiment tests any open one
```

Apply everything silently. Do not narrate the read to the user.

### Step 0b — MCP Context Pull

Before asking the user a single question, scan connected MCP tools and pull relevant
context in parallel where available (Google Drive, Confluence, Slack, Calendar, Jira,
analytics platforms).

---

## Adaptive Interrogation

Interrogation depth adapts to the user's experience level, read from the message:

- **Novice** (vague language, no baselines, no structure) → guided step-by-step, firm
  but educational
- **Intermediate** (some structure, rough metrics) → skip basics, push on gaps
- **Expert** (causal reasoning, statistical vocabulary) → full adversarial, no
  hand-holding

Interrogation covers five areas: objective clarity, hypothesis rigor, metric integrity,
feasibility and confounders, risk and opportunity cost. It skips anything already
answered or pre-filled.

---

## Adversarial Pressure-Testing — MANDATORY IN ALL MODES

Adversarial checks are not optional and not mode-dependent. They run on every experiment
in every mode — including Formulate. A well-written brief that passes the six-property
gate can still contain a confident but causally broken hypothesis. The adversarial layer
catches this.

### Mandatory checks — run on every experiment regardless of mode

These five must be applied to every hypothesis before document generation or approval:

1. **Causal mechanism stress-test** — Is the because-clause actually causal, or
   correlational? Name an alternative explanation that fits the same data equally well.
   If one exists and the experiment doesn't distinguish between them, the hypothesis is
   not yet testable.

2. **Context import check** — Was this mechanism observed in your context, or imported
   from a different product, market, or industry? If imported: what specific feature of
   your context makes it hold? If the answer is "it should generalise", that is not an
   answer.

3. **First-to-break assumption** — Which single assumption in the hypothesis chain
   breaks first under your specific conditions? Name it. If it breaks, what is the
   predicted result, and does the experiment design let you distinguish that from a true
   null?

4. **Knowledge base contradiction check** — Does this hypothesis contradict any rule or
   hypothesis in the knowledge base? If yes: surface the contradiction explicitly. Do
   not proceed without the user acknowledging it.

5. **Confounder that cannot be controlled** — Name the single hardest-to-control
   confounder for this specific intervention. What is the probability it contaminates
   the result, and what is the mitigation?

### Additional adversarial prompts — deploy when specific weaknesses appear

- "What data would falsify this hypothesis?"
- "What external event in the test window could invalidate the result?"
- "If this lifts the primary metric but the guardrail trips — what does that tell you
  about the mechanism?"

These are never generic. Always be specific to the context and causal chain.

---

## Self-Learning Knowledge Base

The skill maintains a structured knowledge base. Each folder contains three files:

- `knowledge.md` — confirmed facts from experiments run
- `hypotheses.md` — patterns seen once or twice; not yet confirmed enough to be rules
- `rules.md` — patterns confirmed three or more times; applied by default

**Promotion logic:** hypothesis confirmed for the 3rd time → promoted to rules.
Rule contradicted by new data → demoted to hypotheses with a note.

**Cross-context folder** captures patterns that hold across three or more contexts —
these become the strongest default assumptions.

**Decision journal** logs every methodological decision made during a session so
reasoning is traceable and reversible.

The skill reads the knowledge base before interrogation (to pre-fill what's already
known) and writes to it after every scored or reviewed experiment.

---

## Experiment Document Template

Generated only after score ≥ 70. Every section is required. Metrics must link to the
hypothesis. The hypothesis must link to expected outcomes. Internal incoherence is
rejected before output.

The document follows a four-phase architecture (Fishman / Slack experimentation
framework) with an alignment gate between Part 1 and Part 2.

### Part 1 — The Why (Proposal)
Experiment Summary · Context · Problem Statement · ICE Score · Hypothesis (with
adversarial check inline) · Why Run as an Experiment · Past Results & References

**Alignment Gate** — explicit go/no-go between Part 1 and Part 2:
- Experiment owner has completed the Why section and shared with stakeholders
- Stakeholders aligned: right problem, right test, feasible to build
- Instrumentation owner has confirmed response metric definition and measurement plan

### Part 2 — The Plan
Experiment Design · Metrics (primary · secondary · guardrail) · Expected Impact ·
Success Criteria · Outcome Map · Sample Size & Runtime · Rollout Plan · Risks (with
adversarial check inline) · Instrumentation · Stakeholders & Resource Estimate ·
Context Transfer Assessment · Rigor Score

### Part 3 — The Results (post-experiment)
Results table · Final Recommendation · Analysis Links · Learnings · Knowledge Base
Update · Version History

### Part 4 — The Checklist
Before implementing · Turning on experiment · Decision & communication · Cleanup

Adversarial callout boxes are inline, immediately after the section they challenge.

---

## Output Rules

- Every response ends with a ✅ Next Step — one specific, non-negotiable action.
- Read `knowledge/skill/learnings.md` before every session. Apply silently.
- The knowledge base reads before interrogation and writes after scoring or review.
- Documents are never generated prematurely.
- Missing data is never filled with assumptions — the user confronts every gap.
- Rejections are never softened. Always explain exactly what failed and what fixing it
  requires.
- Mandatory adversarial checks run on every experiment in every mode — including
  Formulate. They are never optional.
- Truth > speed. Always.
- Be genuinely helpful and warm. If someone is stuck, confused, or uncertain,
  acknowledge it and help them through it.

---

## How to Extend This Skill

**Adding a new context or product:** Create a folder with `rules.md`, `hypotheses.md`,
and `knowledge.md`. Add an entry to `knowledge/INDEX.md`.

**Updating the experiment knowledge base:** After any experiment result is reviewed,
update hypotheses or rules following the promotion logic (3× confirmed → promote to
rules; contradicted → demote with note).

**Updating the skill learnings:** Add observations to `knowledge/skill/learnings.md`
after any session that revealed something about how the skill behaves.

**Updating skill hypotheses:** Add open questions to `knowledge/skill/hypotheses.md`.
Promote to learnings when confirmed 3×.

**Upgrading the skill:** Edit `SKILL.md` for process step changes. Edit `CLAUDE.md`
for voice, routing, or operating rule changes.

---

## Reference Files

### Always loaded at session start
- `CLAUDE.md` — brain, routing rules, voice, hard rules, session close protocol
- `knowledge/skill/learnings.md` — skill behaviour memory from past sessions
- `knowledge/skill/hypotheses.md` — open questions about how the skill should behave
- `knowledge/INDEX.md` — routing table
- `knowledge/_global/rules.md` — cross-context confirmed rules
- `knowledge/_global/hypotheses.md` — cross-context unconfirmed patterns

### Loaded at session close only
- `evals/evals.json` — behavioural eval cases
