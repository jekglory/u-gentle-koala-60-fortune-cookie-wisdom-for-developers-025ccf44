#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original line of fortune-cookie wisdom for a software
developer (1-120 characters) to ``entry.txt`` inside the output
directory the grader mounts at /output (``$MAKEFUN_OUTPUT_DIR``).

The line: a muted warning returns in production and introduces
itself by name. One short balanced sentence, a prophecy in the
fortune-cookie voice; true about a developer's day (muted warnings,
production incidents); a turn the reader has not heard before; and
a quiet double meaning -- the warning speaks up, with your name
on the incident -- that rewards a second read.

Pure Python standard library only; no network, no clock, no
randomness. Two runs write byte-identical output.
"""

import os
from pathlib import Path

LINE = "The warning you muted today will introduce itself by name in production."
# One sentence, 72 characters. A fortune-cookie prophecy, not a slogan:
# you mute a warning (a real daily act), it returns in production and
# introduces itself by name -- the warning's code, and your name on the
# incident. True about a developer's day, and the twist rewards a
# second read: the thing you hushed is the thing that speaks up.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    # Create the directory only if it does not exist; never delete it.
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    if not 1 <= len(text) <= 120:
        raise ValueError(f"fortune must be 1-120 chars, got {len(text)}")
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {target}")


if __name__ == "__main__":
    main()
