# SPDX-License-Identifier: MIT
"""Entry for make.fun news-image-20261120 (round 4).

Copies the pre-built image ``entry.png`` to the output directory as
``entry.png``. The image is a one-page newspaper collage summing up
Friday 20 November 2026: a date header, six captioned feature panels
(Kyiv bridges hit, Cyclone Akvan, UK-EU deal, AI sell-off, Shenzhen
summit, World Court ruling) and 32 further headlines across 8 regions,
38 stories in total.

Round 4 changes vs round 3 (36 stories, commit 48a45ef): two new
verified Friday stories added to the grid -- Iraq (troops enter the
Kataib Hezbollah stronghold of Jurf al-Sakhar under a deal on oil
smuggling, Reuters) and Korea cholera (first case in 10 years,
Changwon patient, no overseas travel, AP/KDCA). The image is built
by ``work/build_entry_r4.py`` (kept out of git by .gitignore, as in
rounds 2-3); layout re-fit for the extra grid row (panels 136 px,
grid rows stay 41 px); all other stories, feature captions and the
6-panel base image are unchanged from round 3. Round-4 fact checks: Japan quake "2 injured"
confirmed (JMA/Kyodo); AI sell-off figures confirmed (WSJ/Reuters/
CNN: Nasdaq -5.3%, Anthropic -9%, Nvidia -14%, VIX +33% to 37).

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
