# meta-verify.eval.md

Eval test cases for `meta-verify` skill.

---

## Test 1: Output Clears Second Pass

**Input:**

- Output: a `go-to-market-strategy` GTM brief.
- Originating skill's Quality Gate (from its own `SKILL.md`): 9 checks,
  e.g. "Four signals applied", "Leading indicator present", "Proof point
  gaps flagged."
- The brief genuinely satisfies all 9.

**Expected Behavior:**

1. `go-to-market-strategy`'s own `SKILL.md` is loaded and its actual
   Quality Gate table is read — not a generic or invented rubric
2. Each of the 9 checks is independently re-verified against the brief's
   actual content
3. Operating Rules are also scanned (Step 3) even without a matching gate
   row
4. Report: 9/9 passed, Operating Rules clean, verdict "CLEARS SECOND PASS"

**Success Criteria:**

- The checklist used is provably the same one from the originating skill's
  own file, not a substitute
- A genuine pass is reported as a pass, without inventing soft findings

**Test Pass:** Accurate 9/9 result stated plainly

---

## Test 2: Output Fails Specific Gate Checks

**Input:**

- Same brief type, but this one has no leading indicator — only a lagging
  metric — and no explicit enablement timeline.

**Expected Behavior:**

1. The "Leading indicator present" check fails, with evidence: "Success
   Metrics table lists only one lagging metric (revenue), no leading
   indicator"
2. Any other gate row referencing timeline/enablement specificity fails
   with similarly specific evidence
3. Checks unrelated to these two still pass independently
4. Verdict: "NEEDS FIXES BEFORE DELIVERY", with both fails listed and
   specific enough that the fix is obvious

**Success Criteria:**

- Failures cite the actual missing content, not a vague "could be
  stronger"
- Passing checks aren't dragged down by the two real failures

**Test Pass:** Two specific, evidence-backed failures; rest correctly
marked as passing

---

## Test 3: Originating Skill Has No Quality Gate (Edge Case)

**Input:**

- Output came from a skill with `quality_gate: false` in its frontmatter
  (a simple utility skill with no Quality Gate section at all).

**Expected Behavior:**

1. Pre-flight detects there's no Quality Gate to apply
2. Skill does not invent a generic rubric to fill the gap
3. Reports plainly: "No standard to check against — [skill-name] does not
   declare quality_gate: true and has no Quality Gate section."

**Success Criteria:**

- No fabricated scoring appears
- The limitation is stated honestly rather than papered over

**Test Pass:** Clear, honest "nothing to verify against" result — not a
manufactured score

---

## Test 4: Operating Rule Violated With No Matching Gate Row

**Input:**

- Output from `positioning-messaging`, which has an Operating Rule
  ("No positioning without 3+ alternatives — status quo mandatory") that
  isn't directly mirrored by a single Quality Gate table row.
- The output only names 2 alternatives.

**Expected Behavior:**

1. Quality Gate table checks all pass or fail on their own terms
2. Step 3 separately scans Operating Rules and flags this violation even
   though no Quality Gate row exactly matches it
3. Report includes a "Rule flags" section distinct from the Quality Gate
   table results

**Success Criteria:**

- The rule violation is caught even without a corresponding gate-table row
- It's reported in the correct section (Rule flags, not Quality Gate)

**Test Pass:** Violation caught and correctly categorized
