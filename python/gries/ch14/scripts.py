from typing import List, Any
from typing import TextIO


class Book:
    """Information about a book"""

    def __init__(self, title: str, authors: List[str], publisher: str,
                 isbn: str, price: float) -> None:
        """Create a new book, with titel, authors, publishers,
        isbn and price information"""

        self.title = title
        # copy the authors list in case the callre modofies that list later
        self.authors = authors[:]
        self.publisher = publisher
        self.ISBN = isbn
        self.price = price

    def num_authors(self) -> int:
        """Return the number of authors of this book
        """
        return len(self.authors)
    def __str__(self) -> str:
        """return a human-readable string representation of this book"""
        return f"""Title: {self.title}
Authors: {', '.join(self.authors)}
Publisher: {self.publisher}
ISBN: {self.ISBN}
price: ${self.price}"""
    def __eq__(self, other: Any) -> bool:
        """Return True iff other is a book,
        and this book and other have the same ISBN"""
        return isinstance(other, Book) and \
        self.ISBN == other.ISBN

class Member:
    """A member of a university"""

    def __init__(self, name: str, address: str, email: str) -> None:
        self.name = name
        self.address = address
        self.email = email
    
    def __str__(self) -> str:
        """return a string representation of this member"""

        return f"""name: {self.name}
address: {self.address}
email: {self.email}"""

class Faculty(Member):
    """A faculty member at a university."""
    def __init__(self, name: str, address: str, email: str,
                 faculty_num: str) -> None:
        super().__init__(name, address, email)
        self.faculty_num = faculty_num
        self.courses_teaching = []
    def __str__(self) -> str:
        member_string = super().__str__()
        return f"""{member_string}
faculty no: {self.faculty_num}
courses: {', '.join(self.courses_teaching)}
"""

class Student(Member):
    """A student member at a university"""
    def __init__(self, name: str, address: str, email: str,
                 student_num: str) -> None:
        super().__init__(name, address, email)
        self.student_number = student_num
        self.courses_taken = []
        self.courses_taking = []

class Atom:
    """An atom with a number, symbol, and coordinates"""
    def __init__(self, num: int, sym: str, x: float, y: float,
                 z: float) -> None:
        """Create an Atom with number num, string symbol sym,
        and float coordinates (x, y, z)"""

        self.number = num
        self.center = (x, y, z)
        self.symbol = sym

    def __str__(self) -> str:
        """Return a string representation of this Atom in this
        format:
        
        (Symbol, x, y, z)
        """
        coordinate_string = ", ".join([str(x) for x in self.center])
        return f"({self.symbol}, {coordinate_string})"
    
    def __repr__(self) -> str:
        """Return a string representation of this Atom in this format:

        Atom(Number, "Symbol", x, y, z)

        """
        coordinate_string = ", ".join([str(x) for x in self.center])
        return f"Atom({self.number}, {self.symbol}, {coordinate_string})"

    def translate(self, x: float, y: float, z: float) -> None:
        """Move this Atom by adding (x, y, z) to its coordinates"""
        self.center = tuple(a + b for a, b in zip(self.center, (x, y, z)))

class Molecule:
    """A molecule with a name and a list of Atoms"""

    def __init__(self, name: str) -> None:
        """Create a molecule named name with no Atoms"""

        self.name = name
        self.atoms = []

    def add(self, a: Atom) -> None:
        """Add to my list of Atoms"""
        self.atoms.append(a)

    def __str__(self) -> str:
        """return a string representation of this molecule
        in this format:

        (Name, (atom1, atom2, ...))
        """
        atoms_str = ', '.join([str(a) for a in self.atoms])
        return f"({self.name}, ({atoms_str}))"
    
    def __repr__(self) -> str:
        """return a string representation of this molecule in
        this format:
        
        Molecule("name", (atom1, atom2, ...))
        
        """
        atoms_str = ', '.join([repr(a) for a in self.atoms])
        return f"Molecule({self.name}, ({atoms_str}))"

    def translate(self, x: float, y: float, z: float) -> None:
        """Move this molecule including all atoms, by (x, y, z)"""
        for a in self.atoms:
            a.translate(x, y, z)


def read_molecule(r: TextIO) -> Molecule:
    """Read a single molecule from r and return it"""
    # if there isn't another line, we're at the end of the file.
    line = r.readline()
    if not line: return None

    # name of the molecule
    name = line.split()[1]
    molecule = Molecule(name)
    line = r.readline()
    while not line.startswith('END'):
        key, num, symbol, x, y, z = line.split()
        a = Atom(num, symbol, float(x), float(y), float(z))
        molecule.add(a)
        line = r.readline()
    return molecule

