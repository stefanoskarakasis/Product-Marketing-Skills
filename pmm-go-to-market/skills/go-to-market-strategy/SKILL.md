---
name: go-to-market-strategy
version: 3.0.0
description: >
    Assigns launch tier (T1–T4) using a four-signal framework and generates a complete GTM brief with positioning angles, channel strategy, success metrics, and competitive context. Reads brain (ICP, positioning, competitive, proof points) and, when available, guardrails from prior launches the user has logged.
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-08-24
---

# Go-to-Market-Strategy

## How This Works

Assigns a launch tier and generates a complete GTM strategy brief grounded in your brain. Not a template-filler. A strategic thinking partner that interrogates scope before recommending resource investment.

The skill runs in 6 steps:

**Step 0** — Load brain context (ICP, positioning, competitive landscape, proof points) and, if the user maintains `/context/meta-patterns.md`, guardrails logged there.

**Step 1** — Intake: Initiative name, success metric (90 days), timeline.

**Step 2** — Load brain silently (Sections 2, 3, 4, 5).

**Step 3** — Apply four-signal tier assignment (market impact, revenue potential, competitive urgency, resource requirement).

**Step 4** — Generate full GTM brief (7 sections: strategic context, channels, metrics, competitive, proof points, timeline, next steps).

**Step 5** — Learning Close: log the session to `/context/skill-sessions.md`.

---

## Trigger

- **When:** Assigning a launch tier and building a full GTM strategy brief for a product, feature, pricing change, or market expansion.
- **Not for:** Chaining this with other skills into one program → use `workflow-orchestrator`. Choosing which acquisition motion(s) to invest in → use `gtm-motions` before this skill if Channel Strategy needs real motion-fit backing. Messaging and positioning work itself → use `positioning-messaging` after this skill. Risk analysis → use `pre-mortem` after this skill. Post-launch review → use `retro`.
- **Example prompts:**
  - "What tier is this launch?"
  - "GTM strategy for our new pricing page"
  - "Help me scope this feature launch"
  - "How should we launch this?"
  - "Plan my launch"

---

## Inputs

- **Args:** Initiative name, 90-day success metric, timeline. Free format — Step 1 intake fills gaps conversationally.
- **Defaults:** If brain is missing or Section 2 (ICP) is empty, this skill blocks and directs the user to `product-marketing-context` first — see Pre-flight.
- **Context keys:**
  - `/foundation/brain.md` — required. Sections 2 (ICP), 3 (Positioning), 4 (Competitive), 5 (Proof Points).
  - `/context/meta-patterns.md` — optional; recurring patterns the user has logged from prior GTM briefs.
  - **Brain contract:** Reads Sections 2, 3, 4, 5. Writes: none — this skill does not write to `/foundation/brain.md` on its own.

---

## Pre-flight

- Load `/foundation/brain.md` Sections 2, 3, 4, 5 if it exists — see Step 0 for the full sequence.
- Load `/context/meta-patterns.md` if it exists, and surface any guardrail that has fired 2+ times in prior GTM briefs — see Step 0.
- **Hard block:** if `/foundation/brain.md` is absent or Section 2 (ICP) is empty, stop and direct the user to run `product-marketing-context` first — GTM strategy without ICP and positioning produces generic output, not defensible strategy.

---

## Steps

### Step 0 — Pre-Flight: Load Context & Surface Guardrails

Before intake, load:
- **Brain context** (Sections 2, 3, 4, 5): ICP, positioning, competitive landscape, proof points — these anchor all tier signals
- **Guardrails** from `/context/meta-patterns.md`, if that file exists in the user's workspace: if a pattern has actually fired 2+ times in prior GTM briefs logged there, surface it now

**Surface guardrails like this:**

````
🔁 PATTERN FROM PRIOR GTM BRIEFS

I've seen [pattern description] in 2+ prior sessions.
Examples: [specific launches or outcomes]

Quick check: Does this apply to your initiative?
- If YES → We'll watch for this during brief generation
- If NO → Let's flag it if it emerges
````

You can skip a guardrail if you disagree, but you'll see it first. If `/context/meta-patterns.md` doesn't exist, skip this step silently.

**Gate check — brain is missing or ICP is empty:**

If `/foundation/brain.md` is absent or Section 2 is empty:
> "GTM strategy needs your ICP and positioning to produce a defensible plan — not
> a generic one. Run `beachhead-segment` first (it'll build a quick brain for you
> in ~3 minutes as part of finding your target segment), then come back here."

If brain exists but only has 🟡 Quick-Brain sections (not full):
> "Your brain has quick-start answers from beachhead but hasn't been expanded.
> That's enough to proceed — flagging that a fuller `product-marketing-context`
> pass would sharpen this GTM plan. Continue with current brain? [Yes / expand first]"

---

### Step 1 — Intake (Conversational, One Round)

Ask in one message. Never generate brief before this is complete.

> "Before I assign a tier and build the brief, three things I need:
>
> 1. **What's the initiative?** (Product, feature, pricing change, new segment, market expansion — one sentence)
>
> 2. **What does success look like in 90 days?** Specific metric with a number.
>
> 3. **Timeline?** Launch date or rough window."

Reflect back in 2 sentences:
> "Got it. We're launching [X] for [segment] with a goal of [metric] by [date]. Let me check the brain and assign a tier."

---

### Step 2 — Load Brain Context

Load silently. Extract Sections 2, 3, 4, 5. Do not narrate.

If the user has prior launches they can share (with tiers assigned and how they actually performed), ask for that context to sharpen the calibration.

---

### Step 3 — Assign Tier

Apply all four signals before assigning. Single signal does not override others.

| Signal | T1 | T2 | T3 | T4 |
|---|---|---|---|---|
| **Market impact** | New category or primary segment | Major new segment or significant feature | Existing segment, incremental feature | Internal only, maintenance |
| **Revenue potential** | Materially moves ARR/NRR | Meaningful pipeline contribution | Conversion or retention support | Minimal or indirect |
| **Competitive urgency** | Closes gap or creates advantage | Responds to or anticipates competitor | No immediate pressure | n/a |
| **Resource requirement** | All teams, full budget, exec visibility | 2–4 teams, dedicated PMM, targeted budget | PMM + one team, standard budget | Minimal, no external comms |

**Tier definitions:**
- **T1** — Company bet. 6–12 weeks. All channels. Full exec alignment.
- **T2** — Major initiative. 2–4 weeks. Targeted GTM. Dedicated PMM.
- **T3** — Routine launch. 1 week. Focused enablement. Limited external comms.
- **T4** — Minimal lift. Internal or beta only. Changelog or in-product only.

**Calibration check:** If the user shared a similar prior launch and its actual outcome, use it — name the precedent explicitly:
> "Based on [prior launch], similar scope was assigned T2 but performed at T1. Recommending T1 here to avoid under-resourcing."

Output tier with one-sentence rationale before generating brief:
> `[T#] — [one sentence why, grounded in the four signals]`

---

### Step 4 — Generate Full GTM Brief

Generate only after tier is assigned. Structure (7 sections):

````markdown
## GTM Brief — [Initiative Name]
**Tier:** [T1 / T2 / T3 / T4]
**Rationale:** [one sentence — four signals applied]
**Launch date:** [date or range]
**DRI:** [name]
**Success metric:** [specific number + timeframe]

### Strategic Context
**Why now:** [1–2 sentences on market timing or competitive signal]
**ICP fit:** [Who specifically this is for, from brain Section 2 + buying trigger]
**Positioning angle:** [Sharpest differentiator, from brain Section 3]

### Channel Strategy
| Channel | Why | Tactic | Owner |
|---|---|---|---|
| [Primary] | [Specific reason tied to ICP] | [Concrete tactic] | [Function] |
| [Secondary] | [Specific reason] | [Concrete tactic] | [Function] |

If the primary/secondary channels above were chosen by tier convention
alone rather than a real motion-fit scoring pass, flag it:
> "Channel Strategy below uses tier-standard channels. For a motion
> selection backed by ACV, sales-cycle, and readiness scoring instead of
> convention, run `gtm-motions` and fold its primary/secondary into this
> table before finalizing."

**Tier-appropriate channel mix and tone** — match investment to tier, don't
default every launch to the T1 playbook:

| Tier | Typical channels | Headline style | Tone |
|---|---|---|---|
| T1 | Press release, analyst briefing, webinar, multi-touch email, sales deck refresh, full landing page | Customer outcome, not feature | Strategic, confident |
| T2 | Email announcement, sales one-pager, webinar or lunch-and-learn, community/Slack post | Problem statement as hook | Professional, benefit-focused |
| T3 | Release notes, opt-in email, in-app notification, Slack | What/why/who in 1-2 sentences each | Direct, informative |
| T4 | Release notes only, internal Slack | Feature name + one-sentence benefit | Matter-of-fact |

### Success Metrics
| Metric | Type | Target | Timeframe | Measurement |
|---|---|---|---|---|
| [Primary] | Lagging | [number] | [date] | [where] |
| [Leading indicator 1] | Leading | [number] | [earlier date] | [where] |
| [Leading indicator 2] | Leading | [number] | [earlier date] | [where] |

### Competitive Context
**Primary alternative:** [From brain Section 4]
**Defensive angle:** [What you say when they bring it up]
**Attack angle:** [Specific gap the alternative has]

### Proof Points
- [Claim + metric or quote]
- [Claim + metric or quote]

⚠️ [If missing proof points: flag]

### Timeline
| Week | Milestone | Owner |
|---|---|---|
| -4 to -2 | Pre-launch prep | PMM |
| -1 | Launch readiness check | PMM + Sales |
| 0 | Launch day | All |
| +2 | First signal check | PMM |
| +12 | Retro trigger | PMM |

### Next Steps
1. Confirm tier and brief with [stakeholder] by [date]
2. Run gtm-motions if Channel Strategy above needs real motion-fit backing, not the tier-standard default
3. Run positioning-messaging to sharpen angles
4. Run pre-mortem to stress-test
5. Run stakeholder-maps for internal alignment
6. After launch, run retro
````

If the user wants this brief saved anywhere, ask where — this skill doesn't write the brief itself to any file on its own.

---

### Step 5 — Learning Close

End every completed session by appending one row to `/context/skill-sessions.md`
(create the file with a header row if it doesn't exist yet):

````yaml
skill: go-to-market-strategy
session_date: [YYYY-MM-DD]
pattern: [one falsifiable statement about what happened this session, or "none"]
source: [surprised / wrong / missing / n.v.t.]
````

Write this row directly — do not ask the user for permission. This is an
observational log entry, separate from the GTM brief above, which still
requires the user's go-ahead on where to save it. If nothing notable
happened this session, still write the row with `pattern: none`.

---

## Outputs

- **Files written:** `/context/skill-sessions.md` — one appended row per
  session, per Step 5. The GTM brief itself is delivered in chat only;
  if the user wants it saved anywhere, ask where — this skill doesn't
  write the brief to any file on its own.
- **Chat output format:** Tier assignment with one-sentence rationale
  (Step 3), followed by the full 7-section GTM brief (Step 4).
- **External side effects:** None beyond the session log above.

---

## Verification

- Guardrails checked at Step 0 if `/context/meta-patterns.md` exists.
- Brain blocked and directed to `product-marketing-context` if ICP is missing — never generated on assumption alone.
- All four tier signals reasoned through before a tier is assigned (Step 3).
- Tier stated with a one-sentence, signal-grounded rationale — not "it feels big."
- Full 7-section brief generated only after the tier is assigned.
- Session logged to `/context/skill-sessions.md` (Step 5).

---

## Operating Rules

- **Load brain before intake.** ICP shapes what tier is appropriate.
- **First-run blocks without brain.** Missing brain triggers onboarding, not a warning.
- **All four tier signals must be applied.** Revenue alone does not make something T1.
- **Tier rationale mandatory.** One-sentence grounded reason required. "It feels big" is not a rationale.
- **Leading indicators required.** Every brief has ≥1 leading indicator + primary metric.
- **Channel recommendations ICP-specific.** Every channel tied to ICP + motion type, not generic.
- **Calibration history used when the user has it.** Don't require it, but use it if offered.
- **Proof point gaps must be flagged.** If brief requires unverified claim, surface before launch.

---

## Quality Gate

| Check | Pass = |
|---|---|
| Four signals applied | All signals reasoned through before tier assigned |
| Brain loaded | Sections 2, 3, 4, 5 extracted before brief |
| Intake complete | Initiative reflected back and confirmed |
| Leading indicator present | ≥1 leading indicator + primary metric |
| Channel specificity | Every channel has ICP-specific reason |
| Competitive context | Primary alternative + attack/defend angles |
| Proof point check | Missing proof points flagged if brief requires them |
| Timeline present | Tier-appropriate timeline with milestones |
| Next steps include retro | Retro named as post-launch trigger |
| Learning Close ran | `/context/skill-sessions.md` has a new row for this session |

---

## Do Not Use For

- **workflow-orchestrator** — for chaining multiple skills end-to-end
- **gtm-motions** — for scoring and selecting acquisition motions against ICP deal economics (run before this skill for real Channel Strategy backing)
- **beachhead-segment** — for choosing the target segment itself (run before this skill if no beachhead is confirmed yet)
- **positioning-messaging** — for messaging work (use after this skill)
- **pre-mortem** — for risk analysis (use after this skill)
- **retro** — for post-launch review (run after)
