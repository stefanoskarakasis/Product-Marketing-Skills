---
description: Tell your brain how you like to work (format, length, detail), kept apart from company facts
---

# /my-context: How You Like to Work

Runs the `product-marketing-context` skill's Step 9 (My context): asks a few short questions about the shape of outputs you like and saves them to `/foundation/me.md` after you confirm.

## Invocation

- /my-context

## Workflow

### Step 1: Check State

Apply the **product-marketing-context** skill's Step 1 (Detect Brain State). `me.md` does not need a brain, so with no brain the command still runs and offers to build the brain afterwards.

### Step 2: Capture How You Work

Follow the skill's Step 9 exactly. This command is a thin entry point; the behavior lives in `product-marketing-context/SKILL.md`. If the two ever disagree, the skill file is correct and this command should be updated to match.
