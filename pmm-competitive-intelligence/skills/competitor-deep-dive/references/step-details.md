# Step details

Moved verbatim from `SKILL.md`.

## Step 2: scope table and connector prompt

| Variable | Options | If skipped |
|---|---|---|
| Competitor | A named rival (a DIY build or doing nothing is a status-quo study, not a deep-dive: route to `alternatives-map`) | Required |
| Decision this supports | Strategy call · RFP response · Pricing change · Roadmap bet · Battlecard source · General reference | General reference |
| Main audience | Sales · Product · Exec · PMM | PMM |
| Depth | Standard (about 2,500 body words) · Short (about 1,500) · Long (up to 3,500) | Standard |
| Delivery | Google Doc (paste-ready, shown here in chat) | Always ask; Google Doc if unanswered. Not asked in Slack: a summary is posted and the Doc is the full document |
| Pricing and deal sources | Connect · Paste · Skip, one choice per not-connected row of the readiness table | Skip, stated in Check before use |

The decision line shapes emphasis, never section order.

**Connector prompt (same message, once).** Show the readiness table, then for each row that is not connected give three options and name the consequence:
1. **Connect.** Name the tool this plugin wires for the category (see "Wired today" in this plugin's `CONNECTORS.md`) and point to `docs/connect-your-tools.md` for sign-in steps. Wait for "connected", re-check which tools are present, and say what the first pull returned (for example "14 deals naming [competitor], Jan 2025 to Oct 2026"). If the tool still is not present, say so and offer Paste or Skip; never pretend.
2. **Paste.** Ask for the smallest useful thing: a closed-won and closed-lost export for this competitor, call excerpts that mention them, or the pricing notes. Pasted material is rank 5 unless it is a hard record the user confirms.
3. **Skip.** The section is built from what exists and carries its status line (see the template). Skipping is always allowed.

Do not nag: one prompt per run, no second reminder. The one exception: if the decision is Pricing change or RFP response and both Part 4 deal pricing and Part 6 would be empty, say in one sentence that a list-price-only deep-dive will not support that decision, and ask for Connect, Paste or "proceed anyway" before researching. A "proceed anyway" is honoured and recorded in Check before use. If the user says "just give it to me", use the defaults, state them in Check before use, and offer to tailor.
