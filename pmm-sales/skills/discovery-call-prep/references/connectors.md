# Connectors

All optional. A category counts as connected only if a tool for it is present and answers; `.mcp.json` lists what is wired, not what you are signed in to. The plan's last section says which answered and which did not ("not queried"). Pulled facts are drafts, tagged with category, tool and date.

## What helps a seller most

| Tier | Category | Used for | Tools wired today | Without it |
|---|---|---|---|---|
| Core | `~~CRM` | Stage, owner, prior opportunities and closed-lost reasons, contact roles, opt-out fields, the outcome join | HubSpot; Salesforce is connect-your-own | Paste the account row |
| Core | `~~calendar` | Call length, attendees and their roles, the invite note that says why they agreed to meet | Google Calendar | Ask for minutes; default 30 |
| Core | `~~call recordings` | Earlier calls with the account, the debrief, the sweep that grades plans | Gong, Wispr Flow, Granola; any other recorder through the paths below | A transcript file in Drive, or a pasted transcript or notes |
| Strong | `~~web research` | Careers pages, newsroom, filings, press, role job posts | Exa; the built-in web search | Built-in search; pasted pages |
| Strong | `~~company data` | Funding, headcount, hiring and leadership changes | Crunchbase | Web search and filings |
| Strong | `~~email` | The inbound thread, earlier replies from the domain | Gmail | Skip |
| Strong | `~~team chat` | The thread you ask in; the plain-question reply that logs the outcome | Slack | Reply in chat |
| Helpful | `~~cloud storage`, `~~knowledge base` | Saves the plan as a Doc; reads account plans | Google Drive and Docs; Notion, Atlassian | Show in the reply |
| Gap | `~~enrichment` | Company fields for a named account | Docs only (connect your own); company fields only in EMEA mode | Paste |
| Gap | third-party intent (no category yet), `~~revenue intelligence` | Third-party intent; engagement and pipeline health | Docs only | Paste |

Not wired and not recommended for a named contact in EMEA: contact-level enrichment and social profile tools. Company-level data is the safe default.

## Any recorder works: four paths in order

The skill needs a transcript or AI notes for a call, not a particular vendor. Use the first path that answers:

1. **A recorder connector** (Gong, Granola, Fireflies, Otter, Fathom, Grain, Chorus or any other `~~call recordings` tool that is present and answers).
2. **The recorder's own transcript, saved to storage you can read.** Google Meet transcripts and Gemini notes save as Docs in the organiser's Drive; Zoom cloud transcripts and AI Companion summaries and Teams transcripts export as files or sit in OneDrive. Read them through `~~cloud storage` when `_config.md` names the folder (`recording_folder`). Which of these exist depends on the plan and on whether the seller turned them on.
3. **A drop folder.** The owner names one folder; sellers or an automation save transcripts there; the sweep reads it.
4. **A paste.** A seller pastes a transcript or notes; works anywhere.

**Matching a call to a plan:** same attendee domain as the account, within 24 hours of the planned date, else the nearest call within 3 days; if two fit, ask the owner once in the sweep report, never guess. A transcript with no matching plan is ignored, not stored.

**Recording consent is the company's:** read only calls the company already records. Never start or request a recording. In EMEA mode keep roles only in outputs, quote nothing from the call, and keep no transcript text in `/context/` beyond the grade and the evidence line.

## Data access is the owner's decision

Reading call recordings and CRM outcomes is decided by the person who owns discovery knowledge, not the seller. On the first run, `library` and `sweep`, say which of `~~call recordings`, `~~CRM`, `~~team chat` and `~~email` answered, and ask the owner to approve each source (role and date stored in `_config.md` as `data_access`, asked again after 90 days). Until then read nothing from those two connectors beyond what the user pastes or uploads. Raise it once and never block the plan on it.

## Reading guides

- **HubSpot:** deal stage, owner, close-date history, last activity, contact roles by live label. Never amounts in Slack for deals the asker does not own.
- **Salesforce:** take names from the live schema. The Opportunity holds stage and close date; the owner is the Opportunity owner; roles come from Opportunity Contact Roles. Ask once if unclear.
- **Calendar:** read the invite title, description and attendee domains. The description often says why the buyer agreed to meet; use it before writing the opener.
- **Call recordings:** read the newest three calls with the account in full; older ones through the last record.
- **Drive:** a Doc named `Discovery plan: [Company], [YYYY-MM-DD]`. Ask before saving; never to a shared drive without saying so.

## Where the brain lives

| `brain_source` | Read through |
|---|---|
| `repo` | The repo's file |
| `drive` | `~~cloud storage` |
| `notion` | `~~knowledge base` |
| `local` | File read, Claude Code and Cowork only |

Read only the sections the plan needs (`scripts/brain_section.py` when present) so the plan stays cheap to load.
