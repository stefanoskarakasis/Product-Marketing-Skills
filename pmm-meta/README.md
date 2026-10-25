# pmm-meta

Meta skills that operate on the skill system itself: skill review, session learning, cross-skill synthesis and output verification.

## Start here

- **You get:** a second check on any skill output, and a way to see patterns across your sessions.
- **First command:** `/pmm-meta:meta-verify`
- **Try:** "Verify this output against the skill that produced it: [paste]"
- **The brain:** `meta-synthesis` needs session logs written by the other plugins and a brain. The brain-building skill is a separate plugin, `product-marketing-context`.

## Skills (4)

- **meta-learn** — Capture what a completed session taught you and log it for meta-synthesis to read later.
- **meta-review** — Audit any SKILL.md against SKILL-SPEC.md with a scored checklist and prioritized fixes.
- **meta-synthesis** — Detect patterns across sessions and propose guardrails or brain updates for your approval.
- **meta-verify** — Run a second-pass quality check on a skill's output before delivery.

## Commands (4)

- `/pmm-meta:meta-learn` — Run post-session learning extraction for any skill.
- `/pmm-meta:meta-review` — Audit a skill's SKILL.md against the authoring spec.
- `/pmm-meta:meta-synthesis` — Detect cross-skill patterns and propose brain updates.
- `/pmm-meta:meta-verify` — Run a second-pass quality check on skill output.

## Connectors

None. This plugin works on your own outputs and needs no external tools.

## Author

Stefanos Karakasis — [Stefanos's Stack on Substack](https://stefanoskarakasis.substack.com/)

## License

MIT
