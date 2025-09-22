from typing import Set, TextIO, List, Any, Dict
from io import StringIO

def observe(reader: TextIO) -> Set[str]:
    return set([line.strip() for line in reader.readlines()])

def count0(reader: TextIO) -> List[List[Any]]:
    counts = []
    for line in reader:
        bird = line.strip()
        found = False
        # Find bird in the list of bird counts
        for entry in counts:
            if entry[0] == bird:
                entry[1] += 1
                found = True
                break
        if not found: counts.append([bird, 1])
    return counts

def count1(reader: TextIO) -> List[List[Any]]: 
    bird_to_observations = {}
    for line in reader:
        bird = line.strip()
        bird_to_observations[bird] = bird_to_observations.get(bird, 0) + 1
    return bird_to_observations

def invert(d: Dict): 
    inverted = {}
    for key, value in d.items():
        if value in inverted:
            inverted[value].append(key)
        else:
            inverted[value] = [key]
    return inverted


    