"""Entry for make.fun news-image-20261120.

Copies the pre-built image ``entry.png`` (a 2x2 news collage summing up
Friday 20 November 2026) to the output directory as ``entry.png``.

Deterministic: the same bytes are written on every run. The program
needs no network and reads only the image shipped in this repository.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
