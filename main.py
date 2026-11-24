"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (at most 140 characters) for the
invented city of Mizzlewick to /output/entry.txt.
"""

import os
import sys
from pathlib import Path

LINE = "In Mizzlewick today: light drizzle, 14°C, umbrellas up — the bus is late again, but the puddles are doing their best impression of mirrors."

DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"


def resolve_output_dir():
    """Return the output directory: MAKEFUN_OUTPUT_DIR wins when non-empty."""
    override = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if override.strip():
        return Path(override)
    return Path(DEFAULT_OUTPUT_DIR)


def entry_path():
    """Return the full path of the entry file to write."""
    return resolve_output_dir() / OUTPUT_FILENAME

def validate_line(line):
    """Check the entry is one clean, non-empty line of at most 140 chars."""
    if not line or not line.strip():
        print("error: entry line is empty", file=sys.stderr)
        sys.exit(1)
    if line != line.strip() or "\n" in line or "\r" in line:
        print("error: entry must be a single clean line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 140:
        print("error: entry exceeds 140 characters", file=sys.stderr)
        sys.exit(1)


def main():
    validate_line(LINE)
    path = entry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
