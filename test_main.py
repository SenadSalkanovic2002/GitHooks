# test_main.py

from main import merge_sort

def test_sorted_array():
    assert merge_sort([1, 2, 3]) == [1, 2, 3]

def test_unsorted_array():
    assert merge_sort([4, 2, 7, 1]) == [1, 2, 4, 7]

def test_empty_array():
    assert merge_sort([]) == []

def test_single_element():
    assert merge_sort([42]) == [42]

def test_duplicates():
    assert merge_sort([5, 3, 5, 3]) == [3, 3, 5, 5]

def test_negative_numbers():
    assert merge_sort([0, -1, -10, 8]) == [-10, -1, 0, 8]
