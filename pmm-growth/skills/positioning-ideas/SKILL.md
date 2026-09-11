---
name: positioning-ideas
version: 1.0.0
description: >
  Generates 3-5 real positioning angles anchored to your named
  alternatives — not five ways of saying "we're better," actual
  different territory to choose from before you commit to one. Use it
  before positioning-messaging, not instead of it: nothing here ships
  until your pick passes that skill's gate.
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-09-06
---

# Positioning Ideas

## How This Works

`positioning-messaging` BUILD mode produces one finished, gated
positioning statement — that's deliberate, since shipping copy needs a
7-point verification gate behind it. But choosing a direction in the
first place is a different job: before committing to one statement, it's
often more useful to see 3-5 genuinely different angles side by side,
each opening different unclaimed territory, and pick (or blend) one.
This skill exists for that moment only — divergent, ungated, disposable
brainstorm output. It writes nothing durable and produces no shippable
copy on its own. Every option it hands back must be run through
`positioning-messaging`'s BUILD mode and its gate before it becomes real
positioning copy — this skill explicitly does not replace that gate, it
feeds it.

**Step 0** — Load brain Section 1 (Product), Section 2 (ICP), and
Section 3 (Alternatives & Positioning) — hard-block if Section 3 has
fewer than 3 named alternatives including status quo, since divergent
positioning options are meaningless without knowing what's actually
being differentiated from.

**Step 1** — Confirm the target segment (from a recent `beachhead-segment`
or `buyer-personas` session if one exists, or ask directly).

**Step 2** — For each named alternative in Section 3, identify the
specific unclaimed territory it leaves open — the thing that alternative
structurally can't claim, not a generic "we're better" gap.

**Step 3** — Generate 3-5 divergent positioning statement options, each
tied to a different alternative's gap, each including a positioning
statement, strategic rationale, supporting message, and the specific
competitive advantage that makes the claim credible.

**Step 4** — Self-check for actual divergence — options that differ only
in wording but claim the same territory get collapsed or flagged, not
delivered as if they were distinct choices.

**Step 5** — Learning Close: log the session to `/context/skill-sessions.md`,
and hand off explicitly to `positioning-messaging` BUILD mode for
whichever option (or blend) gets chosen.

---

## Trigger

- **When:** Choosing a positioning direction before committing to one,
  wanting to see multiple angles side by side, exploring what unclaimed
  territory exists before writing a single finished statement.

- **Not for:** Producing a finished, gated, shippable positioning
  statement or full messaging hierarchy → `positioning-messaging`
  (pmm-positioning) — run this skill first only if a direction hasn't
  been chosen yet, then run that skill's BUILD mode on the winner.
  Auditing an existing live positioning statement → `positioning-messaging`
  AUDIT mode. Fanning an already-set positioning into segment/channel
  copy variants → `value-prop-statements` (pmm-growth). Raw campaign or
  channel ideas once positioning is already set → `experiment-ideas`
  (pmm-growth). Mapping the alternatives themselves before any
  positioning work → `hs-alternatives-map` / brain Section 3.

- **Example prompts:**
  - "Give me a few positioning angles to choose from"
  - "Brainstorm positioning ideas for [product]"
  - "How else could we position this?"
  - "What unclaimed territory is there before we commit to a statement?"
  - "Positioning options before we lock this in"

---

## Inputs

- **Args:** Target segment (if not pulled from a recent session), number
  of options wanted (default 5).
- **Defaults:** No brain, or Section 3 with fewer than 3 alternatives →
  hard block, direct to `hs-alternatives-map` first. Brain exists with
  3+ alternatives → load silently.
- **Context keys:**
  - `/foundation/brain.md` — read Sections 1, 2, 3. Never written to —
    this skill produces no durable brain output.
  - `/context/skill-sessions.md` — check for a recent `beachhead-segment`
    or `buyer-personas` session to pull a real segment instead of asking.

---

## Pre-flight

- Load `/foundation/brain.md` if it exists — Sections 1, 2, 3, silently.
- **Hard block** if brain doesn't exist or Section 3 has fewer than 3
  named alternatives including status quo: "Positioning options only
  mean something against real alternatives. Run `hs-alternatives-map`
  first to name at least 3, including status quo, then come back."
- If a recent `beachhead-segment` or `buyer-personas` session exists,
  offer its segment instead of asking from scratch.

---

## Steps

**Step 1 — Confirm the target segment.**
State which segment these options are for. Pull from a recent
`beachhead-segment`/`buyer-personas` session if one exists; otherwise
ask directly. Do not proceed on an unnamed or "everyone" segment.

**Step 2 — Map unclaimed territory per alternative.**
For each named alternative in brain Section 3, state the specific thing
it structurally can't claim — not "they're worse," but a concrete gap
(e.g., "Alternative X is built for enterprise IT buyers and can't credibly
claim self-serve simplicity without abandoning its own positioning").

**Step 3 — Generate 3-5 divergent options.**
Default 5 unless the user specifies otherwise. Each option includes:
- **Positioning Statement** — one sentence, following "the only
  [category] for [segment] who want [outcome]" shape or equivalent
- **Strategic Rationale** — why this resonates with the named segment
  specifically, tied to brain Section 2 (ICP)
- **Supporting Message** — the 1-2 messages that reinforce this angle
- **Competitive Advantage** — the specific capability that makes this
  claim credible, not aspirational

Options must open genuinely different territory from each other — not
five phrasings of the same claim.

**Step 4 — Self-check for real divergence.**
Compare every pair of options. If two options claim substantively the
same unclaimed territory, collapse them into one or flag the weaker as
`[REDUNDANT — same territory as Option N]` rather than presenting both
as if they were real alternatives.

**Step 5 — Learning Close.**
Append an entry to `/context/skill-sessions.md`, in the format defined in
`product-marketing-context/.claude-plugin/skill-sessions-format.md`
(Type A — execution session):

````yaml
type: execution
skill: positioning-ideas
session_date: {{date}}
pattern: "{{what surprised you, a recurring redundancy pattern, or
  'none' if nothing notable happened — never skip the row}}"
source: {{surprised/wrong/missing/n.v.t.}}
````

State explicitly which option (or blend) is strongest, and that the
next step is running it through `positioning-messaging` BUILD mode's
7-point gate before it becomes shippable copy — this skill's output is
not itself shippable.

---

## Outputs

- 3-5 divergent positioning statement options (Statement / Rationale /
  Supporting Message / Competitive Advantage each), delivered in chat
  only — this skill writes no output file of its own
- Session logged to `/context/skill-sessions.md`
- An explicit handoff line naming the strongest option(s) and stating
  they still require `positioning-messaging` BUILD mode's gate before
  use
- **External side effects:** n.v.t.
- **Next skill:** check `next-skill-map.md` for "After positioning-ideas"
  and surface that prompt.

---

## Verification

- Brain Section 3 had 3+ named alternatives including status quo before
  any option was generated — hard block enforced, not skipped
- Every option has all four required fields
- Every option is tied to a specific named alternative's gap, not a
  generic differentiation claim
- Redundancy self-check run across all option pairs; redundant options
  flagged or collapsed, not delivered as false choices
- Handoff explicitly states these are pre-gate options, not finished
  positioning copy
- Session logged with all four fields, `pattern: none` written explicitly
  if nothing notable happened — the row is never skipped

---

## Do Not Use For

- **positioning-messaging** (pmm-positioning) — when the task is
  producing one finished, verified, shippable positioning statement or
  full messaging hierarchy. This skill only produces pre-commitment
  options; every option still needs BUILD mode's 7-point gate before it
  ships as real copy.

- **value-prop-statements** (pmm-growth) — when the task is fanning an
  already-set, already-gated positioning into segment/channel copy
  variants, not generating divergent directions before one is chosen.

- **experiment-ideas** (pmm-growth) — when the task is raw campaign or
  channel ideas assuming positioning is already set, not positioning
  direction itself.

- **hs-alternatives-map** — when named alternatives don't exist yet at
  all. Run that first; this skill hard-blocks without it.

---

## Operating Rules

1. **Load alternatives first, hard block without 3+.** Divergent
   positioning is meaningless without a real competitive set to
   differentiate from.
2. **Every option ties to a specific alternative's gap.** A "we're just
   better" option isn't a real angle — reject it before it's delivered.
3. **Divergence is checked, not assumed.** Run the redundancy pass every
   time; don't deliver near-duplicates as if they were real choices.
4. **Never present this output as shippable.** State explicitly that the
   winning option still needs `positioning-messaging` BUILD mode's gate.
5. **Write nothing to the brain.** Options are disposable brainstorm
   output; only a gated, chosen positioning earns durability via
   `positioning-messaging`.
6. **Pull a real segment when available.** Check for a recent
   `beachhead-segment`/`buyer-personas` session before asking from
   scratch.

---

## Quality Gate

| Check | Standard | Pass = |
|---|---|---|
| Alternatives loaded, gate enforced | 3+ named alternatives incl. status quo confirmed before generation | Yes |
| All fields present | Statement, Rationale, Supporting Message, Competitive Advantage for every option | Yes |
| Tied to specific alternative | Each option names the specific gap it exploits, not a generic claim | Yes |
| Divergence self-check run | Every pair compared; redundant options flagged or collapsed | Yes |
| Handoff states pre-gate status | Explicit statement that BUILD mode's gate still applies | Yes |
| Learning Close complete | Four-field row appended, never skipped | Yes |

---

## Commands

### /positioning-options [segment]
Run full flow: confirm segment → map unclaimed territory → generate
options → divergence check → handoff.

### /more-angles
Generate additional options beyond the initial set, using the same
segment and alternatives context already established this session.
