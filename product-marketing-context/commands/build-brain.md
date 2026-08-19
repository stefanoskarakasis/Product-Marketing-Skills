---
description: Build or update your GTM brain — product context, ICP, positioning, voice, market context, and proof points
argument-hint: "[optional: section name to jump to, e.g. 'ICP']"
---

# /build-brain — Build Your GTM Brain

Runs the `product-marketing-context` skill end to end: checks whether
`/foundation/brain.md` already exists, and either starts the wizard fresh
or offers to view, edit, or audit what's already there.

## Invocation

- /build-brain 
- /build-brain ICP 
- /build-brain audit
- /setup-GTM brain

## Workflow

### Step 1: Check Brain State

Apply the **product-marketing-context** skill's Step 1 (Detect Brain
State). If an argument was passed (e.g. "ICP" or "audit"), route directly
to that section or to the health audit instead of the full wizard.

### Step 2: Run the Wizard or Audit

Follow the skill's own Execution Flow exactly — this command is a thin
entry point, not a separate set of instructions. Do not duplicate the
skill's step logic here; invoke it.

### Step 3: Confirm and Save

Each section is confirmed by the user before being written to
`/foundation/brain.md`, per the skill's Quality Gate.

## Notes

- This command exists so `/build-brain` is a discoverable, memorable entry
  point — the underlying behavior always lives in
  `product-marketing-context/SKILL.md`. If the two ever disagree, the
  skill file is correct and this command should be updated to match.
