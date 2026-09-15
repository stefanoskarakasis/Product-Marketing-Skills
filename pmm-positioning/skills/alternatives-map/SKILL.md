---
name: alternatives-map
version: 2.0.0
description: >
  Synthesizes research data — win/loss notes, sales call transcripts,
  G2/Capterra reviews, analyst reports — into a named alternatives map
  across four buyer-real types (direct competitors, adjacent tools, DIY,
  and status quo), each with why-chosen, why-left, and unclaimed
  territory, then deepens brain Section 3 in place. Trigger with "map our
  alternatives", "who do we actually compete with", "status quo
  analysis", "our alternatives section is just a competitor list", or any
  request to identify, evidence, or sharpen who buyers compare you to.
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-09-15
---

# Alternatives Map

## How This Works

Buyers don't evaluate products in isolation — they evaluate against what
they're already doing or could do instead. Most teams map only their
direct competitors and miss the alternative that actually wins the most
deals: the status quo. This skill builds the map from evidence — win/loss
notes, sales call transcripts, review-site quotes, analyst reports — across
all four types a buyer actually considers, not just named vendors, and
deepens your brain's existing Section 3 in place. `positioning-messaging`
and `positioning-ideas` both hard-block without it — this is the single
source of truth both read.

**Step 0** — Load brain Section 3 (current alternatives, however thin) and
any guardrails from `/context/meta-patterns.md`.

**Step 1** — Gather and name across all four alternative types: direct
competitors, adjacent tools, DIY/internal build, and status quo. Status
quo is never optional — in most B2B markets it beats every named
competitor combined.

**Step 2** — Map each alternative across three layers: why buyers choose
it, why buyers leave it, and the unclaimed territory that leaves open.
Status quo gets a fourth: the real reason for inaction, distinct from the
stated one.

**Step 3** — Deepen brain Section 3 with the map (on user confirmation).

**Step 4** — Learning Close: log the session to `/context/skill-sessions.md`.

---

## Trigger

- **When:** Defining or sharpening who buyers actually compare you to from
  research data — win/loss notes, sales call transcripts, G2/Capterra
  reviews, analyst reports, competitor sites — or when brain Section 3 has
  fewer than 3 named alternatives, no status quo, or generic
  "competitors" instead of named products.
- **Not for:** Turning a confirmed alternatives map into positioning
  options or copy → `positioning-ideas` (divergent options) or
  `positioning-messaging` (shippable copy), run after. Full brain build
  from zero → `product-marketing-context`, run first if no brain exists
  at all.
- **Example prompts:**
  - "Map our alternatives from these 6 win/loss notes"
  - "Here are 10 sales call transcripts — who do we actually compete with"
  - "Our alternatives section just says 'legacy tools and spreadsheets'"
  - "Build the competitive map before we run positioning"

---

## Inputs

- **Args:** Research data — win/loss notes, sales call transcripts,
  G2/Capterra/TrustRadius reviews, analyst reports, competitor
  positioning pages, support tickets mentioning switches. If none is
  provided, ask for it; this skill synthesizes evidence, it doesn't
  generate a map from assumption alone.
- **Defaults:** If brain Section 3 already has named alternatives but no
  why-they-leave or unclaimed-territory layer, treat this as additive —
  map the missing layers, don't re-litigate a settled alternative list.
- **Context keys:**
  - `/foundation/brain.md` — required. Section 3 (Alternatives &
    Positioning).
  - `/context/meta-patterns.md` — optional; guardrails from prior
    sessions.
  - **Brain contract:** Reads Section 3. Writes Section 3 only — named
    alternatives across all four types, status quo, why-they-leave, and
    unclaimed territory, appended on explicit confirmation. Never
    creates a separate competitive file.

---

## Pre-flight

- Load `/foundation/brain.md` Section 3 if it exists.
- Load `/context/meta-patterns.md` if present; surface any guardrail
  fired 2+ times in prior alternatives-mapping sessions.
- **Hard block:** brain entirely absent → stop, direct to
  `product-marketing-context` first. A thin Section 3 is not a block —
  that's what this skill exists to fix.
- **Soft block:** no research data provided and none referenced from
  brain → ask for it before mapping. A map built on assumption alone
  should say so explicitly, not pass as evidence-based.

---

## Steps

### Step 0 — Load Context

Load brain Section 3 as it exists and any fired guardrails.

**Gate check:** brain absent → surface: *"Brain not found. Run
`product-marketing-context` first — even a thin Section 3 gives this
skill something real to build on."*

### Step 1 — Gather Across All Four Alternative Types

Ask what research is available if not already provided:
> "What do you have to work with? Win/loss notes, sales call
> transcripts, G2 or Capterra reviews, analyst reports, competitor
> pages — any of these work, and more than one is better."

Name real alternatives across all four types a buyer actually considers
— never just named vendors:

| Type | What it is | The trap if skipped |
|---|---|---|
| Direct competitors | Vendors selling the same solution | Gets all the attention, wins fewer deals than teams assume |
| Adjacent tools | Not built for this job but used anyway (spreadsheets, Slack, an ERP module) | Invisible in category pages, wins constantly because it's already paid for |
| DIY / internal build | Buyer builds it or assigns it internally | Rarely mapped because it doesn't feel like a competitor — it is one |
| Status quo / do nothing | Buyer changes nothing | Wins the majority of B2B deals in most markets — never optional |

Reject category placeholders. "Legacy tools" is not an alternative.
"Excel" or "Salesforce" is. State the named alternatives across whichever
types apply before moving to Step 2 — not every deal has a DIY option,
but status quo is always present.

### Step 2 — Map Each Alternative Across Its Layers

Every claim traces to a source. Mark anything without one `[A]`
(assumption) — same convention `ideal-customer-profile` uses. A map that
hides its assumptions behind confident prose is more dangerous than one
that states them.

**For direct competitors, adjacent tools, and DIY:**
- **Why chosen** — the real reason a deal goes here: price, incumbency, a
  specific capability, risk aversion, existing contract.
- **Why left** — the actual friction that opens a deal: a limitation,
  cost growth, support failure, missing capability — pulled from
  lost-deal or churn language, not guessed.
- **Unclaimed territory** — the specific gap this alternative leaves
  open, stated as a sentence a positioning skill could act on directly.
  Test it: could any other alternative in the map make the same claim
  with equal credibility? If yes, it isn't a gap yet — narrow it.

**For status quo — four required elements, none optional:**
1. **What they do today, named specifically** — not "manual process."
   "Tracking deals in a shared spreadsheet, reconciled every Friday."
2. **Cost of inaction** — quantified where possible (time, money,
   error rate). Unquantified → flag `[NEEDS PROOF]`.
3. **Real reason for inaction** — distinct from the stated reason.
   Stated: "no budget." Real: "the buyer doesn't believe the ROI is
   worth the implementation risk." These need different responses.
4. **Trigger to act** — the specific event that moves the buyer from
   inaction to evaluation.

**Exit check — the Named-Not-Abstract Test:** could a salesperson read
this map and know exactly which two products a real prospect is actually
choosing between, and why?

> "[Prospect type] chooses between [us] and [named alternative] because
> [reason], and leaves [named alternative] because [friction]."

If any alternative can't fill that sentence with a real name and a
sourced reason, it's still a category placeholder. Return to Step 1
before Step 3.

### Step 3 — Deepen Brain Section 3 (on Confirmation)

Show the exact addition before writing:
> "Adding to brain Section 3 — Named Alternatives across all four types,
> Status Quo, Why They Leave, and Unclaimed Territory, built from
> [source data]. Existing content stays unchanged. Here's what I'll
> append: [show exact text]. Save this?"

Append to `/foundation/brain.md` Section 3 — do not replace existing
content, do not create a separate file:

```markdown
## Section 3: Alternatives & Positioning
[existing content unchanged]

### Alternatives Map (added via alternatives-map, [date])
**Source:** [win/loss / call transcripts / reviews / analyst — n=X if known]

**Direct Competitors:**
1. [Alternative] — chosen because [reason]; left because [friction];
   unclaimed territory: [gap]

**Adjacent Tools:**
1. [Alternative] — chosen because [reason]; left because [friction];
   unclaimed territory: [gap]

**DIY / Internal Build:** [n.v.t. if not present in this deal cycle]

**Status Quo:** [what buyers do if they buy nothing], named specifically
- Cost of inaction: [quantified or `[NEEDS PROOF]`]
- Real reason for inaction: [not the stated reason]
- Trigger to act: [specific event]

### Named-Not-Abstract Statement
[Prospect type] chooses between [us] and [top alternative] because
[reason], and leaves [top alternative] because [friction].
```

Never write without this explicit confirmation.

### Step 4 — Learning Close

Append one entry to `/context/skill-sessions.md`, in the format defined in
`product-marketing-context/.claude-plugin/skill-sessions-format.md`
(Type A — execution session):

````yaml
type: execution
skill: alternatives-map
session_date: [YYYY-MM-DD]
pattern: [one falsifiable statement about this session, or "none"]
source: [surprised / wrong / missing / n.v.t.]
````

Write directly, no permission needed — separate from the brain write
above, which still requires explicit confirmation.

---

## Outputs

- **Files written:** `/foundation/brain.md` Section 3 — appended
  alternatives across all four types (with why-chosen, why-left,
  unclaimed territory), Status Quo's four required elements, and the
  Named-Not-Abstract Statement (Step 3), only after explicit
  confirmation. `/context/skill-sessions.md` — one appended row per
  session (Step 4).
- **Chat output format:** Source and named alternatives stated by type →
  layered map per alternative → Named-Not-Abstract Statement →
  confirmation prompt for the brain write.
- **External side effects:** n.v.t.
- **Next skill:** After brain Section 3 is deepened, check
  `product-marketing-context/.claude-plugin/next-skill-map.md` for "After
  alternatives-map" and surface that prompt. Do not auto-run — ask.

---

## Verification

- All four alternative types considered — status quo always present,
  DIY marked `n.v.t.` explicitly if genuinely absent, never silently
  skipped.
- Named alternatives, not generic categories.
- Status quo has all four required elements: named specifically,
  quantified cost, real (not stated) reason, and a trigger.
- Every claim without a cited source flagged `[A]`.
- Named-Not-Abstract Test passed before the brain write is proposed.
- Brain Section 3 write shown to the user and confirmed before it
  happens.
- Existing Section 3 content preserved, not overwritten.
- Session logged to `/context/skill-sessions.md`.

---

## Operating Rules

- **Deepen brain Section 3 — never fork a second competitive file.**
  `positioning-messaging` and `positioning-ideas` both expect Section 3
  to be the alternatives source of truth.
- **Status quo is never optional.** In most B2B markets it beats every
  named competitor combined — skipping it is the single most common
  and most expensive mapping mistake.
- **Evidence over assertion.** Every claim without a cited source gets
  `[A]` and lowers confidence in the result.
- **Named alternatives, not categories.** "Legacy tools" or "manual
  process" is a placeholder, not a mapped alternative — status quo is
  the one exception, and even it gets named specifically (which tool,
  which process).
- **Unclaimed territory must survive the "any alternative could say
  this" test.** If another alternative could claim it with equal
  credibility, it isn't a gap yet.
- **Never overwrite existing Section 3 content.** Append; don't replace
  unless the user explicitly asks to revise a settled alternative.
- **Brain write requires explicit confirmation. Never append silently.**

---

## Quality Gate

| Check | Standard | Pass = |
|---|---|---|
| All four types considered | Status quo present; DIY marked n.v.t. if absent, not skipped | Yes |
| Named alternatives, not categories | Real products/tools named, status quo specific | Yes |
| Status quo's four elements complete | Named, quantified cost, real reason, trigger | Yes |
| Assumption flags visible | Every unsourced claim marked `[A]` | Yes |
| Gap survives the equal-credibility test | No other mapped alternative could claim the same gap | Yes |
| Named-Not-Abstract Test passed | Compresses to a real two-product qualifying sentence | Yes |
| Existing content preserved | Prior Section 3 content untouched unless explicitly revised | Yes |
| Brain write confirmed | Exact addition shown and confirmed before writing | Yes |
| Learning Close ran | `/context/skill-sessions.md` has a new row | Yes |

---

## Do Not Use For

- **`product-marketing-context`** — full brain build from zero, or any
  section other than Section 3.
- **`positioning-ideas`** — generating divergent positioning options once
  alternatives are mapped; run this skill first for real inputs.
- **`positioning-messaging`** — turning a confirmed alternatives map into
  a positioning statement or messaging hierarchy; run this skill first,
  then that one.
- n.v.t.
