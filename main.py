"""Copy the round-5 entry image to the grader output directory.

Reads entry.png next to this file and writes it, byte for byte, to
$MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png when the variable
is unset). No network, no randomness, no re-encoding: the output is
identical to the committed image on every run.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
DST = os.path.join(OUT_DIR, "entry.png")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, DST)
print("copied", SRC, "->", DST, os.path.getsize(DST), "bytes")
