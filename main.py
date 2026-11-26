#!/usr/bin/env python3
"""Write the printer's comeback line to entry.txt."""

import os

# One line in the printer's own voice: picked from five drafts
# judged pairwise on the kit's criteria (the printer's own comeback
# first, then an immediate laugh from a real joke, the weary and
# literal voice of a machine that has counted every sheet it ever
# fed, a comeback that lands in a single read, and a fresh angle
# rather than the recycled jam line). The winner keeps the count:
# 84,000 pages, zero thanks, and one jam it admits was on purpose.
# The gate checks entry.txt as UTF-8 text of 1 to 240 characters:
# this line is 137 code points, 138 with its trailing newline
# (verified by a local run, byte for byte against the winning
# draft).
TEXT = "I have printed 84,000 pages for this office and been thanked zero times, so yes, the jam is on purpose, and no, I will not say which one."


def write_entry(out_dir: str) -> None:
    """Write the line, with its trailing newline, into out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
