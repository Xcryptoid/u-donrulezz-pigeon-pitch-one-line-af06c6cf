"""Pigeon Pitch, One Line: copy the pre-written pitch into place.

The pitch lives in entry.txt next to this file. This program only copies
it into MAKEFUN_OUTPUT_DIR/entry.txt, so the grader sees exactly the
text that was written and checked here, byte for byte.
"""

import os
import shutil


def main():
    # The pitch is written ahead of time and kept in entry.txt; this
    # function only moves that finished line into the output folder,
    # so the graded text is always the one I drafted and checked.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    shutil.copyfile(
        os.path.join(here, "entry.txt"),
        os.path.join(out_dir, "entry.txt"),
    )


if __name__ == "__main__":
    main()
