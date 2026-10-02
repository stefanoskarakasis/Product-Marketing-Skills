---
description: Assemble a Sales/CS-ready messaging playbook for a new product or feature — problem, story, one named competitive comparison, discovery questions, objection handling
argument-hint: "<feature/product name, optionally 'vs [competitor]', or paste a message-house/positioning-messaging output>"
---

# /pmm-positioning:product-messaging-playbook -- Product Messaging Playbook

Assembles the one document Sales and CS actually need — problem framing, story, a comparison against the one competitor buyers ask about, and a discovery/objection script — from what already exists in the brain and your other skills' output. Does not derive positioning, pillars, or proof itself; if those don't exist yet, it says so and points at `positioning-messaging`, `message-house`, or `proof-points` first.

## Invocation

```
/pmm-positioning:product-messaging-playbook Build a playbook for our new automations feature
/pmm-positioning:product-messaging-playbook [feature name] vs Breezy HR
/pmm-positioning:product-messaging-playbook [paste a message-house output] now build the full playbook
```

## Workflow

Uses the `product-messaging-playbook` skill. Loads brain Sections 1, 2, 3, 5, 6 (or pasted `message-house`/`positioning-messaging` output, which takes precedence for any field it covers), asks fresh for feature-specific fields the brain doesn't and shouldn't hold (problem framing, forward-looking success targets, keywords, packaging), labels every unmeasured target `[TARGET — not yet measured]` so it's never mistaken for sourced proof, builds a named-competitor comparison only when a competitor is explicitly given, and returns one markdown deliverable — Messaging Foundation, Story, Comparative Positioning (if built), Sales Enablement Kit, plus a "Still needed" list. Blocks and redirects to `positioning-messaging` or `product-marketing-context` if no usable positioning exists yet.
