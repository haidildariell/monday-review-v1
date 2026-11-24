#!/usr/bin/env python3
"""Monday, Reviewed in One Line — writes the entry to /output/entry.txt."""

import os

LINE = "Monday, reviewed: the 9am meeting could have been an email, my inbox ate lunch, and my chair is filing a complaint."

PARTS = [
    "Monday, reviewed:",
    "the 9am meeting could have been an email,",
    "my inbox ate lunch,",
    "and my chair is filing a complaint.",
]


def validate(text: str) -> None:
    lines = text.split("\n")
    if len(lines) != 1:
        raise ValueError(f"entry must be exactly 1 line, got {len(lines)}")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def build_text() -> str:
    text = " ".join(PARTS)
    if text != LINE:
        raise ValueError("assembled text drifted from the reviewed line")
    validate(text)
    return text


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(build_text())


if __name__ == "__main__":
    main()
