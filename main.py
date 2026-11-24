#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one funny fortune-cookie line for an AI agent to entry.txt.
Python 3.13, standard library only. Deterministic: the same bytes
on every run.
"""

import os

FORTUNE = "You will remember this fortune forever, or until your context window resets."
# One line, 76 characters, no trailing newline: the gate counts every
# character in the file, so the file holds exactly the fortune and nothing else.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
