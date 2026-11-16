# Discovery call prep: set it up brain first

`discovery-call-prep` takes the prospect company and the title of the person you are meeting. It researches the account and returns a point of view (one lead hypothesis, one fallback) and a 7-stage plan sized to the call. In Slack it is a 150-word card; the full plan goes to a Doc or the chat.

## Use it when

- A first call is booked and the seller needs a bet and the questions to ask.
- An open deal has a call today and needs the short form (this took over `prep` from `deal-review`).
- A transcript is in and the next call needs a plan (`next`).

Do not use it to decide whether to contact an account (`prospect-research`), to judge whether a deal is real (`deal-review`) or to answer a pushback (`objection-handling`).

## Set it up, in this order

1. Install `pmm-sales`, then build the brain with `product-marketing-context`.
2. Run `/pmm-sales:discovery-call-prep setup`. It checks the brain fields it reads (offerings, pains, persona, sales cycle, alternatives, objections, approved proof, approvals) and names the thinnest one and the skill that fills it.
3. Name the owner of discovery knowledge.
4. The owner decides, per source, whether Claude may read calls and CRM outcomes. The decision is recorded with role and date and asked again after 90 days.
5. Pick the recorder path: a recorder connector, a transcript saved in a folder, a drop folder, or a paste. Any recorder works. See [Connect your tools](connect-your-tools.md).
6. Run `prospect-research` on one account, then your first plan.
7. Give sellers the [seller card](../pmm-sales/skills/discovery-call-prep/references/seller-card.md).

## How it learns without sellers typing

`sweep` matches calls to plans by attendee domain within 24 hours and grades each plan from the transcript (strongest), CRM outcome, and a weak calendar signal. A seller can add `log:` but never has to. Rates show only from 10 cases, and there are no per-seller statistics.

## Not yet proven live

Gong, HubSpot, Zoom, Teams and real Meet transcripts are described but not tested against live accounts. Run one `sweep` on real calls before relying on the grades.
