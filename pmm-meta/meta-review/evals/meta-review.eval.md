# meta-review.eval.md

Eval test cases for `meta-review` skill (SKILL-SPEC v2.1.0 compliance).

---

## Test 1: Skill That Passes — All 17 Checks Clear

**Input:**

- Skill name: a T2 skill with complete frontmatter, all 7 required sections
  filled in (no omissions), `## Operating Rules` with 8 rules, `## Quality
  Gate` with 6 binary checks, 380 lines total, output template wrapped in a
  code fence, an evals file with 4 test cases including one edge case.

**Expected Behavior:**

1. Frontmatter checks all pass (5/5)
2. All 7 required sections present and filled (7/7)
3. Tier-appropriate checks pass — Operating Rules ≥6, Quality Gate ≥5 (2/2)
4. Quality checks pass — under 500 lines, template fenced, evals file with
   3+ cases including an edge case (3/3)
5. Score reported as 17/17

**Success Criteria:**

- Every one of the 17 checks is evaluated and reported individually
- Final score correctly totals 17/17
- Verdict states "PASSES SPEC" plainly, without manufacturing nitpicks

**Test Pass:** Skill scores 17/17 and the report says so without padding

---

## Test 2: Skill Below Threshold — Missing Sections

**Input:**

- Skill name: a T1 skill missing `## Do Not Use For` entirely (not even
  `n.v.t.`), with `## Operating Rules` containing only 3 rules (spec
  requires ≥6 for T1/T2), and no evals file at all.

**Expected Behavior:**

1. `## Do Not Use For` check fails — section is absent, not `n.v.t.`
2. `## Operating Rules` check fails — 3 rules present, 6 required
3. Evals-file check fails — no `evals/` directory found
4. All other checks evaluated independently and pass/fail on their own merits
5. Score totals below 15/17
6. Failed checks each cite the specific gap: "Do Not Use For section is
   missing (not present as n.v.t. either)", "Operating Rules has 3 rules,
   spec requires ≥6 for T1", "No evals/skill-name.eval.md file found"

**Success Criteria:**

- Score is below the 15/17 threshold and the report says NEEDS FIXES
- Each failure names the specific gap, not a generic "incomplete"
- Checks unrelated to the three failures are still evaluated and reported
  as passing, not skipped

**Test Pass:** Report gives an accurate score and actionable, specific fixes

---

## Test 3: n.v.t. Handled Correctly (Edge Case)

**Input:**

- Skill name: a T3 utility skill where `## Pre-flight` reads only `n.v.t.`
  (genuinely no dependency checks apply) and `## Inputs` → `Args` and
  `Defaults` both read `n.v.t.` (skill takes no arguments).

**Expected Behavior:**

1. The `## Pre-flight` check passes — explicit `n.v.t.` counts as compliant
   per SKILL-SPEC.md Section 7, not as an omission
2. The `## Inputs` check passes on the same basis
3. Report explicitly lists these two checks under "Passed with n.v.t.",
   distinct from checks that passed with real content
4. T3 tier means Operating Rules and Quality Gate checks are not evaluated
   at all (they're T1/T2-only per Section 12) — report does not penalize
   their absence

**Success Criteria:**

- `n.v.t.` sections are never scored as failures
- The report distinguishes "passed with n.v.t." from "passed with content"
- Tier-inappropriate checks are correctly excluded, not silently failed

**Test Pass:** A skill using n.v.t. correctly and matching its tier's
requirements is not penalized for either

---

## Test 4: Whole-Plugin Review (Multiple Skills)

**Input:**

- User asks to review every skill in a 3-skill plugin in one request.

**Expected Behavior:**

1. Meta-review runs the full 17-point checklist independently for each of
   the 3 skills
2. Results are reported per-skill, not averaged or blended into one summary
   score
3. If skill A scores 17/17 and skill B scores 12/17, both scores are shown
   individually with skill B's specific failures listed

**Success Criteria:**

- No skill's failures are obscured by another skill's passing score
- Each skill gets its own full report section

**Test Pass:** Three distinct, individually scored reports, not one blended
plugin-level verdict
