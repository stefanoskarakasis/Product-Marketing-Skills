# Changelog

## Unreleased

### pmm-competitive-intelligence

- Added the **pmm-competitive-intelligence** plugin with one skill, **competitive-battlecard** (`/pmm-competitive-intelligence:competitive-battlecard`). It builds a one-page card for one competitor in one deal: win condition, what to say first, a five-row snapshot, questions to ask, replies to what the buyer will say, when to lean in and when to walk away, and the proof you are allowed to use.
- Tailored to role, GTM motion, the competitor's status in the deal, buyer persona, deal stage and segment. It asks once, always asks whether you want a Google Doc (paste-ready in chat, the default) or an HTML page, shows both in one stacked column with identical headers, and states every assumption on the card.
- Checks brain Section 6 forbidden claims and Section 8 prohibited items before it writes a line, keeps unapproved claims about your product off the card, tags and dates every competitor claim, and turns an unsourced weakness into a question.
- Saves each card to `/context/battlecards/`, shows what changed since the last card, reads recent `signal-monitor` lists, and proposes dated field notes back to brain Section 3 only after you confirm the exact text. It never writes any other section and never writes to a CRM.
- With no brain it asks five quick questions and holds the answers for the session.
- Three new connector categories in the root `CONNECTORS.md`: `~~competitive intelligence` (Klue, Crayon and similar), `~~win/loss` and `~~company data`. None is wired in `.mcp.json`, because those vendors give each customer their own endpoint; connect yours or paste. `competitive-battlecard` reads a CI platform's cards first so the card never contradicts them, and never writes back. `~~CRM` now notes Salesforce (connect your own org's server).

### product-marketing-context

- `brain-schema.md` lets `competitive-battlecard` append field notes or a stub to Section 3 after you confirm. `next-skill-map.md` adds an "After competitive-battlecard" entry and offers the card after `alternatives-map`, `signal-monitor` and `proof-points`.

### pmm-go-to-market

- `workflow-orchestrator` 2.6.0 routes the "Competitive Intelligence Program" and "Competitive Response (Fast)" workflows to `competitive-battlecard` instead of a placeholder. The `go-to-market-strategy` T1 template checklist names the skill.

### pmm-positioning

- `product-messaging-playbook` 1.3.1 points to `competitive-battlecard` for a full competitor card.

### pmm-intelligence

- `signal-monitor` 1.0.1 points to `competitive-battlecard` for a competitor card.

### Repo

- `SKILL-SPEC.md` 2.6.2 adds `competitive-battlecard` to the brain-dependent list and the T2 examples.
- Changed the skill count to 37 across 9 plugins.

## v1.12.1 — 2026-10-11

### product-marketing-context

- Added source tags to every brain field: where it came from, the date, whether you stated it or it was pulled or inferred, and whether it is confirmed. Brains without tags keep working.
- Added optional Section 7 (Strategy: priorities, launches, quarterly goals, active bets, what you are not doing) and optional Section 8 (Execution: stakeholders, approvals, what is prohibited, channels, cadence). Section 8 goes stale after 180 days; the audit reports a missing Section 8 as "not built", not as a gap.
- Added an Offerings block to Section 1: how the product is packaged, approved terminology and permitted claims.
- Added one canonical schema, `references/brain-schema.md`, and a test that fails if a skill cites a brain section that does not exist or the brain template drifts from the schema.
- Added **ingest** mode: give it your website and pricing page, then optionally calls, planning notes or decks. It extracts evidence, compares sources and shows a Brain Diff you approve section by section. Two or more agreeing sources are tagged `pulled`, one source is `inferred`, conflicts are shown side by side and a value you confirmed is never overwritten. Website copy is never treated as proof and personal data is not stored.
- Added **refresh** mode (`/product-marketing-context:refresh-brain`): lists only the fields past their section's freshness limit and asks, one at a time, whether each is still true, changed, or dropped.
- Added a gaps queue (`/foundation/gaps.md`) and `/product-marketing-context:brain-gaps`: a skipped question is saved and stays quiet for 30 days. The health audit now reports open gaps and the oldest field in each section.
- Added **My context** mode (`/product-marketing-context:my-context`) and `/foundation/me.md`: how you like outputs (length, detail, shape, bluntness). Skills read it for format and detail only, never for company facts.
- Added `references/evidence-format.md`, `references/gaps-format.md` and `references/me-format.md`, and evals 4 to 28 for the new behaviors.
- Changed the next-steps offer to come from `next-skill-map.md`, with a test that checks every skill name in it.
- Changed "Not applicable" to `N/A` everywhere, and clarified that one brain covers one product or platform: for several product lines, keep one folder and one brain per product.
- Fixed the `build-brain` command pointing to a step that does not exist and listing an invocation that does not match its name.

### pmm-intelligence

- Added the **pmm-intelligence** plugin with one skill, **signal-monitor** (`/pmm-intelligence:signal-monitor`). It reads only the signals you name (pasted notes, files, listed URLs, or `~~market data` and `~~SEO` connectors) and returns at most five opportunities, each with a dated source, the brain field it touches, the Section 7 priority it serves, a confidence label and one suggested next move.
- Made it read-only for your brain: it saves a dated list to `/context/signals/` and hands brain changes to `product-marketing-context`, which asks first. One source is never `high` confidence and a company's own claims are never treated as proof.
- With no brain, it asks three quick questions and holds the answers for the session.

### pmm-positioning

- `positioning-messaging` and `product-messaging-playbook` ask one gap question when a needed brain fact is missing, and read `/foundation/me.md` for format.
- `proof-points` flags a claim that touches a prohibited topic and notes who approves it.

### pmm-go-to-market

- `go-to-market-strategy` reads Section 7, asks one gap question and reads `/foundation/me.md` for format.
- `workflow-orchestrator` 2.5.0 added a "Weekly Opportunities" workflow (`/run weekly-opportunities`).

### pmm-execution

- `pmm-okrs` reads Section 7, can propose a Section 7 update only after you confirm, asks one gap question and reads `/foundation/me.md` for format.
- `stakeholder-maps` starts from your Section 8 stakeholders and can propose new ones; `pre-mortem` tests approval lead times and prohibited claims.
- `interview-summary` 2.5.0 states its brain contract: it reads Sections 2 and 3 only to check the ICP match and compare alternatives, and never writes the brain.
- Fixed the eval fixtures in `prioritization-frameworks`, `stakeholder-maps`, `prd` and `pre-mortem` that described brain sections that never existed ("Revenue Levers", "Personas (§4)"). They now use Sections 2, 3, 7 and 8, and a new test keeps those phantom sections out. Removed leftover "Revenue Levers" references from `retro`, `interview-summary` and `pmm-okrs`.

### pmm-toolkit

- `gaccs-brief` asks one gap question and, with `writing-assistant`, reads `/foundation/me.md` for format.

### Repo

- Added `SKILL-SPEC.md` 2.6.1 with the gap capture rule and the personal context rule, and aligned its lists of brain-dependent and context-agnostic skills with each skill's `context:` label (`prd`, `experiment-doc`, `prioritization-frameworks`, `interview-summary` and `product-marketing-context` were listed wrongly). A new test checks the lists against the labels.
- Added `examples/ingest-demo/` (five fictional sources plus the expected evidence and Brain Diff), `docs/keep-your-brain-fresh.md`, `docs/ai-marketer-loop.md` and a `.gitignore`.
- Changed the skill count to 36 across 8 plugins. This release rolls up the work of steps 1.7 to 1.11.1; a first upload labelled 1.12.0 missed the hidden files, was never released, and 1.12.1 is the complete release.
- Removed the last retired-prefix and storefront links outside the root README, and added tests that keep them out.

## v1.6.0 — 2026-10-10

### pmm-go-to-market

- `gtm-motions` now asks once, after its output, whether to keep the Quick-Brain answers as the start of your brain. Only on a yes it writes a Section 2 stub under the `🟡 Cold start` line, tagged user-stated, and never the motion stack.

### pmm-growth

- `positioning-ideas` now asks the same keep question and, on a yes, writes a Section 3 stub with the alternatives, tagged user-stated, and never the positioning options. Neither skill overwrites an existing section.

## v1.5.0 — 2026-10-10

### product-marketing-context

- The brain skill recognises a brain another skill started (the `🟡 Cold start` line): it lists filled and missing sections, asks only for missing fields, scores absent sections 0, and removes the line once all six are confirmed.

### pmm-go-to-market

- `gtm-motions` no longer stops without a brain: it asks two Quick-Brain questions (best-fit buyer, self-serve or sales conversation), session-only.
- `go-to-market-strategy` wording now matches its Step 0: with no brain it sends you to `beachhead-segment` in the same plugin, no longer to `product-marketing-context`.
- `workflow-orchestrator` 2.4.1 still stops without a brain but sends you to `beachhead-segment` (a quick brain in about 3 minutes) instead of a plugin you may not have installed.
- Fixed `beachhead-segment` Pre-flight saying "hard block" while its Step 0 ran the Quick-Brain: no brain now means three quick questions, not a stop.

### pmm-growth

- `positioning-ideas` no longer stops without a brain: it asks for what you sell, the best-fit buyer and three alternatives including doing nothing, tagged user-stated, session-only.
- `value-prop-statements` asks you to paste or write your positioning instead of sending you to another plugin, and still never invents one.

### pmm-positioning

- `positioning-messaging` offers "name your 3 alternatives now" next to `alternatives-map` when Section 3 is empty, and `alternatives-map` no longer says `positioning-ideas` hard-blocks.
- Fixed `positioning-messaging` 2.4.2 back under the 500-line limit by moving the Onboarding steps to `references/onboarding.md`, and repaired a corrupted frontmatter value (`brain-dependentContext keys`).

### pmm-meta

- Fixed `meta-review` to run all 18 checks in `SKILL-SPEC.md` Section 13 (it ran 17 and missed the Learning Close check). The pass threshold is 16/18.

## v1.4.0 — 2026-10-10

### pmm-positioning

- `alternatives-map`, `ideal-customer-profile` and `proof-points` no longer stop without a brain: they work from the material you paste and, after you confirm, start `/foundation/brain.md` with their own section only. If files cannot be written, they show the block to save and never claim it was saved.
- `product-messaging-playbook` asks five Quick-Brain questions when there is no brain and nothing pasted, labels the result as such and never writes to the brain.
- `message-house` offers two paths that work inside the plugin when there is no positioning: paste it, or run `positioning-messaging`.

### product-marketing-context

- Fixed the `brain-template.md` reference example attributing invented numbers and quotes to a real company; it now points to the fictional example.

### Repo

- Added `SKILL-SPEC.md` v2.4.0 with the missing-brain rule for brain-dependent skills.
- Added `examples/example-brain.md` (a finished brain for a fictional company) and `examples/README.md` with five prompts to try before building your own.
- Added a "Start here" block to each plugin README: the outcome, the first command, a prompt to try and whether it needs the brain.
- Added `docs/eval-results.md`, which records which evals have been run. Nothing is marked as passed yet.

## v1.3.0 — 2026-10-10

### pmm-growth

- Added the **customer-stories** skill and `/pmm-growth:customer-stories`: runs a story from kickoff to customer approval with kickoff questions and an internal brief, interview questions, a draft in one fixed seven-block structure (before, decision, rollout, results, people, limit, next), the customer review pack and an audit of a finished story. You choose the depth (short, standard, deep) and the angle before drafting.
- Made it ask for the names and departments of everyone involved and never assume them. A stage and next action are tracked per story, permission is recorded per use and a cannot-say list is binding on every draft.
- Required a baseline, period, denominator, source and status for every stat, and a named speaker, title and job for every quote. Gaps become placeholders, nothing is invented, "up to" claims need the typical value, and an 8-point gate runs on its own draft before handover.
- Added a story ledger at `/context/customer-stories.md`, logging of each session to `/context/skill-sessions.md`, handover of confirmed claims to `proof-points`, a `~~call recordings` connector category (Fireflies, Gong) and a next-skill-map entry.

### pmm-toolkit

- `writing-assistant` 2.4.1 points case-study requests to the story ledger and to `customer-stories` when a verified story is needed.

### Repo

- Added the five-field session shape (`type`, `skill`, `session_date`, `pattern`, `source`) to the Learning Close template in `SKILL-SPEC.md` 2.3.1, and reworded "four-field" language in 5 skills and 18 eval files to match.
- Removed the `google-prune-upload/` staging folder; every file in it was identical to, or older than, the live copy.

## v1.2.0 — 2026-10-10

### pmm-positioning

- Fixed `pmm-positioning` loading with zero skills and zero commands and no visible error, by removing the hard `dependencies: ["product-marketing-context"]` entry from its `plugin.json` and `marketplace.json` entry. That dependency lived in a different marketplace, which Claude Code can't auto-resolve, so the plugin was silently disabled. All eight skills already handle a missing brain, and that logic can now run. Fixes #1.

### pmm-toolkit

- Added `writing-assistant` 2.4.0, which drafts blog posts, landing pages, press releases, case studies, newsletters and social posts, taking audience, key messages, voice and proof from the brain and asking once for what is missing. It never invents stats, quotes, customer names, results or search volume.
- Added an Audit mode that names AI patterns and quotes the lines without rewriting, a routing step so Slack, email and memo rewrites keep their zero-question behavior, and `references/` format guides for six formats plus an SEO checklist.
- Added `/pmm-toolkit:marketing-content`; `homepage` now follows the landing-page guide.
- Made the skill read `/foundation/brain.md`; the old `.agents/product-marketing-context.md` file still works as a fallback.
- Rewrote the evals to the SPEC format: the original 3 tests plus 12 new ones.

### Repo

- Added Google Docs, Google Sheets and Google Slides servers, each wired only into the plugins whose skills use them: Gmail and Calendar in execution, go-to-market and toolkit; Drive, Docs, Sheets and Slides in the brain; Drive, Docs and Slides in positioning; Drive and Sheets in growth. `pmm-meta` has none.
- Added `~~cloud storage` to the pmm-metrics and experiment-ideas connector blocks.

## v1.1.0 — 2026-10-04

### Connectors

- Added per-plugin `.mcp.json` and `CONNECTORS.md` for six plugins, a root `CONNECTORS.md` category registry, and `docs/connect-your-tools.md`.
- Added optional Connectors blocks and evals to the brain and fifteen skills.
- Added structure Check 5 for connector files.
- Wired Canva, Klaviyo, Supermetrics, Amplitude EU, Gmail, Google Calendar and Google Drive, and added Slack, Ahrefs and Notion to more plugins. Added `~~email marketing` and `~~marketing analytics` categories.
- Added the Slack OAuth client settings that Slack's MCP server needs.
- Added structure Check 6 that blocks credentials in `.mcp.json`, a "personal setup" section in the connect guide, `docs/make-it-yours.md`, and an "other tools that work" column in `CONNECTORS.md`.
- Added consistent display names for all plugins in the marketplace listing.
- Added a Connectors section to `CLAUDE.md` and `CONTRIBUTING.md`, a connect step in `QUICK-START.md`, and an access-requirements note in the README.
- Fixed the dead reference to the retired proof-points skill name in message-house and reset the pmm-positioning version to match the CHANGELOG.

## v1.0.0 — 2026-08-25

### Repo-wide

- Fixed broken JSON syntax in `.claude-plugin/marketplace.json` (unclosed array and object).
- Registered `pmm-foundation` (the `product-marketing-context` folder) as an installable plugin in `marketplace.json` and root `plugin.json` for the first time.
- Fixed the root `plugin.json`'s `skills` field from a single unparseable comma-joined string to a proper array; corrected the `pmm-meta` path.
- Fixed `pmm-meta/.claude-plugin/plugin.json`'s `skills` path, which pointed at a nonexistent `skills/` subfolder.
- Corrected `SKILL-SPEC.md`'s example skill lists to only cite skills that exist in this repo.
- Added `CLAUDE.md` establishing one version number across the entire repo, synced across every manifest.

### product-marketing-context (pmm-foundation)

- Added `.claude-plugin/plugin.json`, `README.md`, and `commands/build-brain.md` — this folder is now a proper installable plugin, not a bare skill folder.
- Removed the redundant `.skill/skill.json` manifest.

# Legacy releases

These three releases use the old numbering from before the repo moved to 1.x. They stay published and tagged; the notes are rewritten in the format above. Skill names are shown without the retired prefix they carried at the time.

## v2.5.0 — 2026-06-12

### Core skills

- Brought `positioning-messaging` (16/19 to 19/19), `stakeholder-maps` (18/19 to 19/19) and `experiment-doc` (17/19 to 19/19) to full `SKILL-SPEC` v2.0.0 compliance. `go-to-market-strategy` stayed at 18/19 and `pre-mortem` at 19/19; both gained evals.
- Added to `positioning-messaging`: `version`, `metadata` and `last_updated` frontmatter; Trigger, Inputs, Pre-flight, Outputs, Verification, Do Not Use For and Changelog sections; 8 Operating Rules; and a Quality Gate of 8 binary checks. All 6 phases are unchanged.
- Added to `experiment-doc`: `last_updated` (renamed from `updated`), `metadata.context` and `metadata.quality_gate`; Trigger, Inputs, Pre-flight (a knowledge check for false beliefs), Outputs, Verification and Changelog sections; and a Quality Gate of 9 binary checks. All four modes (Formulate, Diagnose, Pressure-Test, Score) are unchanged.
- Added to `stakeholder-maps`: `last_updated`, a formal Trigger, an Inputs section (replacing the INTAKE block), Outputs, Verification and Do Not Use For sections. The five sections, the `/map`, `/sprint`, `/deep-dive`, `/update` and `/check` commands and the learning loop are unchanged.

### Evals

- Added 35 evals, 7 each for `go-to-market-strategy`, `positioning-messaging`, `stakeholder-maps`, `pre-mortem` and `experiment-doc`, covering happy paths, modes, refusals, brain-missing cases and the learning close.

### Repo

- Backward compatible: no change to methodology, commands, triggers or brain integration.
- Added `DELIVERABLES-SUMMARY.md`, `REPO-UPDATE-GUIDE.md` and `FILES-INDEX.md`.
- Credited April Dunford (positioning), Gary Klein (pre-mortem), Anthony W. Ulwick (Jobs to Be Done) and Paweł Huryn (learning loops and pattern capture).
- Install: add the marketplace `stefanoskarakasis/Product-Marketing-Skills` in Claude, or run `claude plugin marketplace add stefanoskarakasis/Product-Marketing-Skills`.

## v2.0.0 — 2026-05-23

### product-marketing-context

- Added **product-marketing-context**, a setup wizard and brain health audit in one skill. About 20 minutes of questions across six sections: Product Context (5), ICP (8), Alternatives and Positioning (6), Voice and Tone (5), Market Context (4), Proof Points Registry (3). It creates `/foundation/brain.md`, which other skills read.
- Added a 0 to 100 brain health score with recommendations, and compound intelligence: skills save their outputs to brain Section 7 so the next skill builds on them.

### pmm-positioning

- Added `positioning-messaging`, based on April Dunford's framework, with five modes: BUILD (positioning statement and four-layer messaging doc), AUDIT (scored review and rewrite queue), FLETCH (six-slide internal deck), SALES-ENABLEMENT (persona cards and competitive playbook) and HOMEPAGE (copy with no placeholders). It reads Product, ICP, Alternatives and Market, and saves positioning to Section 7.

### pmm-toolkit

- Added four skills: `writing-assistant` (rewrites copy to brand voice), `pmm-resume`, `privacy-policy` (jurisdiction-aware) and `gaccs-brief`. `writing-assistant` and `gaccs-brief` optionally read the brain; the other two are standalone.

### Repo

- Shipped 3 plugins and 6 skills, with 50+ input validation rules and 15+ evals.
- Replaced 7 separate foundation skills with one brain. v1.x users export their data, run the brain setup, paste the data in and delete the old skills; every v1.x field maps to a v2.0 brain section.
- Install in Claude.ai from the release ZIPs (start with `product-marketing-context.zip`), or in Claude Code with `claude plugin marketplace add stefanoskarakasis/Product-Marketing-Skills`.
- Planned next: execution skills (PRDs, OKRs, retros, pre-mortems, stakeholder maps), value propositions and battlecards, then a visual brain editor, multi-brain support, MCP integrations and brain version control.
- Credited April Dunford, Emily Kramer (MKT1) and Paweł Huryn (self-improving skills). MIT licensed.

## v2.1.0 — 2026-05-22

### product-marketing-context

- Released **product-marketing-context** v2.1.0: a setup wizard with validation (31 onboarding questions, 15 to 20 minutes), a brain health audit scored 0 to 100, compound intelligence where skills write back to the brain, and 15 evals.
- Install in Claude.ai by uploading `product-marketing-context.zip` under Settings, Skills, then saying "Set up my PMM brain".
