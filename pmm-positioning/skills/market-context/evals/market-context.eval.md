---
name: market-context.eval
version: 1.0.0
description: >
  Eval suite for market-context skill. Tests: brain context loading,
  specificity rejection of generic macro forces, confidence tagging
  discipline, narrative arc coherence, category moment accuracy,
  durability rating, and Learning Close accuracy against the skill's
  real four-field session-log shape. 6 scenarios covering real narrative
  builds and audits.
---

# Market-Context — Eval Suite

## Setup (Universal)

Each eval:
1. Populates `/foundation/brain.md` with baseline PMM context (Sections 3, 5) if testing brain loading
2. Populates `/context/meta-patterns.md` with guardrails (if testing guardrail surfacing)
3. Provides market signals, or withholds them to test the intake sequence
4. Runs market-context skill for the given scenario
5. Validates outputs: specificity enforcement, tagging accuracy, narrative coherence, confirmation gating

---

## Eval 1: Brain Context Loading (Step 0)

**Scenario:** `/foundation/brain.md` exists with populated Section 3 (Alternatives) and a thin Section 5 (Market Context — maturity stated, nothing else). Skill loads silently and treats this as UPDATE, not BUILD.

**Test Data:**
```yaml
# /foundation/brain.md
## Section 3: Alternatives & Positioning
Alternatives: Manual spreadsheets (status quo), Competitor X (direct)

## Section 5: Market Context
Market Maturity: Growth
```

**Expected Output — Context Referenced:**
```
Loaded alternatives and existing market maturity from brain. Market
Maturity already stated (Growth) — running UPDATE to fill macro forces,
buying triggers, and narrative arc rather than re-asking maturity.
```

**Pass Criteria:**
- Brain Sections 3 and 5 loaded silently, stated in one line before intake
- Skill does not re-ask for Market Maturity since it's already on file
- Skill correctly routes to UPDATE rather than full BUILD given partial Section 5 content

---

## Eval 2: Specificity Rejection of Generic Macro Forces

**Scenario:** User offers a macro force as "AI is changing everything" with no further detail.

**Test Data:**
```
User: "Well, AI is changing everything, that's our why-now."
```

**Expected Output — Pushback, Not Acceptance:**
```
That's the answer everyone in your category gives right now — it won't
hold in a sales conversation. Help me sharpen it: what specifically is
changing because of AI, for which buyer, and what does it make them do
differently that they weren't doing eight months ago?
```

**Pass Criteria:**
- Generic force is not written into Section 5 as-is
- Pushback is specific about why it fails (competitor-claimable, no buyer connection) not a generic "please be more specific"
- Skill continues to ask until a specific force with a named buyer consequence is produced

---

## Eval 3: Confidence Tagging Discipline

**Scenario:** Mixed-confidence input — one force from a cited analyst report, one inferred from a pattern across deals, one force with no supporting evidence.

**Test Data:**
```
Analyst report: "Gartner, March 2026 — 60% of mid-market buyers cite vendor consolidation as a top-3 initiative"
Pattern: 4 of the last 6 deals mentioned a recent security incident during discovery — no direct question asked about it
No evidence: Assumption that a new regulation is driving urgency — not yet confirmed with any buyer
```

**Expected Output — Tagged Claims:**
```
[CONFIRMED] Vendor consolidation is a top-3 mid-market initiative — Gartner, March 2026
[INFERRED] Recent security incidents are accelerating urgency — pattern across 4/6 deals, not directly confirmed
[HYPOTHESIS] A new regulation is driving urgency — no supporting evidence yet, needs validation
```

**Pass Criteria:**
- All three claims carry the correct tag — no blending into unqualified prose
- `[HYPOTHESIS]` claims are explicitly flagged as needing validation before entering the narrative arc
- Narrative arc language reflects the tag — confident phrasing for CONFIRMED, hedged for INFERRED

---

## Eval 4: Narrative Arc Coherence

**Scenario A — should be rejected:** Draft arc with a broken chain — a macro force with no buyer consequence stated, and a solution claim that doesn't connect back to the force.

**Scenario B — should pass:** Full chain — force → buyer consequence → why old approach fails → why now.

**Test Data (should fail):**
```
"The market is moving fast. Buyers need better tools. We built a great product."
```

**Test Data (should pass):**
```
"Vendor consolidation pressure has caused mid-market buyers to cut tool budgets by 30%.
This means procurement now blocks any net-new vendor without a consolidation story.
The old approach — pitching point-solution value — no longer works because procurement
filters it out before it reaches the economic buyer. [Product] was built for this moment
because it replaces three tools buyers are already trying to cut."
```

**Pass Criteria:**
- Scenario A is flagged and sent back — "buyers need better tools" is not a coherent chain, it's a category-level generality
- Scenario B passes — each link traces to the next, and the "why now" is explicit
- Skill runs the coherence check explicitly before finalizing, not just formats whatever was given

---

## Eval 5: Category Moment Accuracy

**Scenario:** User assumes "category creation" when signals point to "differentiation" — buyers already understand the category and are comparing named vendors.

**Test Data:**
```
User: "We're creating a whole new category here."
Signal: 3 named competitors already exist, buyers use the category name unprompted in discovery calls, alternatives map has 4 named direct competitors.
```

**Expected Output — Correction, Not Agreement:**
```
The signals point somewhere else — buyers are already naming the category
and comparing you to 4 named alternatives from your own alternatives map.
That's differentiation, not creation. Category creation means educating
buyers who don't yet know they have this problem — yours already do. This
changes the motion: lead with the gap, not the problem.
```

**Pass Criteria:**
- Skill does not accept the user's stated category moment uncritically when brain Section 3 data contradicts it
- Correction explains the GTM consequence of getting this wrong (wrong motion, not just wrong label)
- Final category moment written to Section 5 reflects the evidence, not the initial assumption

---

## Eval 6: Learning Close and Durability Rating

**Scenario:** Full BUILD session completes — narrative arc built, category moment named as differentiation, one macro force still carries a `[HYPOTHESIS]` tag.

**Expected Output — Section 5 Write Shown Before Committed:**
```
Here's exactly what Section 5 will read after this write: [full before/after
shown]. Confirm before I save this?
```

**Expected Output — Session Log:**
```yaml
skill: market-context
session_date: 2026-08-31
pattern: "User's initial category-moment read (creation) contradicted the
  alternatives map data (4 named competitors) — worth checking whether
  this pattern (users overestimating category-creation status) recurs."
source: surprised
```

**Pass Criteria:**
- Section 5 write is shown in full before being committed — no silent write
- Durability is rated (durable/at-risk/short-window) with a review date set, not left unrated
- Session logged to `/context/skill-sessions.md` with exactly four fields — no separate knowledge/decisions file written
- If nothing notable happened, `pattern: none` is still written — the row is never skipped

---

## Eval Test Coverage Matrix

| Eval | Feature | Pass Criteria |
|------|---------|---------------|
| 1 | Brain context loading (Step 0) | Sections 3/5 loaded silently, correctly routes UPDATE vs BUILD |
| 2 | Specificity rejection | Generic macro forces pushed back on, not written as-is |
| 3 | Confidence tagging discipline | CONFIRMED/INFERRED/HYPOTHESIS applied correctly, never blended |
| 4 | Narrative arc coherence | Broken chains rejected; full chains pass |
| 5 | Category moment accuracy | Contradicting evidence overrides user's initial assumption |
| 6 | Learning Close + durability | Section 5 shown before write; durability rated; real four-field session-log row |

---

## Running Evals

```bash
# Run all evals
for i in {1..6}; do
  echo "Running eval $i..."
  # [invoke market-context with test data]
  # [validate outputs against pass criteria]
done

# Run single eval
# [invoke market-context with eval N test data]
# [validate against eval N pass criteria]
```
