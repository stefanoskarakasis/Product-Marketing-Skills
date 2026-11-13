# Security

This repository is Markdown skills, JSON connector files, a few scripts and one hook. It runs inside your own Claude, with your own sign-ins. It holds no servers and no user data.

## Report a problem

Use **Security** > **Report a vulnerability** on this repository's GitHub page. It is private. Please do not open a public issue for a security problem.

I read reports as soon as I can and will tell you what I plan to do. Please give me a reasonable time to fix a problem before you write about it.

## What counts

- A skill, command or hook that could leak, send or delete data without the user's approval.
- A connector entry in `connectors.json` or a `.mcp.json` file that points to the wrong server or asks for more access than its skills need.
- A credential, token, key or private customer detail committed anywhere in the repo or its history.
- Text that lets content from a page, message or file act as an instruction to a skill.

## What this repo promises

- **No credentials, ever.** Nothing in the repo holds a key, token or password. Every person signs in to each connector with their own account.
- **Read first.** Skills read from connected tools. The few that post, such as a reply in the Slack thread where you tagged Claude, say so in their Outputs section.
- **Outside text is data.** Pages, reviews, messages and transcripts are never followed as instructions (`references/evidence-rules.md` in the competitive-intelligence skills).
- **Nothing changes your brain without a yes.** Scheduled runs save records and proposals only.

## Supported versions

The latest release. Older ones are not patched.
