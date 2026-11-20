# Discovery call review: set it up brain first

`discovery-call-scoring` takes a discovery call you already ran. It scores the seven stages, names your pattern, replays the moments that cost you and gives two to four moves with the words to say. It reads your brain and never writes it. It works with a pasted transcript and needs nothing else.

## Use it when

- A discovery call is done and you want to know what you missed.
- You want to know whether you are getting better across calls (`trend`).
- You have a plan from `discovery-call-prep` and want to see what the call did with it.

Do not use it to judge whether a deal is real (`deal-review`), to plan a call (`discovery-call-prep`), to summarise a call (`interview-summary`) or to answer a pushback (`objection-handling`).

## Set it up

1. Run `discovery-call-prep` `setup` first. It checks your brain and records who owns discovery knowledge and whether Claude may read recorded calls. Review uses the same decisions.
2. Pick the recorder path: a recorder connector, a transcript saved in a folder, a drop folder, or a paste. Any recorder works. See [Connect your tools](connect-your-tools.md).
3. Give sellers the [seller card](../pmm-sales/skills/discovery-call-scoring/references/seller-card.md).

## It is private

A review is about the seller, so it goes to the seller only. It never goes to a manager, nothing is ranked, the transcript is not saved and `_reviews.md` holds counts with no seller field. A manager view is a separate decision with legal review and is not part of this skill.

## How it learns without sellers typing

Each review appends one counts-only row. `discovery-call-prep` shows a seller their own last review on their next plan. `sales-research-digest` shows counts. `objection-handling` ranks cards by what comes up on calls. Rates show only from 10 reviews. Proposals to the PMM start at the counts in the skill's feed-forward file.

## Not yet proven live

The marks are model judgement. Run five real calls through it, read each review beside the transcript, and note every mark you disagree with before sellers rely on it.
