# product-marketing-context

The PMM brain. Build your company context once, in about 15 minutes. Every other plugin reads `/foundation/brain.md` before it writes a word. Install this first.

## Start here

- No brain yet? → `/product-marketing-context:build-brain`
- Brain gone stale? → `/product-marketing-context:refresh-brain`
- Questions waiting in the gaps queue? → `/product-marketing-context:brain-gaps`
- Agent not reading the brain in every chat? → `/product-marketing-context:agents-map`
- Want it to work your way? → `/product-marketing-context:my-context`
- Want to see one first? Open the [example brain](../examples/example-brain.md), a finished brain for a fictional company.

> [!NOTE]
> 💬 **Try it:** "Build my PMM brain for [product]. We sell to [buyer]."
>
> 🧠 **Brain:** this plugin builds it: one file, `/foundation/brain.md`, that the other plugins read.

## Skills (1)

- **product-marketing-context** — Build your PMM brain with a guided setup, refresh stale fields, answer open gaps, and audit an existing brain's health.

## Commands (5)

- `/product-marketing-context:build-brain` — Build or audit your PMM brain.
- `/product-marketing-context:refresh-brain` — Find the fields that have gone stale and re-confirm only those.
- `/product-marketing-context:brain-gaps` — Answer the open questions other skills left in your gaps queue.
- `/product-marketing-context:agents-map` — Write or refresh the short map in your project's `AGENTS.md` so your agent reads the brain in every chat. It runs by itself when the brain is built. Details: [`docs/agents-map.md`](../docs/agents-map.md).
- `/product-marketing-context:my-context` — Tell the brain how you like to work (length, detail, tone of feedback). Saved to `/foundation/me.md`, kept apart from company facts.

## How a brain gets built

The skill starts from what you already have. It asks for your website and pricing page, drafts from them, and takes decks, call notes and win/loss docs if you have them. It then shows the facts it found, with sources, as a proposed brain you approve section by section. It asks questions only about what your material could not answer. Facts live in `/foundation/evidence.md`; if your folder is under version control, do not commit that file, because it can hold customer details. A demo you can run is in [`examples/ingest-demo`](../examples/ingest-demo/).

## One brain, one product

A brain covers one product or platform (modules and plans go in its Offerings block). If your company has several product lines, keep a separate folder, each with its own `/foundation/brain.md`, and run the skills once per product.

## Why This Comes First

Every other plugin in this marketplace — `pmm-positioning`,
`pmm-toolkit`, `pmm-execution`, `pmm-go-to-market`, `pmm-meta` — reads
`/foundation/brain.md` for company context before producing output.
Building it once here means you never re-explain your product, ICP, or
positioning to another skill again.

## Connectors (Optional)

> [!TIP]
> 🔌 **Every skill works without connectors.**
>
> 📋 **Paste what you have and the output keeps its shape.**
>
> ⚙️ Install this plugin on its own to load its `.mcp.json`.
>
> 🔑 Sign-in steps are in [`docs/connect-your-tools.md`](../docs/connect-your-tools.md).
>
> 📖 Every category, its tools and which skill reads it: [`CONNECTORS.md`](CONNECTORS.md).

## Author

Stefanos Karakasis — [Stefanos's Stack on Substack](https://stefanoskarakasis.substack.com/)

## License

MIT
