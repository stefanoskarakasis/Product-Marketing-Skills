# pmm-sales

Sales skills for sellers and CSMs, built for Slack first: tag Claude in a thread and get the state of a customer, the reason to contact a prospect, the next step on a deal, the next line for an objection or a scored discovery call, every line sourced.

## Start here

- Researching a company you do not sell to yet? → `/pmm-sales:prospect-research`
- Catching up on a customer before a renewal? → `/pmm-sales:customer-context`
- Live deal that might stall? → `/pmm-sales:deal-review`
- Discovery call coming up? → `/pmm-sales:discovery-call-prep`
- Discovery call just ended? → `/pmm-sales:discovery-call-scoring`
- Buyer just pushed back? → `/pmm-sales:objection-handling`
- Weekly report for the PMM? → `/pmm-sales:sales-research-digest`

Try it in Slack: "@Claude review the Marlow deal before Friday's call". Every skill reads your brain (`product-marketing-context`) and never writes to it.

## Skills (7)

- **customer-context** — Before a renewal call, QBR or escalation, it builds a dated brief on one existing customer from your CRM, email, calls, docs, support and usage, checks it against your brain and shows what changed since the last brief. Read-only, and it works in a Slack thread.
- **prospect-research** — Before a first touch, it tells you whether there is a reason to contact one company you do not sell to yet: dated signals mapped to your pains, fit and timing scored separately, and a hypothesis with an angle, a first question and a fallback. EMEA data rules stay on for European accounts.
- **deal-review** — On one live deal that may be stalling, it ranks the evidence by source, shows what the buyer decided in their own words, names the most likely reason the deal dies and gives dated next steps. It also builds a weekly queue of the deals that need you and debriefs a call transcript.
- **discovery-call-prep** — With a prospect company and the title of who you are meeting, it researches the account and returns a point of view, one lead hypothesis with a fallback and a seven-stage plan: the opener, ready-to-ask questions, what good looks like per stage and a fast-disqualify line. It also preps follow-up and open-deal calls.
- **discovery-call-scoring** — Right after a discovery call you ran, paste the transcript and it scores the seven discovery stages, names your pattern, replays the moments that cost you and gives two to four next-call moves with the words to say. Private to the seller: it never goes to a manager.
- **objection-handling** — When a buyer pushes back, it names the type behind the words and gives you the next line, a call digest or a paste-ready email reply, then logs the objection so a shared library improves with every deal.
- **sales-research-digest** — Every week it gives the PMM one plain-language report on how sellers used the research skills: who used them, whether the advice held up against CRM outcomes and up to three things to do. It covers pmm-sales skills only and proposes, never changes.

## Commands (7)

- `/pmm-sales:customer-context` — Get the current state of one customer.
- `/pmm-sales:prospect-research` — Get the reason, angle and first question for one prospect.
- `/pmm-sales:deal-review` — Review one live deal and get the next step.
- `/pmm-sales:discovery-call-prep` — Get the plan for a discovery call.
- `/pmm-sales:discovery-call-scoring` — Get your discovery call scored and coached.
- `/pmm-sales:objection-handling` — Get the next line for a buyer objection.
- `/pmm-sales:sales-research-digest` — Get the weekly report on how the sales research skills are used.

## Connectors (Optional)

Every skill works without connectors: paste what you have and the output keeps its shape.
Install this plugin on its own to load its `.mcp.json`; sign-in steps are in [`docs/connect-your-tools.md`](../docs/connect-your-tools.md).
The full reference, with every category, its tools and which skill reads it, is in [`CONNECTORS.md`](CONNECTORS.md).

## Author

Stefanos Karakasis — [Stefanos's Stack on Substack](https://stefanoskarakasis.substack.com/)

## License

MIT
