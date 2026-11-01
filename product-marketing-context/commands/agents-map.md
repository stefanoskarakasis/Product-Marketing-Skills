---
description: Write or refresh the map that makes your agent read your brain in every chat
---

# /agents-map — Write Your Agent Map

Runs the `product-marketing-context` skill's Step 10 (Write the Agent Map): adds one marked block to your project's `AGENTS.md`, a marked `@AGENTS.md` line to `CLAUDE.md`, and the two helper scripts to `foundation/tools/`. It runs by itself after your brain is built; use this command to refresh it after you add records or change the brain.

## Invocation

- /agents-map

## Workflow

### Step 1: Check Brain State

Apply the **product-marketing-context** skill's Step 1 (Detect Brain State). With no brain, say so and offer to build one. A cold-start brain still gets a map, and the block says which sections exist.

### Step 2: Write the Map

Follow the skill's Step 10 exactly. This command is a thin entry point; the behavior lives in `product-marketing-context/SKILL.md`. If the two ever disagree, the skill file is correct and this command should be updated to match.
