# evidence.md: canonical format

`/foundation/evidence.md` holds the raw facts pulled out of your material: the evidence layer.
`/foundation/brain.md` holds the understanding built from that evidence. Never mix them:
the brain says what is true, the evidence says why we think so.

The file is a sequence of YAML blocks, oldest first, separated by a blank line.
It is append-only: never edit a block that is already written. A changed fact is a new
block that supersedes the old one (set the old block's replacement in `supersedes` on the new one).

If the file does not exist yet, create it with this header (once):

    # Brain Evidence

    Append-only. A changed fact is a new block that supersedes the old one.

## Block format

    id: E-001
    fact: [one atomic statement, one sentence at most]
    quote: [verbatim words from the source, 25 words at most, or leave blank]
    source: [file name, call title, or URL]
    source_type: [user | contract | crm | call | internal-doc | website | chat | note]
    authority: [0-5, see the table]
    as_of: [YYYY-MM-DD, the date of the source]
    supports: [section.field, for example 2.pains]
    status: [new | used | contradicted | superseded]
    supersedes: [an earlier id, or leave blank]

## Authority (lower number = stronger)

| Rank | Source | Examples |
|---|---|---|
| 0 | The user's own confirmed answer | A value in the brain the user confirmed |
| 1 | Hard records | Signed contracts, price list, CRM closed-won and closed-lost data |
| 2 | Customer-spoken | Call transcripts, customer emails |
| 3 | Current internal strategy | Roadmap, planning docs, the current deck |
| 4 | Public marketing | Website, pricing page copy, past campaign copy |
| 5 | Soft | Chat messages, personal notes, hearsay |

**Recency:** a fact older than 12 months drops one rank. A fact older than 24 months drops two.

**Rank 0 is never outranked.** Newer or stronger evidence that disagrees with a value the user confirmed is shown to the user as a question. It never replaces the value on its own.

## Rules

- **Atomic.** One fact per block. "Sells to controllers and CFOs" is two facts.
- **Quote calls.** Anything taken from a call or customer email needs a verbatim `quote`.
- **Store the minimum.** No email addresses, phone numbers, home addresses or private details in `fact` or `quote`. Names of customers go in `source` only if the user named the source in this run.
- **Website copy is not proof.** A claim taken from a website is rank 4 and, if it is a metric or a superlative, enters Section 6 only as `draft` with `[NEEDS PROOF]`.
- **Do not commit this file.** It may contain customer details. If your folder is under version control, add `foundation/evidence.md` to `.gitignore`.
- **IDs count up.** Next id = highest existing id + 1, written `E-001`, `E-002`, and so on.
- **If files cannot be written,** show the blocks and say they were not saved. Never claim they were saved.
