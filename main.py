# SPDX-License-Identifier: MIT
"""Entry for make.fun news-image-20261120 (round 3).

Copies the pre-built image ``entry.png`` to the output directory as
``entry.png``. The image is a one-page newspaper collage summing up
Friday 20 November 2026: a date header, six captioned feature panels
(Kyiv bridges hit, Cyclone Akvan, UK-EU deal, AI sell-off, Shenzhen
summit, World Court ruling) and 30 further headlines across 8 regions,
36 stories in total.

Round 3 changes vs round 2 (30 stories, 7 regions): the UK-EU deal
was promoted to a feature panel, Riyadh moved to the grid, duplicates
were removed, Gaza was re-tagged (WED), and 7 new verified stories
were added (Moldova airspace, Ukraine oil strikes, Haiti raid,
Somalia-UAE expulsion, Nvidia SEC probe, global-markets correction,
tech rout, Japan quake, Cyclone Xavier, Van Gogh record sale).

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
    # Byte-identical on every run: a plain copy, no timestamps embedded.
    # The shipped image is checked at build time: 1024x1024, <= 1 MiB.
    return 0


if __name__ == "__main__":
    sys.exit(main())
