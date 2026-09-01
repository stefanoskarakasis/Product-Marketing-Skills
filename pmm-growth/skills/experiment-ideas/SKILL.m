---
name: experiment-ideas
version: 1.0.0
description: >
  Generates several concrete, cost-efficient growth ideas — each with a
  channel, core message, and cost-efficiency rationale — grounded in
  brain ICP, alternatives, and market context. Trigger with "give me
  marketing ideas", "brainstorm growth tactics", "what should we try",
  "cheap ways to promote this", or any request to generate raw campaign
  or channel ideas before committing to one to test.
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-09-01
---

# Experiment Ideas

## How This Works

Most idea-brainstorm output is five generic tactics that could belong to
any company — "post more on LinkedIn," "run a referral program." This
skill grounds ideation in what's actually known: who the ICP is, what
alternatives buyers compare against, and why now matters, so every idea
is specific enough to differentiate from what a status-quo competitor is
already doing. It doesn't write anything durable — generated ideas are
disposable brainstorm output, not a company fact — and it hands off
explicitly to `experiment-doc` (pmm-execution), which is where a chosen
idea gets pressure-tested before it becomes a real test.

**Step 0** — Load brain Sections 1 (Product), 2 (ICP), 3 (Alternatives),
5 (Market Context) if present, and guardrails from
`/context/meta-patterns.md`.

**Step 1** — Clarify constraints: budget or resource ceiling, channels
already tried (and what happened), how many ideas wanted (default 5).

**Step 2** — Generate ideas: each with Channel, Core Message, Why It
Works (tied to ICP or market energy state when brain data exists), Cost
Efficiency.

**Step 3** — Self-check each idea against the ICP and named alternatives
— an idea indistinguishable from what a status-quo competitor already
does gets flagged, not silently kept.

**Step 4** — Rank by effort-vs-impact, not generation order.

**Step 5** — Learning Close: log the session to `/context/skill-sessions.md`.

---

## Trigger

- **When:** Brainstorming marketing or growth ideas, looking for
  low-budget/high-impact tactics, exploring channels before committing
  budget, or any "what should we try" moment before a specific hypothesis
  exists.

- **Not for:** Pressure-testing a single idea you've already picked
  → `experiment-doc` (pmm-execution), run this skill first only if you
  don't yet have a specific hypothesis to test. Rewriting an already-set
  positioning into segment-specific value-prop copy → `value-prop-statements`
  (pmm-growth), run this skill first only if you need raw campaign ideas,
  not copy variants of an existing statement. A full campaign brief with
  calendar, audience, and metrics → `gaccs-brief`. Channel or motion
  selection for a launch already scoped against ICP deal economics
  → `gtm-motions`. Writing the actual positioning statement or messaging
  hierarchy → `positioning-messaging`.

- **Example prompts:**
  - "Give me 5 marketing ideas for this launch"
  - "What are some cheap ways to get in front of our ICP?"
  - "Brainstorm growth tactics for Q4"
  - "We have almost no budget — what should we try?"
  - "Creative campaign ideas for [product]"

---

## Inputs

- **Args:** Number of ideas wanted (default 5), budget or resource
  ceiling, channels already tried and what happened.
- **Defaults:** No brain → ask directly for product, target segment, and
  constraints before generating. Brain exists → load silently, ask only
  for constraints not already on file.
- **Context keys:**
  - `/foundation/brain.md` — read Sections 1, 2, 3, 5 if present. Never
    written to — this skill produces no durable brain output.
  - `/context/meta-patterns.md` — guardrails, read at Step 0.

---

## Pre-flight

- Load `/foundation/brain.md` if it exists — Sections 1, 2, 3, 5,
  silently.
- If `/context/meta-patterns.md` exists and a weak-idea pattern has fired
  2+ times in prior sessions logged there (e.g., ideas keep skipping the
  cost-efficiency rationale, or keep repeating the same channel), surface
  it once before Step 2.
- If no brain found: surface once, non-blocking — "No brain found. I can
  still generate ideas from what you tell me directly, but they'll be
  more generic without ICP and alternatives context. Continuing."

---

## Steps

**Step 1 — Clarify constraints.**
Ask in one message: budget or resource ceiling (if any), which channels
have already been tried and what happened, how many ideas wanted
(default 5 if not specified). If brain Sections 1–3 are populated, skip
re-asking product/ICP/alternatives — state what's loaded instead.

**Step 2 — Generate ideas.**
For each idea, produce all four fields:
- **Channel** — the primary marketing channel (social, content,
  partnerships, community, email, product-led, etc.)
- **Core Message** — the actual message, in language the ICP would
  recognize, not a category-level description
- **Why It Works** — tied to a specific ICP trait, market energy state
  (if brain Section 5 loaded), or named alternative's weakness — not a
  generic engagement claim
- **Cost Efficiency** — a concrete reason the tactic is cheap or
  resource-light for this specific team's constraints, not an assertion
  ("low cost because it's organic" is not concrete; "no paid spend, ~3
  hours/week from one person, reuses existing customer interview
  transcripts" is)

Ideas must be differentiated from each other — five variations on the
same channel fail this step and get regenerated.

**Step 3 — Self-check against ICP and alternatives.**
For each idea, ask: would a buyer who already uses [named alternative]
find this message meaningfully different from what that alternative
already says? An idea that fails this test is flagged
`[GENERIC — doesn't differentiate from status quo]` rather than silently
delivered as-is.

**Step 4 — Rank by effort vs. impact.**
Order the final list by realistic effort-to-impact ratio for this team's
stated constraints, not by generation order. State the ranking rationale
in one line per idea.

**Step 5 — Learning Close.**
Append a row to `/context/skill-sessions.md`:

```yaml
skill: experiment-ideas
session_date: {{date}}
pattern: "{{what surprised you, a recurring weak-idea pattern, or 'none'
  if nothing notable happened — never skip the row}}"
source: {{surprised/wrong/missing/n.v.t.}}
```

State explicitly which idea(s), if any, look strong enough to send to
`experiment-doc` for real pressure-testing — this skill's output is a
starting list, not a validated plan.

---

## Outputs

- A ranked list of ideas (Channel / Core Message / Why It Works / Cost
  Efficiency each), delivered in chat only — this skill writes no output
  file of its own
- Session logged to `/context/skill-sessions.md`
- An explicit handoff line naming which idea(s) are strong candidates for
  `experiment-doc`
- **External side effects:** n.v.t.
- **Next skill:** check `next-skill-map.md` for "After experiment-ideas"
  and surface that prompt.

---

## Verification

- Every idea has all four required fields, none left implicit
- No two ideas share a channel with substantively the same message
- Every Cost Efficiency claim names a specific reason, not an assertion
- Every idea has passed or been flagged by the alternatives self-check
- Final list is ranked by effort-vs-impact, not left in generation order
- Session logged with all four fields, `pattern: none` written explicitly
  if nothing notable happened — the row is never skipped

---

## Do Not Use For

- **experiment-doc** (pmm-execution) — when the task is pressure-testing
  one specific idea with ICE scoring and statistical rigor, not
  generating the raw list it draws from. Run this skill first only if no
  specific hypothesis exists yet.

- **value-prop-statements** (pmm-growth) — when the task is rewriting an
  already-set positioning statement into segment- or channel-specific
  copy variants, not generating new raw campaign concepts.

- **gaccs-brief** — when the task is a full campaign brief with calendar,
  audience detail, and success metrics, not a raw idea list

- **gtm-motions** — when the task is selecting the channel/motion stack
  for a launch already scoped against ICP deal economics, not
  brainstorming ideas pre-scope

- **positioning-messaging** — when the task is writing the actual
  positioning statement or messaging hierarchy itself, not generating
  campaign concepts

---

## Operating Rules

1. **Load brain first.** Don't re-ask what Sections 1–3 already answer.
2. **Never deliver a generic idea unflagged.** If it fails the
   alternatives self-check, mark it — don't quietly include it as if it
   passed.
3. **Every idea needs all four fields.** A channel with no concrete
   cost-efficiency reason isn't a finished idea.
4. **Rank before delivering.** Generation order is not a prioritization.
5. **Write nothing to the brain.** Ideas are disposable; only a
   pressure-tested experiment (via `experiment-doc`) earns durability.
6. **Name the handoff explicitly.** Don't leave "what's next" implicit —
   state which idea(s) are strong enough for `experiment-doc`.

---

## Quality Gate

| Check | Standard | Pass = |
|---|---|---|
| All fields present | Channel, Core Message, Why It Works, Cost Efficiency for every idea | Yes |
| Ideas differentiated | No two ideas share channel + substantively same message | Yes |
| Cost efficiency concrete | Each claim names a specific reason, not an assertion | Yes |
| Alternatives self-check run | Every idea checked; generic ones flagged, not hidden | Yes |
| Ranked by effort/impact | Final order isn't generation order | Yes |
| Handoff stated | Explicit line naming candidate(s) for experiment-doc | Yes |
| Learning Close complete | Four-field row appended, never skipped | Yes |

---

## Commands

### /brainstorm [product or context]
Run full flow: constraints → generate → self-check → rank → handoff.

### /more
Generate additional ideas beyond the initial set, using the same
constraints and brain context already established this session.
