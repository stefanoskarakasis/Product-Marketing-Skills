---
description: Find the brain fields that have gone stale and re-confirm only those
argument-hint: "[optional: section number, e.g. 3]"
---

# /refresh-brain — Refresh Your Brain

Runs the `product-marketing-context` skill's Step 6 (Refresh Stale Fields): compares every field's date with its section's freshness limit, lists what is stale, and asks one field at a time whether it is still true, changed, or should be dropped.

## Invocation

- /refresh-brain
- /refresh-brain 3

## Workflow

### Step 1: Check Brain State

Apply the **product-marketing-context** skill's Step 1 (Detect Brain State). With no brain, say so and offer to build one.

### Step 2: Refresh

Follow the skill's Step 6 exactly. If a section number was passed, check only that section. This command is a thin entry point; the behavior lives in `product-marketing-context/SKILL.md`. If the two ever disagree, the skill file is correct and this command should be updated to match.
