---
description: Fan an existing positioning statement out into segment- and channel-specific value-prop copy variants, trace-checked against drift
argument-hint: "<segments or channels you need copy for — assumes a positioning statement already exists>"
---

# /pmm-growth:value-prop-statements -- Value Prop Statements

Take your already-set positioning statement and rapidly generate
segment- or channel-specific value-prop copy for marketing, sales, or
onboarding — without re-running the full positioning process. Every
variant is trace-checked against the canonical positioning so drift gets
flagged, not silently shipped.

## Invocation

```
/pmm-growth:value-prop-statements Write variants for Enterprise and SMB segments
/pmm-growth:value-prop-statements Adapt our positioning for a LinkedIn ad and an onboarding email
/pmm-growth:value-prop-statements Give me 3 variants for an A/B test on our homepage
```

## Workflow

Uses the `value-prop-statements` skill. Confirms a canonical positioning
statement exists (from brain Section 3 or a pasted `positioning-messaging`
output) — hard blocks and routes to `positioning-messaging` if none does.
Identifies target segments/channels, pulling real committee roles from a
recent `buyer-personas` session when available. Generates one statement
per segment/channel, then trace-checks each against the canonical
differentiator — flagging anything that drifts rather than just
paraphrasing. Recommends a `positioning-messaging` AUDIT if 3+ statements
in one batch fail the trace-check. Closes with a session log to
`/context/skill-sessions.md`.
