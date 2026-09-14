---
name: pmm-metrics
version: 1.0.0
description: >
  Defines a North Star Metric and 3-5 Input Metrics, then builds a
  capped 8-16 metric scorecard across Financial, Customer, Product &
  GTM, and Process & Growth. Classifies the business game (Attention,
  Transaction, Productivity), scores the NSM against 7 criteria, and
  flags vanity and unowned metrics before delivery. Reads brain ICP and
  beachhead context when available. Trigger on: "what should we
  measure", "North Star metric", "build a PMM scorecard", "what metrics
  should I track", "define our key metrics", "set up a metrics
  framework".
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-09-14
---

# PMM Metrics

## How This Works

Picks one North Star Metric that predicts customer value and revenue,
names the 3-5 Input Metrics that move it, then rounds out a scorecard
across four categories (Financial, Customer, Product & GTM, Process &
Growth), capped at 2-4 metrics per category — 8-16 total, small enough
that a team actually updates it every 1-2 weeks instead of abandoning it
by Q2.

Every target and current value comes from the user — this skill doesn't
invent numbers. If brain Section 2 (ICP/Beachhead) is loaded, it uses
that to check whether a metric is a real leading indicator for the
confirmed segment or just generic. Output is chat-only, disposable —
the brain has no Metrics section to write to (all 6 existing sections
are claimed), same treatment `experiment-ideas` (pmm-growth) gives its
output.

**Step 0** — Load brain Sections 1 (Product), 2 (ICP/Beachhead) if
present, and guardrails from `/context/meta-patterns.md`.

**Step 1** — Classify the business game: Attention, Transaction, or
Productivity.

**Step 2** — Define the North Star Metric and validate it against 7
criteria.

**Step 3** — Define 3-5 Input Metrics that most directly move the North
Star.

**Step 4** — Build the supporting scorecard: 2-4 metrics per category
across Financial, Customer, Product & GTM, and Process & Growth, each
with a target, weight, and cadence.

**Step 5** — Self-check the full set against sprawl and vanity-metric
traps.

**Step 6** — Deliver the scorecard as a markdown table the user saves
themselves — this skill has no durable output file of its own.

**Step 7** — Learning Close: log the session to `/context/skill-sessions.md`.

---

## Trigger

- **When:** Choosing a North Star Metric, building a measurement
  framework from scratch, auditing an existing metrics list that's
  sprawled past what anyone tracks, or preparing a scorecard for
  leadership/exec reporting.
- **Not for:** Quarterly OKRs once metrics exist → `pmm-okrs`
  (pmm-execution) expresses target *change* in metrics this skill
  defines; run this skill first if no North Star exists yet. Launch tier
  assignment → `go-to-market-strategy`. Pressure-testing one
  experiment's hypothesis → `experiment-doc` (pmm-execution) — feed it
  this skill's metric as the guardrail, don't invent a new one.
  Post-launch metrics review → `retro` (pmm-execution) looks backward at
  what this skill's scorecard already tracks.
- **Example prompts:**
  - "What should we be measuring?"
  - "Help me define our North Star metric"
  - "Build a PMM scorecard for leadership"
  - "What metrics should Product Marketing track?"
  - "Our metrics list has 25 things on it and nobody updates it"
  - "Set up a measurement framework for Q1"

---

## Inputs

- **Args:** Business model description (how revenue is made, what
  customers do in-product), current metrics being tracked (if any),
  reporting cadence and audience (team-level vs. exec-level).
- **Defaults:** No brain and no business context given → ask directly
  (Step 1). Brain exists → load Section 1/2 silently, ask only for what
  isn't already on file.
- **Context keys:**
  - `/foundation/brain.md` — optional. Section 1 (Product) informs
    business-game classification; Section 2 (ICP/Beachhead) informs
    which Customer and Product & GTM metrics are actual leading
    indicators for the confirmed segment vs. generic.
  - `/context/meta-patterns.md` — optional; guardrails from prior
    metrics sessions.
  - **Brain contract:** Reads Sections 1, 2. Writes nothing — the brain's
    6 sections are all claimed; adding a Metrics section is a
    `product-marketing-context` schema change, out of scope here.
    Scorecard is chat-only output, same as `experiment-ideas`.

---

## Pre-flight

- Load `/foundation/brain.md` Sections 1, 2 if it exists — silently.
- Load `/context/meta-patterns.md` if it exists, and surface any
  guardrail that has fired 2+ times in prior metrics sessions.
- If no brain found: surface once, non-blocking — "No brain found. I'll
  ask directly about your business model and customer segment instead.
  Metrics will be less sharply targeted without ICP/beachhead context —
  run `product-marketing-context` first for a tighter fit, or continue
  now."
- **No hard block.** This skill runs entirely from user-stated business
  context; brain absence degrades precision, not capability.

---

## Steps

### Step 1 — Classify the Business Game

Ask, or infer from brain Section 1 if loaded:

> "How do customers primarily get value from your product — by spending
> time in it, by transacting through it, or by getting something done
> more efficiently with it?"

Classify into exactly one:

| Game | Core question | Examples |
|---|---|---|
| **Attention** | How much time do customers spend using the product? | Content platforms, social tools, media |
| **Transaction** | How many transactions occur between customers and the platform? | Marketplaces, payment platforms, e-commerce infra |
| **Productivity** | How efficiently can someone complete their work or achieve their goal? | Most B2B SaaS — collaboration, workflow, ops tools |

State the classification with one sentence of rationale — never assume
silently. Most B2B SaaS lands in Productivity; treat that as a
hypothesis to confirm, not a default to skip past.

---

### Step 2 — Define the North Star Metric

A North Star Metric (NSM) is **not** multiple metrics, a revenue/LTV
number, an OKR, or a strategy. It **is** a single, customer-centric KPI
reflecting the value customers get from the product — a leading
indicator of long-term business success.

Propose one candidate matched to Step 1's business game, then validate
it against all seven criteria before confirming:

1. **Easy to Understand** — clear enough that everyone in the org
   comprehends it without a footnote.
2. **Customer-Centric** — reflects value delivered to customers, not
   just revenue or internal activity.
3. **Sustainable Value** — indicates habits and long-term engagement,
   not a one-time spike.
4. **Vision Alignment** — represents meaningful progress toward the
   company's stated vision or mission.
5. **Quantitative** — measurable with clear, numeric tracking.
6. **Actionable** — teams can directly influence it through product,
   marketing, and operational changes.
7. **Leading Indicator** — predicts future business success and revenue
   growth, rather than lagging behind it.

**Score each criterion Pass/Fail with one line of evidence.** 2+ fails →
reject and propose an alternative, never deliver a failing NSM with
caveats. Revenue and ARR usually fail #2 (Customer-Centric); NPS often
fails #7 (Leading Indicator) without a longitudinal retention/expansion
link. Name the specific failure — not a generic "that's not
customer-centric."

---

### Step 3 — Define Input Metrics

Define 3-5 Input Metrics — leading indicators that most directly move
the North Star. Each must:

- Move more easily, short-term, than the NSM itself
- Have a stated causal link to the NSM, not just topical proximity
- Point to where optimization effort should concentrate

For each: **Metric**, **Why it drives the NSM** (causal, one sentence),
**Who owns moving it** (PMM, Product, Sales, CS).

If brain Section 2 (ICP/Beachhead) is loaded, check each against the
confirmed segment — generic enough to apply to any customer? Flag it
`[GENERIC — not segment-specific]` rather than including it silently.

---

### Step 4 — Build the Supporting Scorecard

Select **2-4 metrics per category, 8-16 total** — past that, the
scorecard stops getting updated by Q2. Reference list below, not a
requirement to use all of it:

**Financial**
ARR/Revenue/Bookings · Qualified pipeline ($ and count, by stage) ·
Pipeline sourced from PMM-influenced campaigns · Win rate · Average deal
size · Time to close · Expansion revenue (upsell/cross-sell share) ·
Product-level revenue · Market penetration in target segment

**Customer**
NPS / CSAT · New customer reviews (count + score, e.g. G2/Capterra) ·
Customer advocacy (case studies, reference customers) · Engagement in
sales/customer calls · DAU/MAU (post-launch or feature-specific)

**Product & GTM**
Messaging & positioning effectiveness (win/loss feedback, message
testing) · Sales enablement efficacy (% of calls using PMM content) ·
Content & thought leadership engagement · Competitive edge (battlecard
usage, win rate vs. named competitor) · Market leadership (analyst
recognition) · Feature/product adoption rate · New use case discovery

**Process & Growth**
GTM planning and MRD/PRD creation velocity · Feedback loop efficiency
with GTM team · Asset utilization (content actually used vs. produced) ·
Funnel conversion rate at each stage (MQL→SQL, SQL→Opp, Opp→Closed) ·
Pricing & packaging effectiveness

For each metric: **Name**, plain-language **Definition**, **Target**,
**Weight** (sums to 100% across the full scorecard, not per category),
**Cadence** (default biweekly).

Present as a table, grouped by category, with a subtotal weight shown
per category.

---

### Step 5 — Self-Check Against Sprawl and Vanity Metrics

Before delivering, check the full set:

- **≤16 total metrics.** Over that, cut — ask which 2 matter least,
  don't just append.
- **Every metric has a named owner.** No owner, no metric.
- **No duplicate metrics worded differently** (e.g. "content engagement"
  vs. "thought leadership engagement") — merge or cut.
- **Every category has ≥1 metric** — zero means Step 4 was skipped for
  it; flag and revisit.
- **Weights sum to exactly 100%.**
- Flag anything trackable but not actionable by a named function —
  `[VANITY — no owner can move this]`.

---

### Step 6 — Deliver the Scorecard

Present the finished set — NSM, Input Metrics, and categorized
scorecard table — as the session's final chat output. State plainly
that this is disposable: "Copy this into your tracker of choice (the
[Product Marketing Scorecard template](https://deep-visage-02d.notion.site/Product-Marketing-Scorecard-26df5957c92880f6b1d8c7b15d1e8c6f)
works well for ongoing tracking) — this skill doesn't save it for you."

---

### Step 7 — Learning Close

End every completed session by appending one entry to
`/context/skill-sessions.md`, in the format defined in
`product-marketing-context/.claude-plugin/skill-sessions-format.md`
(Type A — execution session):

```yaml
type: execution
skill: pmm-metrics
session_date: [YYYY-MM-DD]
pattern: [one falsifiable statement about what happened this session, or "none"]
source: [surprised / wrong / missing / n.v.t.]
```

Write this row directly — do not ask the user for permission. This is
the only durable write this skill makes — see Step 6: the scorecard
itself is chat-only, disposable output. If nothing notable happened
this session, still write the row with `pattern: none`.

---

## Outputs

- **Files written:** `/context/skill-sessions.md` — one row per session
  (Step 7). Nothing else — see Step 6.
- **Chat output format:** Business game → NSM with 7-criteria scoring →
  Input Metrics with causal rationale and owners → categorized scorecard
  table → self-check results.
- **External side effects:** n.v.t.
- **Next skill:** After delivery, check
  `product-marketing-context/.claude-plugin/next-skill-map.md` for
  "After pmm-metrics" and surface it as a question — never auto-run.

---

## Verification

- Business game classified with rationale, not assumed.
- NSM scored against all 7 criteria individually, not aggregated.
- 3-5 Input Metrics, each with causal link and named owner.
- Scorecard: 8-16 metrics across all 4 categories, each with target,
  weight, cadence.
- Weights sum to exactly 100%.
- Sprawl/vanity self-check run and shown.
- Scorecard delivered with the explicit "not saved for you" note (Step 6).
- Session logged (Step 7).

---

## Commands

### /classify
Run Step 1 only — classify the business game and stop. Useful when the
user wants the framework concept without building a full scorecard yet.
```
/classify
```

### /north-star
Run Steps 1-3 only — business game, NSM, and Input Metrics. Skips the
broader scorecard.
```
/north-star
```

### /scorecard
Run Step 4 only, assuming NSM and Input Metrics are already defined
(stated inline in this session). Builds the supporting scorecard
directly.
```
/scorecard
```

### /audit
Pressure-test an existing metrics list the user provides — apply Step 5
sprawl/vanity self-check against it directly, without redefining the NSM.
```
/audit
```

---

## Operating Rules

- **NSM is singular.** Never present more than one as interchangeable
  options — pick one, name why the runner-up lost.
- **Revenue-shaped metrics fail customer-centric by default.** Challenge
  any NSM that's really a revenue or company-health metric in disguise.
- **Every metric needs a named owner.** Unowned is a chart, not a
  management tool.
- **Cap the scorecard at 16.** Cut before adding.
- **Weights sum to 100%, shown explicitly.** Never leave weighting as an
  exercise for the user.
- **State output is disposable.** No brain section to write to — never
  imply otherwise.
- **Business game is stated, never assumed** — even the obvious cases.
- **Flag generic and vanity metrics visibly** — never quietly drop or
  quietly include them.

---

## Quality Gate

| Check | Standard | Pass = |
|---|---|---|
| Business game classified | Explicit classification + rationale stated | Yes |
| NSM scored on all 7 criteria | Each criterion Pass/Fail with evidence, not aggregate | Yes |
| NSM is singular and customer-centric | One metric, not revenue-shaped | Yes |
| Input Metrics count | 3-5, each with causal rationale and owner | Yes |
| Scorecard size | 8-16 total metrics across 4 categories | Yes |
| Every category populated | ≥1 metric per category or explicit flag if skipped | Yes |
| Weights sum to 100% | Shown explicitly in output | Yes |
| Sprawl/vanity self-check ran | Results shown, not silently passed | Yes |
| Disposable-output note shown | User told explicitly this isn't saved for them | Yes |
| Learning Close ran | `/context/skill-sessions.md` has a new row for this session | Yes |

---

## Do Not Use For

- **pmm-okrs** (pmm-execution) — quarterly OKRs once metrics exist; this
  skill defines *what* to measure, not the quarter's target change.
- **go-to-market-strategy** — launch tier and channel strategy; feed it
  this skill's metrics as success-metric inputs, don't substitute.
- **experiment-doc** (pmm-execution) — pressure-testing one hypothesis;
  its guardrail metric should come from this skill's scorecard.
- **retro** (pmm-execution) — reviewing how metrics performed after a
  launch; this skill defines the framework, retro looks backward at it.
