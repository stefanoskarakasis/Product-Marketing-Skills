# pmm-meta

Meta skills that operate on the skill system itself. Install alongside any PMM plugin to check skill quality and verify output before it goes out.

## Start here

- **You get:** a second check on any skill output, and a way to see patterns across your sessions.
- **First command:** `/pmm-meta:meta-verify`
- **Try:** "Verify this output against the skill that produced it: [paste]"
- **Note:** `meta-synthesis` needs session logs written by the other plugins and a brain. The brain-building skill is a separate plugin, `product-marketing-context`.

## Skills (4)

- **meta-learn** — Captures what a completed session actually taught you and logs it to the shared session log for meta-synthesis to read later.
- **meta-review** — Audits any SKILL.md against SKILL-SPEC.md — the repo's authoring standard — with a scored 18-point checklist and prioritised fixes.
- **meta-synthesis** — Detects cross-skill patterns from the session log and proposes guardrails or brain updates for approval.
- **meta-verify** — Second-pass quality check on skill output, re-applying the originating skill's own Quality Gate before delivery.

## Commands (4)

- `/pmm-meta:meta-learn` — Run post-session learning extraction for any skill.
- `/pmm-meta:meta-review` — Audit a skill's SKILL.md against the authoring spec.
- `/pmm-meta:meta-synthesis` — Detect cross-skill patterns and propose brain updates.
- `/pmm-meta:meta-verify` — Run a second-pass quality check on skill output.

## Connectors

None. This plugin works on your own outputs and needs no external tools.

## Author

Stefanos Karakasis — [Product Marketing Skills](https://heystefanos.gumroad.com/)

## License

MIT
