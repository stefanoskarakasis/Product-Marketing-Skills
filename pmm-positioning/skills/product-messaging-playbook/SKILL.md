---
name: product-messaging-playbook
version: 1.0.0
description: >
  Assembles a single Sales/CS-ready Product Messaging Playbook for a new
  product or feature — problem, story, one named competitive comparison,
  and a sales enablement kit with discovery questions and objection
  handling. Use when you say "build a messaging playbook," "give sales
  something they can use for this feature," "handoff doc for sales and
  CS," or "solution guide for this launch." Assembles from message-house,
  positioning-messaging, and proof-points — does not derive strategy itself.
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-09-26
---

# Product Messaging Playbook

The document a PMM hands to Sales and CS so they can talk about a new
product or feature the same day it ships — not a strategy deck, not raw
brain output, but one assembled artifact: what the problem is, why the
product solves it, how it compares to the one alternative buyers actually
ask about, and exactly what to say (and not say) on a call. It doesn't
derive positioning, pillars, or proof — those already have owners
(`positioning-messaging`, `message-house`, `proof-points`). This skill
reads their output and the brain, asks only for what's genuinely new
(the problem framing and forward-looking targets for *this* feature), and
assembles the rest into one document a rep can open cold.

---

## Trigger

- **When:** A PMM needs a single Sales/CS-facing document for a specific
  product or feature — new or existing — that bundles the problem it
  solves, the pitch, one named competitive comparison, and a
  discovery/objection script, in a format non-PMMs can use without
  translation.
- **Not for:** Deriving the underlying positioning statement or messaging
  hierarchy → `positioning-messaging`, run first. Formatting general
  company-level positioning into a Roof + Pillars table with no
  feature-specific problem framing or sales script → `message-house`
  already does that; use this skill instead when the ask specifically
  includes discovery questions, objection handling, or a named-competitor
  comparison. Sourcing or auditing the proof points themselves →
  `proof-points`, run first if Section 6 is thin. Building a full
  multi-competitor battlecard, not a single named comparison scoped to
  one feature → that's a distinct, larger deliverable this repo does not
  yet have a dedicated skill for; this skill's Section 3 is intentionally
  scoped to one alternative, not a full battlecard.
- **Example prompts:**
  - "Build a messaging playbook for [feature]"
  - "Give sales something they can use for this launch"
  - "I need a handoff doc for sales and CS on [product]"
  - "Solution guide for [feature] vs [competitor]"
  - "Turn this into something a rep can read cold"

---

## Inputs

- **Args:** Product or feature name (required). Optionally: a pasted
  `message-house` output, a pasted `positioning-messaging` SALES-ENABLEMENT
  output, and/or the name of one competitor to build the comparative
  section against.
- **Defaults:** If no competitor is named, Section 3 (Comparative
  Positioning) is skipped rather than guessed — ask which alternative from
  brain Section 3 to compare against, or proceed without that section if
  the user declines.
- **Context keys:**
  - `/foundation/brain.md` — required. Sections 1 (Product), 2 (ICP), 3
    (Alternatives & Positioning), 5 (Market Context), 6 (Proof Points
    Registry).
  - **Brain contract:** Reads Sections 1, 2, 3, 5, 6. Writes: none. This
    skill is a read-only assembler, same contract as `message-house` — it
    never edits `/foundation/brain.md`.

---

## Connectors (Optional)

| Connector | What it adds |
|---|---|
| `~~call recordings` | Real objections and discovery questions from calls |
| `~~CRM` | The competitor named in lost deals |
| `~~support` | Customer pain-point language |

> **No connectors?** Paste the material and I'll work from that. The output has the same shape.
> Pulled facts are drafts: each is tagged with category, tool and date, and nothing is written until you confirm.

---

## Pre-flight

- Load `/foundation/brain.md` if present. If absent, check for a pasted
  `message-house` and/or `positioning-messaging` output this session.
- **Hard block:** both brain and pasted output are missing →
  *"No brain and no message-house/positioning-messaging output found. This
  skill assembles a playbook from existing positioning — it doesn't create
  one. Run `product-marketing-context` to build the brain, or
  `positioning-messaging` (BUILD mode) first, then come back."*
- **Soft block:** brain exists but Section 3 (Alternatives) is empty or a
  competitor was named that isn't in Section 3 → surface once, don't
  block: *"[Competitor] isn't in your alternatives map. I can still build
  Section 3 from what you tell me now, but consider running
  `alternatives-map` so this and future playbooks are grounded in real
  research, not a one-off."*
- **Soft block:** Section 6 (Proof Points) is empty or every relevant
  entry is still flagged → note once, non-blocking: *"Proof points
  registry is thin. Story and Sales Enablement sections will ship with
  flagged gaps instead of unsourced claims — run `proof-points` first for
  a fuller Story section, or continue now."*

---

## Steps

### Step 1 — Load Source Material

Pull brain Sections 1, 2, 3, 5, 6. If a `message-house` output was pasted
this session, prefer its Roof/Pillars fields over re-deriving them from
raw brain content. If a `positioning-messaging` SALES-ENABLEMENT output
was pasted, prefer its persona cards and competitive playbook over
building fresh from Section 2/3. Note any conflict between pasted output
and brain content to the user in one line.

### Step 2 — Feature-Specific Intake (never pulled from the brain)

Some fields are true every time this skill runs for a *different* feature
of the same product — the brain doesn't and shouldn't hold them, because
writing them there would make the brain describe one feature launch
instead of the durable company-level context every skill shares. Ask for
these directly, this session, and never infer them from Section 1's
company-level product description:

- **Problem:** what specific problem does *this* product/feature solve —
  not the company's problem, the feature's.
- **Experience today:** what happens if this problem goes unsolved.
- **Experience with the product (vision):** what changes once it's solved.
- **Success targets:** any forward-looking numbers this feature is
  expected to hit (e.g. adoption %, stickiness %, usage frequency).
  **These are targets, not proof points — label them explicitly as
  `[TARGET — not yet measured]` and never pass them to Step 5 as if they
  were sourced brain Section 6 evidence.** A target and a measured result
  are different claims with different evidentiary weight; conflating them
  is exactly the failure `proof-points` exists to prevent. Once the
  feature has shipped and these numbers are actually measured, that
  result becomes a genuine proof-points candidate — route it there in a
  future session, not this one.
- **Name of solution:** what this specific feature/product is called, if
  different from the Section 1 product name.
- **Keywords:** search/discovery terms specific to this feature. Ask;
  never invent SEO terms.
- **Products needed:** which plan/tier/product a customer needs to use
  this feature. Ask; brain Section 1 doesn't track packaging.

Any field the user can't answer ships as `[MISSING — <what's needed>]`,
same discipline as `message-house` Step 1 — never filled with
plausible-sounding copy.

### Step 3 — Assemble the Story Section

This is a deliberately compact subset of `message-house`'s full 11-field
Roof table, not a copy of it — a rep needs four things, not eleven. Reuse,
don't re-derive: pull each of the following from the pasted `message-house`
output if one exists; otherwise build it directly from brain Sections 1
and 3. This exact field set is the canonical Story shape — do not expand
it back toward the full Roof table, and do not drop a field:

1. **High-level pitch** — one sentence, why the buyer should care at all.
2. **Short description** — how it works, ≤25 words, one sentence (not a
   fragment).
3. **Core pillars** — up to 3, same cap `message-house` enforces. Each
   renders as `**Pillar name** — one-sentence explanation`, one bullet per
   pillar, never a run-on paragraph.
4. **Key features** — same bullet shape as pillars: `**Feature name** —
   one-sentence explanation`.
5. **Customer proof** — pulled only from brain Section 6 entries that are
   NOT flagged `[NEEDS PROOF]` or `[NEEDS APPROVAL]` — a flagged entry is
   not yet safe to hand to Sales. If no clean entries exist, this ships as
   `[MISSING — no approved proof points yet; run proof-points]`, not empty.

Apply `message-house`'s cell-formatting rules throughout: `•` bullets
only, never `-` or `*`; bolded names before the em dash; one idea per
line, never packed onto one visual line.

### Step 4 — Build the Comparative Positioning Section (if a competitor was named)

Skip this step entirely if no competitor was named in Pre-flight — do not
build a comparison against an unnamed or invented rival.

Pull the named competitor's entry from brain Section 3 (Alternatives).
Structure the comparison using the same high-level-pitch / short
description / detailed-pitch shape the Story section uses, scoped to just
this one alternative:

1. **High-level pitch:** why the buyer should care about this comparison
   specifically.
2. **What we do differently:** pulled from Section 3's stated
   differentiation for this alternative — not a generic "we're better"
   claim.
3. **Which force this addresses:** classify the differentiator using
   Alan Klement's 4 Forces of Progress (push of the current situation,
   pull of the new solution, anxiety about switching, habit/attachment to
   the status quo) — the same framework the source template referenced.
   State which force is strongest and why, in one sentence.
4. **Customer proof for this specific comparison:** pull only from Section
   6 entries that explicitly reference switching from this competitor, if
   any exist. If none, state plainly: *"No customers referencing a switch
   from [competitor] yet."* — never invent one, same rule the original
   template's own "Not yet" placeholder modeled.

### Step 5 — Build the Sales Enablement Kit

Three subsections, sourced — never freehand:

1. **Convey value:** 1–2 open lines a rep can use to introduce the
   problem, pulled from Step 2's Problem framing and brain Section 5
   (Market Context) "why now" if available.
2. **Assess need — discovery questions:** 4–6 questions that surface
   whether the prospect has this problem, pulled from the Problem/
   Experience-today framing in Step 2. If a `positioning-messaging`
   SALES-ENABLEMENT output was pasted, reuse its persona pain points
   directly rather than reinventing questions.
3. **Addressing objections:** pull directly from brain Section 6's
   Forbidden Claims list (what NOT to say and why) plus, if a
   SALES-ENABLEMENT output was pasted, its persona cards' pre-handled
   objections verbatim. If neither source exists, this subsection ships
   as `[MISSING — run positioning-messaging SALES-ENABLEMENT mode or
   proof-points Audit mode for sourced objection handling]` rather than
   invented objection scripts — a rep repeating a fabricated objection
   response is a worse outcome than a visibly incomplete section.

### Step 6 — Assemble & Deliver

Combine Sections 1 (Messaging Foundation), 2 (Story), 3 (Comparative
Positioning, if built), and 4 (Sales Enablement Kit) into one markdown
document with a table of contents at the top, matching the structure a
non-PMM (a rep, a CS lead) can navigate without translation. List every
`[MISSING]` and `[TARGET — not yet measured]` field together at the end
under "Still needed / not yet measurable" so nothing is silently buried
inside a section. Section headers get one functional emoji each, matching
repo convention: 📍 Messaging Foundation, 📖 Story, ⚔️ Comparative
Positioning, 🎯 Sales Enablement Kit, 📋 Still needed (omit if empty).

### Step 7 — Learning Close

Append one entry to `/context/skill-sessions.md`, in the canonical format
defined in `product-marketing-context/.claude-plugin/skill-sessions-format.md`
(Type A — execution session):

```yaml
type: execution
skill: product-messaging-playbook
session_date: [YYYY-MM-DD]
pattern: [one falsifiable statement about this session, or "none" — fold in
  what's useful: which sources were pasted vs. derived fresh, whether a
  comparative section was built, how many fields shipped MISSING/TARGET]
source: [surprised / wrong / missing / n.v.t.]
```

Written directly, no permission required — observational log, not content
approval.

---

## Outputs

- **Files written:** `/context/skill-sessions.md` — one appended entry
  per session (Step 7). No writes to `/foundation/brain.md` — this skill
  is read-only, same contract as `message-house`.
- **Chat output format:** A single markdown document — Messaging
  Foundation, Story, Comparative Positioning (if built), Sales Enablement
  Kit, then "Still needed / not yet measurable." Not fragmented across
  multiple messages.
- **External side effects:** n.v.t.
- **Next skill:** If Step 2's success targets are later measured, prompt
  the user to run `proof-points` (Add mode) to register the real result —
  do not auto-run. If the Sales Enablement Kit shipped with a `[MISSING]`
  objection-handling subsection, prompt `positioning-messaging`
  SALES-ENABLEMENT mode.

---

## Verification

- Every field in Messaging Foundation and Story is sourced (brain,
  pasted skill output, or explicit user statement this session) or
  explicitly flagged `[MISSING]` — no invented copy.
- Every success target from Step 2 is labeled `[TARGET — not yet
  measured]` and never presented as if it were sourced Section 6
  evidence.
- Comparative Positioning section exists only if a competitor was
  explicitly named — never built against an inferred or invented rival.
- Every Customer Proof / competitive-proof entry excludes anything
  flagged `[NEEDS PROOF]` or `[NEEDS APPROVAL]` in Section 6.
- Sales Enablement Kit's objection handling traces to Section 6 Forbidden
  Claims or a pasted SALES-ENABLEMENT output — never freehand.
- Output is one single deliverable, not fragmented.
- Session logged to `/context/skill-sessions.md` with `type: execution`.

---

## Do Not Use For

- **positioning-messaging** — deriving the positioning statement,
  messaging hierarchy, or persona cards themselves. Run first if brain
  Section 3 is thin or no SALES-ENABLEMENT output exists yet.
- **message-house** — a general-purpose Roof + Pillars table with no
  feature-specific problem framing, competitive comparison, or sales
  script. Use that instead when the ask is just "format our positioning,"
  not "give sales a handoff document."
- **proof-points** — sourcing, verifying, or auditing a claim itself,
  or registering a measured result once a feature has shipped. Run first
  if Section 6 is thin; run again after launch to register real
  (not targeted) adoption/stickiness numbers.
- **alternatives-map** — mapping competitive alternatives (Section 3)
  from real research. Run first if the named competitor isn't in Section
  3 yet.
- n.v.t.

---

## Operating Rules

- **Never fabricate a field.** A field with no traceable source is
  `[MISSING]`, never a plausible guess — same discipline `message-house`
  and `proof-points` already enforce.
- **Targets are not proof points.** Forward-looking numbers for a feature
  that hasn't shipped are labeled `[TARGET — not yet measured]` and never
  presented, cited, or handed to Step 5 as if they were sourced Section 6
  evidence. Conflating a target with a measured claim is the exact
  failure mode `proof-points` was built to prevent.
- **This skill does not derive strategy.** If positioning, pillars, or
  proof points don't exist yet, redirect to the owning skill rather than
  inventing them here.
- **Read-only.** This skill never writes to `/foundation/brain.md`. It
  only reads, assembles, and reformats.
- **Comparative Positioning requires a named competitor.** No comparison
  is built against an inferred, assumed, or invented rival — skip the
  section instead.
- **Flagged Section 6 entries never ship as clean proof.** Anything
  marked `[NEEDS PROOF]` or `[NEEDS APPROVAL]` is excluded from Story and
  Sales Enablement content, not softened or paraphrased around.
- **Objection handling is sourced or absent, never invented.** A rep
  repeating a fabricated objection response is worse than a visibly
  incomplete section.
- **Single deliverable.** One document, not sections scattered across
  multiple chat messages.

---

## Quality Gate

| Check | Standard | Pass = |
|---|---|---|
| Source loaded | Brain and/or pasted skill outputs checked before assembling | Step 1 completed, sources noted |
| No fabricated fields | Every Messaging Foundation/Story field sourced or flagged `[MISSING]` | Zero invented copy |
| Targets labeled correctly | Every forward-looking number carries `[TARGET — not yet measured]`, never presented as Section 6 evidence | Zero conflated targets/proof |
| Comparative section gated | Section 3 built only when a competitor was explicitly named | Skipped when none named |
| Proof filtered | No `[NEEDS PROOF]`/`[NEEDS APPROVAL]` Section 6 entry ships as clean proof | Zero flagged entries in Story/Sales Enablement |
| Objection handling sourced | Traces to Section 6 Forbidden Claims or a pasted SALES-ENABLEMENT output | No freehand objection scripts |
| Missing-field list complete | "Still needed / not yet measurable" accounts for every flagged field | Counts match |
| Single deliverable | One document, four sections (or three if no competitor named) | Not fragmented |
| Learning Close logged | `/context/skill-sessions.md` has a new `type: execution` row for this session | Yes |

---

## Self-Improvement Loop

Each session logs to `/context/skill-sessions.md` in the canonical Type A
format (`type: execution`, `skill`, `session_date`, `pattern`, `source`)
defined in `product-marketing-context/.claude-plugin/skill-sessions-format.md`.
Which sources were pasted vs. derived fresh, whether a comparative section
was built, and how many fields shipped `[MISSING]` or `[TARGET]` live
inside the free-text `pattern` line, not as separate fields — shared
schema, not owned per-skill.

Monthly, `meta-synthesis` reads these logs for patterns such as: "Success
targets are requested in nearly every session but never followed up with
a proof-points Add-mode registration once launched → the post-launch
hand-back loop isn't actually closing" or "Comparative Positioning is
skipped more often than built → alternatives-map coverage is thinner than
assumed." Patterns feed brain-quality guardrails surfaced by
`product-marketing-context`, not this skill's own logic — this skill
stays an assembler.
