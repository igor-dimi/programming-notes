from typing import List, Tuple, Callable, Any
import time

def find_two_smallest1(L: List[float]) -> Tuple[int, int]:
    """Return a tupe of the indices of the two smallest values in list L.
    >>> items = [809, 834, 477, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(items)
    (6, 7)
    >>> items == [809, 834, 477, 307, 122, 96, 102, 324, 476]
    True
    """
    # Find the index of the minimum item and remove from the list
    smallest = min(L)
    min_index1 = L.index(smallest)
    L.remove(smallest)

    # Find the index of the new minimum item in the list
    smallest2 = min(L)
    min_index2 = L.index(smallest2)

    # Put the smallest item back in teh list
    L.insert(min_index1, smallest)
    # If necessary, adjust the second index
    if min_index1 <= min_index2: min_index2 += 1
    # Return the two indices
    return (min_index1, min_index2)

def find_two_smallest2(L: List[float]) -> Tuple[int, int]:
    """Return a tupe of the indices of the two smallest values in list L.
    >>> items = [809, 834, 477, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(items)
    (6, 7)
    >>> items == [809, 834, 477, 307, 122, 96, 102, 324, 476]
    True
    """
    # sort a copy of L
    Ls = sorted(L)
    # Get the two smallest numbers
    smallest1 = Ls[0]
    smallest2 = Ls[1]
    # Find their indices in the original list and return them
    i = L.index(smallest1)
    j = L.index(smallest2)
    return i, j

def find_two_smallest3(L: List[float]) -> Tuple[int, int]:
    """Return a tupe of the indices of the two smallest values in list L.
    >>> items = [809, 834, 477, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(items)
    (6, 7)
    >>> items == [809, 834, 477, 307, 122, 96, 102, 324, 476]
    True
    """
    # initialize min1 and min2
    if L[0] < L[1]: 
        min1, min2 = 0, 1
    else: 
        min1, min2 = 1, 0
    # Examine each value in the list in order
    for i in range(2, len(L)):
    #   Update the indices when a new smaller value is found
        if L[i] < L[min1]:
            min2 = min1
            min1 = i
        elif L[i] < L[min2]:
                min2 = i
    return min1, min2

def time_function(f: Callable[[List[float]], Any], l: List[float]) -> float:
     """
     Return how many seconds find_func(l) took to execute
     """
     t1 = time.perf_counter()
     f(l)
     t2 = time.perf_counter()
     return (t2 - t1) * 1000.0
     