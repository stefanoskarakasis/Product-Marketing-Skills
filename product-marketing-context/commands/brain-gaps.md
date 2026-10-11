---
description: Answer the open questions that other skills left in your brain gaps queue
---

# /brain-gaps — Answer Your Brain Gaps

Runs the `product-marketing-context` skill's Step 7 (Answer Open Gaps): reads `/foundation/gaps.md` and goes through the open questions one at a time. Answer or skip each one.

## Invocation

- /brain-gaps

## Workflow

### Step 1: Check Brain State

Apply the **product-marketing-context** skill's Step 1 (Detect Brain State). With no brain, say so and offer to build one.

### Step 2: Answer Gaps

Follow the skill's Step 7 exactly. This command is a thin entry point; the behavior lives in `product-marketing-context/SKILL.md`. If the two ever disagree, the skill file is correct and this command should be updated to match.
