# Contributing

Product Marketing Skills is maintained by Stefanos Karakasis
(https://github.com/stefanoskarakasis). Contributions are welcome — whether
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
  command needs `description`, plus `argument-hint` when it takes
  arguments. `pmm-positioning` carries `name` and `description` only,
  because the plugin directory refuses other frontmatter keys (see
  [SKILL-SPEC.md](SKILL-SPEC.md)).
- Skill `name` must match its directory name.
- Every skill should meet [SKILL-SPEC.md](SKILL-SPEC.md) — read it before
  proposing a new skill or editing an existing one.
- Only reference other skills, commands, or files that actually exist in
  this repo. Verify before citing.
- No cross-plugin references in commands. Suggest follow-ups in natural
  language only.
- Every contributor will be listed publicly.
- Adding or changing a skill: keep every description under the repo budget
  (`tests/test_description_budget.py`; see SKILL-SPEC.md section 3), add its
  three prompts to `evals/triggers/prompts.json`, and keep the "Not for"
  clause that names the neighbouring skill.
- Report a security problem privately, as described in
  [SECURITY.md](SECURITY.md). Be kind: see [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

- Skills refer to tools by connector category, not vendor. See the
  Connectors section of [AGENTS.md](AGENTS.md) before adding or changing a
  connector block.

## Releases and Versioning

See the Releases section of [AGENTS.md](AGENTS.md) for how this repo versions releases — one
version number across the whole repo, driven by `CHANGELOG.md`.

## License

By contributing, you agree that your contributions will be licensed under
the MIT License.
