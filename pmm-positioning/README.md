# pmm-positioning

Positioning and messaging for GTM — unique value clarity, buyer resonance, owned differentiation. Integrates with product-marketing-context brain.

## Skills (1)

- **positioning-messaging** — Build positioning statements, messaging hierarchies, and sales enablement from buyer context, alternatives map, and market narrative.

## Commands (5)

- `/pmm-positioning:build` — Build a positioning statement and messaging hierarchy from ICP + alternatives + market context.
- `/pmm-positioning:audit` — Score existing positioning on clarity, uniqueness, resonance, and messaging alignment.
- `/pmm-positioning:personas` — Generate buyer persona cards showing positioning resonance and objection handles.
- `/pmm-positioning:battlecard` — Create competitive response guide for top 3 alternatives.
- `/pmm-positioning:sales-pitch` — Generate 30-second elevator pitch + key differentiators for sales reps.

## How It Works

**Step 1: Load Context**
Reads brain sections (ICP, alternatives, market context) before positioning runs. Pre-flight validates all required sections exist.

**Step 2: Score Against Rubric**
Positioning scored on: clarity (20), uniqueness (20), resonance (15), messaging alignment (15), tier validation (10). Owned angles vs. alternatives count most.

**Step 3: Validate Differentiation**
Confirms position owns unique angle vs. each named alternative. If generic vs. any competitor, flags for rewrite.

**Step 4: Update Brain**
Logs positioning + learnings to brain Section 5 (Positioning & Messaging) and Section 7 (Meta-Learnings).

**Step 5: Feed Forward**
Downstream skills (value-prop, battlecard, sales enablement) load what was just positioned. Next team member sees guardrails + prior learnings at pre-flight.

## What Gets Stored & Reused

- **positioning_statement** — One clear sentence. Why this buyer chooses us vs. alternatives.
- **target_buyer** — ICP segment + specific job-to-be-done.
- **unique_value_angle** — What we own that competitors don't.
- **differentiation_matrix** — How we differ from each named alternative.
- **messaging_hierarchy** — Primary message + 2-3 supporting pillars.
- **sales_pitch_30sec** — Reps memorize this in training.
- **learnings** — What worked, what didn't, patterns for next positioning.

## Quick Start

1. **Run product-marketing-context** first (builds brain with ICP + alternatives + market context).
2. **Run pmm-positioning** (reads brain, scores positioning, updates brain).
3. **Use downstream** — value-prop, messaging-brief, battlecard now load your positioning.

## Config Files

- `positioning-rubric.yml` — Scoring dimensions (clarity, uniqueness, resonance, alignment, tier).
- `alternatives-anchor.yml` — Validation rules for differentiation vs. named alternatives.
- `brain-sections.yml` — Dependencies on product-marketing-context brain (what we read/write).

## License

MIT
