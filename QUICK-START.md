# Quick Start

## 1. Install

```bash
npx skills add stefanoskarakasis/Product-Marketing-Skills -a claude-code
```

Prefer the plugin marketplace? See the [README](README.md#installation).

## 2. Build your brain

Open Claude Code in your project and run
the `product-marketing-context` skill. It opens by asking for your website,
pricing page, deck or call notes and builds from those first. Then it asks
about what is still empty, one section at a time. Answer, edit or skip each
one. The sections:

- Product context (what you sell, to whom)
- ICP (company size, persona, pain points, buying triggers)
- Alternatives and positioning
- Voice and tone
- Market context
- Proof points
- Strategy and execution (recommended, not required)

Answers save to `/foundation/brain.md`. When the brain is built, the skill also writes a short map into your project's `AGENTS.md`, so your agent reads the brain in every chat, not only when you call a skill. Details: [docs/agents-map.md](docs/agents-map.md).

**No time for 15 minutes?** Copy [`examples/example-brain.md`](examples/example-brain.md) to `/foundation/brain.md` to see what the skills produce, or start with `alternatives-map`, `ideal-customer-profile` or `proof-points` in `pmm-positioning`: each works from your own notes and starts your brain.

## 3. Connect your tools (optional)

Skills work without this. If you want them to pull facts from your own
tools (call recordings, CRM, docs) instead of asking you to paste them,
install each plugin on its own and sign in when Claude asks. Steps and
troubleshooting are in [docs/connect-your-tools.md](docs/connect-your-tools.md).

## 4. Run a skill

Once your brain exists, any brain-dependent skill in this repo reads it
automatically. Try:
- "Build positioning for our platform" 
- "What tier is this launch?" 
- "Run a retro on our last launch"

## 5. Keep it learning (2 minutes a week)

Nearly every skill logs what it learns. Nothing improves until you read it back.

The sweep is the `meta-synthesis` skill, which lives in the `pmm-meta` plugin. If you installed plugin by plugin or picked skills one at a time, make sure `meta-synthesis` is included.

- **Every Friday:** say "run the weekly learning sweep". You get one list of proposed guardrails and brain edits and a table of which skills were used. Approve what is right.
- **Want a reminder?** At the end of the sweep, say yes to "Want this every Friday?" and a scheduled task does the counting for you. Your project map also tells you in chat when a sweep is overdue.

## What You Can Do (48 skills across 10 plugins)

See the [main README](./README.md) for the full skill list and what each
plugin covers.

## Troubleshooting

**"I want to run a skill but haven't built my brain yet."**
Most skills will still run — they'll ask you a few direct questions instead
of reading the brain, and tell you the output would be sharper with a brain
in place. Build the brain with `product-marketing-context` whenever you're
ready. A few need one thing first: `go-to-market-strategy` sends you to
`beachhead-segment` when there is no ICP, and `positioning-messaging` needs a
named buyer and three alternatives, including doing nothing.

**"Can I use this with Claude Code, Cursor, Codex or Claude on the web?"**
Claude Code and Codex: yes, tested (`npx skills add` installs for both). Cursor: the skills are
standard `SKILL.md` folders and the manifests pass Cursor's schemas, but nothing here has been
run inside Cursor itself. Claude on the web or desktop: upload skills as zips from Settings.
Details and the folder for each agent are in the README ("Option 2").

## Questions?

[Open an issue](https://github.com/stefanoskarakasis/Product-Marketing-Skills/issues)
or reach out to [Stefanos](https://github.com/stefanoskarakasis).

If this is useful, star the repo — it helps others find it.

⭐ [Star on GitHub](https://github.com/stefanoskarakasis/Product-Marketing-Skills)
