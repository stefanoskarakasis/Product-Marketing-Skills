# Deep-dive format

Canonical template, tag rules and counting rules for `competitor-deep-dive`.

## Tags

Tags are defined once, in `competitive-battlecard/references/card-format.md`. This skill uses them unchanged and adds none.

| Tag | Use here |
|---|---|
| `[Field: <tool>, n=<n>, <window>]` | Deal, call, win/loss or chat evidence from the user's own tools or paste. Part 6 and the deal pricing in Part 4 |
| `[Brain S<n>]` | A value taken from a confirmed brain section. Part 12 and our side of Part 8 |
| `[Internal <Mon YYYY>]` | A card, story or profile from the CI platform or a `competitive-profile` record, with its own date |
| `[Public <Mon YYYY>]` | The competitor's or our own public page, release or filing, with the date read |
| `[Third-party <Mon YYYY>]` | Review site, analyst or vendor-authored comparison; say which |
| `[A]` | Assumption, no source. Never shown as fact; goes to Open items as a question |
| `[NEEDS PROOF]` | Our-side claim with no registered source. Stays out of the body |

Two flags sit outside that table, used as the sibling skills use them: `[Rep-stated]` (an unsourced Quick-Brain answer) and `[NEEDS APPROVAL]` (a customer name or quote without approval, a Section 6 flag).

Rules from the battlecard: a competitor's own claim proves only that it said it; add "re-check" to anything older than about 90 days; a roadmap or launch date already past is unconfirmed; numbers carry source, n and window; live data replaces a brain value only when n is at least 2, and if they differ by more than 5 points show both.

Freshness windows for "re-check": price 60 days; product, positioning and moves 90; buyer-side 180; review rating 90. A quote keeps its own date at any age.

Ranks come from `product-marketing-context/references/evidence-format.md` (0 confirmed brain value, 1 hard records, 2 customer-spoken, 3 internal strategy, 4 public, 5 soft); a fact older than 12 months drops one rank, older than 24 months two.

## Counting

Body words are counted from "Check before use" to "Card feed", prose and list text only. Not counted: the title line, tables, review quotes, tags, status lines, the Sources list and the footer. Row caps: snapshot 10, reviews 8 per platform, head-to-head 10 per offering, brain check 8.

## Template (Google Doc markdown, one stacked column, table headers bold)

```markdown
# [Competitor] Deep-Dive  (INTERNAL USE ONLY)
[Decision] · [Audience] · [Depth] · as of [YYYY-MM-DD] · v[n]

## Check before use
- Assumptions, stale brain sections, facts marked re-check, what could not be fetched.
- Connector status: one line per category used (connected with tool name / pasted / not connected / skipped by user), and what that costs Part 4 and Part 6.
- Guardrails applied from `/context/meta-patterns.md`.
- Constraint check: Section 6 forbidden_claims and Section 8 prohibited, result.
- Built from Quick-Brain answers (only when true).
- Changed since [date]: up to five differences (only on a refresh).

## 1. Decision and bottom line
Two sentences: the decision this supports, and the answer in plain words.

## 2. Summary by audience
| **Audience** | **What to take from this** | **What to do next** |
| --- | --- | --- |
| Sales | | |
| Product | | |
| Exec | | |

## 3. Company and moves
| **Fact** | **Detail** | **Source** |
### What changed and what did not
(only when there was a rebrand, acquisition or pivot)
| **Area** | **Changed** | **Did not change** |
### Timeline
| **Date** | **Event** |
(newest first)

## 4. What they sell and what it costs
Source: `~~CRM` (tool), pulled [date], n = X  |  Source: pasted by user, [date]  |  Not connected: deal pricing missing, list price only.
Capability list in their own framing, from their own materials.
| **Item** | **Figure** | **Provenance** |
State what could not be confirmed.

## 5. Recent signals
Last 90 days from `/context/signals/`, each with its original confidence. "No signals on file" if none.

## 6. Deal evidence
Source: `~~CRM` / `~~win/loss` / `~~call recordings` (tool), pulled [date], n = X  |  Source: pasted by user, [date]  |  Not connected: no deal evidence available.
| **Source** | **n** | **Finding** | **As of** |
Won, lost, and why. "No deal evidence available" if none: never fill from reviews.

## 7. What reviewers say
### Ratings by platform
| **Platform** | **Rating** | **Reviews** | **As of** |
### The good
| **Reviewer** | **Segment** | **Rating** | **Date** | **Liked** | **Flagged** |
### The bad
| **Platform** | **Date** | **Quote** | **Theme** |
### Cross-cutting themes
| **Theme** | **First seen** | **Last seen** | **Platforms** | **Read** |
One sentence on any praise and complaint that contradict each other across dates.

## 8. Head-to-head
One sub-section per offering from Section 1, in Section 1 order.
### vs. [our offering]
| **Capability** | **[Competitor]** | **[Our offering]** | **Edge** |
Our column: permitted or approved claims only. Competitor column: "no public evidence" where nothing was found.

## 9. Where they genuinely win
At least two bullets, each sourced.

## 10. Talking points
Problem-first framing, three discovery questions, objection handling table (**They say** / **Respond with**). Every response uses only approved claims.

## 11. Card feed
Everything `competitive-battlecard` may lift, with the section it comes from.
| **Card block** | **Content** | **From section** |
| Competitor snapshot rows (max 5) | | |
| Reframe their strengths | | |
| Discovery questions | | |
| Walk-away signals (3) | | |
| Proof gaps ([NEEDS PROOF]) | | |

## 12. Brain check
What the brain believed about this competitor, set against this run's evidence.
| **Brain field** | **Brain says** | **Evidence says** | **Status** |
Status is Confirmed, Contradicted or Untested. A Contradicted row shows both values and their dates and is never resolved here: it feeds the Section 3 write-back as a question.

## 13. Open items
Questions raised by unsourced weaknesses, `[NEEDS PROOF]` items for `proof-points`, connectors skipped and what finishing them would add, and the outcome of the brain write-back (confirmed, declined, none proposed).

## 14. Confidence and methodology
| **Area** | **Confidence** | **Note** |
Review dates approximate; no per-review permalinks; blocked fetches; secondhand items; the standing caveat that absence of evidence is not proof of absence.

## 15. Sources
### Company
### Product and pricing
### Reviews
### Deals and internal
Every source cited inline appears here, grouped, linked where a link exists.

INTERNAL USE ONLY. Facts are dated; check "as of" before quoting.
```

## Saved record

`/context/deep-dives/<competitor-slug>-YYYY-MM-DD.md`. One file per run; if the same competitor and date exist, add `-2`, `-3`. Never overwrite an earlier file.

```markdown
# Deep-dive record — [Us] vs [Competitor] — [YYYY-MM-DD]
Brain read: [sections present, or "Quick-Brain, session only"]
Decision: [decision · audience · depth]
Assumptions: [what was assumed because it was skipped, or "none"]
Sources named this run: [list, each with category, tool and date for pulled items]
Changed since last deep-dive ([date]): [up to 5 lines, or "first deep-dive"]

[the deep-dive, exactly as delivered]

## Evidence log
| id | claim | tag | source | as_of |
|---|---|---|---|---|
| D-1 | [one atomic claim] | [tag] | [file, URL or call title] | [YYYY-MM-DD] |

## Open items
- Our-side claims excluded for lack of proof: [claim] `[NEEDS PROOF]` (to register: `proof-points`)
- Connectors skipped and what finishing them would add: [list, or none]
- Proposed brain write (Section 3): [shown and confirmed, declined, or none]
- Gap raised: [gap id, or none]
```

Evidence ids (`D-1`, `D-2`, ...) are local to this file. They are not brain evidence ids (`E-001`), which only `product-marketing-context` writes, and they are not battlecard ids (`C-n`).

## Proposed Section 3 note

Appended under brain Section 3 only after the user confirms the exact text. Never edits existing text, never touches another section. At most three lines.

```markdown
### Deep-Dive Field Notes — [Competitor] (added via competitor-deep-dive, [YYYY-MM-DD])
- [Dated fact the map lacks, e.g. pricing model or rebrand] [src: <where> | <YYYY-MM-DD> | <pulled|inferred|stated> | draft]
- [Deal evidence with n] [src: <tool> | <YYYY-MM-DD> | pulled | draft]
- [Contradicted brain field, as a question with both values and dates] [src: <where> | <YYYY-MM-DD> | inferred | draft]
```

A stub for a competitor missing from Section 3 is one line in the same block: `- Named alternative: [Competitor] (not yet in the map; run alternatives-map)`.
