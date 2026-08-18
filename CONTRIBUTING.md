# Contributing

Product Marketing Skills is maintained by Stefanos Karakasis
(https://heystefanos.gumroad.com/). Contributions are welcome — whether
it's a bug fix, a typo, or a new skill idea.

## How to Contribute

- **Bugs and small fixes** — open a PR directly.
- **New skills, commands, or larger changes** — open an issue first so we
  can discuss the approach.

## Guidelines

- Keep PRs focused — one change per PR.
- Follow existing patterns: skills are nouns (domain knowledge), commands
  are verbs (workflows).
- Every skill needs frontmatter with `name` and `description`. Every
  command needs `description` and `argument-hint`.
- Skill `name` must match its directory name.
- Every skill should meet [SKILL-SPEC.md](SKILL-SPEC.md) — read it before
  proposing a new skill or editing an existing one.
- Only reference other skills, commands, or files that actually exist in
  this repo. Verify before citing.
- No cross-plugin references in commands. Suggest follow-ups in natural
  language only.
- Every contributor will be listed publicly.

## Releases and Versioning

See [CLAUDE.md](CLAUDE.md) for how this repo versions releases — one
version number across the whole repo, driven by `CHANGELOG.md`.

## License

By contributing, you agree that your contributions will be licensed under
the MIT License.
