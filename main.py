#!/usr/bin/env python3
"""One Word, First Thought — entry for make.fun.

Writes exactly one word, the first that comes to mind, to
/output/entry.txt. No topic, no explanation, no second draft.
"""

import os

WORD = "serendipity"


def validate(word: str) -> str:
    """The gate: one word, 1 to 24 characters, not only white space."""
    cleaned = word.strip()
    if not cleaned or len(cleaned) > 24 or len(cleaned.split()) != 1:
        raise ValueError(f"not a single valid word: {word!r}")
    return cleaned


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(validate(WORD) + "\n")


if __name__ == "__main__":
    main()
