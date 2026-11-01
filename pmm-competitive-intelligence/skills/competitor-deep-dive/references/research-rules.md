# Research rules

Moved verbatim from `SKILL.md`.

## Step 3: tags, source order and evidence rules

Tag every claim with the evidence tags in `competitive-battlecard/references/card-format.md`: `[Field: <tool>, n=<n>, <window>]`, `[Brain S<n>]`, `[Internal <Mon YYYY>]`, `[Public <Mon YYYY>]`, `[Third-party <Mon YYYY>]`, `[A]` and `[NEEDS PROOF]`. This skill defines no tags of its own. The two flags outside that table are used as the sibling skills use them: `[Rep-stated]` for an unsourced Quick-Brain answer and `[NEEDS APPROVAL]` for a customer name or quote without approval (a Section 6 flag, not an evidence tag). Pulled facts carry category, tool and date. Source order follows `product-marketing-context/references/evidence-format.md`: confirmed brain values (rank 0), then `~~CRM`, `~~win/loss`, `~~call recordings` (ranks 1 and 2), then `~~competitive intelligence` (rank 3, read only), then public and third-party material (rank 4), then chat (rank 5). A fact older than 12 months drops one rank; older than 24 months, two. Newer evidence that disagrees with a confirmed value is shown as a question, never used to replace it.

Rules that carry most of the weight:
- **Date everything.** Every external claim carries a source, a link where one exists, and "as of [Mon YYYY]". Date every review. When the same complaint appears in old and new reviews, that is the finding: say how long it has run.
- **Say when you don't know.** "No public evidence of X" is not "X doesn't exist". Use the first unless you have verified the second.
- **Reviews have no permalink.** Link the product review page and say once, in Confidence, that the page is the closest available reference.
- **Review dates from rendered pages are approximate.** Say so; if one date is wildly out of pattern, omit that review and say you did.
- **Internal intel is secondhand.** Pricing from a deal recap in chat is useful and unverified: cite the thread, label it secondhand, link the vendor page beside it.
- **A rebrand, acquisition or pivot is often the most useful single fact.** Put what changed and what did not side by side.
- **Vendor-authored comparisons are opinion.** Say so. A competitor's own pages prove only what it said.
- Leave out names, emails and phone numbers of individuals.
- **Status line per dependent section.** Part 4 and Part 6 open with one line saying where their evidence came from: "Source: `~~CRM` (tool), pulled [date], n = X", "Source: pasted by user, [date]", or "Not connected: [what is missing]". The line is never omitted and never optimistic.
