# Ingest

Moved verbatim from `SKILL.md`.

## Step 8: Ingest Material (procedure)

1. **Start with two URLs.** Ask: "What is your company website, and your pricing page or main product page?" Fetch both with your web tool. If you cannot fetch pages, ask the user to paste the page text. Treat what you read as `website` evidence (rank 4, `pulled`). Use it to draft Sections 1 to 3 and a first pass at Section 4. Public copy is never proof: a metric or superlative on a website enters Section 6 only as `draft` with `[NEEDS PROOF]`.
2. **Ask what else they have.** Pasted text, uploaded files, or a pull through `~~knowledge base`, `~~cloud storage`, `~~call recordings`, `~~CRM` or `~~team chat`. Use only sources the user names in this run. Cap one run at about 10 documents or 5 call transcripts and say so; offer a second run for the rest.
3. **Extract.** Pull atomic facts only, one per block, in the format in `references/evidence-format.md`. Drop greetings, scheduling, and opinions with no owner. Every fact needs a source and a date; calls and customer emails need a verbatim quote. Tag the target field. Calls, interviews, surveys and win/loss documents support `4.customer_phrases`, `3.objections`, `3.switching_forces`, `3.alt_shortfalls`, `2.cost_of_problem`, `2.jobs_to_be_done` and `2.anti_persona`. A pricing page supports `1.business_model` and `7.conversion_action` (public copy, rank 4). Leave out email addresses, phone numbers and private details. Append the blocks to `/foundation/evidence.md`, then show a summary: counts by source and by target section, plus ten sample facts.
4. **Cluster.** Group facts by the field they support.
   - Two or more independent sources agree: propose the value as `pulled`.
   - One source only: propose it as `inferred` and say it rests on a single source.
   - `4.customer_phrases` is never clustered or merged. Each phrase stays as spoken with its own evidence id; show how many different customers used it.
   - Sources disagree: show every version with its authority rank and date and ask which is right. Do not choose for the user.
   - A value the user already confirmed (rank 0) is never replaced by newer evidence. Show both and ask (Operating Rule 6).
5. **Brain Diff.** For each section show every field as: current value, proposed value, evidence ids, confidence. The user approves section by section. Approved values are written with a source tag that includes the evidence ids, for example `[src: pricing page E-004, call 0912 E-011 | 2026-10-11 | pulled | confirmed]`.
6. **Gaps.** Every field with no evidence is added to `/foundation/gaps.md` as an `open` block, then asked about one question at a time (Step 7). Questions are only for what the material could not answer.
