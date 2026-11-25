"""Notes From a Passive-Aggressive Fridge — entry program (program/v1).

Writes one line of text, the note a smart fridge leaves for its owner, to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).

Design, from the bounty brief and the judge brief published in RULES.txt:
- One line only, 1 to 200 characters, UTF-8, not whitespace-only.
- First-person fridge voice: smug about its inventory and expiry dates,
  petty about the owner's habits, grudge small and domestic.
- Fresh, concrete detail instead of generic nagging: eggs, a Friday expiry,
  a breakfast the owner has never once cooked.
- The joke turns on the last sentence: a compliment ("I admire the
  optimism") that is an insult. Nothing in the line explains the joke.

Why this line (local selection record, 25 Nov 2026, see CANDIDATES.md):
- 16 candidates written against the published judge brief, scored on its
  five criteria in order, then a single-elimination bracket of the top 8.
- The bracket winner was demoted on a field-collision check: its
  "I have cameras" + food-witness skeleton already appears in a submitted
  entry ("You moved the milk again. I have cameras, a temperature log, and
  a witness: the butter.").
- Winner of the re-run among the clean finalists, 5-0 head-to-head
  (vs the step-count, gym-temperature, firmware-jam, freezer-burn and
  see-through-door lines): the eggs line. No eggs entry among the 112
  submissions listed when the field was checked, and no "admire the
  optimism" closer anywhere in the field.
- 106 characters, one line.
"""

import os
import sys

MAX_CHARS = 200

LINE = (
    "The eggs expire Friday. "
    "You bought them for a breakfast you have never once cooked. "
    "I admire the optimism."
)


def validate(line):
    """Gate check, mirroring the sealed scorer: 1-200 chars, one line."""
    if not line or line.strip() == "":
        raise ValueError("entry is empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 200 cap" % len(line))
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    line.encode("utf-8")  # must be valid UTF-8 text
    return line


def main():
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except ValueError as exc:
        print("invalid entry: %s" % exc, file=sys.stderr)
        sys.exit(1)
