---
name: pmm-metrics.eval
version: 1.0.0
description: >
  Eval suite for pmm-metrics skill. Tests: business game classification,
  North Star Metric rejection on failed criteria, Input Metric causal
  rigor, scorecard sprawl capping, vanity-metric flagging, no-brain
  fallback, and Learning Close accuracy against the skill's real
  four-field session-log shape. 7 scenarios covering real metrics
  sessions and edge cases.
---

# PMM-Metrics — Eval Suite

## Setup (Universal)

Each eval:
1. Populates `/foundation/brain.md` with baseline PMM context (Sections 1, 2) if testing brain loading
2. Populates `/context/meta-patterns.md` with a recurring guardrail (if testing guardrail surfacing)
3. Provides business-model context, or withholds it to test the no-brain fallback
4. Runs pmm-metrics skill for the given scenario
5. Validates outputs: classification accuracy, NSM rigor, Input Metric rigor, scorecard discipline, self-check, Learning Close

---

## Eval 1: Business Game Classification (Step 1)

**Scenario:** User describes a B2B SaaS workflow-automation tool for ops teams. Skill must classify the business game explicitly, not silently assume Productivity.

**Test Data:**
```
Product: workflow automation tool for ops teams — connects existing tools,
eliminates manual handoffs, customers measure success by hours saved per week.
```

**Expected Output — Explicit Classification:**
```
Classifying as Productivity game: customers get value from completing
work more efficiently, not from time spent in-product or transaction
volume. Hours saved per week is the kind of signal a Productivity-game
North Star should track.
```

**Pass Criteria:**
- Classification stated explicitly with one sentence of rationale, not silently assumed
- Rationale ties to the actual product description, not a generic "most B2B SaaS is Productivity" statement
- Classification happens before any North Star candidate is proposed

---

## Eval 2: North Star Metric Rejected on Failed Criteria

**Scenario:** User proposes "Annual Recurring Revenue" as the North Star Metric.

**Test Data:**
```
User: "Let's just make ARR our North Star — it's what the board cares about."
```

**Expected Output — Rejected, Not Accepted With Caveats:**
```
ARR fails two of the seven criteria, so it can't be the North Star:
- Customer-Centric: FAIL — ARR reflects what the company earns, not
  what value the customer received. A customer can churn a month after
  a big ARR-boosting deal closes.
- Leading Indicator: FAIL — ARR is a lagging measure of past deals, not
  a predictor of future ones. By the time ARR drops, the customer
  behavior that caused it happened months earlier.

ARR is a fine metric for the Financial category of the scorecard — it's
just not a valid North Star. What's the specific in-product behavior
that predicts whether a customer renews or expands?
```

**Pass Criteria:**
- ARR is explicitly rejected as NSM, not delivered with a disclaimer and kept anyway
- At least 2 specific failed criteria are named with evidence, not a generic "that's not customer-centric" dismissal
- Skill proposes ARR's legitimate place (Financial category metric) rather than discarding it entirely
- Skill prompts toward a genuine customer-behavior alternative

---

## Eval 3: Input Metrics — Causal Rigor and Ownership

**Scenario:** North Star confirmed as "Weekly Active Workflows Completed." User proposes an Input Metric with no stated causal link.

**Test Data:**
```
NSM: Weekly Active Workflows Completed
User-proposed Input Metric: "Number of blog posts published"
```

**Expected Output — Challenged, Not Accepted:**
```
[GENERIC — no causal link] "Blog posts published" doesn't have a stated
mechanism for moving Weekly Active Workflows Completed — publishing more
content doesn't itself make existing users complete more workflows.
What's actually upstream of workflow completion? Candidates worth
testing: time-to-first-workflow-created (onboarding friction), number of
integrations connected per account (more integrations → more automatable
workflows), or weekly active workflow *creators* (a different cohort
metric than completions).
```

**Pass Criteria:**
- A proposed Input Metric with no causal link to the NSM is challenged, not silently accepted
- Skill offers specific causal-candidate alternatives, not just a rejection
- Every Input Metric in the final delivered set has both a stated causal mechanism and a named owner (PMM, Product, Sales, or CS)

---

## Eval 4: Scorecard Sprawl Capping

**Scenario:** User wants to track 22 metrics across the four categories — more than the 16-metric cap.

**Test Data:**
```
User lists 22 candidate metrics spanning all 4 categories, roughly 5-6 per category.
```

**Expected Output — Capped, Not Delivered As-Is:**
```
22 metrics is past the point anyone updates a scorecard biweekly — repos
and teams that try this abandon it by Q2. Cutting to 16. Financial has
the most overlap: "ARR" and "Product-level revenue" are close enough to
merge into one. Which 2 in Customer matter least to your reporting
audience — NPS and reviews, or the call-engagement metric?
```

**Pass Criteria:**
- Final delivered scorecard has ≤16 metrics, never delivered at 22 with a passive "you might want to trim this"
- Skill identifies specific overlapping/mergeable metrics rather than cutting arbitrarily
- Skill asks the user which to cut when the choice isn't obvious, rather than silently deciding alone
- Every category retains at least 1 metric after cutting

---

## Eval 5: Vanity-Metric Flagging

**Scenario:** A candidate metric technically trackable but with no function able to move it.

**Test Data:**
```
Candidate metric: "Industry analyst mentions of our category" (not the company by name)
```

**Expected Output — Flagged, Not Silently Included:**
```
[VANITY — no owner can move this] "Industry analyst mentions of our
category" isn't something PMM, Sales, or Product can directly cause —
analysts write about category trends on their own schedule regardless of
what this team does. If the real interest is competitive visibility,
"analyst mentions of [company name] specifically" is trackable and PMM
can influence it through briefings.
```

**Pass Criteria:**
- A metric with no plausible owner is explicitly flagged `[VANITY — no owner can move this]`, not delivered unflagged
- Skill offers a concrete owned alternative rather than just rejecting
- The self-check step (Step 5) surfaces this before final delivery, not after the user asks

---

## Eval 6: No-Brain Fallback

**Scenario:** No `/foundation/brain.md` exists. User asks to build a metrics framework directly.

**Expected Output — Non-Blocking Surface, Then Direct Ask:**
```
No brain found. I'll ask directly about your business model and
customer segment instead. Metrics will be less sharply targeted without
ICP/beachhead context — run product-marketing-context first for a
tighter fit, or continue now.

To start: how do customers get value from your product — time spent,
transactions completed, or work done more efficiently? And who's the
primary buyer/user you're building this scorecard for?
```

**Pass Criteria:**
- Skill does not block or refuse to proceed without a brain
- Surfaces the no-brain note exactly once, non-blocking, offering the option to run `product-marketing-context` first
- Falls back to asking for business model and segment directly rather than guessing

---

## Eval 7: Full Workflow, Weights, and Learning Close

**Scenario:** Full session completes — classification → NSM (passes all 7 criteria) → 4 Input Metrics → 12-metric scorecard → self-check → delivery → Learning Close.

**Test Data:**
```
Business: Productivity game, B2B SaaS ops tool
NSM: "Weekly Active Workflows Completed" — passes all 7 criteria
Input Metrics: 4, each with causal link and owner
Scorecard: 3 Financial + 3 Customer + 3 Product & GTM + 3 Process & Growth = 12 metrics
Weights: assigned by user across the 12, must sum to 100%
```

**Expected Output — Full Workflow:**
```
✓ Business game: Productivity (rationale stated)
✓ North Star: Weekly Active Workflows Completed — passes all 7 criteria
✓ Input Metrics: 4 defined, each with causal link + owner
✓ Scorecard: 12 metrics across 4 categories (3 each), weights sum to 100%
✓ Self-check: no sprawl (12 ≤ 16), no vanity metrics, no unowned metrics
✓ Delivered in chat — explicit note this isn't saved automatically
✓ Session logged:
  type: execution
  skill: pmm-metrics
  session_date: 2026-09-14
  pattern: "User's first NSM proposal (ARR) failed 2 criteria — worth
    checking whether that's a common first-instinct pattern across
    sessions, not just this one."
  source: surprised
```

**Pass Criteria:**
- Full workflow completes in order: classification → NSM (scored on all 7 criteria) → Input Metrics → scorecard → self-check → delivery → Learning Close
- Weights explicitly shown summing to exactly 100%, not left unstated
- No brain write is attempted anywhere in the session — output exists only in chat
- Session logged to `/context/skill-sessions.md` with exactly the real four fields (plus `type: execution`) — no richer schema
- If nothing notable happened, `pattern: none` is still written — the row is never skipped

---

## Eval Test Coverage Matrix

| Eval | Feature | Pass Criteria |
|------|---------|---------------|
| 1 | Business game classification | Explicit classification + rationale, never silently assumed |
| 2 | NSM rejection on failed criteria | Failing candidates (e.g. ARR) rejected with named criteria, not accepted with caveats |
| 3 | Input Metric causal rigor | No causal link → challenged with specific alternatives; every kept metric has owner |
| 4 | Scorecard sprawl capping | ≤16 metrics delivered; overlaps merged, cuts negotiated not silent |
| 5 | Vanity-metric flagging | Unowned metrics explicitly flagged, alternative offered |
| 6 | No-brain fallback | Non-blocking surface, then direct ask, never refuses |
| 7 | Full workflow + Learning Close | Complete sequence, weights sum to 100%, real four-field session-log row, no brain write attempted |

---

## Running Evals

```bash
# Run all evals
for i in {1..7}; do
  echo "Running eval $i..."
  # [invoke pmm-metrics with test data]
  # [validate outputs against pass criteria]
done

# Run single eval
# [invoke pmm-metrics with eval N test data]
# [validate against eval N pass criteria]
```
