---
description: Orchestrate a multi-skill PMM program end to end
argument-hint: "<program name, e.g. full launch, positioning refresh>"
---

# /pmm-go-to-market:workflow-orchestrator -- Workflow Orchestrator

Chain multiple skills into one coherent, end-to-end PMM program with a
master document and checkpoints.

## Invocation

```
/pmm-go-to-market:workflow-orchestrator Full launch for Q3 feature
/pmm-go-to-market:workflow-orchestrator Positioning refresh
```

## Workflow

Uses the `workflow-orchestrator` skill. Builds a Program Charter,
sequences the skills the program needs, runs coherence checks between
their outputs, and produces one master document at the end.
