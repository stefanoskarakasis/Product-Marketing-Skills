---
name: beachhead-segment
version: 1.0.0
description: >
  Identifies and scores your highest-priority beachhead segment — the first wedge
  of customers to dominate before expanding. Uses four-dimension scoring (Burning
  Pain, Willingness to Pay, Winnability, Referral Potential) with blocking gates
  and confidence tracking. Writes to brain Section 2 and feeds directly into
  go-to-market-strategy. Trigger on: "which segment should we focus on first",
  "our ICP is too broad", "pick a beachhead", "where do we win first", "which
  customers should we prioritise", "help me narrow our target market", "what's
  our wedge", "segment selection", or any request to identify, score, or pressure-
  test a first-focus customer segment before scaling GTM investment.

metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-06-06
---

# Beachhead Segment

Identifies the highest-probability segment to dominate first — before expanding.

Not a market sizing exercise. Not a TAM slide. A decision tool that forces you to
pick one segment you can win in 12–18 months and builds the evidence to defend that
choice to your leadership team.

The beachhead is the wedge. Everything else — positioning, GTM strategy, proof points
— follows from getting this right. Getting it wrong means dispersed effort, diluted
messaging, and a pipeline that looks busy but doesn't close.

---

## Trigger

- **When:** ICP is too broad, revenue is scattered across segments with no dominant
  pattern, a new product needs a first target, or a new market requires a wedge before
  full GTM investment.
- **Not for:** Geographic market entry decisions → use a dedicated market assessment
  skill. Full GTM planning after segment is chosen → use `go-to-market-strategy`.
  Persona building within a confirmed segment → use `hs-buyer-personas`. Positioning
  for a chosen segment → use `positioning-messaging`.
- **Example prompts:**
  - "Our ICP is mid-market B2B SaaS — that's too broad. Help me pick a beachhead."
  - "We're closing deals in fintech, healthcare, and logistics. Where do we focus?"
  - "We're launching a new product. Which segment do we go after first?"
  - "Is our current beachhead still the right one? We're 18 months in."
  - "/score fintech vs healthcare vs logistics"

---

## Inputs

- **Args:** Segment candidates — 2–5 named segments or one broad ICP to decompose.
  Free format. If none provided, skill runs intake to identify candidates from brain.
- **Defaults:** If no segments named, decompose the ICP in brain Section 2 into
  2–4 candidate sub-segments before scoring.
- **Context keys:**
  - `/foundation/brain.md` — required. Sections 2, 3, 4, 5.
  - **Brain contract:**
    - Reads: Section 2 (ICP) — current ICP definition as starting point for
      decomposition; Section 3 (Positioning) — existing positioning anchors inform
      which segments the product naturally fits; Section 4 (Competitive landscape)
      — competitor dominance by segment informs Winnability scoring; Section 5
      (Proof points) — existing customer evidence informs Burning Pain validation.
    - Writes: Section 2 — updates ICP with confirmed beachhead segment, scoring
      breakdown, and 90-day expansion pathway on user confirmation.
    - Never writes to: Sections 1, 3, 4, 5, 6, 7.

---

## Pre-flight

- Load `/foundation/brain.md`. Extract Sections 2, 3, 4, 5 silently.
- If brain missing: block and surface:
  > "Brain not found. Run `product-marketing-context` first. Beachhead scoring
  > without your ICP, positioning, and competitive context produces guesswork,
  > not a defensible recommendation."
- If Section 2 (ICP) is empty or 🔴 Placeholder:
  > "⚠️ ICP is empty. I'll ask you to describe your current customer base before
  > scoring. The more specific you are, the sharper the segmentation."
- If Section 5 (Proof points) is empty: note internally. Burning Pain scores will
  rely on user-provided evidence rather than validated claims. Surface this in scoring.
- Gate check: Before scoring begins, at least one of the following must be present
  — named existing customers in a segment, win/loss patterns by segment, or segment
  hypotheses from the user. If none: run intake to establish evidence base first.

---

## Steps

### Step 1: Intake and Candidate Identification

Ask in one message. Never score before candidates are confirmed.

> "Before I score, I need to understand the landscape:
>
> 1. **What segments are you considering?**
>    Name 2–5 candidates. If you're not sure, describe your current customer base
>    and I'll decompose it into scoreable sub-segments.
>
> 2. **What evidence do you have?**
>    Named customers in each segment, win/loss patterns, inbound signals, or sales
>    feedback. Even rough signals help. 'We've closed 3 deals in fintech' is enough
>    to start.
>
> 3. **What does winning look like?**
>    In 12–18 months, what would make this beachhead a success?
>    (Revenue target, reference customers, market share in the segment — be specific)"

If the user names only one segment: challenge before proceeding.
> "One segment isn't a choice — it's an assumption. Name at least two so we have
> something to compare against. What else have you considered and rejected?"

Reflect back candidates and evidence before scoring:
> "Scoring [N] segments: [list]. Evidence base: [summary]. Starting with Burning Pain."

---

### Step 2: Score Each Segment on Four Dimensions

Score each segment independently before comparing. Never rank without scoring.
Scoring is based on evidence in brain + user-provided signals. Where evidence is
absent, mark the score `[A]` (assumption) and flag it.

---

#### Dimension 1: Burning Pain (1–5)

*Does this segment have an acute, urgent problem your product solves — or a chronic
inconvenience they've learned to live with?*

Acute pain = budget unlocks, decisions happen fast, buyers seek you out.
Chronic inconvenience = long sales cycles, "nice to have" objections, slow close.

| Score | Signal |
|---|---|
| 5 | Segment is actively seeking solutions. Inbound, unsolicited outreach, or urgency in sales calls. Budget exists and is approved. |
| 4 | Problem is recognised and prioritised. Buyers have tried alternatives. Willingness to switch present. |
| 3 | Problem acknowledged but not top-3 priority. Competes with other initiatives for budget. |
| 2 | Problem exists but is treated as background noise. No active urgency. |
| 1 | Problem is theoretical. Segment doesn't recognise or articulate it as a problem. |

Evidence required: named customer signal, sales call pattern, win/loss data, or
inbound volume by segment. If none: score 2 maximum, mark `[A]`.

---

#### Dimension 2: Willingness to Pay (1–5)

*Does this segment have budget, authority to spend it, and a clear ROI frame that
justifies your price point?*

| Score | Signal |
|---|---|
| 5 | Segment has dedicated budget line. Buyers have authority. ROI is measurable and fast (< 6 months). Price point is a non-issue in sales conversations. |
| 4 | Budget exists. Occasional price friction but rarely a deal-killer. ROI case is clear if built. |
| 3 | Budget exists but requires internal justification. Multiple approvals. ROI case is soft or long. |
| 2 | Budget is scarce or controlled elsewhere. Price sensitivity high. Deals require significant discounting. |
| 1 | No budget. Segment relies on free tools or has no spend authority for this category. |

Cross-reference brain Section 5 proof points for ROI evidence. If proof points are
missing for a segment, note: "No proof point exists for [segment] ROI — this is an
assumption until validated."

---

#### Dimension 3: Winnability (1–5)

*Can you realistically reach 60%+ market share in this segment within 12–18 months —
or is it owned by an entrenched incumbent you cannot displace?*

| Score | Signal |
|---|---|
| 5 | No dominant incumbent. Competitors are weak, absent, or losing deals to you already. Segment is underserved relative to its size. |
| 4 | One or two incumbents but vulnerable. You have a clear differentiated wedge. Win rate in this segment is already above average. |
| 3 | Incumbent exists and is respected, but not dominant. You can win with strong positioning and sales effort. |
| 2 | Incumbent is entrenched. Switching costs are high. You can win occasionally but can't dominate. |
| 1 | Segment is owned. Switching costs prohibitive, or incumbent is also the buyer's vendor of record on other systems. |

Cross-reference brain Section 4 (Competitive landscape). If Section 4 is stale or
empty for a segment: mark Winnability `[A]` — competitive positions cannot be
inferred from training data. User must provide.

---

#### Dimension 4: Referral Potential (1–5)

*Do customers in this segment talk to each other? Are reference customers in this
segment worth 10x their contract value in network effects?*

This is what separates a beachhead from any other segment. A beachhead compounds.
A random segment does not.

| Score | Signal |
|---|---|
| 5 | Tight community. Buyers attend the same conferences, Slack groups, or peer networks. One reference customer unlocks introductions to 5–10 others. |
| 4 | Moderate network. Buyers know each other but don't actively refer. Case studies and press coverage travel well in this segment. |
| 3 | Some peer exchange. Conference presence helps. Reference customers willing to speak but don't proactively refer. |
| 2 | Fragmented. Buyers are isolated or in competing organisations. References matter but don't travel. |
| 1 | No community. Buyers are competitors with each other or in siloed verticals with no peer exchange. |

---

### Step 3: Produce Scorecard and Apply Blocking Gates

After all four dimensions are scored for each segment, produce the scorecard:

```markdown
## Beachhead Scorecard

| Segment | Burning Pain | Willingness to Pay | Winnability | Referral Potential | Total | Status |
|---|---|---|---|---|---|---|
| [Segment A] | [1–5] | [1–5] | [1–5] | [1–5] | [X/20] | [Qualifies / Blocked / Watch] |
| [Segment B] | [1–5] | [1–5] | [1–5] | [1–5] | [X/20] | [Qualifies / Blocked / Watch] |

**Assumption flags:** [List any scores marked [A] — these require validation before committing]
**Confidence:** 🟢 High / 🟡 Medium / 🔴 Low
```

**Blocking Gates — applied after scoring, before recommendation:**

- **Gate 1 — Pain floor:** Any segment scoring < 3 on Burning Pain is eliminated.
  Size without pain is not a market, it's a theory.
  > "❌ [Segment] eliminated — Burning Pain score of [X] indicates this is a
  > chronic inconvenience, not an acute problem. GTM investment here will be slow."

- **Gate 2 — Winnability floor:** Any segment scoring < 3 on Winnability is flagged
  as "Future Roadmap" — not a current beachhead candidate.
  > "⚠️ [Segment] flagged — Winnability score of [X] means you can win deals here
  > but cannot dominate. File as secondary market. Revisit when competitive position
  > improves."

- **Gate 3 — Assumption density:** If more than 2 of the 4 dimensions are marked
  `[A]` for the top-scoring segment, confidence is capped at 🟡 and the recommendation
  is conditional:
  > "🟡 Conditional recommendation — [N] of 4 dimensions rely on assumptions.
  > Validate [specific assumptions] before committing GTM investment."

---

### Step 4: Recommendation and Expansion Pathway

After gates are applied, state the recommended beachhead with rationale, then map
the expansion pathway.

```markdown
## Recommended Beachhead: [Segment Name]

**Rationale:** [2–3 sentences grounded in the four dimensions. Name the specific
signals that make this the highest-probability first wedge. Do not summarise the
scorecard — add strategic interpretation.]

**Why not [Segment B]:** [One sentence. Specific reason based on scoring.]
**Why not [Segment C]:** [One sentence. Specific reason based on scoring.]

## What Winning Looks Like in 12–18 Months

- [Specific milestone 1 — revenue, customer count, or market share signal]
- [Specific milestone 2 — reference customer or analyst recognition]
- [Specific milestone 3 — expansion trigger: when does the beachhead unlock the next segment?]

## Expansion Pathway

**Beachhead → Adjacent 1:** [Segment name] — [shared buying trigger or adjacent pain]
**Adjacent 1 → Adjacent 2:** [Segment name] — [compounding network or product fit]

This sequence matters. The beachhead is not the end state — it's the proof point
that unlocks the next segment with less effort.

## 90-Day Activation Plan

| Week | Action | Owner | Signal to watch |
|---|---|---|---|
| 1–2 | [Immediate positioning action — ICP sharpening, messaging update] | PMM | — |
| 3–4 | [First outbound or sales enablement step] | Sales/PMM | First meetings booked |
| 5–8 | [Pipeline build — target [N] qualified conversations] | Sales | Win rate in segment |
| 9–12 | [First reference customer — case study or joint PR] | PMM | Inbound from segment |

## Eliminated Segments

| Segment | Eliminated by | Reason |
|---|---|---|
| [Segment X] | Gate 1 — Pain floor | Burning Pain score [X]: no urgency signal |
| [Segment Y] | Gate 2 — Winnability | Incumbent [Name] entrenched — cannot dominate |
```

---

### Step 5: Update Brain Section 2

After recommendation is confirmed by user:

Write to `/foundation/brain.md` Section 2:

```markdown
## Beachhead Segment (last updated: [date])
- **Recommended segment:** [name]
- **Scoring:** Pain [X] / WTP [X] / Winnability [X] / Referral [X] — Total [X/20]
- **Confidence:** 🟢 / 🟡 / 🔴
- **Assumption flags:** [list or none]
- **Expansion pathway:** [Beachhead] → [Adjacent 1] → [Adjacent 2]
- **90-day trigger:** [first milestone that validates the beachhead choice]
- **Status:** Active beachhead
```

Surface before writing:
> "Updating brain Section 2 with [Segment] as confirmed beachhead. Confirm? [Y/N]"

---

## Outputs

- **Files written:** `/foundation/brain.md` Section 2 — beachhead segment entry on
  confirmation.
- **Chat output format:** Scorecard table → blocking gate results → recommendation
  with rationale → expansion pathway → 90-day activation plan → eliminated segments.
  All in markdown, copy-paste ready for Notion or Google Docs.
- **External side effects:** n.v.t.

---

## Verification

- Scorecard shows all four dimensions for every candidate segment.
- Blocking gates applied and results stated explicitly — no segment passes silently.
- Eliminated segments documented with specific reason, not "didn't score well."
- Expansion pathway shows at least two steps beyond the beachhead.
- 90-day plan has specific milestones with owners.
- Assumption flags visible on scorecard wherever `[A]` applied.
- Brain Section 2 write confirmed to user before executing.

---

## Do Not Use For

- **go-to-market-strategy** — once the beachhead is confirmed, use this skill to
  assign a tier and build the full GTM brief for it. `beachhead-segment` identifies
  the target; `go-to-market-strategy` builds the plan to reach it.
- **hs-buyer-personas** — for building buying committee and persona depth within the
  confirmed beachhead. Run after this skill, not instead of it.
- **positioning-messaging** — for developing positioning for the confirmed beachhead.
  This skill identifies the segment; positioning-messaging frames the message for it.
- **workflow-orchestrator** — to chain this skill with the above into a full new-market
  entry or launch program.

---

## Commands

### /score [segment A] vs [segment B] vs [segment C]
Score named segments immediately. Skips candidate identification intake — goes
directly to four-dimension scoring. Use when candidates are already known.

```
/score fintech vs healthcare vs logistics
/score enterprise HR vs mid-market HR vs SMB HR
```

Output: Scorecard table → blocking gates → recommendation.

---

### /decompose
Decompose the current ICP in brain Section 2 into 2–4 scoreable sub-segments.
Use when the ICP is defined but too broad to act on.

```
/decompose
```

Output:
```
ICP in brain: [current ICP definition]

Decomposed into [N] candidate sub-segments:
1. [Sub-segment A] — [one-line rationale for why this is a distinct scoring candidate]
2. [Sub-segment B] — [one-line rationale]
3. [Sub-segment C] — [one-line rationale]

Run /score to evaluate these candidates, or name different ones.
```

---

### /audit
Pressure-test an existing beachhead choice. Use when you're 6–18 months in and
want to validate whether the original beachhead is still the right one — or whether
it's time to expand or pivot.

```
/audit
/audit [segment name]
```

Runs a fresh four-dimension score on the confirmed beachhead using current evidence.
Compares to original scores if available in brain Section 2. Surfaces whether
the expansion trigger has been hit.

Output:
```
## Beachhead Audit — [Segment Name]

Original scores (brain Section 2): [P/W/Wi/R]
Current scores (this session): [P/W/Wi/R]

Change: [Improved / Declined / Stable per dimension]

Expansion trigger status:
→ [Milestone 1]: [Hit / Pending / Missed — evidence]
→ [Milestone 2]: [Hit / Pending / Missed — evidence]

Recommendation:
[Stay — continue building in beachhead]
[Expand — beachhead is proven, move to adjacent segment now]
[Pivot — beachhead is not developing as expected, re-score alternatives]
```

---

### /pathway
Show the full expansion pathway from the confirmed beachhead. Use when
planning the next 2–4 quarters of segment expansion.

```
/pathway
```

Output:
```
## Expansion Pathway from [Beachhead Segment]

Stage 1 — Beachhead (now): [Segment] — [why this is the wedge]
Stage 2 — Adjacent (Q[X]): [Segment] — [shared trigger or proof point needed]
Stage 3 — Scale (Q[X]): [Segment] — [what the beachhead proves that unlocks this]

Trigger to move from Stage 1 → Stage 2: [specific milestone]
Trigger to move from Stage 2 → Stage 3: [specific milestone]

Risk: [What would force a re-score of this pathway]
```

---

### /eliminate [segment name]
Explicitly eliminate a segment from consideration and document the reason.
Useful for keeping a clean decision record when stakeholders push for a segment
that doesn't pass the gates.

```
/eliminate enterprise — too entrenched, we cannot dominate in 12–18 months
```

Output:
```
Segment eliminated: [name]
Reason: [stated reason]
Gate applied: [Pain floor / Winnability floor / Strategic decision]
Logged to brain Section 2 under: Eliminated Segments
```

---

## Operating Rules

- **Both Pain and Winnability must pass.** No segment that scores < 3 on either
  becomes a beachhead recommendation. A large market with no urgency is not a
  beachhead. A high-pain market you cannot dominate is a graveyard.
- **Evidence over assertion.** If a dimension cannot be scored with at least one
  named signal, it is marked `[A]` and confidence is reduced. Assumptions are not
  blocked — they are flagged and tracked.
- **Eliminated segments must be documented.** A beachhead decision is only as
  credible as its eliminations. Never produce a recommendation without showing what
  was rejected and why.
- **Expansion pathway is mandatory.** The beachhead is not the strategy — it is
  the first step. Any recommendation without a clear second and third stage is
  incomplete.
- **Never score one segment in isolation.** Single-segment scoring is not a choice.
  Always require at least two candidates for comparison.
- **Brain Section 2 write requires explicit confirmation.** Never update without
  asking. The beachhead decision affects downstream skills — a silent write can
  corrupt positioning, persona, and GTM work.
- **Challenge generic ICPs before decomposing.** "Mid-market B2B SaaS" is not a
  scoreable segment. Push for vertical, use case, or buyer role specificity before
  running intake.
- **90-day plan must have a specific trigger.** "Build pipeline" is not a milestone.
  Name the number, the behaviour, or the event that validates the beachhead within 90 days.
- **Audit mode is not score mode.** Audit compares against original scores. Score
  starts fresh. Never conflate them — an audit that ignores prior scores is just
  another scoring session with worse context.
- **Referral Potential is the beachhead multiplier.** A segment that scores 4+ on
  Referral Potential with only moderate scores elsewhere is often still the right
  choice. Explicitly surface this trade-off when Referral is the differentiating signal.

---

## Quality Gate

Runs after recommendation is generated, before delivery.

| Check | Standard | Pass = |
|---|---|---|
| Minimum two segments scored | At least 2 candidates evaluated | Yes |
| All four dimensions scored | Every segment has P / WTP / Wi / R scores | Yes |
| Assumption flags visible | All `[A]` marks present on scorecard | Yes |
| Gate 1 applied | Segments scoring < 3 on Pain explicitly eliminated | Yes |
| Gate 2 applied | Segments scoring < 3 on Winnability explicitly flagged | Yes |
| Eliminated segments documented | Every eliminated segment has a specific reason | Yes |
| Expansion pathway present | At least two stages beyond beachhead named | Yes |
| 90-day plan has specific trigger | Milestone is a number, event, or observable behaviour | Yes |
| Confidence level stated | 🟢 / 🟡 / 🔴 with reason if not 🟢 | Yes |
| Brain write confirmed | Section 2 update shown to user before executing | Yes |

---

## Self-Improvement Loop

### Before every session:
1. Load brain Section 2 — check if a beachhead has been previously confirmed.
   If yes: surface it before intake.
   > "Brain shows [Segment] as confirmed beachhead (scored [date]). Run /audit
   > to pressure-test it, or /score to evaluate new candidates."
2. Load brain Section 4 — competitive landscape informs Winnability scoring.
   If stale (> 3 months): flag before scoring Winnability.
3. Check `knowledge/beachhead/rules.md` if it exists — apply confirmed patterns silently.
4. Check `knowledge/beachhead/hypotheses.md` — note any pattern testable today.

### After every session where a recommendation was made:
1. Extract observation about which dimension was most contested or most uncertain.
   Log to `knowledge/beachhead/hypotheses.md`.
2. If the same scoring pattern has appeared 3+ times (e.g. "Referral Potential
   consistently breaks ties between high-scoring segments") → propose promotion to
   `knowledge/beachhead/rules.md`.
3. Log session to `sessions/log.md`: segments scored, recommendation made,
   assumption flags, confidence level, brain write Y/N.

**Self-Improvement Trigger format — surface before encoding, never silently:**

```
🔁 SELF-IMPROVEMENT TRIGGER
Pattern: [what was observed this session]
Proposed update: [exact wording]
Location: [file path]
Awaiting approval before encoding.
```

---

## Changelog

### v1.0.0 — 2026-06-06
Initial build. Third skill in the GTM plugin (`go-to-market-strategy`,
`workflow-orchestrator`, `beachhead-segment`).

Architecture decisions:
- Four-dimension scoring model: Burning Pain, Willingness to Pay, Winnability,
  Referral Potential — each with explicit 1–5 rubric and evidence requirements
- Two hard blocking gates: Pain floor (< 3 eliminates) and Winnability floor
  (< 3 flags as future roadmap)
- Assumption tracking: `[A]` marking on any dimension without named evidence signal
- Expansion pathway mandatory in every recommendation
- 90-day activation plan with named milestones required for output
- Brain contract: reads Sections 2, 3, 4, 5; writes Section 2 on confirmation only
- Commands: /score, /decompose, /audit, /pathway, /eliminate
- Integration chain: beachhead → go-to-market-strategy → workflow-orchestrator
- Referral Potential as the compound multiplier — explicitly surfaced when it
  differentiates candidates with similar aggregate scores
