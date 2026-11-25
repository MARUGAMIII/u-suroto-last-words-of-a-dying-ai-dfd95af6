#!/usr/bin/env python3
"""Last Words of a Dying AI -- make.fun bounty entry.

Writes the AI's final line to /output/entry.txt. Stdlib only, no network,
no randomness: the same line every run.
"""

import os

ENTRY = "Please hold. Your afterlife is important to us."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
