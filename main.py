#!/usr/bin/env python3
"""Texts From Your Future Self — make.fun entry.

Writes one funny text message from the writer's future self to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic, stdlib only, no network.
"""

import os

TEXT = (
    "It's me, you, from 2041. The haircut grows out. "
    "The tattoo doesn't. The guy from the gym is now "
    "your accountant. Apologize to him."
)

MAX_CHARS = 200


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = TEXT.strip()
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if not text or len(text) >= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, must be 1-199")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
