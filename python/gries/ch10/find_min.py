from typing import TextIO
from io import StringIO
import time_series

def smallest_value(reader: TextIO) -> int:
    """
    Read and process reader and return the smallest value after 
    the time_series header
    >>> infile = StringIO('Example\\n# Comment\\n# Comment\\nn1\\n2\\n3\\n')
    >>> smallest_value(infile)
    1
    >>> infile = StringIO('Example\\n# Comment\\n# Comment\\nn2\\n1\\n3\\n')
    >>> smallest_value(infile)
    1
    """

    line = time_series.skip_header(reader).strip()
    if not line.isnumeric(): smallest = float("inf")
    else: smallest = int(line)


    for line in reader:
        if not line.isnumeric(): continue
        smallest = int(line.strip())
    return smallest

if __name__ == '__main__':
    with open('hopedale.txt') as infile:
        print(smallest_value(infile))