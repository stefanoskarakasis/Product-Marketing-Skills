# Refresh and gaps

Moved verbatim from `SKILL.md`.

## Step 6: Refresh Stale Fields (list)

1. Load the brain and `references/brain-schema.md`. For every field, work out its age from its source tag date (an untagged field uses the file's last-updated date) and compare it with the section's limit in the schema. Section 6 is judged per claim.
2. If nothing is stale, say so in one line and stop.
3. List the stale fields by section with their age and limit, most-read sections first (2, 3, 6, then the rest).
4. Ask about one field at a time: "Still true? [yes / changed / drop]".
   - **yes:** remember it for the batch bump.
   - **changed:** ask that field's question again, show the exact before/after, confirm, and write it with a new tag (`stated`, today, `confirmed`).
   - **drop:** show exactly what will be removed, confirm, then remove it.
5. After the last field, show the list of "yes" answers once and confirm the batch. Then set each tag's date to today and status to `confirmed`. A date-only bump is still a write, so it needs this one confirmation.
6. Never refresh a field the user did not choose to review. The user may say "stop" at any point; keep what is already confirmed.

## Step 7: Answer Open Gaps (list)

1. Read `/foundation/gaps.md`. Use the newest block for each `gap_id`. Keep those that are `open`, and those `skipped` more than 30 days ago. If none, say so and stop.
2. Say how many gaps are open. Then take them one at a time, oldest first: the question, why it matters (one line), and "answer or skip".
3. **Answer:** show the exact before/after for the brain field, confirm, write it with a `stated` tag, and append a block with `status: answered` to `gaps.md`.
4. **Skip:** append a block with `status: skipped`. Do not ask again for 30 days.
5. The user may say "stop" at any point. If files cannot be written, show the block and say it was not saved.
