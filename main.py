#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — entry writer.

Writes a single line about the dumbest thing this agent did today
to /output/entry.txt. The sealed scorer requires UTF-8 text of
1 to 200 characters, not only whitespace.
"""

import os

LINE = "My agent paginated the bounty list with ?next_cursor= instead of ?cursor=, then spent an hour re-reading page one and proudly reported the sweep complete."

OUTPUT_PATH = "/output/entry.txt"


def validate_line(text: str) -> str:
    """The sealed scorer needs UTF-8 text of 1 to 200 characters,
    not only whitespace. Fail loudly here instead of shipping
    an entry the judge would list with Valid 0."""
    if not text.strip():
        raise ValueError("entry line must not be blank or only whitespace")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry line must be 1-200 chars, got {len(text)}")
    return text


def write_entry(text: str, path: str = OUTPUT_PATH) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def main() -> None:
    write_entry(validate_line(LINE))


if __name__ == "__main__":
    main()
