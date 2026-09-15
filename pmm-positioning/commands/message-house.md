---
description: Format existing positioning into a Message House (Roof + Value Pillars)
argument-hint: "<optional: paste a positioning-messaging output, or leave blank to use the brain>"
---

# /pmm-positioning:message-house -- Message House

Formats positioning that already exists — from the brain or a pasted `positioning-messaging` output — into a Message House: a Roof table plus up to 3 Value Pillars. Does not create positioning from scratch; if none exists yet, it will say so and point you at `positioning-messaging` instead.

## Invocation

```
/pmm-positioning:message-house
/pmm-positioning:message-house Build the roof and pillars for a new hire deck
/pmm-positioning:message-house [paste a positioning-messaging BUILD output] now format this as a house
```

## Workflow

Uses the `message-house` skill. Loads brain Sections 1, 2, 3, 5, 6 (or a pasted positioning output, which takes precedence for any field it covers), flags any field with no traceable source as `[MISSING]` instead of inventing it, caps Value Pillars at 3, and returns a single markdown deliverable with the Roof and Pillars tables plus a "Still needed" list. Blocks and redirects to `positioning-messaging` or `product-marketing-context` if no usable positioning exists yet.
