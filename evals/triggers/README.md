# Trigger prompts

Claude picks a skill from its name and description alone. `prompts.json` holds the prompts that check it picks the right one.

## What is in `prompts.json`

- **144 skill prompts, three per skill.** *Direct* names the job. *Indirect* describes the situation without the skill's words. *Near-miss* belongs to a neighbouring skill, named in `expect`.
- **12 prompts that should trigger no skill** (`non_pmm`): code, travel, recipes, translation.
- Every prompt carries its own material. A prompt that says "the deal below" without the deal makes Claude ask for it, which scores as a miss.

## How to check by hand (no terminal)

1. Install the plugins. Open a **fresh** chat for each prompt, so earlier answers do not steer the next one.
2. Paste one prompt exactly as written.
3. Note which skill answers. **Pass** = the skill in `expect`. For a `non_pmm` prompt, pass = no skill answers.
4. Start with the near-misses. They are the ones that fail first when two descriptions overlap.

The competitive family also has a by-hand battery in `docs/routing-checks.md`. Run both after you change a description.

## What the tests guard

- `tests/test_trigger_prompts.py` fails when a skill has no direct, indirect and near-miss prompt, so a new skill cannot ship without its three prompts.
- `tests/test_description_budget.py` keeps all descriptions under a shared ceiling (see `SKILL-SPEC.md` section 3).
- `tests/test_triggers.py` catches duplicate trigger phrases and missing "Not for" clauses.

None of these tests runs a model. A model-run scorer (headless `claude -p` over this file) is the next step; coreyhaines31/marketingskills publishes one under the MIT license, and it reports that identical runs of one set vary by several points, so repeat any run before you trust a small change.

## Adding a skill

Add its three prompts in the same pull request. Write the near-miss from the neighbour's scope, then add the skill to that neighbour's "Not for" clause.
