# Preflight details

Moved verbatim from `SKILL.md`.

## Pre-flight (moved verbatim)

Context is loaded in a fixed order so the right facts come from the right place. Paths and field keys are defined in `product-marketing-context/references/brain-schema.md`; evidence ranks in `product-marketing-context/references/evidence-format.md`.

| Load | From | Why |
|---|---|---|
| Section 3 first | `/foundation/brain.md` | The roster starts here: `alternatives`, `status_quo`, `category`, `market_type`, `unique_capabilities`, and any Alternatives Map block |
| Sections 1, 2 | same | Your market: `target_market`, `offerings`, `geography`, `company_size`; the profile is always read against who you sell to |
| Section 6, 8 | same | What you may claim, and what you may not research or compare (`prohibited`) |
| Section 5, 7 | same | Why-now and this quarter's priorities decide which competitor gets deep attention |
| Earlier profiles | `/context/competitor-profiles/` | The newest record per competitor is the baseline; a refresh is a delta against it |
| Debriefs | `/context/battlecards/`, `/context/signals/` | v2 `intake` only |
| Every CI record | `/context/battlecards/`, `/context/deep-dives/`, `/context/signals/`, Section 3, `~~competitive intelligence` | `ask` reads all of them for the named competitor, whatever the question |
| Guardrails | `/context/meta-patterns.md` | Surface any guardrail fired 2+ times in earlier competitive-profile sessions |
| Format | `/foundation/me.md` | Length and shape only. Never a company fact |

- **Brain absent: Quick-Brain, don't block.** Say once: "No PMM brain found, so I'll work from five quick answers and hold them for this session. Run `product-marketing-context` later (a separate plugin) to keep them." Ask all five in one message: (1) what you sell, in one sentence; (2) the market and the buyer you sell to; (3) the up to five competitors that show up in deals; (4) where you honestly lose to each; (5) where your deal data lives. Use them as stand-ins for Sections 1 to 3. Label every profile "Built from Quick-Brain answers" and mark unsourced items `[Rep-stated]`. Do not write to a brain that does not exist.
- **No named competitors in Section 3:** do not invent a roster. Say so and route to `alternatives-map`; offer to start with the competitors the user names now, tagged `[Rep-stated]`.
- **Freshness** (limits in `brain-schema.md`): a loaded section past its limit goes into Check before use. A roster older than 90 days is flagged for `roster`.
- **Constraints first:** read Section 8 `prohibited` and `approvals`, and Section 6 `forbidden_claims`. If a named competitor, or competitor research itself, is prohibited, stop on that competitor and show the entry.
- **Gap capture** (see the gap capture rule in `SKILL-SPEC.md`): if a field this run needs is empty or stale and the answer would change the profile (most often Section 3 `unique_capabilities` or `why_leaving`), ask one question: the question, one line on why it matters, "answer or skip". Skip: continue with a labelled assumption and append a `skipped` block to `/foundation/gaps.md` (format in `product-marketing-context/references/gaps-format.md`). At most one gap question per run. None in unattended runs.
- **Personal context** (see the personal context rule in `SKILL-SPEC.md`): `/foundation/me.md` is read for format and detail only.
- **`ask` is lighter.** It loads brain Sections 3, 6 and 8 only (Section 1 `permitted_claims` only if the answer states a claim about us). It never runs Quick-Brain, never asks a gap question and never routes to `alternatives-map` for a missing roster: with no brain it says "No brain found, answering from your records and public pages" and carries on. A seller waiting in a thread is never sent a five-question intake.
