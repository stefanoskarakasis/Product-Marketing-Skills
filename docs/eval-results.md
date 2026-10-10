# Eval results

The evals in each skill's `evals/` folder are written test cases. This page records whether anyone has **run** them. The checks that run automatically on every change (structure and version consistency) do not run evals.

**Status: not yet run.** Nothing below is a pass until a row says so.

## How to run an eval

1. Start a fresh session with the plugin installed. One eval per session so earlier work does not leak.
2. Set up the fixture exactly as the eval's Setup says (brain present, absent or thin; files in place).
3. Paste the eval's input or prompt.
4. Compare the output with the eval's Expected Output and Pass Criteria, line by line.
5. Record one row below: **Pass** (every criterion met), **Partial** (some met; say which failed), or **Fail**. Add what you would change.
6. Fix the skill, bump the version, and re-run any failed eval before marking it Pass.

## Results

| Skill | Version | Eval | Date | Result | What failed or changed |
|---|---|---|---|---|---|
| customer-stories | 1.0.0 | Eval 1: Full notes to a standard story | | Not run | |
| customer-stories | 1.0.0 | Eval 2: Thin notes, no invention | | Not run | |
| customer-stories | 1.0.0 | Eval 7: Kickoff asks for roles | | Not run | |
| alternatives-map | 2.1.0 | Eval 10: Cold start (no brain) | | Not run | |
| alternatives-map | 2.1.0 | Eval 1 | | Not run | |
| alternatives-map | 2.1.0 | Eval 7: Confirmation-gated write | | Not run | |
| ideal-customer-profile | 1.1.0 | Eval 9: Cold start (no brain) | | Not run | |
| ideal-customer-profile | 1.1.0 | Eval 1 | | Not run | |
| ideal-customer-profile | 1.1.0 | Eval 6: Confirmation-gated write | | Not run | |
| proof-points | 1.1.0 | Eval 11: Cold start (no brain) | | Not run | |
| proof-points | 1.1.0 | Eval 1: Extract mode | | Not run | |
| proof-points | 1.1.0 | Eval 13: Learning Close | | Not run | |
| product-messaging-playbook | 1.1.0 | Eval 1: Quick-Brain (no brain) | | Not run | |
| product-messaging-playbook | 1.1.0 | Eval 2: Full run | | Not run | |
| product-messaging-playbook | 1.1.0 | Eval 9: Learning Close | | Not run | |
| gtm-motions | 1.1.0 | Eval 1: No brain, Quick-Brain | | Not run | |
| positioning-ideas | 1.1.0 | Eval 1: Fewer than 3 alternatives, Quick-Brain | | Not run | |
| value-prop-statements | 1.1.0 | Eval 1: No positioning, user supplies one | | Not run | |
| product-marketing-context | 2.1.0 | Eval 3: Cold-start brain recognised | | Not run | |
| meta-review | 3.1.0 | Test 1: Skill that passes (18/18) | | Not run | |
| workflow-orchestrator | 2.4.1 | Test Case 2: Brain missing, routes to beachhead-segment | | Not run | |
