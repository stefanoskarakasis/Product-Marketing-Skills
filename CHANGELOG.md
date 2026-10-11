# Changelog

## v1.12.1 — 2026-10-11

This release rolls up six steps (1.7 to 1.11.1) that were built in order and shipped together. The sections below keep each step's notes. A first upload labelled 1.12.0 missed the hidden files (manifests, `.github`, `.gitignore`); it was never released, and 1.12.1 is the complete release.

### Step 1.11.1

#### Test text and labels now match reality

- The eval fixtures in `prioritization-frameworks`, `stakeholder-maps`, `prd` and `pre-mortem` no longer describe brain sections that never existed ("Revenue Levers", "Personas (§4)"). They now use Sections 2, 3, 7 and 8, and the `prd` fixture takes persona detail from the session log, as the skill does. A new test keeps those phantom sections out.
- `interview-summary` 2.5.0 states its brain contract: it reads Sections 2 and 3 only to check the ICP match and compare alternatives, and never writes the brain.
- `SKILL-SPEC.md` 2.6.1: the lists of brain-dependent and context-agnostic skills now match each skill's `context:` label. Before this, `prd`, `experiment-doc`, `prioritization-frameworks` and `interview-summary` were listed as agnostic while using the brain, and `product-marketing-context` was labelled agnostic. A new test checks the lists against the labels.

### Step 1.11.0

#### A weekly read on the world, tied to your brain

- New plugin `pmm-intelligence` with one skill, `signal-monitor` (`/pmm-intelligence:signal-monitor`). It reads only the signals you name (pasted notes, files, URLs you list, or `~~market data` and `~~SEO` connectors) and returns at most five opportunities. Each has evidence with a source and date, the brain field it touches, the Section 7 priority it serves, a confidence label and one suggested next move.
- Read-only for your brain. It saves a dated list to `/context/signals/` and hands off any brain change to `product-marketing-context`, which asks first. One source is never `high` confidence, and a company's own claims are never treated as proof.
- With no brain it asks three quick questions and holds the answers for the session.
- `workflow-orchestrator` 2.5.0 adds a "Weekly Opportunities" workflow (`/run weekly-opportunities`).
- New page `docs/ai-marketer-loop.md`: know, notice, decide, act, learn, and how to schedule the weekly read.
- The skill count is now 36 across 8 plugins.

### Step 1.10.0

#### Your brain knows how work gets done, and how you like to work

- New optional Section 8, Execution: stakeholders, approvals, what is prohibited, channels and cadence. The audit reports it as "not built" rather than a gap, and refresh treats it as stale after 180 days.
- `stakeholder-maps` starts from your Section 8 stakeholders and can propose new ones. `pre-mortem` tests approval lead times and prohibited claims. `proof-points` flags a claim that touches a prohibited topic and notes who approves it.
- New "My context" mode (`/product-marketing-context:my-context`) and `/foundation/me.md`: how you like outputs (length, detail, shape, how blunt). Skills read it for format and detail only, never for company facts, and your request always wins. Six skills adopt it: `positioning-messaging`, `product-messaging-playbook`, `go-to-market-strategy`, `pmm-okrs`, `gaccs-brief` and `writing-assistant`.
- `SKILL-SPEC.md` v2.6.0 adds the personal context rule.
- Evals added for each changed skill.

### Step 1.9.0

#### Build your brain from material you already have

- New ingest mode in the brain skill: give it your website and pricing page, then optionally customer calls, planning notes or decks. It extracts atomic evidence, compares sources, and shows a Brain Diff you approve section by section. Nothing is written without your yes.
- Two or more agreeing sources are tagged `pulled`; one source is `inferred`. Conflicts are shown side by side and never resolved for you. A value you confirmed is never overwritten.
- Website copy is never treated as proof. Personal data (emails, phone numbers) is not stored.
- New `references/evidence-format.md`: the evidence file format and the authority ranking.
- New practice kit `examples/ingest-demo/`: five fictional sources plus the expected evidence and Brain Diff, so you can check the skill against a known answer.
- Evals 15 to 23 cover URL fallback, conflicts, caps, personal data and approvals.

### Step 1.8.0

#### Your brain stops going stale

- New refresh mode (`/product-marketing-context:refresh-brain`): lists only the fields that are past their section's freshness limit and asks, one at a time, whether each is still true, changed, or should be dropped.
- New gaps queue (`/foundation/gaps.md`) and mode (`/product-marketing-context:brain-gaps`). When a skill needs a fact the brain lacks, it now asks one question in the moment. Skip it and it is saved to the queue for later; a skipped question stays quiet for 30 days.
- `positioning-messaging`, `go-to-market-strategy`, `product-messaging-playbook`, `gaccs-brief` and `pmm-okrs` ask that one gap question. The rule is in `SKILL-SPEC.md` for other skills to adopt.
- The health audit now reports open gaps and the oldest field in each section.
- New page `docs/keep-your-brain-fresh.md`, including how to schedule a weekly read-only check. Nothing updates your brain without your yes.
- New test: the sections in the brain template must match the schema.

### Step 1.7.0

#### Your brain now shows its sources

- Every brain field can carry a source tag: where it came from, the date, whether you stated it or it was pulled or inferred, and whether it is confirmed. Brains without tags keep working.
- New optional Section 7, Strategy: priorities, launches, quarterly goals, active bets and what you are not doing.
- New Offerings block in Section 1: how it is packaged, approved terminology and permitted claims.
- One canonical schema, `product-marketing-context/references/brain-schema.md`, and a test that fails if a skill cites a brain section that does not exist.
- Fixed: the build-brain command pointed to a step that does not exist and listed an invocation that does not match its name. The stale skill table in the brain template is replaced by a pointer to the schema.
- One brain covers one product or platform. The README and the brain plugin now say so; for several product lines, keep one folder and one brain per product.
- `pmm-okrs` and `go-to-market-strategy` now read Section 7. `pmm-okrs` can propose a Section 7 update, only after you confirm it. Leftover references to a brain section called "Revenue Levers", which never existed, are removed from `retro`, `interview-summary` and `pmm-okrs`.
- The brain skill now offers next steps from `next-skill-map.md`, and a test checks every skill name in that file. A value you confirmed is never overwritten by newer evidence: the skill shows both and asks.
- "Not applicable" now reads `N/A` everywhere. The last retired-prefix and storefront links outside the root README are removed, and tests keep them out.

## v1.6.0 — 2026-10-10

### Keep your quick answers

- `gtm-motions` and `positioning-ideas` now ask, once, after the output, whether to keep the
  Quick-Brain answers as the start of your brain, so the next skill does not ask the same
  questions again. Only on a yes: `gtm-motions` writes a Section 2 stub, `positioning-ideas`
  writes a Section 3 stub with the alternatives, both under the `🟡 Cold start` line and tagged
  user-stated. Neither overwrites an existing section, and neither ever writes the motion stack
  or the positioning options.

## v1.5.0 — 2026-10-10

### Fewer dead ends

- `gtm-motions` and `positioning-ideas` no longer stop when there is no brain.
  `gtm-motions` asks two Quick-Brain questions (best-fit buyer, self-serve or sales
  conversation); `positioning-ideas` asks for what you sell, the best-fit buyer and
  three alternatives including doing nothing, tagged user-stated. Both are session-only
  and never write to the brain.
- `value-prop-statements` asks you to paste or write your positioning instead of
  sending you to another plugin, and still never invents one.
- `go-to-market-strategy` wording now matches its Step 0: with no brain it sends you
  to `beachhead-segment` in the same plugin. It no longer names `product-marketing-context`
  as the first step.
- `workflow-orchestrator` 2.4.1 still stops without a brain, but now sends you to `beachhead-segment` in the same plugin (a quick brain in about 3 minutes) instead of a plugin you may not have installed.
- `positioning-messaging` offers "name your 3 alternatives now" next to `alternatives-map` when Section 3 is empty. `alternatives-map` no longer says `positioning-ideas` hard-blocks.
- `beachhead-segment` Pre-flight said "hard block" while its Step 0 ran the Quick-Brain. The Pre-flight now matches Step 0: no brain means three quick questions, not a stop.
- `product-marketing-context` recognises a brain that another skill started (the
  `🟡 Cold start` line): it lists filled and missing sections, asks only for missing
  fields, scores absent sections 0, and removes the line once all six are confirmed.

### Fixes

- `meta-review` runs the 18 checks in `SKILL-SPEC.md` Section 13 (it ran 17 and missed
  the Learning Close check). Pass threshold is 16/18.
- `positioning-messaging` v2.4.2 is back under the 500-line limit: the Onboarding steps
  moved to `references/onboarding.md`. Fixed a corrupted frontmatter value
  (`brain-dependentContext keys`).

## v1.4.0 — 2026-10-10

### Works without a brain

- `alternatives-map`, `ideal-customer-profile` and `proof-points` no longer stop when
  there is no brain. They work from the material you paste and, after you confirm,
  start `/foundation/brain.md` with their own section only. If files cannot be
  written, they show the block to save and never claim it was saved.
- `product-messaging-playbook` asks five Quick-Brain questions when there is no brain
  and nothing pasted, builds the playbook from the answers and labels it as such.
  It still never writes to the brain.
- `message-house` now offers two paths that work inside the plugin when there is no
  positioning: paste it, or run `positioning-messaging`.
- `SKILL-SPEC.md` v2.4.0: new missing-brain rule for brain-dependent skills.

### Try it first

- New `examples/example-brain.md`: a finished brain for a fictional company, with
  `examples/README.md` listing five prompts to try before building your own.
- The `brain-template.md` reference example no longer attributes invented numbers and
  quotes to a real company; it points to the fictional example instead.
- Each plugin README opens with a "Start here" block: the outcome, the first command,
  a prompt to try, and whether it needs the brain.

### Evidence

- New `docs/eval-results.md` records which evals have been run. Nothing is marked as
  passed yet.

## v1.3.0 — 2026-10-10

### Customer stories

- New skill `customer-stories` in `pmm-growth`: runs a story from kickoff to customer
  approval. Kickoff questions and an internal brief, interview questions, a draft in
  one fixed seven-block structure (before, decision, rollout, results, people, limit,
  next), the customer review pack, and an audit of a finished story. You choose the
  depth (short, standard, deep) and the angle before drafting.
- Asks for the names and departments of everyone involved and never assumes them. A
  stage and next action are tracked per story. Permission is recorded per use, and a
  cannot-say list is binding on every draft.
- Every stat needs a baseline, period, denominator, source and status; every quote
  needs a named speaker, title and job. Gaps become placeholders; nothing is invented.
  "Up to" claims need the typical value. Runs an 8-point gate on its own draft before handover.
- Keeps a story ledger at `/context/customer-stories.md` and logs each session to
  `/context/skill-sessions.md`. Confirmed claims are handed to `proof-points`.
- Added `/pmm-growth:customer-stories`, a `~~call recordings` connector category
  (Fireflies, Gong) to `pmm-growth`, and a next-skill-map entry.
- `writing-assistant` v2.4.1 points case-study requests to the ledger and to
  `customer-stories` when a verified story is needed.
- `SKILL-SPEC.md` v2.3.1: the Learning Close template now includes `type: execution`
  and the five-field shape, matching `skill-sessions-format.md`.

### Cleanup

- Reworded "four-field" session-log language to the five-field shape (`type`, `skill`,
  `session_date`, `pattern`, `source`) in 5 skills' Verification and Quality Gate lines
  and in 18 eval files. The skills already wrote `type: execution`; only the wording and
  eval checks were stale.
- Removed the `google-prune-upload/` staging folder. Every file in it was identical to,
  or older than, the live copy.

## v1.2.0 — 2026-10-10

### pmm-positioning

- Removed the hard `dependencies: ["product-marketing-context"]` entry from
  `pmm-positioning`'s `plugin.json` and `marketplace.json` entry. That
  dependency lived in a different marketplace than the one `pmm-positioning`
  is submitted to, which Claude Code can't auto-resolve across marketplaces —
  the result was a silent `dependency-unsatisfied` disable: the whole plugin
  loaded with zero skills and zero commands, with no visible error. All
  eight skills already handle a missing brain gracefully (hard-block and
  redirect, or soft-warn and continue); this fix lets that logic actually
  run. Fixes #1.

### Writing assistant

- `writing-assistant` v2.4.0 drafts marketing content: blog posts, landing pages,
  press releases, case studies, newsletters, and social posts. It takes audience,
  key messages, voice, and proof from the brain and asks once for what is missing,
  or lists its assumptions when told to just draft it.
- Added an Audit mode that names AI patterns and quotes the lines without rewriting.
- Added a routing step so Slack, email, and memo rewrites keep their zero-question
  behavior, with explicit rules for email vs newsletter and post vs blog post.
- Never invents stats, quotes, customer names, results, or search volume. Gaps become
  placeholders, and press release and case study quotes are always placeholders.
- Added `references/` format guides for the six formats plus an SEO checklist.
- Added `/pmm-toolkit:marketing-content` (and the in-skill `marketing-content`
  command). `homepage` now follows the landing-page guide.
- The skill now reads `/foundation/brain.md`. The old
  `.agents/product-marketing-context.md` file still works as a fallback.
- Rewrote the evals to the SPEC format: the original 3 tests plus 12 new ones.

### Connectors

- Added Google Docs, Google Sheets and Google Slides servers. Each plugin wires only
  the Google servers its skills use: Gmail and Calendar in execution,
  go-to-market and toolkit; Drive, Docs, Sheets and Slides in the brain; Drive,
  Docs and Slides in positioning; Drive and Sheets in growth. `pmm-meta` has none.
- Added `~~cloud storage` to the pmm-metrics and experiment-ideas connector blocks.

## v1.1.0 — 2026-10-04

### Connectors

- Added per-plugin `.mcp.json` and `CONNECTORS.md` for six plugins, a root
  `CONNECTORS.md` category registry, and `docs/connect-your-tools.md`.
- Added optional Connectors blocks and evals to the brain and fifteen skills.
- Added structure Check 5 for connector files.
- Wired Canva, Klaviyo, Supermetrics, Amplitude EU, Gmail, Google Calendar and
  Google Drive, and added Slack, Ahrefs and Notion to more plugins. Added
  `~~email marketing` and `~~marketing analytics` categories.
- Added the Slack OAuth client settings that Slack's MCP server needs.
- Added structure Check 6 that blocks credentials in `.mcp.json`, a
  "personal setup" section in the connect guide, `docs/make-it-yours.md`, and
  an "other tools that work" column in `CONNECTORS.md`.
- Added consistent display names for all plugins in the marketplace listing.
- Added a Connectors section to `CLAUDE.md` and `CONTRIBUTING.md`, a connect
  step in `QUICK-START.md`, and an access-requirements note in the README.
- Fixed the dead reference to the retired proof-points skill name in message-house and
  reset the pmm-positioning version to match the CHANGELOG.

## v1.0.0 — 2026-08-25

### Repo-wide

- Fixed broken JSON syntax in `.claude-plugin/marketplace.json` (unclosed
  array and object).
- Registered `pmm-foundation` (the `product-marketing-context` folder) as
  an installable plugin in `marketplace.json` and root `plugin.json` for
  the first time.
- Fixed the root `plugin.json`'s `skills` field from a single unparseable
  comma-joined string to a proper array; corrected the `pmm-meta` path.
- Fixed `pmm-meta/.claude-plugin/plugin.json`'s `skills` path, which
  pointed at a nonexistent `skills/` subfolder.
- Corrected `SKILL-SPEC.md`'s example skill lists to only cite skills
  that exist in this repo.
- Added `CLAUDE.md` establishing one version number across the entire
  repo, synced across every manifest.

### product-marketing-context (pmm-foundation)

- Added `.claude-plugin/plugin.json`, `README.md`, and
  `commands/build-brain.md` — this folder is now a proper installable
  plugin, not a bare skill folder.
- Removed the redundant `.skill/skill.json` manifest.
