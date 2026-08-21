---
description: Review or tailor a PMM resume against a specific job description
argument-hint: "<paste resume and job description>"
---

# /pmm-toolkit:resume -- Resume Review

Review and tailor a Product Marketing resume against a specific job
description — dissects the JD, ranks your bullets by fit, and rebuilds
the resume in one pass.

## Invocation

```
/pmm-toolkit:resume [paste resume + job description]
/pmm-toolkit:resume Tailor this for a Director-level role
```

## Workflow

Uses the `pmm-resume` skill. Extracts what the JD is actually asking
for, scores each existing bullet against it, and rewrites the resume to
lead with the strongest matches.
