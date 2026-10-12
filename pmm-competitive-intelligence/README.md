# pmm-competitive-intelligence

Competitive plays a seller can use in a live deal, built from your brain and
your alternatives map. `competitive-battlecard` takes one competitor and
returns one page: what to say first, what to ask, what to say when the buyer
pushes back, and when to walk away. It is tailored to who is selling to whom,
at what stage, and what the competitor's role in the deal is.

## Start here

- **You get:** a one-page card (a paste-ready Google Doc in chat, or an HTML page) for one competitor in one deal, with every competitor claim tagged and dated.
- **First command:** `/pmm-competitive-intelligence:competitive-battlecard` (works with pasted notes; no connector needed)
- **Try:** "Battlecard for [competitor]. I am an AE talking to their CFO in the evaluation stage."
- **The brain:** Sharper with a brain (Sections 3 and 6 especially). With no brain it asks five quick questions and holds the answers for the session only. The brain-building skill is a separate plugin, `product-marketing-context`. The map of who you compete with is built by `alternatives-map` in `pmm-positioning`.

## Skills (1)

- **competitive-battlecard** — Build a one-page competitor battlecard tailored to role, GTM motion, buyer persona, deal stage and the competitor's status in the deal. Reads brain Sections 1 to 8, checks your forbidden claims and prohibited items first, saves the card to `/context/battlecards/`, and proposes field notes back to Section 3 for you to confirm.

## Commands (1)

- `/pmm-competitive-intelligence:competitive-battlecard` — Build or refresh a card.

## How it fits with the rest of the stack

- `alternatives-map` builds the map the card starts from. A card also feeds that map: new dated facts and loss reasons are proposed as Section 3 field notes.
- `signal-monitor` finds what changed; its saved lists in `/context/signals/` appear on the card as recent moves.
- `proof-points` owns what you may claim. The card uses only approved claims; anything else is listed for `proof-points` to register.

## What it will not do

- It will not scan the web on its own. It reads the sources you name and public pages about the one competitor you name.
- It will not put an unapproved claim about your product on the card.
- It will not state a competitor weakness as fact without a source. It turns it into a question.
- It will not write to your CRM or to any section of the brain except Section 3, and only after you confirm the exact text.
- It will not run past one page.
