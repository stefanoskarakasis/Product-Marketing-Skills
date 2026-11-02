# Design Handoff

How the page leaves the skill as a layout. The copy and the ledger are the same in every target; only the container changes.

## Contents
1. Choosing the target
2. Claude Design (default in Claude)
3. HTML or Doc
4. Figma text spec
5. Block map (all targets)

## 1. Choosing the target

Ask once, in setup, only if the user has not said: "Where does this page get built: Claude Design (a clickable wireframe you can edit), a Doc or one-column HTML, or a Figma file?" Default: Claude Design when the session offers a Design artifact type; otherwise HTML. A named target in the request wins. The target never changes the claims: a held public render stays held in every target.

## 2. Claude Design (default in Claude)

- Build one fluid artboard, about 1280 px wide, that shrinks to a phone-width column. Grayscale wireframe, one accent. Blocks are real markup so the user can retype text and restyle.
- Use the block map below, in order. Put a ledger id on every table cell, a dashed amber `[PASTE]` on every value the evidence could not fill, and no invented stat, logo or quote.
- If the public render is held, show a status strip at the top saying why. A wireframe of a held page is allowed because it contains no unsourced claim; label it.
- Create the Design artifact only after the page passed the Quality Gate, and never publish content the gate cut. The link is private until the user shares it: say so.
- Not in Claude, or no Design type listed: use section 3.

## 3. HTML or Doc

A single column, same block order, same ledger tags. Prefer a Doc for review and edit, HTML for a page the user will host.

## 4. Figma text spec

For teams that build in Figma. Produce `figma-spec.md`: frame order, table column widths, the value vocabulary as component variants (Yes, Partial, Beta, Plan-gated, Not publicly available, No), a one-column mobile layout, copy per frame with ledger ids, a state for expired claims (flag, do not hide), and accessibility notes (no meaning by color alone). It is a text spec, not a Figma file, and has not been tested against a live Figma connector. Say so.

## 5. Block map (all targets)

1. Title, owner, updated date, next review date.
2. Verdict above the fold, one CTA.
3. Compare-at-a-glance table (8 to 12 rows, fixed value vocabulary, unit column on prices).
4. Who should choose which, plus a "where the rival wins" callout.
5. Pricing, with units and an as-of date.
6. Switching block: what moves, what does not, sample run, undo or keep-both.
7. Proof: quote, case study and rating blocks, only those that have a source.
8. FAQ from real buyer questions.
9. One closing CTA.
10. Trust footer: methodology, affiliation disclosure, sources, expiry rule.
