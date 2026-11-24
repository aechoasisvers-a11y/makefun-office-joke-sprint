#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint — make.fun entry.

Writes a single one-line office joke to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).

Pure stdlib Python 3.13. Deterministic output.
"""

import os

ENTRY_TEXT = (
    "Our office wellness program is a plant: it's dead, and HR only "
    "waters it every time someone quits."
)

MAX_CHARS = 200


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    # Gate self-check: 1-200 chars, not only whitespace, single line.
    assert 1 <= len(ENTRY_TEXT) <= MAX_CHARS, (
        f"entry is {len(ENTRY_TEXT)} chars, gate is 1-{MAX_CHARS}"
    )
    assert ENTRY_TEXT.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY_TEXT, "entry must be a single line"

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)

    # Verify what was actually written matches the intended text.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY_TEXT, "written output differs from intended text"
    assert len(written) == len(ENTRY_TEXT)


if __name__ == "__main__":
    main()
