# Battlecard: canonical format

One page a seller skims in 60 seconds, five minutes before a call, and can quote from mid-call. The layout is fixed so sellers learn one shape and find things by position. Emphasis changes with the deal; the order never does.

## Length and row caps

- Whole card: about 350 words, hard ceiling 450, counted from Check before use to Next move. The deal line, evidence tags, sources and footer are not counted. Cells: 20 words or fewer. A quotable line: two sentences at most.
- Caps per block are in the template below. Over budget: cut the weakest row of a block. Never shrink type below 9 pt and never turn every line into a fragment.
- `/foundation/me.md` may shorten the card or change its shape. It never lengthens it past one page.

## Design rules (both formats)

- **One column, stacked.** Every block is full width, in the fixed order below. No side-by-side blocks in HTML; no multi-column layouts in the Doc. The only two-column element is the snapshot table.
- **One emoji per H2 header, nowhere else** except the snapshot shading marks and ✅ 🛑. No emoji in body text, titles or table headers.
- **Plain-language headers**, identical in Doc and HTML, so a seller finds things by name and by position.
- **Two calls to action up top.** 🏆 and 🎤 sit directly under the title and the check line, so the page works if the seller reads nothing else.
- **One home per fact.** The same point never appears under two headers. A buyer objection is answered in 🔄 only.
- **Context is separated from content.** The deal facts sit in their own labelled table under the title, never in running lines. The Win condition is plain text: bold is reserved for labels.
- **Tags small, quotes loud.** Evidence tags are plain brackets after the claim, not italics in the middle of a sentence; quotable lines are in quotation marks.

## Emoji legend (use no others)

| Mark | Meaning |
|---|---|
| ⚠️ | Check before use |
| 🏆 | Win condition |
| 🎤 | Say this first |
| 🔍 | Competitor snapshot |
| ❓ | Discovery questions |
| 🔄 | Reframe their strengths |
| 🚦 | Win vs. walk away (✅ lean in, 🛑 walk away) |
| 💎 | Proof to use |
| 🧭 | Next move |
| 🟢 🟡 ⚪ | Snapshot shading: documented strength / gap or unbacked claim / parity or unknown |

## Evidence tags (one per claim)

| Tag | Meaning | Authority (evidence-format.md rank) |
|---|---|---|
| `[Field: <tool>, n=<n>, <window>]` | Closed deals, calls, support or chat evidence from the user's own tools or paste | 1 to 2 (chat is 5) |
| `[Brain S<n>]` | Taken from a brain section value the user confirmed | 0 |
| `[Internal <Mon YYYY>]` | A card, story or profile from your CI platform or planning docs, with its own date. The team's claim, not a source | 3 |
| `[Public <Mon YYYY>]` | The competitor's or our own public page, release or filing, with the date read | 4 (financial filings are a hard record about what was reported) |
| `[Third-party <Mon YYYY>]` | Review site, analyst or vendor-authored comparison. Say which if vendor-authored | 4 to 5 |
| `[A]` | Assumption, no source | none |
| `[NEEDS PROOF]` | Our-side claim with no registered source. Never shown in 💎 | none |

Rules: a competitor's own claim proves only that it said it. Add "re-check" to anything older than about 90 days. A roadmap or launch date already past today is treated as unconfirmed. Numbers carry source, n and window. Live data replaces a brain value only when n is at least 2; if they differ by more than 5 points, show both.

## Tailoring tables

**Persona: what to lead with**

| Persona | Lead with | Avoid |
|---|---|---|
| Economic buyer | Business metric, risk, total cost | Feature lists |
| Champion | A line they can repeat internally; how this makes them look good | Giving them claims you cannot prove |
| Technical evaluator | Architecture, integration, security, test criteria | Price talk |
| Security / compliance | Controls, certifications, data handling, audit trail | Positioning language |
| Procurement / legal | Terms, switching cost, references, exit | Product pitch |
| Exec sponsor | Strategic risk and timing | Detail |
| End user | The day-to-day workflow | Cost arguments |

**Stage: the 🧭 Next move**

| Stage | Play |
|---|---|
| Prospecting | One ❓ question that earns a meeting |
| Discovery | Questions that expose the gap; set evaluation criteria early |
| Evaluation / POC | Shape the test: criteria, baseline, a scenario where they are weak |
| Negotiation / procurement | Total cost, risk, references, a reason to decide now |
| Renewal | Proof of value delivered; early signs of a rival pitch |

**Competitor status × deal type**

| Situation | Posture | Weight |
|---|---|---|
| Incumbent, new logo | Displace | ❓ and 🔄; make the cost of switching smaller than the cost of staying |
| Challenger alongside us, expansion or renewal | Defend | 💎 and 🎤; make staying the safe choice |
| In the final two | Win the criteria | 🚦 and the evaluation test |
| Status quo / DIY | Name the hidden cost | Only costs from brain Section 3 `status_quo`; never invented figures |

**Role**

| Role | Emphasis |
|---|---|
| Account executive / sales leader | 🏆 and negotiation levers |
| SDR / BDR | 🎤 and one ❓ |
| Solutions engineer | Technical snapshot rows and test criteria |
| CSM / account manager | Retention proof and early-warning signs |
| Partner / channel | Where we are complementary |
| PMM | Gaps worth fixing in messaging; proposed brain notes |

**GTM motion (optional, from the user or from `gtm-motions` output)**

| Motion | Adds to 🧭 |
|---|---|
| Outbound / ABM | Multi-thread plan: which second and third contact to open |
| Inbound-led | Fast qualification: the one question that confirms fit |
| PLG to enterprise | Usage-led proof and the internal champion's expansion case |
| Partner / channel | What the partner must say, and what they must not |
| Expansion / renewal | The value delivered since signing |

## Roster tier and Re-check by

Two cells in the deal block, outside the word count.

**Roster.** Read `roster_position` from the front matter of the newest profile record in `/context/competitor-profiles/` (the same record the card already reads for claims). 1 or 2 is High, 3 or 4 is Medium, 5 is Watch. Written `#2 of 5 · High`. No profile record, or the competitor is not on the roster: write `not on roster`. Never invent a tier and never ask for one.

**Re-check by.** The date of the oldest competitor claim displayed on the card, plus about 90 days (the re-check window above). If that date has already passed, write `now` and name the claim in Check before use. The deal block shows the month; the saved record shows the full date. A saved card is never edited when it passes this date: it is flagged on the `competitive-profile` freshness board and rebuilt on request.

## The card (template)

This markdown is the Google Doc version. The HTML page carries the same headers in the same order.

```markdown
# [Us] vs. [Competitor]
**BATTLECARD · INTERNAL USE ONLY**

| | | | |
|---|---|---|---|
| **Role** | [role] | **Stage** | [stage] |
| **Motion** | [motion] | **Buyer** | [persona] |
| **Competitor is** | [incumbent / challenger / final two / status quo] | **Segment** | [segment, region] |
| **Win rate vs [Competitor]** | [x% (source, n, window) or "no data"] | **As of** | [Mon YYYY] |
| **Roster** | [#n of 5 · High, Medium or Watch, or "not on roster"] | **Re-check by** | [Mon YYYY, or "now"] |
| **Brain read** | [sections or "none (Quick-Brain)"] | **Assumptions** | [list or "none"] |

## ⚠️ Check before use
[Only if needed: stale brain section, thin data, legal-review rule, past-dated roadmap item, or logged field results (two or more outcomes): "Field results: n=3, 2 won, 1 lost (seller-reported)".]

## 🏆 Win condition
[One sentence: the deal where we beat them. Plain text, no bold.]

## 🎤 Say this first
> "[35 words at most, tuned to the persona, speakable aloud.]"

## 🔍 Competitor snapshot
*Axis: [x] vs. [y]*
| | [Competitor] | [Us] |
|---|---|---|
| **Buyer and use case** [🟢/🟡/⚪] | | |
| **Value promise** | | |
| **Business-metric link** | | |
| **Price and terms** | | |
| **Who wins where** | | |

(each cell: one line, one evidence tag; shading mark on the row label for the side it describes best)

## ❓ Discovery questions (4 at most)
| Question | Why it works |
|---|---|
| "[Question]" | [the specific gap it exposes] |

## 🔄 Reframe their strengths (4 at most)
| What they say | Reply |
|---|---|
| "[Claim or objection]" | "[Quotable reply. First clause acknowledges what is true.]" |

## 🚦 Win vs. walk away
**✅ Lean in:** [3 signals]
**🛑 Walk away:** [3 signals, one about the champion or the incumbent relationship]

## 💎 Proof to use (3 at most)
- **[Claim]**: [one line] [tag]

## 🧭 Next move ([stage])
[One or two lines: the concrete next action for this persona and stage.]

*Sources: [list] · Internal use only. Do not forward to customers.*
```

Snapshot rows are fixed at five. Add a sixth only when the deal turns on it (integrations, compliance, deployment), and then cut the weakest of the others. In the Doc version, shading is carried by the 🟢 🟡 ⚪ mark in the row label; in HTML it is the cell background plus the same mark, so it survives black-and-white printing.

## Slack variant

Used when the card is requested from a Slack thread (`competitive-profile/references/slack-mode.md` section 11). Slack text does not render tables reliably, so the card keeps the same blocks in the same order and drops the tables.

| Block | In Slack |
|---|---|
| Title and deal table | Title line, then one line: `Role · Motion · Stage · Buyer · Competitor is · Segment · As of · Roster · Re-check by` |
| ⚠️ Check before use | Unchanged, plain text |
| 🏆 Win condition, 🎤 Say this first | Unchanged |
| 🔍 Competitor snapshot | Axis line, then five bullets in the same row order (Buyer and use case, Value promise, Business-metric link, Price and terms, Who wins where). Each bullet: mark (🟢 🟡 ⚪), row name, one line for them, one line for us |
| ❓ Discovery questions | Bullets: "Question" followed by why it works |
| 🔄 Reframe their strengths | Bullets: "They say" followed by the quotable reply |
| 🚦 Win vs. walk away, 💎 Proof, 🧭 Next move | Unchanged |

Block names are bold lines. The word ceiling (450), the caps per block and the footer stay the same. Evidence tags stay in the saved record; the thread shows the source in words and a date.

## The saved record: `/context/battlecards/<competitor-slug>-YYYY-MM-DD.md`

One file per run. If a file for the same competitor and date exists, add `-2`, `-3`. Never overwrite an earlier card.

```markdown
# Battlecard record — [Us] vs [Competitor] — [YYYY-MM-DD]
Brain read: [sections present, or "Quick-Brain, session only"]
Deal: [role · motion · status · persona · stage · segment, region]
Assumptions: [what was assumed because it was skipped, or "none"]
Sources named this run: [list, each with category, tool and date for pulled items]
Changed since last card ([date]): [up to 3 lines, or "first card"]
Roster: [#n of 5 · tier, or "not on roster"]
Re-check by: [YYYY-MM-DD, or "now"]

[the card, exactly as delivered]

## Evidence log
| id | claim | tag | source | as_of |
|---|---|---|---|---|
| C-1 | [one atomic claim] | [tag] | [file, URL or call title] | [YYYY-MM-DD] |

## Open items
- Our-side claims excluded for lack of proof: [claim] `[NEEDS PROOF]` (to register: `proof-points`)
- Proposed brain write (Section 3): [shown and confirmed, declined, or none]
- Gap raised: [gap id, or none]
```

Evidence ids (`C-1`, `C-2`, …) are local to this file. They are not brain evidence ids (`E-001`), which only `product-marketing-context` writes.

## Proposed Section 3 note (write-back)

Appended under brain Section 3 only after the user confirms the exact text. Never edits existing text, never touches another section.

```markdown
### Battlecard Field Notes — [Competitor] (added via competitive-battlecard, [YYYY-MM-DD])
- [Dated fact the map lacks] [src: <where> | <YYYY-MM-DD> | <pulled|inferred|stated> | draft]
- [Objection or loss reason seen in field data, with n] [src: <tool> | <YYYY-MM-DD> | pulled | draft]
```

A stub for a competitor missing from Section 3 is one line in the same block: `- Named alternative: [Competitor] (not yet in the map; run alternatives-map)`.

## Related formats

- The index of saved cards for a roster ("set of cards"): `references/pack-format.md`.
- Logged deal outcomes and how they reach Section 3: `references/outcome-log.md`.
