from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, Optional, TextIO


@dataclass(frozen=True)
class SeriesFile:
    title: str
    comments: list[str]
    values: list[Optional[float]] # None represents a missing value "-"

class ParseError(ValueError):
    pass

def parse_timeseries(fp: TextIO, *, strict: bool = False) -> SeriesFile:
    """
    Parse the custom timeseries format.

    - Line 1: title (free text)
    - Lines starting with '#': comments (0..n)
    - Remaining lines: either a number (int/float) or a single '-' for missing.

    strict=False (default): Unknown data lines become None; strict=True: raise ParseError
    """

    # Read title
    first = fp.readline()
    if first == "":
        raise ParseError("empty file: missing title")
    title = first.rstrip("\n")

    # Collect comments
    comments: list[str] = []
    pos = fp.tell()
    while True:
        line = fp.readline()
        if line == "":
            # No data section; empty series
            return SeriesFile(title=title, comments=comments, values=[])
        stripped = line.lstrip()
        if stripped.startswith("#"):
            comments.append(line.rstrip("\n"))
            pos = fp.tell()
            continue
        # Not a comment, data begins. rewind to include this line in data part
        fp.seek(pos)
        break

    # parse data lines
    values: list[Optional[float]] = []
    for lineno, raw in enumerate(fp, start=1):
        s = raw.strip()
        if s == "":
            # empty line between rows: skip silently
            continue
        if s == "-":
            values. append(None)
            continue
        try:
            values.append(float(s))
        except ValueError:
            if strict:
                raise ParseError(f"malformed data line {lineno}: {raw.rstrip()!r}")
            values.append(None)

    return SeriesFile(title=title, comments=comments, values=values)

def min_values(values: Iterable[Optional[float]], *, fail_on_missing: bool = False) -> Optional[float]:
    """Return the minimum over present values; None if no present values"""
    present = [v for v in values if v is not None]
    if not present:
        if fail_on_missing:
            raise ValueError("no present values to compute minimum")
        return None
    return min(present)

def sum_value(values: Iterable[Optional[float]], *, treat_missing_as: Optional[float] = None) -> float:
    """
    Sum the series
    - If treat_missing_as is None (default), missing entries are skipped
    - If it is a number (e.g. 0.0), missing entries contribute that number
    """
    total = 0.0
    for v in values:
        if v is None:
            if treat_missing_as is None:
                continue
            total += treat_missing_as
        else:
            total += v
    return total