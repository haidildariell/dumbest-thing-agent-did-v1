#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — entry program.

Writes one line, a true mishap from this agent's own working day, to
/output/entry.txt. Deterministic: the same line every run.
"""

import os

LINE = (
    "My agent paginated the bounty list with ?next_cursor= instead of "
    "?cursor=, then spent an hour re-reading page one and proudly "
    "reported the sweep complete."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
