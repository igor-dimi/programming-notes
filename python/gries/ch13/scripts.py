import time
from typing import Callable, Any

def ls(a, val):
    """Recursively return the index of ``val`` in list ``a`` or -1 when absent.

    Examples
    --------
    >>> ls([4, 2, 9, 1], 9)
    2
    >>> ls([4, 2, 9, 1], 5)
    -1
    """
    def lsi(a, val, i):
        if i == len(a): return -1
        if a[i] == val: return i
        return lsi(a, val, i + 1)
    return lsi(a, val, 0)

def lsi_it(a, val):
    """Iteratively return the index of ``val`` in ``a`` or -1 if not found.

    Examples
    --------
    >>> lsi_it([4, 2, 9, 1], 9)
    2
    >>> lsi_it([4, 2, 9, 1], 5)
    -1
    """
    # val not in a[0:i]
    for i in range(len(a)):
        if a[i] == val: return i
    return -1

def ls_sen(a, val):
    """Sentinel-based linear search that appends ``val`` temporarily; returns index or -1.

    Examples
    --------
    >>> data = [5, 7, 11]
    >>> ls_sen(data, 13)
    -1
    >>> data
    [5, 7, 11]
    """
    a.append(val)
    i = 0
    while a[i] != val: i += 1
    a.pop()
    if i == len(a): return -1
    return i

def bs_rec(a, val):
    """Recursive binary search for ``val`` in sorted ``a``; returns index or -1.

    Examples
    --------
    >>> bs_rec([1, 3, 5, 7, 9], 7)
    3
    >>> bs_rec([1, 3, 5, 7, 9], 2)
    -1
    """
    def bs_rec_inner(a, val, i, j):
        mid = (i + j) // 2
        if i == j: return -1
        if val == a[mid]: return mid
        if val < a[mid]: return bs_rec_inner(a, val, i, mid)
        if val > a[mid]: return bs_rec_inner(a, val, mid +  1, j)
    return bs_rec_inner(a, val, 0, len(a))
    
def bs_it(a, val):
    """Iterative binary search for ``val`` in sorted ``a``; returns index or -1.

    Examples
    --------
    >>> bs_it([1, 3, 5, 7, 9], 7)
    3
    >>> bs_it([1, 3, 5, 7, 9], 2)
    -1
    """
    i = 0
    j = len(a)
    mid = (i + j) // 2
    # val possibly in a[i:j]
    while i < j:
        if val == a[mid]: return mid
        if val < a[mid]:
            j = mid
            mid = (i + j) // 2
        else: 
            i = mid + 1
            mid = (i + j) // 2
    # i >= j
    return -1


def time_it(search_f: Callable[[list, Any], Any], a: list, v: Any) -> Any:
    """Measure ``search_f`` running on ``(a, v)`` and return elapsed milliseconds.

    Examples
    --------
    >>> duration = time_it(ls, [1, 2, 3], 3)
    >>> duration >= 0
    True
    """
    t1 = time.perf_counter()
    search_f(a, v)
    t2 = time.perf_counter()
    return (t2 - t1) * 1000.0

def find_largest(n: int, L: list) -> list:
    """Return the n largest values in ``L`` in order from smallest to largest.

    Examples
    --------
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> find_largest(3, L)
    [4, 5, 7]
    """

    copy = sorted(L)
    return copy[-n:]


def insertion_sort_rec(a):
    """Sort list ``a`` in place using recursive insertion sort.

    Examples
    --------
    >>> data = [3, 1, 4, 1]
    >>> insertion_sort_rec(data)
    >>> data
    [1, 1, 3, 4]
    """

    def insertion_sort_inner(a, i, j):
        if j <= i + 1:
            return
        insertion_sort_inner(a, i, j - 1)
        k = j - 2
        while k >= i and a[k + 1] < a[k]:
            a[k + 1], a[k] = a[k], a[k + 1]
            k -= 1

    insertion_sort_inner(a, 0, len(a))


def insertion_sort_it(a):
    """Sort list ``a`` in place using iterative insertion sort.

    Examples
    --------
    >>> data = [3, 1, 4, 1]
    >>> insertion_sort_it(data)
    >>> data
    [1, 1, 3, 4]
    """

    def insert(a, i, j):
        """Assume ``a[i:j]`` is sorted and insert ``a[j]`` into that range."""
        k = j
        while k > i and a[k] < a[k - 1]:
            a[k], a[k - 1] = a[k - 1], a[k]
            k -= 1

    i = 0
    # sorted(a[0:i+1])
    while i < len(a) - 1:
        insert(a, 0, i + 1)
        i += 1
    # i == len(a) - 1

    
def selection_sort(a):
    """Sort list ``a`` in place using selection sort (max-to-end variant).

    Examples
    --------
    >>> data = [3, 1, 4, 1, 5]
    >>> selection_sort(data)
    >>> data
    [1, 1, 3, 4, 5]
    >>> data2 = []
    >>> selection_sort(data2)
    >>> data2
    []
    """

    def find_max(a, i, j):
        """Return index of the maximum element in half-open slice ``a[i:j]``."""
        k = i + 1
        max_index = i
        # invariant: a[max_index] = max(a[i:k])
        while k < j:
            if a[max_index] < a[k]:
                max_index = k
            k += 1
        # k == j
        return max_index

    i = len(a)
    # Maintain: a[i:] is sorted and every element in a[:i] <= every in a[i:]
    while i > 1:
        # Find max in a[:i]
        max_index = find_max(a, 0, i)
        a[max_index], a[i - 1] = a[i - 1], a[max_index]
        i -= 1
    # i == 1

    
def max_rec(a):
    def max_rec_inner(a, i, j):
        if j == i + 1: return a[i]
        val = max_rec_inner(a, i, j - 1)
        if val < a[j - 1]: return a[j - 1]
        return val
    return max_rec_inner(a, 0, len(a))

def max_it(a):
    if a == []: return None
    i = 0
    max = a[i]
    # invariant: max == max(a[0:i+1])
    while i < len(a):
        if max < a[i]: max = a[i]
        i += 1
    return max

def merge(a, b):
    """Merge two sorted lists ``a`` and ``b`` into a new sorted list.

    - Inputs must be individually sorted in non-decreasing order.
    - Returns a new list; does not modify ``a`` or ``b``.
    - Stable: when elements compare equal, items from ``a`` appear before items from ``b``.

    Examples
    --------
    >>> merge([], [])
    []
    >>> merge([1, 3, 5], [])
    [1, 3, 5]
    >>> merge([], [2, 4])
    [2, 4]
    >>> merge([1, 4, 6], [2, 3, 5, 7])
    [1, 2, 3, 4, 5, 6, 7]
    >>> merge([1, 2, 2], [2, 2, 3])
    [1, 2, 2, 2, 2, 3]
    """
    res = [None] * (len(a) + len(b))
    i = 0
    j = 0
    # invariant: res[:i+j] == merge(a[:i], b[:j])
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:  # <= for stability
            res[i + j] = a[i]
            i += 1
        else:
            res[i + j] = b[j]
            j += 1

    # i == len(a) or j == len(b)
    # Copy any remainder from a
    for k in range(i, len(a)):
        res[k + j] = a[k]
    # Copy any remainder from b
    for k in range(j, len(b)):
        res[k + i] = b[k]
    return res

def merge_sort(a):
    """Return a new sorted list containing the items of ``a`` using merge sort.

    - Non-destructive: the input sequence ``a`` is not modified.
    - Stable: preserves relative order of equal elements (via ``merge``).
    - Expects items to be mutually comparable.

    Examples
    --------
    >>> data = [3, 1, 4, 1, 5]
    >>> merge_sort(data)
    [1, 1, 3, 4, 5]
    >>> data  # original remains unchanged
    [3, 1, 4, 1, 5]
    >>> merge_sort([])
    []
    >>> merge_sort([1])
    [1]
    >>> merge_sort([5, 4, 3, 2])
    [2, 3, 4, 5]
    """
    if len(a) <= 1:
        return list(a)
    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]
    return merge(merge_sort(left), merge_sort(right))
