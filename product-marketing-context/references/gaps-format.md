# gaps.md: canonical format

`/foundation/gaps.md` is the queue of questions the brain still needs answered.
Any brain-dependent skill may add to it (see the gap capture rule in `SKILL-SPEC.md`).
The `product-marketing-context` skill answers them (Step 7).

The file is a sequence of YAML blocks, oldest first, separated by a blank line.
It is append-only: never edit a block that is already written. To change a gap's
status, append a new block with the same `gap_id`. The newest block for a `gap_id`
is its current status.

If the file does not exist yet, create it with this header (once):

    # Brain Gaps

    Append-only. The newest block for a gap_id is its current status.

## Block format

    gap_id: G-001
    raised_by: [skill-name]
    raised_on: [YYYY-MM-DD]
    section: [1-8]
    field: [field key from brain-schema.md]
    why_it_matters: [the output this answer would change, one sentence]
    question: [one question, answerable in one sentence]
    status: [open | answered | skipped]
    resolved_on: [YYYY-MM-DD, or leave blank while open]

## Rules

- **One question per block.** If you need two answers, write two blocks.
- **No duplicates.** If the newest block for the same `section` and `field` is `open`, do not add another.
- **Skipped means quiet for 30 days.** A skipped gap is not shown or asked again until 30 days after `resolved_on`.
- **Answers go to the brain, not here.** An `answered` block records that the question was closed. The answer itself is written to `/foundation/brain.md` with a source tag.
- **IDs count up.** Next id = highest existing id + 1, written `G-001`, `G-002`, and so on.
- **If files cannot be written,** show the block and say it was not saved. Never claim it was saved.
