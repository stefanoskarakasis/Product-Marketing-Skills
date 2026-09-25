---
name: proof-points
version: 1.0.0
description: >
  Build and maintain a sourced, gated registry of the proof points your
  messaging relies on — metrics, customer quotes, case study results, and
  analyst citations. Use when pulling proof points out of a deck or
  battlecard, checking whether a stat is safe to use in copy, sourcing a new
  claim before it ships, or auditing an existing set of claims for anything
  unsourced, stale, or unapproved.
metadata:
  author: Stefanos Karakasis
  context: brain-dependent
  quality_gate: true
last_updated: 2026-09-25
---

# Proof Points

## How This Works

Every stat, quote, and case study in your messaging is a promise — and every
promise sales, legal, or a skeptical prospect can eventually ask you to back
up. Almost no company has a clean registry of these; what they actually have
is a mash of sales decks, battlecards, one-pagers, and case study PDFs, each
one repeating (and slowly staling) numbers nobody's re-checked since the deck
was built. This skill is both the intake and the gate: it mines claim
candidates out of that mess, then makes sure nothing gets called "approved"
without a source, no customer name ships without documented permission to use
it, and every forbidden claim carries a stated reason — not a bare
prohibition nobody can act on. It deepens your brain's existing Section 6 in
place, the same Proof Points Registry `message-house` and
`positioning-messaging` already read.

**Step 0** — Load brain Section 6 (current registry, however thin).

**Step 1** — Classify the request: Extract from source material, Add one
claim directly, Verify a claim before it ships, or Audit the existing
registry.

**Step 2 (Extract)** — Mine claim-shaped statements out of pasted decks,
battlecards, case studies, or other GTM collateral; every candidate starts
flagged, regardless of whether the source material cites its own source.

**Step 3 (Add)** — Require a source for a directly-supplied claim; unsourced
claims get flagged, never silently approved.

**Step 4 (Verify)** — Check a claim someone wants to use against the
registry: approved, forbidden, or not yet registered.

**Step 5 (Audit)** — Walk every existing entry for missing sources, stale
dates, undocumented customer names, and unsupported superlatives.

**Step 6** — Deepen brain Section 6 with the result (on user confirmation).

**Step 7** — Learning Close: log the session to `/context/skill-sessions.md`.

---

## Trigger

- **When:** Building a proof points registry from scratch out of existing
  sales decks, battlecards, case studies, or pricing pages; adding a single
  new metric, quote, or case study directly; checking whether a specific
  stat or phrase is safe to use before it ships in copy; or auditing brain
  Section 6 for unsourced claims, stale proof, undocumented customer names,
  or unsupported superlatives.
- **Not for:** Structuring raw, unstructured customer conversation — a call
  recording or interview transcript nobody's synthesized yet — into
  discovery insights → `interview-summary`, run first. That's a
  qualitatively different task (JTBD synthesis of what customers said) from
  this skill's Extract mode, which mines already-written claims out of
  already-somewhat-structured GTM collateral (a deck, a battlecard, a case
  study doc) — if Extract mode turns up a customer quote that traces back to
  a raw call nobody's written up, route that call through
  `interview-summary` first, then bring the resulting quote back here.
  Vocabulary, tone, and forbidden *language* (not claims) → `brand-voice`.
  Building the positioning statement or messaging hierarchy itself →
  `positioning-messaging`, run this first so it has a gated registry to cite
  from.
- **Example prompts:**
  - "Pull proof points out of this battlecard"
  - "We don't have a registry — start one from these 3 sales decks"
  - "Add a proof point: 40% faster onboarding, from our Q3 customer survey"
  - "Can I say 'industry-leading' in this deck?"
  - "Audit our proof points — anything stale or unsourced?"

---

## Inputs

- **Args:** For Extract mode — one or more source documents or pasted text
  (a sales deck, battlecard, case study, pricing page, one-pager). For Add
  mode — a single claim with its source. For Verify mode — a claim to check.
  For Audit mode — no additional args beyond "audit." If the mode isn't
  clear from what's given, ask.
- **Defaults:** If brain Section 6 already has entries but they're missing
  the layers this skill requires (source, approval-to-use, staleness date),
  treat this as additive — fill the missing layers on the existing entries
  rather than re-litigating claims that are already sourced and current. If
  Section 6 is empty or near-empty and the user hasn't specified a mode,
  ask whether they have source material to extract from before assuming
  claims will be added one at a time — most first-time registries start
  from Extract mode, not Add mode.
- **Context keys:**
  - `/foundation/brain.md` — required. Section 6 (Proof Points Registry).
    Section 1 (Product Context) read for plausibility only — never to
    invent a claim the user didn't supply.
  - **Brain contract:** Reads Section 6, and Section 1 for context only.
    Writes Section 6 only — approved metrics, customer quotes/case
    studies, and forbidden claims, appended on explicit confirmation.
    Never writes to any other section.

---

## Pre-flight

- Load `/foundation/brain.md` Section 6 if it exists.
- **Hard block:** brain entirely absent → stop, direct to
  `product-marketing-context` first. A thin or empty Section 6 is not a
  block — that's what Extract mode exists to fix.
- **Soft block:** request doesn't clearly state Extract, Add, Verify, or
  Audit → ask which applies. If Section 6 is empty and the user just says
  "build our proof points," default the question toward Extract mode first:
  *"Do you have decks, battlecards, or case studies I can pull from, or are
  you adding claims one at a time?"*
- **Soft block (Add mode only):** a claim offered with no source → do not
  reject it outright; proceed to Step 3, where it gets flagged
  `[NEEDS PROOF]` instead of silently marked approved.

---

## Steps

### Step 0 — Load Context

Load brain Section 6 as it currently exists, and Section 1 for product-name
context only.

**Gate check:** brain absent → surface: *"Brain not found. Run
`product-marketing-context` first — even a thin Section 6 gives this skill
something real to work from."*

### Step 1 — Classify the Request

Determine which of four modes applies. If ambiguous, ask:
> "Do you want to pull proof points from existing material (decks,
> battlecards, case studies), add one claim directly, check whether a
> specific claim is safe to use, or audit the existing registry?"

### Step 2 — Extract Mode: Mine Claims from Source Material

This is the on-ramp for the common case: no clean registry exists, only a
mash of sales decks, battlecards, one-pagers, and case study documents.

1. Read through every piece of source material provided and pull out every
   claim-shaped statement: a number or stat, a named customer outcome, a
   direct quote, a case study reference, or a superlative/comparison claim
   ("industry-leading," "fastest," "the only platform that...").
2. Classify each extracted candidate by type — Metric, Customer quote, Case
   study result, Analyst citation, or Superlative — same taxonomy Add mode
   uses.
3. **Every extracted claim starts `[NEEDS PROOF]`, regardless of whether the
   source material itself cites a source.** A deck slide that says "per Q3
   earnings" is not the same as a confirmed-current source — decks get
   copied forward for quarters after the number goes stale. If the source
   material does cite something, carry that citation through as a proposed,
   unconfirmed source attached to the flag: `[NEEDS PROOF — deck cites Q3
   2025 earnings, unconfirmed]`. This gives the user something concrete to
   confirm or reject rather than a blank slate, without treating an in-deck
   citation as verified provenance on its own.
4. A customer name or quote pulled from a deck gets `[NEEDS APPROVAL]` in
   addition to `[NEEDS PROOF]` — sales enablement material routinely reuses
   customer names before (or after the expiry of) actual legal/customer
   sign-off. A name appearing in a deck is not documented permission to use
   it.
5. When the same claim (or a near-duplicate phrasing) appears across
   multiple source documents, surface it once as a single candidate, noting
   how many source documents it appeared in — never register the same claim
   twice because it showed up in two decks.
6. Return the full candidate list before writing anything, grouped by type:
   > "Found [N] claim-shaped statements across [source documents]. All
   > flagged `[NEEDS PROOF]` until confirmed current — here they are:
   > [list]. Register all of them as flagged candidates, or go through and
   > confirm/reject first?"
7. On confirmation, batch-append to Section 6 via Step 6 — still flagged.
   Extraction never promotes a claim to approved on its own; that only
   happens later, through Add mode's explicit source confirmation or Verify
   mode, once the user has actually checked the source is current.

### Step 3 — Add Mode: Register a New Claim Directly

Classify the claim by type — Metric, Customer quote, Case study result, or
Analyst citation — and require a source for each:

| Claim type | What "sourced" means |
|---|---|
| Metric | Where the number comes from and when it was pulled (internal dashboard, public filing, survey — with date) |
| Customer quote | Who said it, their role and company, and confirmation they've approved being named — not just that they said it on a call |
| Case study result | A published or internally-approved case study the number traces back to |
| Analyst citation | The named report, firm, and publication date |

No source → the claim is registered as `[NEEDS PROOF]`, not silently
promoted to approved. A customer quote with no documented approval-to-use
gets `[NEEDS APPROVAL]` even if the quote itself is real — a customer
saying something on a call is not the same as a customer agreeing to be
named in your marketing.

Reject vague quantifiers as claims on their own: "many customers report..."
is not a proof point. Either name the number and its source, or don't
register it yet.

### Step 4 — Verify Mode: Check a Claim Before It Ships

User supplies a specific stat or phrase they want to use. Check it against
the current registry and return one of three answers:

1. **Approved** — it's in the registry with a source (and approval-to-use,
   if it names a customer). Cite the source back to the user.
2. **Forbidden** — it matches or resembles an entry in the Forbidden Claims
   list. State which entry and why (see Step 5's Forbidden Claims layer,
   built or updated in either Extract or Add mode).
3. **Not yet registered** — it isn't in the registry either way. This is
   not automatic approval or automatic rejection — route to Extract mode
   (if it likely lives in existing collateral) or Add mode (if the user has
   the source in hand) rather than flagging it unusable with no path
   forward.

Superlatives ("industry-leading," "best-in-class," "the only platform
that...") without a named comparison are flagged as unsupported even if no
Forbidden Claims entry names them specifically — a superlative with no
comparison is a claim with no evidence, whether or not it's been banned
outright.

### Step 5 — Audit Mode: Review the Existing Registry

Walk every entry currently in Section 6 — not a sample — and flag:

- **No source** — mark `[NEEDS PROOF]`.
- **Customer name with no documented approval-to-use** — mark
  `[NEEDS APPROVAL]`.
- **Stale** — a dated metric or citation older than 12 months with no
  refresh noted. Flag `[STALE — recheck]`, don't silently drop it.
- **Unsupported superlative** — language claiming "best," "most," "only,"
  or similar with no named comparison anywhere in the entry.

Also build or update the Forbidden Claims list here: every forbidden claim
requires a stated reason — legal exposure, unproven, competitively risky,
or previously retracted — never a bare "don't say this."

```markdown
**Forbidden Claims:**
- "[claim or claim pattern]" — [reason: legal / unproven / competitively
  risky / retracted]. [One sentence of context if useful.]
```

Return the full flagged list as the punch list — this is the output of
Audit mode; it does not also rebuild the registry from scratch.

### Step 6 — Deepen Brain Section 6 (on Confirmation)

Show the exact addition before writing:
> "Adding to brain Section 6 — [new approved metric(s) / flagged
> candidate(s) / customer quote(s) / case study result(s) / forbidden
> claim(s)], sourced from [source]. Existing content stays unchanged.
> Here's what I'll append: [show exact text]. Save this?"

Append to `/foundation/brain.md` Section 6 — do not replace existing
content, do not create a separate file:

```markdown
## Section 6: Proof Points Registry
[existing content unchanged]

### Registry Update (added via proof-points, [date])
**Approved Metrics:**
- [claim] — [source, date] `[NEEDS PROOF]` if unsourced

**Customer Quotes & Case Study Results:**
- "[quote]" — [name, role, company] ([approval-to-use confirmed / `[NEEDS APPROVAL]`])

**Forbidden Claims:**
- "[claim]" — [reason]

**Extracted this session (if Extract mode ran):**
- [candidate] — [claim type] `[NEEDS PROOF — <proposed source if the
  material cited one, else blank>]`, found in [source document(s)]

**Audit flags (if this session ran Audit mode):**
- [entry] — [NEEDS PROOF / NEEDS APPROVAL / STALE / unsupported superlative]
```

Never write without this explicit confirmation.

### Step 7 — Learning Close

Append one entry to `/context/skill-sessions.md`, in the canonical format
defined in `product-marketing-context/.claude-plugin/skill-sessions-format.md`
(Type A — execution session):

```yaml
type: execution
skill: proof-points
session_date: [YYYY-MM-DD]
pattern: [one falsifiable statement about this session, or "none"]
source: [surprised / wrong / missing / n.v.t.]
```

Write directly, no permission needed — separate from the brain write above,
which still requires explicit confirmation.

---

## Outputs

- **Files written:** `/foundation/brain.md` Section 6 — appended approved
  metrics, extracted candidates, customer quotes/case studies, and
  forbidden claims (Step 6), only after explicit confirmation.
  `/context/skill-sessions.md` — one appended entry per session (Step 7).
- **Chat output format:** Mode stated (Extract / Add / Verify / Audit) →
  candidate list, findings, or new registry entries → confirmation prompt
  for the brain write.
- **External side effects:** n.v.t.
- **Next skill:** After brain Section 6 is deepened, check
  `product-marketing-context/.claude-plugin/next-skill-map.md` for "After
  proof-points" and surface that prompt. Do not auto-run — ask.

---

## Verification

- Every approved claim traces to a stated source — no exceptions.
- Every extracted candidate starts `[NEEDS PROOF]`, even when the source
  material cited its own source — no extraction shortcut to "approved."
- Every customer-named quote or case study has documented approval-to-use,
  not just evidence the customer said it or appeared in a deck.
- Every forbidden claim carries a reason, not a bare prohibition.
- Duplicate claims found across multiple source documents are merged into
  one candidate, not registered twice.
- Audit mode covers every existing Section 6 entry, not a sample.
- Superlatives without a named comparison are flagged even without a
  matching Forbidden Claims entry.
- Brain Section 6 write shown to the user and confirmed before it happens.
- Existing Section 6 content preserved, not overwritten.
- Session logged to `/context/skill-sessions.md` with `type: execution`.

---

## Operating Rules

- **Every approved claim requires a source. No source means not approved,
  full stop.** A plausible-sounding number with no traceable origin is a
  liability, not a proof point.
- **Extraction never grants approval.** A claim pulled from a deck or
  battlecard is a candidate, not a verified fact — even when the source
  material cites its own source, that citation is carried through as
  unconfirmed until the user actively checks it's still current.
- **Customer names require documented approval-to-use, not just usage in
  a past call or a deck.** A customer saying something to your sales rep,
  or appearing in a battlecard, is not the same as a customer agreeing to
  be quoted publicly.
- **Forbidden claims need a stated reason.** A bare "don't say this" can't
  be applied consistently by anyone who wasn't in the room when it was
  decided.
- **Never silently promote an unsourced or extracted claim to approved.**
  Flag it and move on — don't let a plausible draft slip through because
  asking for confirmation felt like friction.
- **Deepen brain Section 6 — never fork a second claims file.**
  `message-house` and `positioning-messaging` both expect Section 6 to be
  the single source of truth for proof.
- **Superlatives get flagged, not auto-blocked.** "Industry-leading" isn't
  banned outright — it's flagged as unsupported until the user either
  finds the comparison evidence or decides to cut it. The decision stays
  with the user; the flag makes sure it's a decision, not an oversight.
- **Brain write requires explicit confirmation. Never append silently,**
  including bulk writes from Extract mode.

---

## Quality Gate

| Check | Standard | Pass = |
|---|---|---|
| Every approved claim sourced | No claim marked approved without a cited source | Yes |
| Extracted claims start flagged | Every Extract-mode candidate registered `[NEEDS PROOF]` regardless of in-deck citation | Yes |
| Customer approval-to-use documented | Every named customer quote/case study has confirmed permission, not just evidence they said it or appeared in a deck | Yes |
| Forbidden claims carry a reason | Every entry states legal / unproven / competitively risky / retracted | Yes |
| Duplicates merged | The same claim across multiple source documents is registered once, with occurrence count | Yes |
| Audit covers full registry | Every existing Section 6 entry reviewed, not a sample | Yes |
| Superlatives flagged | Unsupported superlatives caught even with no matching Forbidden Claims entry | Yes |
| Existing content preserved | Prior Section 6 content untouched unless explicitly revised | Yes |
| Brain write confirmed | Exact addition (including bulk Extract-mode writes) shown and confirmed before writing | Yes |
| Learning Close ran | `/context/skill-sessions.md` has a new `type: execution` row for this session | Yes |

---

## Do Not Use For

- **`interview-summary`** — structuring a raw, unsynthesized call
  recording or interview transcript into discovery insights. Run that
  first if the source is genuinely raw conversation, not existing GTM
  collateral; bring the resulting quote back here once it's written up.
- **`brand-voice`** — vocabulary, tone, and forbidden *language* (how you
  sound). This skill governs factual claims and their evidence — a
  distinct concern even where both maintain a "don't say this" list.
- **`positioning-messaging`** — building the positioning statement or
  messaging hierarchy itself. Run this skill first so positioning has a
  gated, sourced registry to cite from.
- n.v.t.
