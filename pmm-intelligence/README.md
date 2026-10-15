# pmm-intelligence

A weekly read on what changed around your product, tied to your brain.
`signal-monitor` takes the signals you name (competitor pages, search and
traffic shifts, win/loss notes, pasted news) and returns at most five
opportunities. Each one is tied to a brain field and to a Section 7
priority, so you can tell what matters from what is only interesting.

## Start here

- **You get:** a short weekly list of opportunities, each with the evidence, the brain field it touches, and one suggested next move.
- **First command:** `/pmm-intelligence:signal-monitor` (works with pasted signals; no connector needed)
- **Try:** "Here is what changed on two competitor pricing pages this week: [paste]. What matters for us?"
- **The brain:** Sharper with a brain (Sections 3 and 7 especially). With no brain it asks three quick questions and holds the answers for the session only. The brain-building skill is a separate plugin, `product-marketing-context`.

## Skills (1)

- **signal-monitor** — Turn the signals you name into at most five
  opportunities, each tied to a brain field and a Section 7 priority, with
  the evidence, a confidence label and one suggested next move. Read-only:
  it saves a dated list to `/context/signals/` and never changes your brain.

## Connectors (Optional)

Every skill works without connectors. Install this plugin on its own to load its `.mcp.json`. Only the sources you name in a run are read.

| Category | What it adds | Tools |
|---|---|---|
| `~~market data` | competitor traffic and audience shifts | Semrush |
| `~~team chat` | team threads, launch coordination, field feedback | Slack |
| `~~email` | customer and stakeholder email context | Gmail |
| `~~calendar` | meeting cadence, launch dates and attendees | Google Calendar |
| `~~SEO` | keyword demand, competitor organic positioning | Semrush |
| `~~company data` | funding, headcount, hiring and leadership changes for a named company | Crunchbase |
| `~~web research` | open-web search and page fetch for competitor moves, launches and market signals | Exa |

Sign-in steps: [`docs/connect-your-tools.md`](../docs/connect-your-tools.md). Category list: [`CONNECTORS.md`](CONNECTORS.md).

## Commands (1)

- `/pmm-intelligence:signal-monitor` — Run this week's read.

## Weekly use

Schedule it, then read the result and decide. The pattern is in
[`docs/ai-marketer-loop.md`](../docs/ai-marketer-loop.md).

## What it will not do

- It will not scan the web on its own. It reads only the sources you name in the run.
- It will not edit your brain. A suggested brain change goes to `product-marketing-context`, which asks you first.
- It will not list more than five opportunities, or one with no evidence.
