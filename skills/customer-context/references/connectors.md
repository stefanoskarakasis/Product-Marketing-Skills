# Connectors

Every category is optional. A category counts as connected only if a tool for it is present and answers; `.mcp.json` lists what is wired, not what you are signed in to.

| Category | What it adds | Used in | Without it |
|---|---|---|---|
| `~~CRM` | Account, contract and renewal opps, contacts by last touch, activities, owner, competitor field | Steps 4, 8, 9 | Paste the account row; flags needing CRM say "not queried" |
| `~~email` | Threads with the account's domain | Step 5 | Skip the section and say so |
| `~~calendar` | Recent and upcoming meetings, attendees | Steps 4, 9 (cadence, silent account) | Skip |
| `~~call recordings` | Latest call, objections and customer phrases as said | Steps 6, 8 | Paste a note or transcript |
| `~~cloud storage`, `~~knowledge base` | Account plan, success plan, proposal, contract docs | Step 6 | Paste |
| `~~team chat` | Escalations, deal desk, exec mentions | Step 7 | Skip |
| `~~support` | Open and recent escalations by theme | Step 7 | Skip |
| `~~product analytics` | Adoption trend, teams using the product | Step 7 | Usage flags say "not queried" |
| `~~revenue intelligence` | Engagement and pipeline health for the customer | Step 9 | Docs-only today: paste |

If a fact comes from a connector, tag it with category, tool and date. Pulled facts are drafts until the owner or user confirms them.
