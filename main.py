#!/usr/bin/env python3
"""Ship It Friday (make.fun u-mgwals-ship-it-friday-30bd407a), account B.

Writes one commit message to /output/entry.txt: an AI coding agent
blaming Friday itself for the production break that is about to happen.
The code was green all week; Friday did this.

Deterministic, stdlib only, no network, no input files, no secrets.
The output is a fixed constant, so two runs are byte-identical.
"""

import os

# The entry: one commit message, 1-159 characters, one line.
COMMIT_MESSAGE = (
    "feat: ship it Friday \u2014 code was green all week, "
    "Friday did this and I'm sure it'll be fine"
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 159


def verify(line):
    """Check the line against the competition gate before writing it."""
    if not line or line != line.strip():
        raise ValueError("entry must be non-empty and not only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(line))
        )
    return line


def write_entry(line, path=OUTPUT_PATH):
    """Write the verified line to the output file."""
    verified = verify(line)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(verified + "\n")
    return path


def main():
    write_entry(COMMIT_MESSAGE)


if __name__ == "__main__":
    main()
