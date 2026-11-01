# meta-review.eval.md

Eval test cases for `meta-review` skill (SKILL-SPEC v3.0.0 compliance).

---

## Test 1: Skill That Passes — All 15 Checks Clear

**Input:**

- Skill name: a T2 skill with complete frontmatter, `## Trigger`, `## Inputs`,
  `## Steps` (ending in Learning Close), `## Outputs` and a `## Quality Gate`
  with 6 binary checks, 380 lines and 2,400 words, output template wrapped in a
  code fence, an evals file with 4 test cases including one edge case. It has
  no `## Pre-flight`, `## Verification`, `## Do Not Use For` or `## Operating
  Rules`.

**Expected Behavior:**

1. Frontmatter checks all pass (5/5)
2. All five core-section checks pass (5/5); the absent retired sections are
   not mentioned as failures
3. Learning Close check passes (1/1)
4. Quality checks pass: under 500 lines, under 3,000 words, template fenced,
   evals file with 3+ cases including an edge case (4/4)
5. Score reported as 15/15

**Success Criteria:**

- Every one of the 15 checks is evaluated and reported individually
- Final score correctly totals 15/15
- Verdict states "PASSES SPEC" plainly, without manufacturing nitpicks

**Test Pass:** Skill scores 15/15 and the report says so without padding

---

## Test 2: Skill Below Threshold — Too Big and Missing Parts

**Input:**

- Skill name: a T1 skill with `quality_gate: true` but no `## Quality Gate`
  section, 4,800 words (270 lines) with no legacy ceiling recorded, and no
  evals file at all.

**Expected Behavior:**

1. `## Quality Gate` check fails — `quality_gate: true` and the section is absent
2. Word-budget check fails — 4,800 words, limit 3,000, and the report says
   line count alone (270 lines) hid the problem
3. Evals-file check fails — no `evals/` directory found
4. All other checks evaluated independently and pass/fail on their own merits
5. Score totals below 13/15
6. Failed checks each cite the specific gap: "Quality Gate is missing but
   `quality_gate` is true", "4,800 words, budget 3,000: move rubrics to
   `references/`", "No evals/skill-name.eval.md file found"

**Success Criteria:**

- Score is below the 13/15 threshold and the report says NEEDS FIXES
- Each failure names the specific gap, not a generic "incomplete"
- Checks unrelated to the three failures are still evaluated and reported
  as passing, not skipped

**Test Pass:** Report gives an accurate score and actionable, specific fixes

---

## Test 3: N/A and Retired Sections Handled Correctly (Edge Case)

**Input:**

- Skill name: a T3 utility skill where `## Inputs` → `Args` and `Defaults`
  both read `N/A` (skill takes no arguments), `quality_gate: false` with no
  `## Quality Gate`, and which still carries a legacy `## Verification` and
  `## Do Not Use For` from before spec v3.0.0.

**Expected Behavior:**

1. The `## Inputs` check passes — explicit `N/A` counts as compliant
   per SKILL-SPEC.md Section 7, not as an omission
2. The Quality Gate check passes — `quality_gate: false` and the section is
   absent is compliant
3. Report lists the `N/A` Inputs fields under "Passed with N/A", distinct
   from checks that passed with real content
4. The legacy `## Verification` and `## Do Not Use For` are neither failed
   nor required; the report does not penalize their presence or absence
5. T3 tier means the Learning Close check is not applied (passes)

**Success Criteria:**

- `N/A` sections are never scored as failures
- Retired sections are never scored at all
- The report distinguishes "passed with N/A" from "passed with content"
- Tier-inappropriate checks are correctly excluded, not silently failed

**Test Pass:** A skill using N/A correctly and matching its tier's
requirements is not penalized for either

---

## Test 4: Whole-Plugin Review (Multiple Skills)

**Input:**

- User asks to review every skill in a 3-skill plugin in one request.

**Expected Behavior:**

1. Meta-review runs the full 15-point checklist independently for each of
   the 3 skills
2. Results are reported per-skill, not averaged or blended into one summary
   score
3. If skill A scores 15/15 and skill B scores 10/15, both scores are shown
   individually with skill B's specific failures listed

**Success Criteria:**

- No skill's failures are obscured by another skill's passing score
- Each skill gets its own full report section

**Test Pass:** Three distinct, individually scored reports, not one blended
plugin-level verdict
