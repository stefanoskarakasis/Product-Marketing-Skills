# Inputs detail

Moved verbatim from `SKILL.md`.

## Context keys

- **Context keys:**
  - `/foundation/brain.md` — read if it exists (load silently, skip answered sections); written to, section by section, only after user confirmation.
  - `/foundation/evidence.md` — read if it exists (format in `references/evidence-format.md`). Append-only: Step 8 appends the facts it extracts from your material.
  - `/foundation/me.md` — read if it exists (format in `references/me-format.md`). Written only by Step 9, after you confirm. Describes you, not the company.
  - `/foundation/gaps.md` — read if it exists (format in `references/gaps-format.md`). Append-only: Step 7 appends resolved blocks. Other skills may append `open` or `skipped` blocks.
  - `.agents/*.md`, `.claude/*.md` — optional legacy files; offered for migration if found.
  - `AGENTS.md`, `CLAUDE.md` (project root) — written by Step 10 only, inside one marked block each; text outside the markers is never read for company facts or changed.
  - **Brain contract:** Reads all sections (1 to 8) if present, and `me.md` for format and detail only. Writes: any section, but only after explicit user confirmation of the exact before/after (Operating Rule 1).
