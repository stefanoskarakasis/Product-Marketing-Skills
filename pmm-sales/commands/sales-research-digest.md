---
description: Get one plain-language report on how your sales team used the research skills this week, whether the advice held up, and what to do next
argument-hint: "<optional: 'since 1 Nov' or a question about the logs>"
---

# /pmm-sales:sales-research-digest -- Sales Research Digest

Reads the logs the sales research skills already write, checks your CRM for what happened next, and gives you one report in plain words: who used the skills, whether the advice held up, what the companies have in common, and up to three things to do. Saves the full report to `/context/digests/` and posts a short summary with teams only. It proposes changes and writes none.

## Invocation

```
/pmm-sales:sales-research-digest
/pmm-sales:sales-research-digest since 1 Nov
/pmm-sales:sales-research-digest Which red reports did sellers ignore?
```

## Workflow

Uses the `sales-research-digest` skill. Loads the logs, counts use, judges the advice, matches companies to deals in your CRM (read-only, and it tells you to connect one if none answers), finds what the companies have in common, writes at most three actions, runs a 10-check gate, saves the file and logs the session. For all skills together, use `meta-synthesis` instead.
