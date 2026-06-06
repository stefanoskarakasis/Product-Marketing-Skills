---
name: go-to-market-strategy
version: 2.0.0
description: >
  Assigns launch tier (T1–T4) and generates a complete GTM strategy brief with
  positioning angles, channel strategy, success metrics, and competitive context.
  Self-learns from past launches stored in the brain. Trigger on: "what tier is
  this launch", "GTM strategy for", "help me scope this", "how should we launch",
  "what channels for this launch", "is this a T1 or T2", "plan my launch",
  "launch strategy for", or any request to scope, tier, or build a GTM plan for
  a product, feature, pricing change, or market expansion.

metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-06-06
---

# Go-to-Market Strategy

Assigns a launch tier and generates a complete GTM strategy brief — with positioning
angles, channel recommendations, success metrics, and competitive context — grounded
in your brain and sharper with every launch.

Not a template-filler. A strategic thinking partner that interrogates scope before
recommending resource investment.

---

## Trigger

- **When:** Any request to scope, tier, or plan a GTM initiative: product launch,
  feature release, pricing change, new segment entry, or market expansion.
- **Not for:** Multi-skill end-to-end launch programs → use `workflow-orchestrator`.
  Positioning or messaging work → use `positioning-messaging`. Post-launch review
  → use `retro`. Risk analysis → use `pre-mortem`.
- **Example prompts:**
  - "What tier is our SSO launch?"
  - "Help me scope the GTM for our analytics dashboard"
  - "Is this pricing change a T1 or T2?"
  - "Build a GTM strategy for our new enterprise segment"
  - "We're entering the healthcare vertical — where do we start?"

---

## Inputs

- **Args:** Initiative name or description — free format. One sentence minimum.
- **Defaults:** If no initiative is named, run intake before proceeding.
- **Context keys:**
  - `/foundation/brain.md` — required. Sections 2, 3, 4, 5, 7.
  - **Brain contract:**
    - Reads: Section 2 (ICP & personas) — target segment and buying triggers;
      Section 3 (Positioning) — current positioning angles and category;
      Section 4 (Competitive landscape) — alternatives and differentiation;
      Section 5 (Proof points) — claims to anchor the brief;
      Section 7 (Launch history) — prior tier assignments and actuals for calibration.
    - Writes: Section 7 — adds new launch entry as "Planned" with tier, rationale,
      and success metrics. Updates to "Completed" after retro.
    - Never writes to: Sections 1, 2, 3, 4, 5, 6.

---

## Pre-flight

- Load `/foundation/brain.md`. Extract Sections 2, 3, 4, 5, 7 silently.
- If brain missing: surface once, non-blocking:
  > "No brain found. Run `product-marketing-context` first — this brief will be
  > significantly sharper with your ICP, positioning, and launch history loaded.
  > Continuing with assumption-based output."
- If Section 7 (Launch history) is empty or missing: note internally. Tier
  calibration will rely on initiative signals only — no historical precedent to draw from.
- If Section 3 (Positioning) is 🔴 Placeholder: flag before intake:
  > "⚠️ Positioning is marked Placeholder. The GTM brief will lack sharp angles.
  > Run `positioning-messaging` first for better output."

---

## Steps

### Step 1: Run Intake

Ask in one message. Never generate before this is complete.

> "Before I assign a tier and build the brief, three things I need:
>
> 1. **What's the initiative?** (Product, feature, pricing change, new segment,
>    market expansion — one sentence on what it is and who it's for)
>
> 2. **What does success look like in 90 days?**
>    Specific metric with a number. Not "more pipeline" — a target.
>
> 3. **What's your timeline and do you have a hard launch date?**
>    Name the date if there is one. If not, give me the rough window."

If the user has already provided this context, skip and proceed to Step 2.

Reflect back the initiative in 2 sentences before proceeding:
> "Got it. We're launching [X] for [segment] with a goal of [metric] by [date].
> Let me check what the brain tells us and assign a tier."

---

### Step 2: Load Brain Context

Load silently. Do not narrate to the user. Extract:

- **ICP (Section 2):** primary persona, buying triggers, deal size, motion type
- **Positioning (Section 3):** current category, key differentiators, primary alternatives
- **Competitive landscape (Section 4):** who this launch affects competitively
- **Proof points (Section 5):** claims relevant to this initiative
- **Launch history (Section 7):** prior launches of similar type or tier — what worked,
  what didn't, which tier was assigned vs. which was warranted

If launch history shows a tier calibration mismatch (T2 that performed like T1,
or T1 that underdelivered), surface it as a calibration note before assigning tier.

---

### Step 3: Assign Tier

Apply all four signals before assigning. A single strong signal does not override the others.

**Tier assignment criteria:**

| Signal | T1 | T2 | T3 | T4 |
|---|---|---|---|---|
| Market impact | New category, primary segment, company-defining | Major new segment or significant feature | Existing segment, incremental feature | Internal only, maintenance |
| Revenue potential | High — materially moves ARR or NRR | Meaningful — measurable pipeline contribution | Moderate — conversion or retention support | Minimal or indirect |
| Competitive urgency | Closes a critical gap or creates an advantage | Responds to or anticipates competitor move | No immediate competitive pressure | n/a |
| Resource requirement | All teams, full budget, exec visibility | 2–4 teams, dedicated PMM, targeted budget | PMM + one team, standard budget | Minimal, no external comms |

**Tier definitions:**

- **T1 — Company bet.** 6–12 weeks. All channels. Full exec alignment. The kind
  of launch you build a quarter around.
- **T2 — Major initiative.** 2–4 weeks. Targeted GTM. Dedicated PMM time.
  Measurable pipeline or adoption goal.
- **T3 — Routine launch.** 1 week. Focused enablement. Limited external noise.
  Conversion or retention impact.
- **T4 — Minimal lift.** Internal or beta only. No GTM investment. Changelog or
  in-product comms only.

**Calibration from launch history:** Before confirming the tier, check Section 7.
If a similar initiative was previously under- or over-resourced, adjust recommendation
and name the precedent:
> "Based on [prior launch], similar scope was assigned T2 but performed at T1 signal.
> Recommending T1 here to avoid under-resourcing."

Output the tier with a one-sentence rationale before generating the brief:
> `[T#] — [one sentence why, grounded in the four signals]`

---

### Step 4: Generate GTM Brief

Generate only after tier is assigned and rationale is stated. Structure:

```markdown
## GTM Brief — [Initiative Name]

**Tier:** [T1 / T2 / T3 / T4]
**Tier rationale:** [one sentence grounded in the four signals]
**Launch date / window:** [date or range]
**DRI:** [name or TBD]
**Success metric:** [specific number + timeframe]

---

### Strategic Context

**Why now:** [1–2 sentences on market timing, competitive signal, or internal
readiness that makes this launch worth doing now — not generic]

**ICP fit:** [Who specifically this is for, drawn from brain Section 2. Include
the buying trigger that makes this initiative relevant to them right now.]

**Positioning angle:** [The sharpest differentiator relevant to this initiative,
drawn from brain Section 3. Not a tagline — a strategic claim that separates
this launch from what competitors or alternatives can say.]

---

### Channel Strategy

Channels recommended based on ICP, tier, and motion type. Listed by priority.

| Channel | Why | Tactic | Owner |
|---|---|---|---|
| [Primary] | [Specific reason tied to ICP and motion] | [Concrete tactic] | [Function] |
| [Secondary] | [Specific reason] | [Concrete tactic] | [Function] |
| [Tertiary] | [Specific reason] | [Concrete tactic] | [Function] |

**Motion type:** [Sales-led / PLG / CS-led / Partner — drawn from brain]

For T3/T4: list only 1–2 channels. Do not over-engineer low-tier launches.

---

### Success Metrics

| Metric | Type | Target | Timeframe | Measurement method |
|---|---|---|---|---|
| [Primary] | Output (lagging) | [number] | [date] | [where to measure] |
| [Leading indicator 1] | Input (leading) | [number] | [earlier date] | [where to measure] |
| [Leading indicator 2] | Input (leading) | [number] | [earlier date] | [where to measure] |
| [Guardrail] | Health | [threshold] | Ongoing | [where to measure] |

**Why this metric set:** [1 sentence explaining the causal logic — why moving
the leading indicators should move the primary metric]

---

### Competitive Context

**Primary alternative:** [What buyers compare this to — from brain Section 4]
**Defensive angle:** [What you say when they bring it up]
**Attack angle:** [Where you go on offense — the specific gap the alternative has]

---

### Proof Points

Relevant claims from brain Section 5 to anchor the launch narrative:
- [Proof point 1 — metric or quote]
- [Proof point 2 — metric or quote]

Flag any missing proof points:
> "⚠️ No proof point exists for [claim]. Recommend gathering before launch."

---

### Timeline

| Week | Milestone | Owner |
|---|---|---|
| -4 to -2 | [Pre-launch prep — enablement, assets, positioning locked] | PMM |
| -1 | [Launch readiness check — all assets live, sales briefed] | PMM + Sales |
| 0 | [Launch day — announcement, outbound, in-product] | All |
| +2 | [First signal check — leading indicators tracked] | PMM |
| +4 | [Mid-launch review — adjust if leading indicators off] | PMM |
| +12 | [Post-launch retro trigger] | PMM |

Adjust timeline length to tier: T1 = 8–12 weeks total, T2 = 4–6 weeks,
T3 = 2–3 weeks, T4 = 1 week max.

---

### Next Steps

1. Confirm tier and brief with [stakeholder] by [date]
2. Run `positioning-messaging` to sharpen angles for this launch
3. Run `pre-mortem` to stress-test the plan before committing resources
4. Run `stakeholder-maps` to align internal champions and surface blockers
5. After launch, run `retro` → updates brain Section 7 with actuals
```

---

### Step 5: Update Brain Section 7

After brief is confirmed (user explicitly accepts or approves):

Write to `/foundation/brain.md` Section 7:

```markdown
## Launch: [Initiative Name]
- **Date planned:** [launch date]
- **Tier assigned:** [T#]
- **Tier rationale:** [one sentence]
- **Primary metric:** [metric + target]
- **Status:** Planned
- **Actuals:** [To be updated after retro]
```

Surface this to the user:
> "Logged to brain Section 7 as Planned. Run `retro` after launch to update
> with actuals — the 4th launch will be better calibrated than the 1st."

If the user declines brain write: proceed without writing. Do not force it.

---

## Outputs

- **Files written:** `/foundation/brain.md` Section 7 — new launch entry on confirmation.
- **Chat output format:** Tier assignment with rationale → full GTM brief in the
  structure above. Output is markdown formatted for copy-paste into Notion or Google Docs.
- **External side effects:** n.v.t.

---

## Verification

- Tier is stated with a one-sentence rationale before the brief.
- Brief contains all seven sections: Strategic Context, Channel Strategy, Success
  Metrics, Competitive Context, Proof Points, Timeline, Next Steps.
- Leading indicators are present alongside the primary metric.
- Channel recommendations are specific to ICP and motion type — not generic lists.
- Brain Section 7 write confirmed to user after brief acceptance.

---

## Do Not Use For

- **workflow-orchestrator** — when you need to chain multiple skills end-to-end
  (positioning → competitive → GTM → stakeholder maps) for a full launch program.
  Use this skill for the GTM strategy step within that program.
- **positioning-messaging** — when the primary need is messaging, copy, or positioning
  statement work rather than launch scope and channel strategy.
- **pre-mortem** — when the primary need is risk analysis before committing to a launch.
  Run `go-to-market-strategy` first, then `pre-mortem` on the output.
- **retro** — for post-launch review and brain Section 7 actuals update.

---

## Commands

### /tier
Assign a tier only — no full brief. Use when the user needs a quick scope decision
without the full strategy output.

```
/tier [initiative description]
```

Output format:
```
Tier: [T#]
Rationale: [one sentence — four signals applied]
Calibration note: [prior launch precedent if applicable, or "No prior precedent in brain"]
Confidence: [High / Medium / Low — based on signal quality]
Next: Run /brief for the full GTM strategy, or /pre-mortem to stress-test before committing.
```

---

### /brief
Generate the full GTM brief for an initiative. Assumes tier is already known or
runs /tier first.

```
/brief [initiative description]
```

Runs Steps 1–5 sequentially. Outputs the full structured brief.

---

### /calibrate
Review the tier assigned to a prior launch against what actually happened. Updates
brain Section 7 with actuals and surfaces a calibration rule for future launches.

```
/calibrate [launch name] — [what actually happened vs. what was projected]
```

Output format:
```
Launch: [name]
Tier assigned: [T#]
Actual performance: [what happened]
Calibration: [Over-resourced / Under-resourced / Correct]
Rule proposed: "[pattern statement for future similar launches]"
→ Add to brain Section 7? [Y/N]
```

---

### /history
Show launch history from brain Section 7. Useful before a new launch to calibrate
tier against prior initiatives of similar scope.

```
/history
/history [filter: T1 / T2 / T3 / T4 / segment name]
```

Output: table of prior launches with tier, metric, status, and actuals.

---

## Operating Rules

- **Load brain before intake.** ICP, positioning, and launch history change what tier
  is appropriate. A T2 for one company is a T3 for another.
- **All four tier signals must be applied.** Never assign tier on a single signal.
  Revenue potential alone does not make something T1.
- **Reflect back the initiative before tiering.** Assumption-surfacing is not polish —
  it's how misaligned briefs get caught before work starts.
- **Tier rationale is mandatory.** No tier without a one-sentence grounded reason.
  "It feels big" is not a rationale.
- **Leading indicators are required.** A brief with only a lagging metric has no
  early warning system. Always pair primary metric with at least one leading indicator.
- **Channel recommendations must be ICP-specific.** Generic channel lists (email,
  LinkedIn, events) are not acceptable. Every channel must have a reason tied to the
  ICP and motion type.
- **Calibration history must be checked.** Before confirming tier, check Section 7.
  A pattern of tier mismatches is a system problem, not a one-off.
- **Brain write requires explicit confirmation.** Never write to Section 7 without
  the user accepting the brief. Ask before writing.
- **T4 is not a downgrade — it's a scope decision.** Never use T4 as a way to avoid
  work. Use it when external GTM investment is genuinely not warranted.
- **Proof point gaps must be flagged.** If the brief requires a claim that has no
  supporting proof point in Section 5, surface it as a risk before launch.

---

## Quality Gate

Runs after brief generation, before delivery. Surface failures — do not deliver
incomplete output.

| Check | Standard | Pass = |
|---|---|---|
| Tier assigned with rationale | All four signals applied, one-sentence rationale stated | Yes |
| Brain loaded | Sections 2, 3, 4, 5, 7 extracted before brief was generated | Yes |
| Intake complete | Initiative reflected back and confirmed before brief generated | Yes |
| Leading indicator present | At least one leading indicator alongside primary metric | Yes |
| Channel specificity | Every channel has ICP-specific rationale, not generic listing | Yes |
| Competitive context present | Primary alternative named with attack and defend angle | Yes |
| Proof point check | Missing proof points flagged inline if brief requires unverified claims | Yes |
| Calibration history checked | Section 7 checked; precedent noted or absence noted | Yes |
| Timeline present | Tier-appropriate timeline with milestones and owners | Yes |
| Next steps include retro trigger | Step 5 of next steps names retro for brain update | Yes |

**On any failure:** flag the specific check, fix before delivering. Do not present
a partial brief as complete.

---

## Self-Improvement Loop

### Before every session:
1. Load `/foundation/brain.md` Section 7 — scan for tier calibration patterns.
   If a tier was consistently over- or under-assigned for a given initiative type,
   apply that as a default calibration before running Step 3.
2. Check `knowledge/gtm/rules.md` if it exists — apply confirmed rules silently.
3. Check `knowledge/gtm/hypotheses.md` — note any hypothesis testable with today's launch.

### After every session where a brief was generated:
1. Extract any tier calibration observation → `knowledge/gtm/hypotheses.md`
2. If the same calibration pattern has appeared 3+ times → propose promotion to
   `knowledge/gtm/rules.md` with user approval.
3. If proof point gaps were flagged → log to `knowledge/gtm/knowledge.md` as
   a signal for the proof points skill to address.
4. Append session summary to `sessions/log.md`.

**Self-Improvement Trigger format — surface before encoding, never silently:**

```
🔁 SELF-IMPROVEMENT TRIGGER
Pattern: [what was observed this session]
Proposed update: [exact wording of what would be added or changed]
Location: [file path]
Awaiting approval before encoding.
```

---

## Changelog

### v2.0.0 — 2026-06-06
Full rebuild to SKILL-SPEC v2.0.0. Replaced README-grade file (93 lines) with
production-grade skill.

Changes from v1.0.0:
- Added all 7 required sections: Trigger, Inputs, Pre-flight, Steps, Outputs,
  Verification, Do Not Use For
- Intake step added — tier never assigned without reflected-back initiative
- Four-signal tier assignment model formalised with calibration history check
- Full GTM brief structure with 7 sections including leading indicators
- /tier, /brief, /calibrate, /history commands added
- Brain contract declared: reads Sections 2, 3, 4, 5, 7; writes Section 7
- Operating rules (10), quality gate (10 checks), self-improvement loop added
- Explicit routing away from workflow-orchestrator, positioning-messaging, pre-mortem, retro

### v1.0.0 — 2026-04-01
Initial build. Tier framework and brain integration concept. README-grade.
