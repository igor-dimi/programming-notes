from typing import TextIO
from io import StringIO
from typing import Iterable, Optional, TextIO
import my_ts


def process_file(reader: TextIO) -> list[Optional[float]]:
    """
    Skip the title, i.e. the first line,
    Skip comment line, i.e. ones starting with '#',
    return a list of numeric data values that
    """
    values = []
    def split_line(line: str) -> list[Optional[float]]:
        """
        split a string like '1. 2. 3.' into [1, 2, 3]
        """
        return  [float(v.strip('.')) for v in line.split()]

    line = my_ts.skip_header(reader)
    values += split_line(line)
    for line in reader:
        values += split_line(line)
    return values

