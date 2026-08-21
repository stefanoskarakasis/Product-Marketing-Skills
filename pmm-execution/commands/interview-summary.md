---
description: Summarize a customer interview transcript using JTBD analysis
argument-hint: "<paste transcript or describe the interview>"
---

# /pmm-execution:interview-summary -- Interview Summary

Turn a raw customer or prospect interview transcript into a structured
discovery summary anchored in Jobs to Be Done theory.

## Invocation

```
/pmm-execution:interview-summary [paste transcript]
/pmm-execution:interview-summary Win-loss call with Acme Corp, lost to
Salesforce
```

## Workflow

Uses the `interview-summary` skill. Extracts the Job, pain points, and
signal quotes from the transcript, flags any competitor or pattern
signal worth routing elsewhere, and produces the structured summary.
