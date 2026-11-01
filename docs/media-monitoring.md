# Media monitoring: schedule it and share it

`media-monitoring` sweeps your core competitors' public pages and returns one screen: what needs you this week, with the fix already drafted, and what it could not see. This page covers who runs it, how to schedule it and what your team sees.

## Who does what

| Person | Role |
|---|---|
| **Executor** (VP Product Marketing or CI lead) | Sets it up once, reviews the brief, approves actions |
| **Backup** (required) | Runs the sweep and approves actions when the executor is away |
| **The team** | Reads the Slack post and the Doc. Nothing to configure |

Only the executor and backup can say `go` or `post`. A reply from anyone else in a Slack thread is ignored.

## Set it up

1. Run `/pmm-competitive-intelligence:media-monitoring Set up media monitoring`.
2. Answer five questions (they are pre-filled from your brain's Section 3), and name an executor and a backup.
3. Read the channel preflight. Fix or paste what is blocked.
4. Run the first sweep. It is a baseline: it alerts only on the last 30 days and saves snapshots for next week's diff.

## Schedule it

Each scheduled run starts a fresh session, so everything the next run needs lives in `/context/monitoring/` and the Doc's State Block.

- **Weekly sweep:** for example Monday morning. It never asks questions and never runs setup.
- **Monthly review:** the first Monday. It ends by asking whether to run `meta-synthesis`; it never runs it for you.

Use the scheduling tools in your environment and give them the prompt "Run the weekly competitor sweep for [company]; post to #[channel]". Run the sweep by hand twice before you trust a schedule: confirm that the second run sees the first run's snapshots.

## What your team sees

- A three-line Slack ping on Monday, and a Monitor section in the weekly board post.
- A shared Doc: latest brief, open actions, the watchlist (the one editable section), a 90-day log and the State Block.
- Replies they can send: `acted M-id`, `useful M-id`, `noise M-id`, `mute [topic]`, `we missed this`. These are noted for the executor and change nothing on their own.

## What it will not do

- Change a card or send a message without a `go` or `post` from the executor or backup.
- Log in anywhere, or read sites that forbid automation. Professional networks and review platforms are paste only.
- Use non-public information about a listed company.
- Write your brain.

## How it fits with the other plugins

- `pmm-competitive-intelligence` collects and produces for named competitors.
- `pmm-intelligence` ranks signals of any kind against your priorities. Run `signal-monitor` after a sweep when more than one thing moved.
- `pmm-meta` learns from the session log: `meta-review` audits the skill, `meta-verify` double-checks an outward note, `meta-synthesis` finds patterns across sessions.
