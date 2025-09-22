from __future__ import annotations
from typing import TextIO
import argparse, sys
from contextlib import ExitStack

def sum_number_pairs(in_file : TextIO, out_file : TextIO) -> None:
    for line in in_file:
        line = line.strip()
        if not line: continue # ignore blank lines
        a_str, b_str = line.split()
        a = float(a_str)
        b = float(b_str)
        out_file.write(f"{a_str} {b_str} {a + b}\n")

def _open_text(path: str, mode: str) -> TextIO:
    """Open a path as text. '-' maps to stdin/stdout."""
    if path == "-":
        if "r" in mode: return sys.stdin
        elif "w" in mode or "a" in mode: return sys.stdout
        else: raise ValueError("Unsupported mode for '-': " + mode)
    return open(path, mode, encoding="utf-8", newline="")
    
if __name__ == '__main__':
    with open('number_pairs.txt', 'r') as in_file, \
        open('number_pairs_sums.txt', 'w') as out_file:
        sum_number_pairs(in_file, out_file)