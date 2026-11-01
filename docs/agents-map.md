# The agent map, the helper scripts and the send guard

Three small things that make the brain work in every chat and keep your agent from sending something you never approved.

## The map

When your brain is built, `product-marketing-context` writes a block of about 230 words into your project's `AGENTS.md`. It lists the brain's sections and what each is for, the records that exist (battlecards, competitor profiles, and so on), and the two helper scripts. Your agent reads it at the start of every session, so it knows your brain exists even when you do not call a skill.

- It adds one block between `<!-- pmm-skills:map start` and `<!-- pmm-skills:map end -->`. Your own text in `AGENTS.md` is never touched.
- It adds a marked `@AGENTS.md` line to `CLAUDE.md` so Claude Code reads the map. It creates `CLAUDE.md` if you have none.
- Refresh it any time with `/product-marketing-context:agents-map`. A second run with nothing new changes nothing.
- To remove it, delete the marked block in `AGENTS.md` and the marked lines in `CLAUDE.md`.

The map holds pointers, not company facts. Your facts stay in the brain.

## The helper scripts

Copied to `foundation/tools/` so the map can name them. Plain Python 3, no installs. Every skill still works without them.

- `python3 foundation/tools/brain_section.py 3` prints one section (`1,4,6` prints several), so an agent reads what it needs.
- `python3 foundation/tools/lint_draft.py draft.md` checks a draft against your forbidden phrases (Section 4), forbidden claims (Section 6) and prohibited topics (Section 8). It also lists numbers that are not in your approved metrics and leftover `[NEEDS PROOF]` markers. It is a plain text search: read each hit in context.

## The send guard (Claude Code)

Skills say "show the draft and wait for your yes". An instruction can be skipped; a hook cannot. The `pmm-competitive-intelligence` plugin ships a hook that asks you before a connector tool sends, posts, replies to or forwards a message through Slack, Gmail, Outlook or Teams. Reading, searching and drafting are never asked about.

- Turn it off: set `PMM_GUARD=off`.
- Allow one service, for example for a scheduled run you have already approved: set `PMM_GUARD_ALLOW=slack` (a comma list works).
- It needs `python3` on your path. If Python is missing the guard does nothing and your run is not interrupted.
- It works in Claude Code. Other apps do not run Claude Code hooks, so rely on the skills' own approval steps there.
