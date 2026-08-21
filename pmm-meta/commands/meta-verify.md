---
description: Run a second-pass quality check on skill output before delivery
argument-hint: "<the output to verify, or the skill that produced it>"
---

# /pmm-meta:meta-verify -- Output Verification

Run a second-pass quality check on a skill's output before it goes out
the door — catching issues the first pass missed.

## Invocation

```
/pmm-meta:meta-verify Check this positioning brief before I send it
/pmm-meta:meta-verify Verify the last GTM strategy output
```

## Workflow

Uses the `meta-verify` skill. Re-checks the output against the
originating skill's own quality bar, flags anything that doesn't meet
it, and returns specific fixes rather than a pass/fail verdict alone.
