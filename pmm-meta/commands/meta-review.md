---
description: Audit a skill's SKILL.md against the repo's authoring standard
argument-hint: "<skill name to review>"
---

# /pmm-meta:meta-review -- Skill Spec Review

Audit any `SKILL.md` in this repo against `SKILL-SPEC.md`, the skill
authoring standard, with a full checklist and prioritized fixes.

## Invocation

```
/pmm-meta:meta-review retro
/pmm-meta:meta-review stakeholder-maps
```

## Workflow

Uses the `meta-review` skill. Checks the named skill against every spec
requirement, flags what's missing or wrong, and prioritizes fixes by
how much they affect the skill's real-world reliability.
