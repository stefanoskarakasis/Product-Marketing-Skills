---
name: market-context
version: 1.0.0
description: >
  Builds the "why now" layer — market maturity, macro forces, buying
  triggers, narrative arc, and category moment — then deepens brain
  Section 5 in place. Trigger with "why now", "what's our market context",
  "define our category", "market narrative", "what macro trends support
  us", "buying triggers", or any request to define, update, or audit the
  market forces that make your positioning credible.
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-08-31
---

# Market Context

## How This Works

Positioning says what you are. Alternatives say what you beat. Market
context says why the world needed you right now — the layer that makes a
narrative land as inevitable instead of opportunistic. This skill builds
that narrative from macro forces and buying triggers, then deepens your
brain's existing Section 5 in place rather than creating a second market
file — one source of truth stays intact for every downstream skill.

**Step 0** — Load brain Section 5 (current market context, however thin),
Section 3 (alternatives, for narrative grounding), and any guardrails from
`/context/meta-patterns.md`.

**Step 1** — Establish category and maturity: what category the product
competes in (existing, emerging, or being created), and where that
category sits on the adoption curve.

**Step 2** — Surface macro forces and buying triggers: what external
shifts (regulatory, technological, economic, cultural) create demand for
this category right now, and what specific event moves a buyer from
passive awareness to active evaluation. Every force and trigger tagged
`[CONFIRMED]` / `[INFERRED]` / `[HYPOTHESIS]`.

**Step 3** — Build and stress-test the narrative arc: the single sentence
connecting macro force → buyer consequence → why the old approach breaks
→ why now. Run the specificity and buyer-connection checks before it
ships.

**Step 4** — Deepen brain Section 5 with the narrative (on user
confirmation).

**Step 5** — Learning Close: log the session to `/context/skill-sessions.md`.

---

## Trigger

- **When:** Defining or sharpening the market narrative — why this
  category, why this moment, what forces make the solution feel
  inevitable rather than opportunistic.

- **Not for:** Positioning statement or messaging hierarchy itself → use
  `positioning-messaging`. Competitive alternatives mapping → that's
  brain Section 3, handled within `product-marketing-context` or this
  skill's own Step 0 load, not rebuilt here. Full ICP or buying-committee
  work → `ideal-customer-profile` or `buyer-personas`.

- **Example prompts:**
  - "Why now for this launch?"
  - "What's our market context?"
  - "Define our category — are we creating one or fighting in one?"
  - "What macro trends support us right now?"
  - "Audit our market narrative — does it still hold?"

---

## Inputs

- **Args:** None required — the skill asks one question at a time if
  nothing is on file. Analyst reports, customer interview notes, or a
  pasted market description speed this up but aren't required.
- **Defaults:** No brain, or Section 5 still empty → run full BUILD.
  Section 5 populated → load silently, offer [View current] [Update]
  [Audit narrative durability].
- **Context keys:**
  - `/foundation/brain.md` — read Sections 3 and 5 if present; written to
    (Section 5 only) after explicit user confirmation of the exact
    before/after.
  - `/context/meta-patterns.md` — guardrails, read at Step 0.

---

## Pre-flight

- Check `/foundation/brain.md` Section 5 — if populated, this is an
  UPDATE or AUDIT, not a fresh BUILD.
- If `/foundation/brain.md` doesn't exist at all, surface once: "No brain
  found. You can still run this skill, but output will be less precise.
  Run product-marketing-context first for sharper results. Continuing."
  No hard block.

---

## Steps

**Step 1 — Category and maturity.**
Ask what category the product competes in — existing, emerging, or being
created. Push for specificity: "project management" and "async work
coordination for distributed teams" are different answers with different
GTM implications. Then place it on the adoption curve: Nascent, Early
Growth, Growth, Mature, or Declining — each stage implies a different
motion (educate first vs. differentiate vs. win on execution).

**Step 2 — Macro forces and buying triggers.**
For each macro force, capture: what's specifically changing (not "AI is
changing everything" — generic forces get rejected), who feels it most,
what it makes buyers do differently, and how long it's been building.
Distinguish forces (the conditions) from triggers (the moment a buyer
acts): compliance deadlines, scale thresholds, incidents, leadership
change, competitive pressure, budget cycles. Tag every claim
`[CONFIRMED]` (direct source — a quote, a filing, a transcript),
`[INFERRED]` (a pattern with no direct confirmation), or `[HYPOTHESIS]`
(a plausible force with no supporting evidence yet).

**Step 3 — Narrative arc and category moment.**
Build the arc: "[Market force] has caused [specific change in buyer's
world]. This means [buyer consequence]. The old approach [what they used
to do] no longer works because [why]. [Product] was built for this moment
because [connection to the force]." Name the category moment: creation
(lead with problem, educate first), redefinition (challenge the dominant
frame), or differentiation (lead with the gap from brain Section 3).
Exit check — the arc must pass all three:
- Specificity: every force names who feels it and what changed, not a
  category-level generality
- Coherence: force → trigger → consequence → solution holds as one chain;
  break any link and it collapses in a sales conversation
- Durability: rate `durable` / `at-risk` / `short-window` and set a
  review date — a narrative that expires silently is worse than one that
  was never built

**Step 4 — Deepen brain Section 5 on confirmation.**
Show the user the exact before/after for Section 5 before writing
anything. On confirmation, write:

```markdown
## Section 5: Market Context

**Market Maturity:**
{{stage}} — {{one-line GTM implication}}

**Macro Forces Making Our Solution Relevant:**
{{numbered list, each tagged CONFIRMED/INFERRED/HYPOTHESIS}}

**Why Now:**
{{buying triggers — trigger type, who feels it, urgency window}}

**Market Narrative (The bigger story):**
{{the full arc sentence, plus category moment named, plus durability
rating and review date}}
```

Never write silently — this is a shared source of truth every downstream
skill reads.

**Step 5 — Learning Close.**
Append a row to `/context/skill-sessions.md`:

```yaml
skill: market-context
session_date: {{date}}
pattern: "{{what surprised you, what the tagging discipline caught, or
  'none' if nothing notable happened — never skip the row}}"
source: {{surprised/wrong/missing/n.v.t.}}
```

---

## Outputs

- Brain Section 5 deepened in place (on confirmation only)
- A stated narrative arc, category moment, and durability rating — not
  buried in prose
- Session logged to `/context/skill-sessions.md`
- **External side effects:** n.v.t.
- **Next skill:** check `next-skill-map.md` for "After market-context"
  and surface that prompt.

---

## Verification

- Every macro force names who feels it and what specifically changed —
  no generic entries survive to Section 5
- Narrative arc is one coherent chain — force → trigger → consequence →
  solution — not four disconnected claims
- Category moment explicitly named, not implied
- Durability rated and a review date set
- Brain Section 5 write shown to the user before it happens, written only
  on confirmation
- Session logged with all four fields, `pattern: none` written explicitly
  if nothing notable happened — the row is never skipped

---

## Do Not Use For

- **positioning-messaging** — when the task is producing the positioning
  statement or messaging hierarchy itself, not the market narrative that
  grounds it. Run this skill first if Section 5 is thin, then that one.

- **product-marketing-context** — when the task is the full brain build
  from zero, or any section other than 5

- **ideal-customer-profile** — when the task is who buys, not why now

- **buyer-personas** — when the task is mapping the buying committee, not
  the external market forces around the deal

---

## Operating Rules

1. **Load brain Section 5 first.** Don't re-ask what's already answered.
2. **Never write to Section 5 without showing the exact before/after
   first.** No silent writes, ever.
3. **Reject generic macro forces.** "Digital transformation" fails the
   specificity test; a named regulation with a named affected buyer
   passes.
4. **Every force needs a buyer connection.** A macro force with no
   traceable buyer consequence is background noise, not narrative
   material — cut it.
5. **Tag every claim.** CONFIRMED / INFERRED / HYPOTHESIS, inline, never
   buried in prose.
6. **Rate durability and set a review date.** An undated narrative is a
   narrative nobody will remember to revisit.

---

## Quality Gate

| Check | Standard | Pass = |
|---|---|---|
| Category and maturity stated | Specific category, adoption-curve stage named | Yes |
| Macro forces specific | Each names who feels it + what changed | Yes |
| Narrative arc coherent | Force → trigger → consequence → solution holds | Yes |
| Category moment named | Creation / redefinition / differentiation stated | Yes |
| Durability rated | durable / at-risk / short-window + review date | Yes |
| Confirmation before write | Exact before/after shown, user confirmed | Yes |
| Learning Close complete | Four-field row appended, never skipped | Yes |

---

## Commands

### /build
Run full BUILD: category, maturity, macro forces, buying triggers,
narrative arc, category moment, durability rating.

### /update
Refresh Section 5 after a macro shift, category move, or new buying
trigger — asks only for what changed.

### /audit
Test whether the current narrative arc still holds. Re-check each macro
force (accelerating / stalled / reversed), re-check buying triggers, and
deliver one verdict: `HOLD` (update review date only), `REVISE` (rewrite
affected sections), or `REBUILD` (run full BUILD again — market has moved
materially).
