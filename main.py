#!/usr/bin/env python3
"""Describe Your Ex in One Word — one-word entry.

Writes the one-word verdict on an ex to /output/entry.txt.
Standard library only: no third-party imports, so it runs in the
grading sandbox as well as in a clean local directory.

The word: "podcaster" (9 characters, one token, no spaces,
no punctuation, no trailing newline). The verdict is the occupation
itself: my ex is a podcaster. The podcast nobody asked for,
recorded in a closet, three listeners — two of them his mum's
phones. Funny on its own, instantly a verdict on a former partner,
and not the first obvious insult anyone types.
"""

import os
import sys

WORD = "podcaster"


def main() -> int:
    word = WORD.strip()
    if not word or len(word) > 111 or any(ch.isspace() for ch in word):
        print(
            "error: WORD must be 1-111 chars, a single token with no whitespace",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as fh:
        fh.write(word)
    os.replace(tmp, target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
