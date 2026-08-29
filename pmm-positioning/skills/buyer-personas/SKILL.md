---
name: buyer-personas
version: 1.0.0
description: >
  Maps the enterprise buying committee — Economic Buyer, Champion, Technical
  Evaluator, End User, Procurement — before writing a single message, then
  builds Dunford-structured, alternatives-anchored personas ready for
  positioning-messaging. Trigger with "map our buying committee", "who do we
  need to win over", "build our buyer personas", "who kills our deals", or
  any request to identify or profile the people involved in a B2B purchase.
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-08-29
---

# Buyer Personas — Skill

## How This Works

Enterprise B2B purchases aren't made by personas — they're made by
committees. A messaging deck built for one buyer title routinely misses
the person who can actually kill the deal. This skill maps power first
(who approves, who champions, who can veto, who just uses the thing) and
only then builds messaging personas from that map — Dunford-structured,
anchored to named alternatives, ready to feed straight into
`positioning-messaging`.

It reads your brain's ICP and alternatives (Sections 2 and 3) instead of
starting cold, and it compounds the way every other skill in this repo
does — one row per session in `/context/skill-sessions.md` — not through a
separate knowledge or decisions system of its own.

**Step 0** — Load brain Sections 2 (ICP) and 3 (Alternatives), and any
guardrail from `/context/meta-patterns.md` fired 2+ times.

**Step 1** — Gather input: research data if provided, or run a structured
5-question intake if none exists.

**Step 2** — Map the committee: identify roles by behavior, not title, and
extract kill pattern / champion pattern / messaging gap for each.

**Step 3** — Build messaging personas: one card per role that needs
differentiated messaging, each anchored to named alternatives.

**Step 4** — Deliver both outputs, then hand off to `positioning-messaging`
with an explicit note on which persona is primary.

**Step 5** — Learning Close: log the session to `/context/skill-sessions.md`.

---

## Trigger

- **When:** Mapping who's actually involved in a B2B purchase decision, or
  building persona cards to feed into positioning and messaging work.
- **Not for:** Positioning statement or messaging hierarchy itself →
  `positioning-messaging`, run after this skill. Segment selection among
  multiple candidates → `beachhead-segment`. Deep ICP research
  (demographics/behaviors/JTBD/needs at the org level, not committee-level)
  → `ideal-customer-profile`, run before this skill if the ICP itself is
  still thin.
- **Example prompts:**
  - "Map our buying committee for enterprise deals"
  - "Who do we need to win over to close this?"
  - "Build persona cards for our sales enablement deck"
  - "Our deals keep stalling in legal — who's actually involved?"

---

## Inputs

- **Args:** Research data if available — call transcripts, CRM/deal
  history, win/loss notes, survey data. If none, this skill runs a
  5-question intake instead of guessing.
- **Defaults:** If brain has a confirmed beachhead or deepened ICP
  (Section 2), use it to ground role relevance and deal size assumptions
  rather than asking again.
- **Context keys:**
  - `/foundation/brain.md` — recommended. Section 2 (ICP), Section 3
    (Alternatives).
  - `/context/meta-patterns.md` — optional; guardrails from prior sessions.
  - **Brain contract:** Reads Sections 2, 3. Writes nothing to the brain —
    committee maps and persona cards are delivered in chat and handed to
    `positioning-messaging`, not stored as a brain fact. A buying
    committee shifts per deal and per segment; treating it as durable
    brain content would drift the brain every time a new deal looks
    different.

---

## Pre-flight

- Load `/foundation/brain.md` Sections 2, 3 if present.
- Load `/context/meta-patterns.md` if present; surface any guardrail fired
  2+ times in prior committee-mapping sessions.
- **No hard block on missing brain** — this skill can run cold with the
  5-question intake, same as `beachhead-segment`'s Quick-Brain fallback.
  A thin or absent brain is a reason to ask more questions up front, not
  a reason to stop.

---

## Steps

### Step 0 — Load Context

Load brain Sections 2–3 if they exist, and any fired guardrail from
`/context/meta-patterns.md`. State what's loaded in one line before
proceeding: *"Loaded ICP and alternatives from brain. No prior guardrails
fired."* — or the equivalent if either is missing.

### Step 1 — Gather Input

If research data is provided (transcripts, CRM signals, win/loss notes,
survey data), read all of it before drawing conclusions.

If nothing is provided, ask in one message — not one question at a time:
> "1. What does your product do, and who's the primary buyer title?
> 2. What's your typical deal size and sales-cycle length?
> 3. What does a lost deal usually look like — who said no, and why?
> 4. What does a won deal look like — who pushed it through internally?
> 5. Who else shows up during procurement or a security review?"

Don't proceed until at least questions 1, 3, and 4 are answered — a
committee map without knowing who kills and who champions deals is a org
chart, not a buying map.

### Step 2 — Map the Committee

Identify roles by behavior, not title — titles lie, behaviors don't.

| Role | Cares About | Signal |
|---|---|---|
| **Economic Buyer** | ROI, risk, vendor longevity | Asks about pricing tiers, contract terms, renewal conditions |
| **Champion** | Their own internal credibility | Shares your collateral internally, initiates intros unprompted |
| **Technical Evaluator / Blocker** | Integration, security, compliance, scale | Requests architecture docs, security questionnaires, SSO/SAML specs |
| **End User** | Daily workflow fit | Gap between user enthusiasm and champion enthusiasm often predicts post-sale churn |
| **Procurement / Legal** | Terms, liability | Deal stalls at "sent to legal" with no timeline |
| **Executive Sponsor** (enterprise only) | Top-level air cover | Appears on the signature block, rarely in evaluation |

Not every deal has every role — map what's actually present, don't force
all six onto a small deal.

For each role identified, extract or infer:
- **Kill pattern** — what unaddressed concern causes this role to block or delay?
- **Champion pattern** — what does this role need to see to advocate internally?
- **Messaging gap** — what does current collateral say vs. what this role actually needs?

Tag every claim: `[CONFIRMED]` (from provided data), `[INFERRED]`
(logical inference from signals, needs validation), or `[HYPOTHESIS]` (no
direct evidence — flag for testing). Never blend these into unqualified
prose; a reader should be able to tell confidence level at a glance.

**Quality gate — do not proceed to Step 3 if:**
- No Economic Buyer and no Champion could be identified at all
- Named alternatives are unknown for the primary persona
- Every signal is `[HYPOTHESIS]` — ask for more input first

### Step 3 — Build Messaging Personas

One card per committee member who needs differentiated messaging — not
every role gets a full card if the messaging genuinely doesn't differ.

```markdown
## [Role Name] Persona
Title range: [titles at relevant company size]
Input confidence: [CONFIRMED / INFERRED / HYPOTHESIS]

### Job to Be Done
[The outcome they're hired to produce — not their job description]

### Named Alternatives
[What they compare you to, or what they'd do if you didn't exist]
→ Dunford anchor. Do not skip. Flag [HYPOTHESIS] if unknown — if brain
Section 3 already has alternatives, use them instead of re-deriving.

### Pains (tied to named alternatives)
1. [Pain] → made worse by [alternative]
2. [Pain] → made worse by [alternative]
3. [Pain] → made worse by [alternative]

### Gains (what winning looks like for them personally)
1. [Gain] — how they measure it
2. [Gain] — how they measure it

### Trigger and Blockers
- **Shift:** what put them in-market at all?
- **Blocker:** what specific concern could kill the deal from their side?
- **Motivator:** what gives them confidence to move forward?

### Messaging Implication
[One paragraph brief for whoever builds the positioning/value prop]

### What Not to Say
[1–2 messages that consistently backfire with this persona]
```

**Exit check:** if you could paste a persona card onto a competitor's
page and it would still read as accurate, the alternatives anchor is too
generic — go back and name the real alternative, not the category.

### Step 4 — Deliver and Hand Off

Output both layers together:

```markdown
## Buying Committee Map — [Company/Segment]
Input sources: [what was analyzed, or "5-question intake"]

| Role | Likely Title(s) | Kill Pattern | Champion Pattern | Messaging Priority |
|---|---|---|---|---|
| Economic Buyer | | | | |
| Champion | | | | |
| Technical Evaluator | | | | |
| End User | | | | |
| Procurement | | | | |

### Deal Dynamics
- Who typically initiates the evaluation
- Who typically kills deals, and at what stage
- Power shift pattern between early and late stage
```

Followed by the persona cards from Step 3.

Before handing off, state explicitly:
> "Primary buyer for top-of-funnel messaging: [role]. [N] personas need
> separate landing pages or sales enablement content: [list]. Still
> `[HYPOTHESIS]`, don't let these drive final copy yet: [list, or 'none']."

### Step 5 — Learning Close

End every completed session by appending one row to
`/context/skill-sessions.md` (create with header row if absent):

```yaml
skill: buyer-personas
session_date: [YYYY-MM-DD]
pattern: [one falsifiable statement about this session, or "none"]
source: [surprised / wrong / missing / n.v.t.]
```

Write directly, no permission needed — this is a mechanical log entry,
separate from any downstream use of the output.

---

## Outputs

- **Files written:** `/context/skill-sessions.md` — one appended row per
  session (Step 5). No brain write — committee maps and personas are
  delivered in chat only.
- **Chat output format:** Buying Committee Map table + Deal Dynamics →
  one Messaging Persona card per role needing differentiated messaging →
  explicit handoff note (primary persona, which need separate content,
  which claims are still unvalidated).
- **External side effects:** n.v.t.
- **Next skill:** After output is delivered, check
  `product-marketing-context/.claude-plugin/next-skill-map.md` for "After
  buyer-personas" and surface that prompt. Do not auto-run — ask.

---

## Verification

- At least one Economic Buyer and one Champion identified before persona
  building starts.
- Named alternatives present for the primary persona — not skipped, not
  left as `[HYPOTHESIS]` without being flagged.
- Every claim tagged `[CONFIRMED]` / `[INFERRED]` / `[HYPOTHESIS]` — none
  left unmarked.
- Persona cards pass the competitor-swap test (can't be pasted onto a
  rival's page unchanged).
- Handoff note states the primary persona and flags any still-hypothesis
  claims before positioning-messaging picks this up.
- Session logged to `/context/skill-sessions.md`.

---

## Operating Rules

- **Power before messaging.** Map the committee before writing a single
  message. The persona who needs messaging is almost never the one who
  controls budget.
- **Alternatives before attributes.** Never describe what the product
  does without first naming what the persona would do instead — the most
  common B2B messaging failure.
- **Titles lie, behaviors don't.** Identify roles by what they ask for and
  do, not by what's on their business card.
- **Confidence tags are binding, never blended.** `[CONFIRMED]` earns
  confident language. `[INFERRED]` earns hedged language. `[HYPOTHESIS]`
  gets flagged, not used to drive final copy.
- **Specificity is the credibility test.** If the messaging could sit on
  a competitor's site unchanged, it isn't done yet.
- **No brain write.** A buying committee is deal- and segment-specific;
  writing it as a durable brain fact would drift the brain every time a
  new deal looks different from the last one.
- **Compounding runs through `/context/skill-sessions.md`, not a private
  knowledge tree.** Every skill in this repo logs the same way — a second,
  skill-specific memory system that only this skill reads would fragment
  the compounding the rest of the stack already relies on.

---

## Quality Gate

| Check | Standard | Pass = |
|---|---|---|
| Committee mapped before messaging | Step 2 completes before Step 3 starts | Yes |
| Economic Buyer + Champion identified | At least one of each, or explicit note why not | Yes |
| Named alternatives present | Primary persona has real alternatives, not `[HYPOTHESIS]` left unflagged | Yes |
| Confidence tags applied | Every claim marked CONFIRMED/INFERRED/HYPOTHESIS | Yes |
| Competitor-swap test passed | No persona card is genuinely generic | Yes |
| Handoff note present | Primary persona + unvalidated claims stated explicitly | Yes |
| No brain write attempted | Output stays in chat / handoff only | Yes |
| Learning Close ran | `/context/skill-sessions.md` has a new row for this session | Yes |

---

## Do Not Use For

- **`positioning-messaging`** — the positioning statement or messaging
  hierarchy itself. Run this skill first, hand off the personas, then run
  that one.
- **`beachhead-segment`** — choosing among multiple candidate market
  segments. This skill maps the committee inside one already-chosen
  segment or deal.
- **`ideal-customer-profile`** — org-level ICP research (demographics,
  behaviors, JTBD, needs). Run that first if the ICP itself is still
  thin; this skill assumes a real target and maps the humans inside the
  purchase decision.
- n.v.t.
