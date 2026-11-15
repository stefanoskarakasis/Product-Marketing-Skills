# Method

Read before `now`, `call`, `reply` or `prep`. One spine for every objection. A card (`library/`) supplies the specifics; the price play (`plays/price.md`) is the long form.

## The spine

| # | Move | Purpose |
|---|---|---|
| 0 | **Gate** | Stage, role, new or renewal. Silent. Decides the likely type. |
| 1 | **Acknowledge** | Lower defence. No apology, no defence, no discount signal. |
| 2 | **Isolate** | Is this the only blocker? "If that were solved, is everything else a fit?" |
| 3 | **Locate** | Compared to what: a budget, an alternative, an expectation, a past experience? |
| 4 | **Size** | Put the cost of the problem in the buyer's numbers. |
| 5 | **Prove** | One sourced fact, quote or metric. If none exists: unverified, or ask. |
| 6 | **Trade** | Every concession gets a give. Never a cut for nothing. |
| 7 | **Route** | If the speaker does not own the decision, arm them for the person who does. |
| 8 | **Lock** | A dated next step with an owner role and the condition to proceed. |

## Rules that never bend

- Diagnose before responding. Say the type behind the words.
- No concession in the first reply. Qualify, then route. "We may not have X, but" is a concession.
- Never invent a figure. Use the buyer's number, `approved_metrics`, or ask one question.
- Never quote a rival's price or claim from memory. Hand off to `competitive-battlecard`.
- Never reveal a floor, a walk-away or an internal approval limit.
- No false urgency. Quarter end is the seller's deadline, not the buyer's.
- Do not argue with a person who cannot buy: ask who owns it.
- If the buyer's own numbers make the fee higher than the saving, say so plainly and stop arguing price.

## Categories and what each one needs

| Category | Usual real issue | Lead move | Proof slot | Hand-off |
|---|---|---|---|---|
| Product fit | A gap, a workaround, or a need that is not real | Locate the need; size the workaround | `offerings`, roadmap only if approved | Product via the owner |
| Value and adoption | The business case was never built | Size, then prove | `approved_metrics`, `quotes` | `proof-points` |
| Proof and trust | Fear of being first or of being let down | Offer a checkable reference | `quotes`, named references if approved | `proof-points` |
| Switching risk | Cost and fear of the move | Plan the move, not the promise | Migration facts, if approved | Implementation lead |
| Security and legal | A real control or a checkbox | Document first, claim second | A named document only | Security or Legal owner |
| Incumbent | Habit, sunk cost, or a real fit | Size what the current setup costs | `alternatives` | `competitive-battlecard` |
| Price | Seven types, see `plays/price.md` | Diagnose type | `cost_of_problem` | Finance or deal desk |

## Surface rules

- **`now`:** one objection, one move, about 100 words in Slack.
- **`call`:** list every objection with its timestamp, the type, what was done well, what was missed, one dated next step each.
- **`reply`:** diagnose, then a paste-ready draft. Honest drafts beat persuasive ones: if the right move is to park the point, draft that.
- **`prep`:** from the deal and the brain, the three objections most likely on this call, the diagnostic question for each and the proof slot to have ready. Then the readiness check below.

## Talk track (every card, every surface)

The spoken line has three beats, so the seller regains control instead of defending:

1. **Acknowledge.** One short line that shows the point was heard and is fair to raise. No "but".
2. **Reframe.** One line that moves the buyer from the words to the underlying issue, with at most one proof point from `approved_metrics`, `quotes` or the buyer's own numbers. No source: say "unverified" or drop it. Never a metric that is not on file.
3. **Ask.** End on a question the seller owns: what, how often, who else, by when. A reply that ends on a statement hands the floor back. Add a dated next step in the line below.

Localize the wording to the buyer's role (finance wants audit and cost, IT wants security and effort, procurement wants terms and risk) and to the market in `geography` (EMEA mode in `rules.md`). If role or market is unknown, ask once or say the line is generic.

## Brain gap

Without a brain, or with a thin one, answer anyway and say the line is "not tailored". Name the single field that would change this answer (for example `offerings` for an integration claim, `approved_metrics` for a proof point). Hand the owner the missing fields, at most six: `offerings`, `target_market`, `persona`, `alternatives`, `approved_metrics`, `forbidden_claims`, with the instruction to run `/product-marketing-context`. The skill never writes the brain. Public facts (company site, pricing page, review sites) and category knowledge may inform a draft only when marked unverified.

## Readiness check (end of `prep`)

A seller who reads a good line on the way into a call still freezes. So ask first, show second:

1. For each likely objection, ask the seller to write the exact words they would say. Do not show your line yet.
2. Grade their words against the spine: acknowledged, isolated, sourced, no concession, a dated next step. Say what is missing in one line each.
3. Show the card's line only after, or if they ask.
4. Say plainly how many of their top ten objections are ready in their own words and how many are still `seed`. A card used live but never tailored is not ready.
5. Show a 20-second role-play of the card: buyer line, seller's three beats, buyer's answer. Short, spoken, no script longer than four lines.
6. Keep the seller's improved words as a `proposed` card (`setup.md`). Never clear it.

If the seller skips it, say once that an unrehearsed answer is the most likely one to concede, and move on.

## Hand-offs

Whole deal → `deal-review`. Customer state → `customer-context`. Rival claims → `competitive-battlecard`. Polishing words → `writing-assistant`. Messaging that keeps failing → a proposal to `product-messaging-playbook` once the n in `ledger.md` is met.
