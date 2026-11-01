# Preflight details

Moved verbatim from `SKILL.md`.

## Pre-flight (moved verbatim; route check, brain load, constraints and cost line stay in SKILL.md)

- Load `/context/meta-patterns.md` if present; surface any guardrail fired 2+ times in earlier media-monitoring sessions.
- Load `/context/monitoring/watchlist.md` and `_state.md`. No watchlist means `setup`. A watchlist with a schema other than `schema: 1` stops the run with a one-line migration note.
- **Brain absent: Quick-Brain, don't block.** Say once: "No PMM brain found, so I'll work from the watchlist and three quick answers for this session. Run `product-marketing-context` later (a separate plugin) to keep them." Ask (1) who we sell to, one line; (2) our two real strengths against competitors, with a source; (3) the quarter's one priority. Our side of every card carries only what the user sourced.
- **Constraints first:** read Section 8 `prohibited` and `approvals` and Section 6 `forbidden_claims`. If naming a competitor to the reader is prohibited, stop and show the entry.
- **Cost line, always.** Before any fetch, say in one line what the run will do: competitors, channel checks, read-only, connectors used, and the rough effort. In a scheduled run this is the first line of the record, not a question.
- **Freshness:** use the `competitive-profile` windows (price 60 days; product, positioning and moves 90 days). Ownership and investor facts have a 180-day window.
- **Gap capture:** if a brain field this run needs is empty and the answer would change it, ask one question, once. Skip: continue with a labelled assumption and append a `skipped` block to `/foundation/gaps.md` (format in `product-marketing-context/references/gaps-format.md`).
