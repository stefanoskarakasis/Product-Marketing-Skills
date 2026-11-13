# Routing runs

This page records **which skill answered**, prompt by prompt. It is separate from `eval-results.md`, which records skill output quality.

**Status: not yet run.** A cell is empty until someone has done the run.

## Sets

| Set | File | Rows | Blind? |
|---|---|---|---|
| A | `evals/triggers/prompts.json` | 144 + 12 non-PMM | No: written alongside the descriptions |
| B | `evals/triggers/heldout.json` | 96 + 12 non-PMM | **No.** Written by an assistant that had read every description. Treat results as an upper bound |
| Battery | `docs/routing-checks.md` | 46 | No |

A truly blind set must be written by someone who has not read the descriptions. Until one exists, do not quote any score here as proof of routing quality.

## Rules

1. One prompt per fresh chat, with the plugins installed and nothing else enabled that you do not normally use.
2. Never edit a prompt after seeing its result. Add a new row instead.
3. A Miss is a description problem. Change the description, not the prompt.
4. Re-run the same set after a change. Identical runs of the same prompts can differ by several points, so repeat a close result.

## Runs

| Date | Plugin version | Set | Prompts | Passed | Misses (exact prompt, skill that answered) |
|---|---|---|---|---|---|
| | | | | | |
