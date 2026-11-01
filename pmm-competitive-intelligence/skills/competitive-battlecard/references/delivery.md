# Delivery formats

Moved verbatim from `SKILL.md` so it loads only when the step names it.

- **Google Doc (first-class):** show the full card in chat as clean markdown in the exact order of the template in `references/card-format.md`: headings, tables, no HTML, no code fence around it, so the user can select it and paste it into a Google Doc with headings and tables intact. Say that in one line. Do not claim a Google Doc was created, shared or saved to Drive unless a connector actually did it. With a `~~cloud storage` connector that can create a Doc, offer it and ask before writing.
- **HTML page:** copy `templates/battlecard.html`, fill every `{{placeholder}}`, remove unused rows, and save as `Battlecard-<competitor-slug>-YYYY-MM-DD.html` beside the record. One self-contained file, no external dependencies, one stacked column with the same headers as the Doc. If a browser or PDF tool is available, print it and confirm one page; if not, say the page count was not verified.
- **Slack thread:** post the card in the thread in the Slack variant (`references/card-format.md`, "Slack variant"): same blocks and order, no tables, sources in words. Offer a Google Doc if a `~~cloud storage` tool can create one; otherwise say where the full card is saved. The record is saved as usual.
- **Anything else** (Word, PDF, slides): say it is not built here and offer the two formats above.
- When the HTML file was chosen, the chat reply is the 🏆, 🎤 and 🧭 sections plus the file, not a second copy of the card.
