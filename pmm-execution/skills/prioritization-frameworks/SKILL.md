---
name: hs-prioritization-frameworks
version: 1.0.0
description: >
  GTM-native prioritization reference for PMMs — 9 frameworks with formulas, PMM interpretation
  layer, and launch tier output logic (T1–T4). Use when selecting a prioritization method,
  scoring strategic projects, triaging a launch backlog, or deciding how much GTM weight a
  product or initiative deserves. Trigger on: "how do I prioritize this", "should this be a
  big launch", "what tier is this", "help me score these initiatives", "RICE vs ICE",
  "prioritization framework", "launch backlog", "what gets GTM investment", "how do I decide
  what to launch first", or any request to rank, score, or tier product or GTM initiatives.
---

# hs-prioritization-frameworks

A PMM-practitioner reference for selecting and applying the right prioritization framework —
with GTM intelligence baked in at every step.

---

## ⓪ PMM CONTEXT — LOAD FIRST

Before starting, check `.agents/product-marketing-context.md`.

**If it exists — load silently:**
- `## ICP Prioritisation` → defines which segments a high-scoring initiative must serve to qualify as T1
- `## Revenue Levers` → stack-ranked levers anchor what "Impact" actually means in RICE/ICE
- `## Goals & KPIs` → North Star and OMTM shape Opportunity Score weighting
- `## Positioning` → Kano classification should align with how you're positioning each feature
- `## Big Bet Campaigns` → pre-qualifies which initiatives are already candidates for T1/T2

**Confidence awareness:** If Revenue Levers or ICP is 🔴, flag before scoring:
> "Revenue Levers is marked Placeholder — tier recommendations may lack precision. Update context first?"

**If missing:** Proceed. Surface once:
> "Run `hs-product-marketing-context BUILD` for sharper tier recommendations. Continuing."

---

## RELATED SKILLS

Wire prioritization outputs into the right downstream skill:

- **hs-gtm-launch-planner** → T1–T4 tier output feeds directly into launch planning; tier definitions must stay in sync
- **hs-gaccs-brief** → tier recommendation drives campaign brief scope and resource allocation
- **hs-brainstorm-okrs** → RICE/ICE scores should map to OKR project prioritization; high-scoring initiatives become Q-level bets
- **hs-competitive-battlecard** → competitive urgency input for Risk vs Reward scoring; battlecard win/loss data improves Confidence scores
- **hs-value-prop-statements** → Kano classification determines messaging hierarchy in value prop work
- **hs-product-marketing-context** → this skill reads from it; update it when ICP or revenue lever assumptions shift

---

## REASONING ARCHITECTURE

These three blocks govern how the skill thinks — not just what it produces.
They run automatically at the start, during decisions, and at the end of every session.

### Block 1 — Knowledge Architecture (Learning Loop)

**Before starting any task:**
1. Check whether a `knowledge/` folder exists in the skill directory.
2. If it exists, read `knowledge/INDEX.md` and load the relevant domain folder(s):
   - `knowledge/prioritization/` — scoring patterns, confirmed rules, active hypotheses
   - `knowledge/gtm/` — GTM-specific signals, tier calibration patterns, launch outcomes
   - `knowledge/[company]/` — company-specific signals if the user has seeded this
3. Apply all rules in `rules.md` by default — no re-explanation needed.
4. Check `hypotheses.md` — if any hypothesis can be tested with today's session, test it.

**At the end of every session where scoring or tier decisions are made:**
1. Extract 1–3 insights from the session (scoring patterns, tier calibration signals, framework misapplications caught).
2. Store them in the appropriate domain folder under `knowledge/`:
   - Unconfirmed → `hypotheses.md`
   - Confirmed 3+ times → auto-promote to `rules.md`
   - Contradicted by new data → demote from `rules.md` back to `hypotheses.md`
3. Update `knowledge/INDEX.md` to reflect any new domains or files added.

**Knowledge folder structure:**
```
knowledge/
  INDEX.md                    ← routes to each domain folder
  prioritization/
    knowledge.md              ← facts and patterns about framework application
    hypotheses.md             ← patterns seen 1–2 times, needs more data
    rules.md                  ← confirmed 3+ times, applied by default
  gtm/
    knowledge.md              ← tier calibration signals, launch outcome patterns
    hypotheses.md
    rules.md
  [company-slug]/             ← optional, seeded by user context
    knowledge.md
    hypotheses.md
    rules.md
```

> **Note on environment:** The full learning loop (persistent `/knowledge/` folder) works in Claude Code and Cowork where the file system persists. In Claude.ai chat, apply in-session pattern tracking only — surface insights at end of session so the user can carry them forward manually.

---

### Block 2 — Decision Journal (Reviewable Reasoning)

**Before making any tier recommendation or framework selection:**
1. Check whether a `decisions/` folder exists. If it does, grep it for prior decisions in the relevant area (tier calibration, framework selection, scoring criteria).
2. If a prior decision exists → follow it, unless new information in this session explicitly invalidates the reasoning.
3. If no prior decision exists — or you are replacing one — log it immediately after making it.

**Decision log format:**
```
File: decisions/YYYY-MM-DD-{topic}.md

## Decision: {what you decided}
## Context: {why this came up}
## Alternatives considered: {what else was on the table}
## Reasoning: {why this option won}
## Trade-offs accepted: {what you gave up}
## Supersedes: {link to prior decision if replacing one}
```

**When to log a decision:**
- Choosing one framework over another for a specific scoring task
- Assigning a tier where the signal was ambiguous or split across dimensions
- Overriding a prior tier recommendation based on new competitive or market data
- Any recommendation that will affect GTM resource allocation, not just today's session

---

### Block 3 — Quality Gate (Independent Evaluation Pass)

**The problem:** Claude confidently marks its own tier recommendations as correct — every time. The agent that scored the initiative cannot objectively evaluate its own output.

**The fix:** After generating any tier recommendation or scored output, run a separate evaluation pass — treat it as a different role (evaluator, not author). Do not carry forward the confidence of having just written it.

**Evaluation pass protocol (runs automatically after every `/score`, `/tier`, and `/audit`):**
1. Re-read the output cold, as if you didn't produce it.
2. Run each Quality Gate below as binary pass/fail — no partial credit.
3. If any gate fails, flag it with an ADVERSARIAL CALLOUT and rewrite before delivering.
4. Report gate results inline with the output.

**Quality Gates:**
- **Gate 1 — Signal integrity:** Is the tier based on scored evidence, or assumption? If no customer data supports the Opportunity Score, flag it.
- **Gate 2 — Confidence honesty:** Is the Confidence input ≥7 without win/loss data, customer evidence, or prior validation? That's inflation — call it out.
- **Gate 3 — Framework fit:** Is the right framework being used for the decision type? Applying Eisenhower to a launch decision is a failure, not a suboptimal choice.
- **Gate 4 — Tier consistency:** Does the tier output align with `hs-gtm-launch-planner` tier criteria? If not, flag the conflict before the PMM presents to stakeholders.
- **Gate 5 — Actionability:** Does the output tell the PMM what to do next — specifically? A tier without a rationale sentence and a clear next step is incomplete.

Do not deliver output that has not passed this evaluation pass. Rewrite first, then deliver.

---

## HOW TO START

Paste any command below — or describe your situation in plain language.
The skill will detect what you need and run the right mode automatically.

---

## COMMANDS

### /score
Score one or more initiatives using the right framework for the decision type.
The skill will ask what you're deciding, select the appropriate framework, run the scoring,
and output a tier recommendation with rationale.

**Example prompts:**
- `/score` — starts intake; skill selects the right framework
- `Score these three initiatives for next quarter's roadmap`
- `Help me decide which of these five features deserves a big launch`
- `We're choosing between a new market entry and a product expansion — which gets GTM priority?`
- `I need to prioritize a backlog of 8 campaign ideas with my team`

---

### /tier
Assign a launch tier (T1–T4) to a named initiative based on available signals.
Produces a tier assignment with one-sentence rationale, confidence score, and next step.

**Example prompts:**
- `/tier` — intake: what's the initiative and what signals do you have?
- `Is this a T1 or T2 launch?`
- `We're launching a new pricing tier — what tier does this warrant?`
- `Help me tier this quarter's launches so I can allocate PMM time correctly`
- `My CEO wants to treat this as a T1. I'm not sure that's right. Pressure-test it.`

---

### /compare
Compare two or more frameworks and recommend which fits the current decision.
Useful before a planning meeting or workshop where you need to choose a method.

**Example prompts:**
- `/compare RICE vs ICE` — explains the trade-offs and recommends one
- `What's the difference between Opportunity Score and ICE?`
- `Should I use a Weighted Decision Matrix or RICE for this stakeholder decision?`
- `Which framework works best for prioritizing a new market entry?`
- `My team uses MoSCoW but it never works. What should we use instead?`

---

### /workshop
Run a live prioritization workshop session for a cross-functional group.
Skill acts as the facilitator: selects framework, guides scoring, surfaces conflicts,
and outputs a ranked list with tier assignments the group can align on.

**Example prompts:**
- `/workshop` — starts the facilitation flow
- `I'm running a planning session with Product, Sales, and PMM. Help me run the prioritization.`
- `We have 12 initiatives and 60 minutes. What's the fastest way to get to a ranked list?`
- `Facilitate a scoring session for our Q3 GTM bets`

---

### /audit
Pressure-test an existing prioritization decision or tier assignment.
Runs the Quality Gate against a prior decision and surfaces what's weak, inflated, or missing.

**Example prompts:**
- `/audit` — paste your current tier assignment or scoring output
- `We ranked these launches last quarter. Looking back, was the scoring right?`
- `My leadership disagreed with my T1 call. Help me audit whether I was right.`
- `Pressure-test this RICE score — I think Confidence is inflated`
- `We under-resourced this launch. Was it a bad tier call or a bad execution call?`

---

### /learn
Extract insights from a completed launch or scoring session.
Updates knowledge files with what the tier prediction got right or wrong.

**Example prompts:**
- `/learn` — paste a launch debrief or post-mortem
- `This was supposed to be a T2 but it performed like a T1. What does that tell us?`
- `We over-invested in this launch based on the score. Let's extract what we missed.`
- `Update our scoring patterns based on what we learned from the Q1 launches`

---

## GTM LAUNCH TIER OUTPUT

Every framework in this skill feeds into a tier recommendation.
Use this as your output layer once you've scored.

| Tier | Signal | What It Means |
|------|--------|---------------|
| **T1** | High Opportunity Score, large addressable segment, high Confidence, strong strategic fit, competitive urgency | Full GTM motion. All channels, all teams, exec visibility. |
| **T2** | Strong signal on 2–3 dimensions but not all — real opportunity, limited reach or confidence | Significant launch. Targeted GTM. Not all hands on deck. |
| **T3** | Moderate signal — validated problem, but narrow reach, low confidence, or high effort | Soft launch. Focused enablement. Limited external noise. |
| **T4** | Low scores across the board, or too early to validate | Internal only, beta, or deprioritize. No GTM investment yet. |

> **Tier Rationale Format:** Always output as: `[T#] — [one sentence why].`
> Example: *T2 — Strong customer pain signal in the upper-left quadrant, but Confidence is limited by thin win/loss data.*

> **Tier Sync:** Tier definitions here must stay consistent with `hs-gtm-launch-planner`. If they conflict, flag it before presenting to stakeholders. Do not paper over the conflict.

> **GTM Overlay:** Marketing tactics by tier will be added in a future update. Your own tier-based frameworks will be added to the GTM Framework Overlay section below.

---

## FRAMEWORK REFERENCE

### 1. Opportunity Score

**What it does:** Surfaces highest-value customer problems by combining how important a need is with how poorly it's currently being served.

**Formula:**
- Opportunity Score = Importance × (1 − Satisfaction)
- Current Value = Importance × Satisfaction
- Value Created = Importance × (S2 − S1)

Normalize both inputs to 0–1. High Importance + low Satisfaction = highest score = best opportunity. Plot on an Importance vs Satisfaction chart — upper-left quadrant is your target.

**PMM Use:** Run this before any launch debrief or roadmap review. If a problem scores high here but your product doesn't address it fully, that's a positioning gap — own that narrative before Engineering does.

**Tier signal:** High Opportunity Score on a problem your product solves cleanly → strong T1 or T2 signal. Upper-left quadrant with no credible competitor solution → T1 candidate.

---

### 2. ICE Framework

**What it does:** Prioritizes initiatives by balancing value, risk, and implementation cost in a single score.

**Formula:**
- I (Impact) = Opportunity Score × Number of customers affected
- C (Confidence) = How confident are we? (1–10)
- E (Ease) = How easy to implement? (1–10)
- **Score = I × C × E** — higher scores go first

**PMM Use:** Use ICE when triaging a backlog of launch candidates quickly. Confidence is your sanity check — if you're scoring ≥7 on Confidence without customer evidence or win/loss data, you're inflating. Call it out before it drives a bad tier call.

**Tier signal:** Top-quartile ICE score → T1 or T2 candidate. Low Confidence drags a strong Impact score to T3.

---

### 3. RICE Framework

**What it does:** Adds granularity to ICE by separating Reach from Impact. Built for teams that need to defend prioritization decisions to leadership.

**Formula:**
- R (Reach) = Number of customers affected
- I (Impact) = Opportunity Score (value per customer)
- C (Confidence) = 0–100%
- E (Effort) = Person-months to implement
- **Score = (R × I × C) / E**

**PMM Use:** Use RICE when building a prioritization case for leadership or cross-functional stakeholders. The Reach input forces you to define your addressable segment explicitly — which is exactly where PMMs should be leading the conversation, not following it.

**Tier signal:** High Reach + high Impact + high Confidence = T1. Low Reach narrows to T2 or T3 even with a strong Impact score.

---

### 4. Eisenhower Matrix

**What it does:** Separates tasks by Urgency and Importance across a 2×2. A personal productivity tool.

**PMM Use:** Use this for your own task management during a launch sprint — not for strategic decisions. If you're using Eisenhower to prioritize launches, you're operating tactically when you should be operating strategically. Reserve it for workload triage, not GTM decisions.

**Tier signal:** Not applicable. No tier output from this framework.

---

### 5. Impact vs Effort Matrix

**What it does:** Quick 2×2 triage. High Impact / Low Effort quadrant wins first.

**PMM Use:** Useful in workshop settings to rapidly sort a large list of ideas with a cross-functional group. Not rigorous enough for strategic launch decisions. Use it to build alignment and narrow the field, then hand off to RICE or ICE for actual scoring.

**Tier signal:** High Impact / Low Effort items are T2–T3 candidates pending deeper scoring. Never assign T1 from this framework alone.

---

### 6. Risk vs Reward Matrix

**What it does:** Like Impact vs Effort, but replaces Effort with Risk. Useful when implementation cost is roughly equal across options but uncertainty varies.

**PMM Use:** Use when evaluating new market entry, pricing changes, or positioning pivots where the cost of being wrong is high. Map against your Confidence score from ICE/RICE to pressure-test assumptions before committing GTM resources. Pull win/loss data from `hs-competitive-battlecard` to sharpen the Risk input.

**Tier signal:** High Reward / Low Risk = T1 or T2. High Reward / High Risk = T2 or T3 with explicit Confidence thresholds set before proceeding.

---

### 7. Kano Model

**What it does:** Classifies features by how they affect customer satisfaction — Must-be, Performance, Attractive, Indifferent, Reverse. A diagnostic tool, not a prioritization tool.

**PMM Use:** Use before writing messaging, not after. Kano tells you whether a feature is table stakes (don't lead with it — assumed), a differentiator (lead with it), or a delighter (use it to create urgency). If you're leading your launch narrative with Must-be features, your messaging is invisible. Feed Kano output directly into `hs-value-prop-statements` to set messaging hierarchy.

**Tier signal:** Attractive features with strong Opportunity Scores → T1 messaging anchor. Must-be features don't drive tier — they're baseline expectations.

---

### 8. Weighted Decision Matrix

**What it does:** Assigns weights to multiple criteria, scores each option, and produces a ranked list. Useful when stakeholders have competing priorities that all need to be represented.

**PMM Use:** Use when you need cross-functional alignment on a decision with multiple legitimate competing criteria — launch timing, segment fit, revenue potential, competitive urgency. Build the matrix with the room, not in isolation. Wire GTM variables (pipeline impact, segment size, competitive pressure) directly into the weights so the output is already tier-relevant.

**Tier signal:** Build tier criteria into the matrix weights directly. A well-structured matrix with GTM-native weights can output a tier recommendation without additional translation.

---

### 9. MoSCoW

**What it does:** Categorizes requirements into Must Have, Should Have, Could Have, Won't Have.

**PMM Use:** Use sparingly. MoSCoW inflates the Must Have category under stakeholder pressure — set a hard cap of 60% maximum before you start, or the framework breaks. More useful for scoping what's included in a launch at a given tier than for determining the tier itself. The Won't Have column is as important as the Must Have — it's where scope creep goes to die.

**Tier signal:** Not a tier input. Use it to scope deliverables within a tier, not to assign the tier.

---

## FRAMEWORK SELECTION GUIDE

| Situation | Recommended Framework |
|-----------|----------------------|
| Prioritizing customer problems before a roadmap cycle | Opportunity Score |
| Quickly triaging a launch backlog | ICE |
| Building a leadership-ready prioritization case | RICE |
| Evaluating new market entry or pricing risk | Risk vs Reward + Confidence check |
| Aligning a cross-functional group in a workshop | Impact vs Effort → hand off to ICE/RICE |
| Writing launch messaging hierarchy | Kano → feed into `hs-value-prop-statements` |
| Scoping deliverables for a launch at a given tier | MoSCoW |
| Managing your own launch sprint workload | Eisenhower Matrix |
| Multi-criteria decision with competing stakeholder priorities | Weighted Decision Matrix |

---

## TEMPLATES

- [Opportunity Score Template — Google Slides](https://docs.google.com/presentation/d/1jg-LuF_3QHsf6f1nE1f98i4C0aulnRNMOO1jftgti8M/edit#slide=id.g796641d975_0_3)
- [Opportunity Score intro (PDF)](https://drive.google.com/file/d/1ENbYPmk1i1AKO7UnfyTuULL5GucTVufW/view)
- [ICE Template — Google Sheets](https://docs.google.com/spreadsheets/d/1LUfnsPolhZgm7X2oij-7EUe0CJT-Dwr-/edit?usp=share_link&ouid=111307342557889008106&rtpof=true&sd=true)
- [RICE Template — Google Sheets](https://docs.google.com/spreadsheets/d/1S-6QpyOz5MCrV7B67LUWdZkAzn38Eahv/edit?usp=sharing&ouid=111307342557889008106&rtpof=true&sd=true)

---

## GTM FRAMEWORK OVERLAY

*This section will be populated with GTM-native frameworks and marketing tactics by tier
in a future update. Your own tier-based frameworks will be added here.*

---

## ⑨ SELF-IMPROVEMENT LOOP

Run at the end of every session, after all outputs are delivered and the Quality Gate has passed.

### Extract and store knowledge

**Patterns** — what scoring sessions consistently reveal about framework application or tier calibration.
**Hypotheses** — things that seemed true but need more data (source + date required).
**Rules** — confirmed patterns. Threshold: **3+ confirmations** across different initiatives or contexts.

```
knowledge/prioritization/
  knowledge.md    → tagged: framework + date + initiative type
  hypotheses.md   → new entries + increment confidence on existing
  rules.md        → promote at ≥3 confirmations; demote if contradicted

knowledge/gtm/
  knowledge.md    → tier calibration signals, launch outcome patterns
  hypotheses.md
  rules.md
```

Update `knowledge/INDEX.md`. Append to `sessions/log.md`.

### Log architectural decisions

When this session makes or changes a structural decision — about tier assignment, framework
selection, or scoring criteria — log it:

```
File: decisions/YYYY-MM-DD-{topic}.md

## Decision: {what was decided}
## Context: {why this came up}
## Alternatives considered: {what else was on the table}
## Reasoning: {why this option won}
## Trade-offs accepted: {what was given up}
## Supersedes: {link to prior decision if replacing one}
```

### Promotion / Demotion logic

- Hypothesis → Rule: confirmed **3+** times across different initiatives or contexts
- Rule → Hypothesis: contradicted by new data — add note + date
- Stale hypothesis: untested in 90 days — flag for review in next maintenance pass

### Self-maintenance schedule

> **Weekly (if running multiple sessions):** "Any hypotheses testable with this week's scoring work?"
> **Monthly:** "Review all rules — any tier calibration rules contradicted by recent launch outcomes?"
> **Quarterly:** "Prune stale patterns. Review all decisions. Archive anything not tested in 90 days."

When the maintenance prompt fires: run the review and update files before proceeding with the session.

### Deployment

**Claude Code / Cowork:** All files update automatically across sessions.
**Claude.ai:** Output updated content in a copyable block at end of session:
`📋 SAVE THIS — Knowledge, decisions, and session log updates for next session`

---

## SELF-IMPROVEMENT TRIGGERS

Surface proposed updates to this skill if:
- A framework proves systematically misapplied by PMMs in practice — update the PMM Use callout
- A tier calibration rule is confirmed 3+ times — promote to `rules.md` and flag for skill update
- A new GTM framework is ready to be added to the overlay section
- A Quality Gate catches the same failure mode 3+ times — tighten the gate criteria
- `hs-gtm-launch-planner` tier definitions drift from this skill's — flag immediately

All proposed skill updates require explicit user approval before encoding.
