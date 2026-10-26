# Pack: the index of saved cards

A pack answers "what cards do we have, and can I trust them?" It is an index. It never builds, refreshes or rewrites a card. Triggered by: "set of cards", "all five competitors", "which cards are current", "card status".

## What is read

1. The roster: the newest record per competitor in `/context/competitor-profiles/` (front matter `roster_position`, 1 to 5), or brain Section 3 if no profile record exists.
2. For each roster competitor, the newest saved card in `/context/battlecards/<competitor-slug>-*.md` (by date, then `-2`, `-3`).
3. Nothing else. No connector, no web, no brain write.

If there is no roster, say so in one line and offer `competitive-profile` `setup`. Do not build a roster here.

## What is shown, per competitor

| Field | Source |
|---|---|
| Competitor and tier | Roster cell: `#n of 5 · High, Medium or Watch` |
| Card date | Record title date |
| Status | `current`, `re-check` (past its `Re-check by`) or `no card` |
| Re-check by | Record header |
| Tailored for | The record's `Deal:` line, verbatim. A card built for one role, buyer and stage says so |
| Win condition | The card's 🏆 line, verbatim |
| Next action | One line. `re-check`: "Rebuild the [competitor] card." `no card`: "Build a card for [competitor]." `current` and deal-tailored: "Tailored to [stage]; build a neutral card for general use." `current`: none |

Order: by `roster_position`. A competitor with no saved card is still listed, as `no card`, so the gap is visible.

## Shapes

**Chat or Doc: one table**, same fields as columns. First line: "Index of saved cards. Nothing was rebuilt."

**Slack: bullets, no table.** One bullet per competitor, then one line for the single most useful next action:

```
Index of saved cards. Nothing was rebuilt.
• #1 Brightwire · High · card 12 Oct · current · re-check by Jan 2027
  Tailored for: AE · outbound · incumbent · CFO · evaluation
  Win condition: [the card's line, verbatim]
• #2 Northgate AP · High · card 3 Jul · re-check (past 3 Oct)
  Next: rebuild the Northgate AP card.
• #3 Tidewater · Medium · no card
  Next: build a card for Tidewater.
Most useful next step: rebuild the Northgate AP card.
```

Words only for status. The emoji legend in `card-format.md` is not extended: no new marks for current, stale or missing.

## Rules

- The win condition is copied, never reworded. If a record has no 🏆 line, show `card record incomplete` and name the file.
- Tier comes from the roster; a competitor not on the roster is not in the pack. If the user names one, say it is not on the roster and offer a single card.
- A competitor listed in brain Section 3 but not in the roster is not added.
- No printed or PDF pack. If asked, say it is not built here and offer the index plus one card per competitor in the formats the card supports.
- Log one Learning Close row with `pattern: none`, or a falsifiable pattern if something surprised you (for example, every card deal-tailored).
