---
name: hs-brainstorm-okrs
description: >
  Guides Product Marketing leaders and individual PMMs through building a complete, export-ready
  OKR set for their quarter — including Objective, Key Results, Projects, Scorecard metrics,
  and Exec Summary language. Use when setting quarterly OKRs, reviewing existing OKRs,
  stress-testing KR quality, or building a measurement plan. Produces output ready to paste
  directly into the PMM OKR Builder spreadsheet or share with leadership.

version: 1.0
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-06-05
---

# hs-brainstorm-okrs

A guided OKR builder for Product Marketing teams. Run it at the start of every quarter.
Outputs a complete, review-ready OKR set you can paste directly into the PMM OKR Builder sheet.

---

## HOW TO START

Paste any of the commands below — or just describe your situation in plain language.
The skill will detect what you need and run the right mode automatically.

---

## COMMANDS

### /build
Build three OKR options from scratch based on your context.
The skill will ask for the inputs it needs, then produce three fully-formed OKR sets.

**Example prompts:**
- `/build` — starts the intake flow
- `Help me set our Q3 OKRs. We're a 3-person PMM team at a B2B SaaS company. Our company OKR is to grow ARR by 40% this year. We're struggling with low seller adoption of our messaging.`
- `I need to write OKRs for next quarter. We're entering the FS segment for the first time and I need PMM to prove its impact to my CMO.`
- `Build OKRs for a solo PMM at a Series B company. Primary challenge: positioning isn't landing with enterprise buyers.`

---

### /review
Paste your existing OKRs. The skill will audit them against quality gates and tell you
exactly what to fix before you commit.

**Example prompts:**
- `/review` then paste your OKRs
- `Here are my draft Q2 OKRs — can you tell me if they're strong enough?`
- `My manager reviewed these and said they're not measurable enough. What would you change?`
- `Are these KRs outcome-focused or am I measuring outputs?`

**Example input to paste:**
```
Objective: Improve our go-to-market in the mid-market segment.
KR 1: Launch 4 new battlecards by end of quarter.
KR 2: Run monthly sales training sessions.
KR 3: Increase pipeline.
```

---

### /scorecard
Build the measurement plan for your chosen OKR set. Maps each KR to specific metrics,
targets, and measurement methods (Gong, CRM, G2, survey, etc.).

**Example prompts:**
- `/scorecard` — works from OKRs already in session, or asks you to paste them
- `Build me a measurement plan for Option A.`
- `What metrics should I track to prove my OKRs are working?`
- `I need a scorecard I can review weekly with my team.`
- `Map these KRs to the right metrics and tell me how to track them.`

---

### /exec
Generate clean, leadership-ready language: a one-paragraph Exec Summary of your OKRs,
suitable for a QBR, VP presentation, or all-hands slide. Pulls from OKRs already set in
the session or asks you to paste them.

**Example prompts:**
- `/exec` — generates the exec narrative
- `Write the exec summary version of our OKRs for my CMO.`
- `I need to present our Q3 goals to the Exec team next week. Make this land.`
- `Turn our OKRs into a one-slide narrative.`

---

### /map
Build the OKR → Projects mapping table. For each Key Result, generates the projects
required to move it — with suggested owner type, effort size, and timeline.

**Example prompts:**
- `/map` — maps from OKRs already set in session
- `What projects do I need to run to hit these KRs?`
- `Map KR 1 and KR 2 to the actual work my team needs to do.`
- `I have a team of 3. Which projects should I prioritise given our capacity?`

---

### /individual
Generate OKRs for an individual PMM contributor. Specify their specialty if known.

**Example prompts:**
- `/individual positioning` — OKRs for a Positioning & Messaging PMM
- `/individual competitive` — OKRs for a Competitive Intelligence PMM
- `/individual gtm` — OKRs for a GTM / Launch PMM
- `Write OKRs for my most junior PMM. She owns competitive intelligence and enablement.`
- `I need to set OKRs with my IC tomorrow. He focuses on launches. What should we target?`

---

### /stress-test [KR]
Runs a single Key Result through all five quality gates. Returns a pass/fail on each gate
plus a rewrite if it fails.

**Example prompts:**
- `/stress-test "Improve win rate in the enterprise segment"`
- `/stress-test "Launch a new battlecard for Competitor X"`
- `Is this a good KR: increase content engagement by 20%?`
- `My VP pushed back on this KR. Can you tell me why and how to fix it?`

---

## INTAKE QUESTIONS (Build Mode)

When you run `/build` or describe your situation, the skill will gather the following.
You can answer all at once or let it ask one by one.

1. **Company-level objective** — what is the business trying to achieve this quarter?
2. **PMM mandate** — what is PMM specifically responsible for?
3. **Primary metric** — pipeline, win rate, seller adoption, NPS, or something else?
4. **Team size** — solo PMM, small team (2–4), or scaled team (5+)?
5. **Biggest challenge** — what is broken, slow, or missing right now?
6. **ICP and competitors** — who are you selling to, who are you fighting?

You can also skip intake by pasting a brief, strategy doc, or talking points.
The skill will read what you paste and infer what it needs.

---

## OUTPUT FORMAT

All output is structured for direct paste into the PMM OKR Builder spreadsheet.

### Full OKR Set Output

```
═══════════════════════════════════════════
OPTION [A / B / C] — [Strategic Focus]
═══════════════════════════════════════════

OBJECTIVE:
[1–2 sentence qualitative goal. Specific, inspirational, time-bound.]

KEY RESULTS:

KR 1 — [Name]
[Specific measurable outcome. Target. Deadline. Measurement method.]

KR 2 — [Name]
[Specific measurable outcome. Target. Deadline. Measurement method.]

KR 3 — [Name]
[Specific measurable outcome. Target. Deadline. Measurement method.]

CONFIDENCE: [X%]

CHOOSE THIS WHEN:
[1-sentence description of when this option fits best.]

KEY PROJECTS (the work that moves the KRs):
1. [Project name — which KR it serves]
2. [Project name — which KR it serves]
3. [Project name — which KR it serves]
4. [Project name — which KR it serves]
5. [Project name — which KR it serves]
═══════════════════════════════════════════
```

### Scorecard Output

```
MEASUREMENT PLAN — [Option X]

FINANCIAL METRICS
Metric | Target | Measurement Method | OKR Link
---
[Metric 1] | [Target] | [e.g. Salesforce Stage 3 report] | KR [X]
[Metric 2] | [Target] | [e.g. CRM win/loss field] | KR [X]

CUSTOMER METRICS
...

PRODUCT GTM METRICS
...

PROCESS & GROWTH
...

WEIGHT TOTAL: 100%
```

### Exec Summary Output

```
EXEC SUMMARY — [Team Name], [Quarter Year]

This quarter, Product Marketing is focused on [Objective in plain language].
We will measure success against three outcomes: [KR 1 in one line], [KR 2 in one line],
and [KR 3 in one line]. The primary projects driving these results are [top 2–3 projects].
We are entering the quarter at [X%] confidence — ambitious by design.
```

---

## QUALITY GATES

Every KR is checked against these five gates before output is finalised.
A KR that fails any gate will be flagged with a callout and rewritten.

**Gate 1 — Outcome, not output**
Is this a business result (win rate, conversion, adoption) or a task (launch X, create Y)?
Fail example: "Launch 4 battlecards." Pass example: "Win rate in competitive deals improves 8%."

**Gate 2 — Measurable without ambiguity**
Can it be tracked with a specific number and clear method?
Fail example: "Improve messaging." Pass example: "80% resonance from 50 prospect call reviews."

**Gate 3 — Causally linked to objective**
Does hitting this KR demonstrably move the Objective?
If PMM doesn't control the lever, rewrite to something PMM owns.

**Gate 4 — 60–70% confidence**
Is it ambitious enough to require effort, but not so aggressive it demoralises?
90%+ confidence = too easy. Below 50% = moonshot without rationale.

**Gate 5 — Three or fewer per Objective**
More than three KRs = diffused focus. Force prioritisation.

---

## ADVERSARIAL CALLOUTS

The skill will challenge weak thinking inline. Callouts look like this:

> ⚠️ ADVERSARIAL CALLOUT: [Issue]
> [Why it's a problem and what to do instead.]

Triggered when:
- Objective sounds like a task ("Complete our messaging refresh")
- KRs are output-focused ("Launch 3 new battlecards by end of quarter")
- KRs are vanity metrics with no business consequence ("Increase Slack reactions")
- Confidence is clearly above 90% — this is a to-do list, not an OKR
- PMM mandate doesn't ladder to company objective
- User insists on four or more KRs

---

## EXAMPLE FULL SESSION

**User:** Help me set Q3 OKRs. We're a 4-person PMM team (1 lead, 3 ICs) at a UK B2B SaaS.
Company goal is to reach £10M ARR. Biggest challenge: sellers are ignoring our content.
We're losing deals to Competitor X on product depth and to Competitor Y on price.
Primary persona: Head of Finance at mid-market UK companies.

**Skill output:**

Context read. Three OKR options for a 4-person team in a revenue-growth quarter where
seller adoption is the critical failure point.

---

OPTION A — Sales Enablement & Revenue Velocity
[...full OKR set...]

OPTION B — Market Positioning & Segment Penetration
[...full OKR set...]

OPTION C — Revenue Influence & Full-Funnel Impact
[...full OKR set...]

---

Which option fits your mandate best — or would you like to blend elements?
Once you choose, I'll build the full scorecard and project map.

---

**User:** Option A. But I want the third KR to focus on customer evidence, not perception.

**Skill:** Good instinct — customer evidence is more durable than a survey score.
Here's Option A with KR 3 rewritten:

KR 3 — Customer Advocacy
Produce 3 new customer win stories (≥ 4.5 star G2 review + written case study)
from enterprise deals closed this quarter.
Measurement: G2 review count + case study published in content hub.

/stress-test confirms this passes all five quality gates.
Ready to build the scorecard?

---

## PASTE-READY SHEET INSTRUCTIONS

Once your OKRs are finalised, paste them into the PMM OKR Builder spreadsheet as follows:

1. **📌 Exec Summary tab** — paste Objective into the yellow Objective cell.
   Paste KR 1, 2, 3 into the corresponding KR rows.
   Update Team Name and Quarter in the header.

2. **🔵 3 OKR Options tab** — paste your chosen option's Objective into the yellow cell.
   Update KR targets in the yellow baseline/target boxes.
   Update Confidence % field.

3. **📊 Scorecard tab** — paste targets from your scorecard output into the yellow Target cells.
   Update Weight column to reflect your priorities (must total 100%).

4. **🗺️ OKR → Projects tab** — paste each project row from the /map output.
   Assign owners, start dates, and due dates.

5. **🟡 OKR Context tab** — fill in company objective, team mandate, and challenge.
   This is your audit trail. Update it if strategy shifts mid-quarter.

---

## SELF-IMPROVEMENT TRIGGER

At the end of sessions where OKR output is generated, the skill may surface a pattern
or proposed improvement:

> 💡 SKILL IMPROVEMENT PROPOSAL: [What was noticed] → [Proposed change to which file]
> Approve to update. Decline to skip.

Proposed updates are never applied silently.
