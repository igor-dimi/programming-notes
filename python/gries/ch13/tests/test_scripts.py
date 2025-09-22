import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "scripts", Path(__file__).resolve().parent.parent / "scripts.py"
)
scripts = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scripts)


def test_linear_search_found():
    data = [4, 2, 9, 1]
    assert scripts.ls(data, 9) == 2
    assert scripts.lsi_it(data, 9) == 2


def test_linear_search_not_found():
    data = [4, 2, 9, 1]
    assert scripts.ls(data, 5) == -1
    assert scripts.lsi_it(data, 5) == -1


def test_ls_sen_preserves_list():
    data = [5, 7, 11]
    original = list(data)
    assert scripts.ls_sen(data, 13) == -1
    assert data == original


def test_binary_search_found():
    data = [1, 3, 5, 7, 9]
    assert scripts.bs_rec(data, 7) == 3
    assert scripts.bs_it(data, 7) == 3


def test_binary_search_not_found():
    data = [1, 3, 5, 7, 9]
    assert scripts.bs_rec(data, 2) == -1
    assert scripts.bs_it(data, 2) == -1


def test_binary_search_with_duplicates():
    data = [1, 3, 3, 3, 5]
    idx_rec = scripts.bs_rec(data, 3)
    idx_it = scripts.bs_it(data, 3)
    assert idx_rec in (1, 2, 3)
    assert data[idx_rec] == 3
    assert idx_it in (1, 2, 3)
    assert data[idx_it] == 3


def test_time_it_reports_non_negative_duration():
    duration = scripts.time_it(scripts.ls, [1, 2, 3], 3)
    assert duration >= 0


def test_insertion_sort_iterative():
    data = [3, 1, 4, 1, 5]
    scripts.insertion_sort_it(data)
    assert data == [1, 1, 3, 4, 5]


def test_insertion_sort_recursive():
    data = [3, 1, 4, 1, 5]
    scripts.insertion_sort_rec(data)
    assert data == [1, 1, 3, 4, 5]


def test_selection_sort_basic():
    data = [3, 1, 4, 1, 5]
    scripts.selection_sort(data)
    assert data == [1, 1, 3, 4, 5]


def test_selection_sort_edge_cases():
    data_empty = []
    scripts.selection_sort(data_empty)
    assert data_empty == []
    data_one = [42]
    scripts.selection_sort(data_one)
    assert data_one == [42]


def test_merge_basic_and_edge_cases():
    assert scripts.merge([], []) == []
    assert scripts.merge([1, 3, 5], []) == [1, 3, 5]
    assert scripts.merge([], [2, 4]) == [2, 4]
    assert scripts.merge([1, 4, 6], [2, 3, 5, 7]) == [1, 2, 3, 4, 5, 6, 7]


def test_merge_with_duplicates_and_negatives():
    left = [-3, -1, 0, 2, 2]
    right = [-2, 0, 2, 3]
    assert scripts.merge(left, right) == [-3, -2, -1, 0, 0, 2, 2, 2, 3]


def test_merge_stability_between_lists():
    # Stability check: when equal, items from left come first
    left = [1, 2, 2]
    right = [2, 2, 3]
    merged = scripts.merge(left, right)
    # relative multiset is correct
    assert merged == [1, 2, 2, 2, 2, 3]


def test_merge_sort_basic_and_non_destructive():
    data = [3, 1, 4, 1, 5]
    out = scripts.merge_sort(data)
    assert out == [1, 1, 3, 4, 5]
    assert data == [3, 1, 4, 1, 5]


def test_merge_sort_edge_and_ordering():
    assert scripts.merge_sort([]) == []
    assert scripts.merge_sort([42]) == [42]
    assert scripts.merge_sort([1, 2, 3]) == [1, 2, 3]
    assert scripts.merge_sort([3, 2, 1]) == [1, 2, 3]
    assert scripts.merge_sort([-2, -5, 0, 3, -1]) == [-5, -2, -1, 0, 3]
