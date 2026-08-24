---
name: beachhead-segment
version: 2.2.0
description: >
  Identifies and scores your highest-priority beachhead segment using four-dimension scoring (Burning Pain, Willingness to Pay, Winnability, Referral Potential) with blocking gates. Reads brain context (ICP, positioning, competitive landscape, proof points) and, when available, guardrails from prior beachhead decisions the user has logged. Writes confirmed beachhead to brain Section 2, on explicit confirmation.
---

# Beachhead-Segment — Skill

## How This Works

Identifies the highest-probability segment to dominate first — before expanding. This is the wedge. Everything else (positioning, GTM strategy, proof points) follows from getting this right.

The skill runs in 7 steps:

**Step 0** — Load brain context (ICP, positioning, competitive landscape, proof points) and, if the user maintains `/context/meta-patterns.md`, guardrails logged there.

**Step 1** — Identify candidates: Name 2–5 segments or ask user to decompose current ICP.

**Step 2** — Score each segment on four dimensions: Burning Pain, Willingness to Pay, Winnability, Referral Potential.

**Step 3** — Apply blocking gates: Pain floor (≥3), Winnability floor (≥3), assumption density check.

**Step 4** — Recommend beachhead with expansion pathway and 90-day activation plan.

**Step 5** — Pressure-test eliminated segments with specific reasons.

**Step 6** — Update brain Section 2 with confirmed beachhead (on user confirmation).

**Step 7** — Learning Close: log the session to `/context/skill-sessions.md`.

---

## Step 0 — Pre-Flight: Load Context & Surface Guardrails

Before intake, load:
- **Brain context** (Sections 2, 3, 4, 5): ICP, positioning, competitive landscape, proof points — these anchor all four-dimension scoring
- **Guardrails** from `/context/meta-patterns.md`, if that file exists in the user's workspace: if a pattern has actually fired 2+ times in prior beachhead decisions logged there, surface it now

**Surface guardrails like this:**

````
🔁 PATTERN FROM PRIOR BEACHHEAD DECISIONS

I've seen [pattern description] in 2 prior sessions.
Examples: [specific segments or outcomes]

Quick check: Does this apply to your candidates?
- If YES → We'll watch for this during scoring
- If NO → Let's flag it if it emerges
````

You can skip a guardrail if you disagree, but you'll see it first. If `/context/meta-patterns.md` doesn't exist, skip this step silently.

**Gate check — block if brain is missing:**
If `/foundation/brain.md` is absent or Section 2 (ICP) is empty, block and surface:
> "Brain not found. Run `product-marketing-context` first. Beachhead scoring without ICP, positioning, and competitive context produces guesswork, not defensible recommendation."

---

## Step 1 — Candidate Identification

Ask in one message. Never score before candidates are confirmed.

> "Before I score, I need to understand the landscape:
>
> 1. **What segments are you considering?**
>    Name 2–5 candidates. If not sure, describe your current customer base and I'll decompose it.
>
> 2. **What evidence do you have?**
>    Named customers in each segment, win/loss patterns, inbound signals, sales feedback. Rough signals help.
>
> 3. **What does winning look like in 12–18 months?**
>    Revenue target, reference customers, market share — be specific."

If the user names only one segment: challenge before proceeding.
> "One segment isn't a choice — it's an assumption. Name at least two so we have something to compare. What else have you considered and rejected?"

Reflect back candidates and evidence:
> "Scoring [N] segments: [list]. Evidence base: [summary]. Starting with Burning Pain."

---

## Step 2 — Score Each Segment on Four Dimensions

Score each independently before comparing. Mark any dimension without evidence as `[A]` (assumption).

### Dimension 1: Burning Pain (1–5)

*Acute, urgent problem your product solves — or chronic inconvenience they've learned to live with?*

| Score | Signal |
|---|---|
| 5 | Segment actively seeking solutions. Budget exists. Buyers seek you out. |
| 4 | Problem recognised and prioritised. Buyers have tried alternatives. |
| 3 | Problem acknowledged but not top-3 priority. Competes for budget. |
| 2 | Problem exists but background noise. No active urgency. |
| 1 | Problem is theoretical. Segment doesn't recognise it. |

Evidence required: named customer signal, sales call pattern, win/loss data, or inbound volume. If none: score ≤2, mark `[A]`.

### Dimension 2: Willingness to Pay (1–5)

*Does this segment have budget, authority, and clear ROI justifying your price?*

| Score | Signal |
|---|---|
| 5 | Dedicated budget line. Buyers have authority. ROI measurable and fast (<6 months). |
| 4 | Budget exists. Occasional price friction but rarely deal-killer. ROI case clear. |
| 3 | Budget exists but requires justification. Multiple approvals. ROI case soft or long. |
| 2 | Budget scarce or controlled elsewhere. Price sensitivity high. Discounting required. |
| 1 | No budget. Segment relies on free tools. |

Cross-reference brain Section 5 proof points for ROI evidence. If missing: mark `[A]`.

### Dimension 3: Winnability (1–5)

*Can you realistically reach 60%+ market share in this segment within 12–18 months?*

| Score | Signal |
|---|---|
| 5 | No dominant incumbent. Competitors weak or absent. Segment underserved. |
| 4 | One or two incumbents but vulnerable. Clear differentiated wedge. Win rate above average. |
| 3 | Incumbent exists but not dominant. Can win with strong positioning and sales effort. |
| 2 | Incumbent entrenched. Switching costs high. Can win occasionally, can't dominate. |
| 1 | Segment owned. Switching costs prohibitive. |

Cross-reference brain Section 4 (Competitive landscape). If stale or empty: mark `[A]` — competitive positions cannot be inferred.

### Dimension 4: Referral Potential (1–5)

*Do customers in this segment talk to each other? Is one reference customer worth 10x their contract value in network effects?*

This is what separates a beachhead from any other segment.

| Score | Signal |
|---|---|
| 5 | Tight community. Buyers attend same conferences/networks. One reference unlocks 5–10 others. |
| 4 | Moderate network. Buyers know each other. Case studies travel well. |
| 3 | Some peer exchange. Conferences help. References willing to speak. |
| 2 | Fragmented. Buyers isolated or competing. References matter but don't travel. |
| 1 | No community. Buyers compete with each other. |

---

## Step 3 — Apply Blocking Gates

**Gate 1 — Pain floor (≥3):** Any segment scoring <3 on Burning Pain is eliminated.
> "❌ [Segment] eliminated — Burning Pain [X]. No urgency signal. GTM investment will be slow."

**Gate 2 — Winnability floor (≥3):** Any segment scoring <3 on Winnability is flagged as "Future Roadmap" — not current beachhead.
> "⚠️ [Segment] flagged — Winnability [X]. You can win deals but cannot dominate. File as secondary. Revisit when competitive position improves."

**Gate 3 — Assumption density:** If >2 of 4 dimensions are marked `[A]` for top-scoring segment, confidence caps at 🟡.
> "🟡 Conditional — [N] dimensions rely on assumptions. Validate [specific items] before committing."

---

## Step 4 — Recommend Beachhead

After gates pass, state recommendation with rationale and expansion pathway.

````markdown
## Recommended Beachhead: [Segment Name]
**Rationale:** [2–3 sentences grounded in four dimensions]
**Why not [Segment B]:** [One sentence specific reason]
**Why not [Segment C]:** [One sentence specific reason]

## What Winning Looks Like in 12–18 Months
- [Specific milestone 1 — revenue, customer count, or market share]
- [Specific milestone 2 — reference customer or analyst recognition]
- [Specific milestone 3 — expansion trigger]

## Expansion Pathway
**Beachhead → Adjacent 1:** [Segment] — [shared trigger or proof point needed]
**Adjacent 1 → Adjacent 2:** [Segment] — [what beachhead proves that unlocks this]

Trigger to move Beachhead → Adjacent 1: [specific milestone]
Trigger to move Adjacent 1 → Adjacent 2: [specific milestone]

## 90-Day Activation Plan
| Week | Action | Owner | Signal to watch |
|---|---|---|---|
| 1–2 | [Positioning action] | PMM | — |
| 3–4 | [First outbound step] | Sales/PMM | Meetings booked |
| 5–8 | [Pipeline build — target N qualified conversations] | Sales | Win rate |
| 9–12 | [First reference customer] | PMM | Inbound from segment |

## Eliminated Segments
| Segment | Gate | Reason |
|---|---|---|
| [X] | Pain floor | Burning Pain [score]: no urgency |
| [Y] | Winnability | Incumbent [name] entrenched |
````

---

## Step 5 — Update Brain Section 2 (on Confirmation)

After recommendation confirmed:
> "Updating brain Section 2 with [Segment] as confirmed beachhead. Confirm? [Y/N]"

Write to `/foundation/brain.md` Section 2:
````markdown
## Beachhead Segment (last updated: [date])
- **Segment:** [name]
- **Scores:** Pain [X] / WTP [X] / Winnability [X] / Referral [X] — Total [X/20]
- **Confidence:** 🟢 / 🟡 / 🔴
- **Assumption flags:** [list or none]
- **Expansion pathway:** [Beachhead] → [Adjacent 1] → [Adjacent 2]
- **90-day trigger:** [first milestone]
- **Status:** Active beachhead
````

Never write without this explicit confirmation.

---

## Step 6 — Learning Close

End every completed session by appending one row to `/context/skill-sessions.md`
(create the file with a header row if it doesn't exist yet):

````yaml
skill: beachhead-segment
session_date: [YYYY-MM-DD]
pattern: [one falsifiable statement about what happened this session, or "none"]
source: [surprised / wrong / missing / n.v.t.]
````

Write this row directly — do not ask the user for permission. This is a
separate, mechanical log entry from the brain Section 2 write above, which
still requires the user's explicit confirmation. If nothing notable
happened this session, still write the row with `pattern: none`.

---

## Commands

### /score [segment A] vs [segment B] vs [segment C]
Score named segments immediately. Skips intake.
````
/score fintech vs healthcare vs logistics
````
Output: Scorecard → gates → recommendation.

### /decompose
Decompose current ICP into 2–4 scoreable sub-segments.
````
/decompose
````

### /audit [segment name]
Pressure-test existing beachhead. Compares original vs. current scores. Surfaces expansion trigger status.
````
/audit
````

### /pathway
Show full expansion pathway from confirmed beachhead.
````
/pathway
````

### /eliminate [segment name]
Explicitly eliminate a segment. Documents reason.
````
/eliminate enterprise — too entrenched
````

---

## Operating Rules

- **Both Pain and Winnability must pass.** No <3 on either becomes beachhead.
- **Evidence over assertion.** Dimension without signal = marked `[A]` and confidence reduced.
- **Eliminated segments documented.** Every elimination has specific reason, not "didn't score well."
- **Expansion pathway mandatory.** Beachhead is first step. Recommendation without clear stage 2 and 3 is incomplete.
- **Never score one segment in isolation.** Always require ≥2 candidates for comparison.
- **Brain Section 2 write requires explicit confirmation.** Never update silently.
- **Challenge generic ICPs.** "Mid-market B2B SaaS" is not scoreable. Require vertical, use case, or buyer role specificity.
- **90-day plan must have specific trigger.** Name the number, behaviour, or event. "Build pipeline" is not a milestone.
- **Referral Potential is the beachhead multiplier.** Segment with 4+ Referral but moderate others is often still the right choice. Explicitly surface this trade-off.

---

## Quality Gate

| Check | Pass = |
|---|---|
| Minimum 2 segments scored | Yes |
| All 4 dimensions scored | Yes |
| Assumption flags visible | All `[A]` marks present |
| Gate 1 applied | Segments <3 Pain eliminated |
| Gate 2 applied | Segments <3 Winnability flagged |
| Eliminated segments documented | Specific reason per segment |
| Expansion pathway present | ≥2 stages beyond beachhead |
| 90-day plan has specific trigger | Measurable milestone |
| Confidence level stated | 🟢 / 🟡 / 🔴 with reason |
| Brain write confirmed | Section 2 update shown to user |
| Learning Close ran | `/context/skill-sessions.md` has a new row for this session |

**Note (2026-08-22):** This skill is missing `## Trigger`, `## Inputs`,
`## Outputs`, and `## Verification` — required sections per `SKILL-SPEC.md`
Section 4. It's also missing from the Section 12 tier table entirely
despite meeting every T1/T2 structural requirement (brain write, 9
Operating Rules, 10-row Quality Gate) — both gaps flagged here; the tier
table is fixed in this same batch, the missing sections are not.

---

## Do Not Use For

- **go-to-market-strategy** — after beachhead confirmed, use this to build full GTM brief
- **positioning-messaging** — for messaging for confirmed beachhead (run after)
- **workflow-orchestrator** — to chain this with above for full market entry program
