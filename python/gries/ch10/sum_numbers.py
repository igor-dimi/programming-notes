from typing import TextIO
from io import StringIO

def process_pairs(input_file: TextIO, output_file: TextIO) -> None:
    """
    Read lines from `input_file`, each containing two floats separated by whitespace.
    For each line, write the original two numbers followed by their sum to `output_file`,
    with values separated by a single space.


    >>> infile = StringIO('1.3 3.4\\n2 4.2\\n-1 1\\n')
    >>> outfile = StringIO()
    >>> process_pairs(infile, outfile)
    >>> outfile.getvalue()
    '1.3 3.4 4.7\\n2 4.2 6.2\\n-1 1 0.0\\n'
    """
    for line in input_file:
        parts = line.strip().split()
        total = float(parts[0]) + float(parts[1])
        output_file.write(f"{line.strip()} {total}\n")

def main() -> None:
    with open("pairs.txt", "r", encoding="utf-8") as input_file, \
         open("pairs_sum.txt", "w", encoding="utf-8") as output_file:
        process_pairs(input_file, output_file)


if __name__ == "__main__":
    main()
