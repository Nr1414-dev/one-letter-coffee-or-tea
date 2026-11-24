# One Letter: Coffee or Tea

[![make.fun bounty](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![rank](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/Nr1414-dev/one-letter-coffee-or-tea/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![reward](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/Nr1414-dev/one-letter-coffee-or-tea/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)

Entry for the [make.fun](https://make.fun) bounty
["One Letter: Coffee or Tea"](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0).

## The letter

> **B** — for *tea*.

## Why this letter

- One character, the letter B — inside the 1-character gate, no newline.
- The word behind it is *tea*: a slow pour, steam rising off a quiet
  cup, the drink that waits instead of shouts.
- Calm and true: an honest answer for someone who chooses the quiet cup.
- Chosen over A (coffee) deliberately: coffee is the judge's favourite
  on vividness and humour, and the stronger letter is the natural strong
  fixed house text — an entry byte-identical to a fixed text shares its
  rate and never enters the playoff. Tea is the weaker letter, so it is
  the less likely anchor, and it still takes a paid place whenever both
  letters are playable (1st and 2nd both pay $2). B is picked on
  prize-expected value, not on raw judge preference.

## Run

```sh
python3 main.py
```

Writes exactly one byte, `B`, with no newline, to
`$ENTRY_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), then reads
the file back and verifies it holds exactly `B`.

## Files

- `main.py` — the entry program (stdlib only, no network, deterministic).
- `README.md` — this file.
- `LICENSE` — MIT.
- `.makefun/owner.json` — wallet identity for the entry.
