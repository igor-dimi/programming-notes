from typing import TextIO, List, Optional
from io import StringIO

def read_molecule(reader: TextIO) -> list:
    """
    Read a single molecule from reader and return it, or return None to signal
    end of file. The first item in the result is the name of the compund;
    each list contains and atom type and the X, Y, and Z coordinates of that atom
    """
    # if there isn't anohter line, we're at the end of the file.
    line = reader.readline()
    if not line: return None

    # Name of the molecule: "CMPND <<name>>"
    name = line.split()[1]
    
    molecule = [name]

    line = reader.readline()
    while not line.startswith('END'):
        molecule.append(line.split()[2:])
        line = reader.readline()
    return molecule

def read_all_molecules(reader: TextIO) -> List[list]:
    """Read zero or more molecules from reader, returning a list of the molecule 
    information"""
    molecules: List[list] = []
    molecule: Optional[list] = read_molecule(reader)
    while molecule is not None:
        molecules.append(molecule)
        molecule = read_molecule(reader)
    return molecules





def read_molecule2(reader, line):
    """Read a molecule from reader, where line refers to the first line
    of molecule to be read. Return the molecucle and the first line after it.
    (or empty string if the end of file has been reached)"""

    fields = line.split()
    molecule = [fields[1]]
    line = reader.readline()
    while line and not line.startswith('COMPND'):
        fields = line.split()
        if fields[0] == 'ATOM':
            key, num, atom_type, x, y, z = fields
            molecule.append([atom_type, x, y, z])
        line = reader.readline()
    return molecule, line

def read_all_molecules2(reader: TextIO) -> list:
    """Read zero or more molecules from reader,
    returning a list of the molecules read.
    """

    result = []
    line = reader.readline()
    while line:
        molecule, line = read_molecule(reader, line)
        result.append(molecule)
    return result