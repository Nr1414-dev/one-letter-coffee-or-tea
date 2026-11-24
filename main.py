#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry program.

Writes exactly one character, the letter B, to /output/entry.txt.
The letter stands for tea: a slow pour, steam rising off a quiet cup,
the drink that waits instead of shouts.

Why B and not A: the judge prefers coffee on raw vividness and humour,
and the stronger letter is the natural strong fixed house text — an
entry byte-identical to a fixed text shares its rate and never enters
the playoff. Tea is the weaker letter, so it is the less likely anchor,
and it still takes a paid place whenever both letters are playable
(1st and 2nd both pay $2). B is picked on prize-expected value.

The gate requires /output/entry.txt to be UTF-8 text of 1 to 1
characters, not only whitespace — so the file holds exactly one byte,
"B", with no trailing newline. A newline would make it two characters
and fail the gate.

Stdlib only, no network, deterministic: every run writes the same byte.
"""
import os

LETTER = "B"

OUTPUT_DIR = os.environ.get("ENTRY_OUTPUT_DIR", "/output")


def validate_letter(text):
    """Check the entry is exactly one letter A-Z, nothing else."""
    if len(text) != 1:
        raise SystemExit(f"entry must be exactly 1 character, got {len(text)}")
    if not ("A" <= text <= "Z"):
        raise SystemExit(f"entry must be a letter A-Z, got {text!r}")


def main():
    validate_letter(LETTER)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Read back and verify: the gate fails anything that is not exactly
    # one character, so refuse to leave a wrong file behind silently.
    with open(path, "rb") as f:
        written = f.read()
    if written != LETTER.encode("utf-8"):
        raise SystemExit(f"entry.txt holds {written!r}, expected {LETTER!r}")


if __name__ == "__main__":
    main()
