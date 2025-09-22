from typing import TextIO, Iterable, Optional
from io import StringIO

def skip_header(reader: TextIO) -> str:
    """
    Skip the header in reader and return the first real piece of data
    >>> infile = String('Title\\n# Comment\\n# Comment\\n1.3\\n2.3\\n')
    >>> skip_header(infile)
    '1.3\\n'
    """

    # read the description line
    line = reader.readline()

    # find the frist non-comment line
    line = reader.readline().strip()
    while line.startswith('#'):
        line = reader.readline().strip()
    # now line contains the first data line
    return line

def process_file(reader: TextIO) -> list[Optional[float]]:
    """
    Read and print the data from reader, which must start with a single
    description line, then a sequence of lines beginning with '#', then a 
    sequence of data.
    >>> infile = String('Title\\n# Comment\\n# Comment\\n1.3\\n2.3\\n')
    >>> process_file(infile)
    [1.3, 2.3]
    """

    values: list[Optional[float]] = []
    values.append(skip_header(reader).strip())
    for line in reader:
        values.append(line.strip())
    return [float(v) if v not in ("", "-", "--") else None for v in values]

def min_value(values: Iterable[Optional[float]]) -> Optional[float]:
    values = [v for v in values if v is not None]
    if not values: return None
    return min(values)
    

