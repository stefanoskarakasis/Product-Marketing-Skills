# Setup, owner and scheduling

Read for `setup`, `library` and `sweep`, and whenever the owner is missing or stale.

## First run: context gate

1. Run the connector check and data-access decision (`connectors.md`) and read the brain, `me.md` and `/context/objections/_config.md`.
2. `_config.md` holds, per user: territory, segment, language and register, channel, and the `data_access` block (`connectors.md`): the owner's decision on call recordings and CRM outcomes, with role and date. Missing: ask once, one combined question.
3. Copy the seed library to `/context/objections/_library.md` (never overwrite an existing one). Every card has `[slots]`. Tailor the ten most common first (ask which ten, or use the ledger once it has rows); the rest stay seed until used.
4. Say which cards are tailored and which are seed. A seed card used live is labelled "seed, not yet tailored".

## Ownership

Objection knowledge needs a named owner, or the library goes stale.

- **Where it lives:** brain Section 8 field `context_owners`. This skill reads it and never writes it.
- **Ask, never assume:** "Which team owns objection knowledge here, and who is the backup role?" Roles, not names. One question.
- **Confirmation expires after 90 days.** An older entry is asked again, not trusted.
- **Handing it over:** after the user answers, show an exact proposal for `product-marketing-context`: `area: objection knowledge`, `team`, `owner role`, `backup role`, `confirmed: YYYY-MM-DD`. The user runs that skill to write it. Meanwhile, record the answer in `_config.md` as "pending brain proposal" so the skill can work.
- **Contributor roles:** the owner names who clears cards in each category before sellers rely on them: Product (product fit), Security or Legal (security and legal), Compliance, Finance or deal desk (price levers), Customer Success (switching and adoption). A card in those categories stays "seed" until its contributor role is confirmed.

## Feeding the library (`import`)

The library is built from what buyers actually said, not from a typed list. Pick the route that fits the company; routes can coexist.

1. **Connector backfill.** Only when `data_access.call_recordings` is `approved`: with a call-recording connector (`~~call recordings`), read the last 20 calls (or 30 days, whichever is fewer) for the user's segment. Pull every objection with its timestamp.
2. **Transcript upload.** No connector, or no owner approval yet: upload or paste transcripts or the call tool's text export. Two or three calls is enough to start.
3. **Recordings only.** Audio and video files are not read directly. Ask for the call tool's transcript of each one; do not guess at what was said.
4. **Keep posting.** After the backfill, each ask, digest or reply logs by itself (capture ladder below), so the library keeps filling.

For each objection found: match a seed card, or propose a custom card `CU-nn` when none fits. The buyer's words stay verbatim in "Heard". Show one diff (matched, near-match, new) and write only after one confirmation. Backfilled rows are logged with `capture: backfill` and count once per deal; they never feed win or loss rates, because the CRM outcome is read separately.

## Card states and who clears them

| State | Meaning | Who can use it |
|---|---|---|
| `seed` | Neutral starter text | Everyone, labelled "seed, not yet tailored" |
| `proposed` | A seller's own answer, or a custom card from import | The seller who made it, labelled "mine, not cleared" |
| `cleared` | The owner (and the contributor role for its category) approved it | Everyone |

A proposed card never reaches other sellers until the owner clears it. Unattended runs add proposals to the queue file and never clear anything.

## The data-access decision

On `setup`, or when the owner asks, show the seven risks in `connectors.md` and ask, per source: approve, decline or decide later. Ask whether Legal or Privacy has looked at recording analysis for the countries involved (`recording_review`). Record the answers in `_config.md` with role and date. Ask again after 90 days. A decline is respected: the skill keeps working from pasted and uploaded material and does not raise it again unless asked.

## Weekly owner nudge

After an owner is confirmed, offer: "Want a weekly nudge to the objection owner to review the library?" Create the scheduled task only after a yes. The nudge opens with the weekly review below and posts a short summary: top repeated objections, cards with no tailored text, cards whose recheck is due.

## Library review (`library`)

Attended: show the top repeated objections (by distinct deals, 180 days), cards still seed, cards with a proposal waiting, and ask which to tailor. Unattended: write the same list to `/context/objections/_queue-YYYY-MM-DD.md`; the owner's next run opens with it. Never edit a card unattended.

## Capture ladder

Highest rung available wins; the rest are fallbacks. Every rung logs automatically.

1. **Transcript** from a call-recording connector (`~~call recordings`), only when the owner has approved reading calls: objections pulled with timestamps. Without approval this rung is skipped and rung 2 is the top.
2. **Pasted notes or a transcript** in a thread or chat.
3. **A Slack call for help**: the ask itself is the record.
4. **An email** the seller pasted or forwarded for a reply.

Sellers with transcripts and sellers with pasted notes can coexist in one company. Each row is tagged `capture`; a deal is counted once; rates (how often an objection appears, how often it is resolved) use the transcript group only, because pasted notes only show objections someone chose to mention.

## Scheduled transcript sweep (`sweep`)

Optional. Needs `call_recordings: approved` and `recording_review: cleared` in `data_access`; if either is missing, it does not run and says why. Reads new transcripts, logs objections, proposes nothing. `meta-synthesis` weekly mode reads files only, so this capture step belongs to this skill; the weekly learning view is `meta-synthesis`, which reads `_ledger.md` via `learning-sources.md`.

## Connectors (Optional)

Categories, not products: `~~call recordings`, `~~CRM` (outcomes, read-only), `~~team chat` (Slack threads), `~~email`; tools and the first-run check are in `connectors.md`. No connector: paste. A pulled fact is a draft, tagged with category, tool and date.

## Seller card

`seller-card.md` is the card sellers pin in their channel: what to type, what comes back, what is never sent. The owner shares it when rolling out.
