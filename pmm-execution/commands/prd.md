---
description: Create a product requirements document with an embedded Solution Story
argument-hint: "<feature or problem statement>"
---

# /pmm-execution:prd -- Product Requirements Document

Create a structured PRD from a feature idea or problem statement,
including a standalone Solution Story for PMM-led communications.

## Invocation

```
/pmm-execution:prd SSO support for enterprise customers
/pmm-execution:prd Users are dropping off during onboarding step 3
```

## Workflow

Uses the `prd` skill. Gathers context on the problem, users, and
success metrics through conversation, then produces both the full PRD
and a shorter Solution Story extracted from it.
