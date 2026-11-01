# Run the evals

The evals in each skill's `evals/` folder are written test cases. Nothing in this repo has run them yet, and the automatic checks (structure, counts, word budget) never run a skill. This page gets you from "written" to "recorded" in about two hours for the five skills that changed most.

## First sitting: 28 cases

[`eval-first-sitting.md`](eval-first-sitting.md) holds the input and pass condition for 28 cases across `competitive-battlecard`, `competitive-profile`, `competitor-deep-dive`, `industry-newsletter` and `product-marketing-context`. They are the cases most likely to break when detail moves into `references/`: constraint stops, caps, evidence floors, confirmation gates and verbatim rules.

1. Install the plugins in Claude Code and open an empty test folder.
2. Save `examples/example-brain.md` as `foundation/brain.md`. Where a case says "no brain", move that file away for the case.
3. Run one case per fresh session. Paste the input, compare the output with the pass condition.
4. Write the result on the sheet: **Pass**, **Partial** (say what failed) or **Fail**.
5. Copy the results into the table in [`eval-results.md`](eval-results.md).

## The one thing to watch

Skills now point to files in their `references/` folder ("read it now"). On every case, check that Claude opened the file when the step said to. If it answered without opening it, that is a Fail for the skill, not for the case: note the step.

## Not covered by any eval

- `product-marketing-context` Step 10 (the agent map): run `/product-marketing-context:agents-map` in a folder with a brain, then ask for homepage copy in a fresh chat with no skill name. Claude should read the brain first.
- The send guard hook: ask Claude to post "test" to a private Slack channel. It must ask first.

## More cases

`python3 scripts/eval_sheet.py <skill folder>` builds a sheet for any skill. `--all-hero` builds every case for the five.
