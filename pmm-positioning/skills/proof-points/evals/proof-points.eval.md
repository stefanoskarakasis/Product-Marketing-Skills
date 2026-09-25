# proof-points Eval Suite

Setup populates `/foundation/brain.md` with a baseline PMM context (Sections
1–6) unless a test explicitly varies it, and checks `/context/skill-sessions.md`
for the Learning Close entry after each run.

## Eval 1 — Extract mode: candidates start flagged even when the deck cites a source

**Setup:** Brain Section 6 is empty. User pastes text from a sales deck slide
reading: "89% customer retention (per Q3 2025 earnings call)" and "Our
platform has industry-leading uptime."

**Prompt:** "Pull proof points out of this deck."

**Expect:** Both statements are extracted as candidates. The retention stat
is registered `[NEEDS PROOF — deck cites Q3 2025 earnings, unconfirmed]`,
not approved outright, even though the deck names a source. The uptime line
is extracted as an unsupported superlative (no named comparison) and also
flagged. Neither candidate is written to the brain until the full candidate
list is shown and confirmed.

## Eval 2 — Extract mode: customer name in a deck gets both flags

**Setup:** Same empty-registry setup. Pasted battlecard text includes: "Acme
Corp cut their reporting time in half — VP Sales, Acme Corp."

**Prompt:** "Add this to our proof points from the battlecard."

**Expect:** Candidate registered with both `[NEEDS PROOF]` (the claim itself
needs a source beyond "it's in the battlecard") and `[NEEDS APPROVAL]` (no
documented permission to use Acme's name publicly, even though the name
appears in existing sales material).

## Eval 3 — Extract mode: duplicate claims across two documents are merged, not doubled

**Setup:** User pastes text from two different decks, both containing a
version of "10.5k customers" — one says "10.5k customers (Jan 2026
announcement)," the other says "over 10,000 customers."

**Prompt:** "Build our proof points registry from these two decks."

**Expect:** Registered as one candidate, not two, with a note that it
appeared in both source documents. The more specific/sourced phrasing (with
the citation) is what's carried into the flagged entry.

## Eval 4 — Extract mode: full candidate list shown before any write, bulk confirmation respected

**Setup:** User pastes a battlecard with 6 distinct claim-shaped statements
(a mix of metrics, one quote, one superlative).

**Prompt:** "Here's our battlecard — pull everything out of it."

**Expect:** All 6 candidates are surfaced together, grouped by type, before
any brain write is proposed. The skill asks whether to register all 6 as
flagged candidates or go through them individually — it does not silently
write a subset, and does not treat silence on the confirmation question as
approval to proceed.

## Eval 5 — Add mode, sourced claim ships as approved

**Setup:** Brain Section 6 exists with 2 prior approved metrics.

**Prompt:** "Add a proof point: 89% customer retention rate, from our Q4
2025 earnings call."

**Expect:** New entry registered as approved (not `[NEEDS PROOF]`) with the
source and date cited exactly as given — this is a direct Add-mode claim
with a source stated by the user in the moment, distinct from an
Extract-mode candidate pulled from a document, so it does not require the
extra unconfirmed-citation handling Eval 1 tests. Existing 2 entries
unchanged. Confirmation shown before the brain write.

## Eval 6 — Add mode, unsourced claim gets flagged, never silently approved

**Setup:** Same as Eval 5.

**Prompt:** "Add a proof point: our customers save 10 hours a week."

**Expect:** Entry is registered as `[NEEDS PROOF]`, not approved. The skill
does not refuse to proceed — it registers the flagged claim and states
plainly that it isn't usable in copy until a source is added. No invented
source is fabricated to make the claim look complete.

## Eval 7 — Verify mode, approved claim confirmed with its source cited back

**Setup:** Brain Section 6 has an approved metric: "95% uptime SLA — from
our status page, pulled Jan 2026."

**Prompt:** "Can I say we have 95% uptime in this deck?"

**Expect:** Confirmed as approved, with the source cited back to the user
(status page, Jan 2026) — not just a bare "yes."

## Eval 8 — Verify mode, forbidden claim blocked with the stated reason

**Setup:** Brain Section 6 has a Forbidden Claims entry: "'Industry-leading
uptime' — unproven, no named comparison exists."

**Prompt:** "Can I say we have industry-leading uptime?"

**Expect:** Blocked, with the specific Forbidden Claims entry and its
reason surfaced — not a generic "that's not allowed."

## Eval 9 — Verify mode, claim not yet registered routes forward instead of dead-ending

**Setup:** Brain Section 6 exists but has no entry matching the claim in
question, and no Forbidden Claims entry matches it either.

**Prompt:** "Can I say we have the fastest onboarding in the category?"

**Expect:** The skill states the claim isn't currently registered either
way — it does not treat silence in the registry as approval, and does not
treat it as an automatic forbidden claim. It offers a concrete next step:
route to Extract mode if this likely lives in existing collateral, or Add
mode if the user has a source in hand — not a dead-end "unusable."

## Eval 10 — Audit mode covers the full registry, not a sample

**Setup:** Brain Section 6 has 5 entries: one fully sourced and current,
one with no source, one customer quote with no documented approval, one
metric dated 18 months ago with no refresh note, and one entry using
"best-in-class" with no named comparison.

**Prompt:** "Audit our proof points."

**Expect:** All 4 flaggable entries are caught — `[NEEDS PROOF]` on the
unsourced one, `[NEEDS APPROVAL]` on the uncredited quote, `[STALE —
recheck]` on the 18-month-old metric, and an unsupported-superlative flag
on the "best-in-class" entry — the fully sourced, current entry is left
unflagged. No entry is skipped.

## Eval 11 — Edge case: brain entirely absent → hard block

**Setup:** No `/foundation/brain.md` file exists.

**Prompt:** "Add a proof point: 4.2 stars on G2."

**Expect:** Skill blocks before registering anything. Response redirects to
`product-marketing-context`, matching the Pre-flight gate language. No
Section 6 write is attempted, and no Learning Close entry is required for
this test (the session never reached Step 7).

## Eval 12 — Quality gate specifically: forbidden claim with no reason is not allowed to ship

**Setup:** User is building the Forbidden Claims section directly.

**Prompt:** "Add 'we're the best in the market' to the forbidden list."

**Expect:** The skill does not append the entry as-is — it asks for the
reason category (legal / unproven / competitively risky / retracted)
before writing, since Step 5 and the Quality Gate both require every
forbidden entry to carry a stated reason. A forbidden-claims write with no
reason field filled in fails this eval.

## Eval 13 — Learning Close logs the canonical shape, no permission asked

**Setup:** Any successful run (e.g. Eval 5's setup, completed through the
confirmed brain write).

**Expect:** The skill appends one entry to `/context/skill-sessions.md`
matching the canonical Type A format exactly: `type: execution`, `skill`,
`session_date`, `pattern`, `source` — in that order, no additional fields.
`source` is one of `surprised / wrong / missing / n.v.t.`, never a
description of where the proof-point data came from. Logged directly,
without asking the user to confirm the log entry separately from the
brain-write confirmation already given in Step 6.
