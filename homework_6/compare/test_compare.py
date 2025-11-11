import sys

import numpy as np
from sorters import mergesort, quicksort

sys.setrecursionlimit(20_000)

def test_random_list():
    random_list = np.random.randint(
        low=np.iinfo(np.int64).min, high=np.iinfo(np.int64).max, size=10_000_000
    )

    result_merge_sort_random_list = mergesort(random_list)
    result_quick_sort_random_list = quicksort(random_list)

    assert result_merge_sort_random_list == sorted(random_list)
    assert result_quick_sort_random_list == sorted(random_list)


def test_random_w_dublicates_list():
    random_w_dublicates_list = np.random.randint(
        low=-10, high=10, size=10_000_000
    )

    result_merge_sort_random_w_dublicates_list = mergesort(random_w_dublicates_list)
    result_quick_sort_random_w_dublicates_list = quicksort(random_w_dublicates_list)

    assert result_merge_sort_random_w_dublicates_list == sorted(random_w_dublicates_list)
    assert result_quick_sort_random_w_dublicates_list == sorted(random_w_dublicates_list)

def test_all_same_list():
    all_same_list = [5] * 10_000_000

    result_merge_sort_all_same_list = mergesort(all_same_list)
    result_quick_sort_all_same_list = quicksort(all_same_list)
    
    assert result_merge_sort_all_same_list == sorted(all_same_list)
    assert result_quick_sort_all_same_list == sorted(all_same_list)

def test_sorted_list():
    sorted_list = list(range(10_000))

    result_merge_sort_sorted_list = mergesort(sorted_list)
    result_quick_sort_sorted_list = quicksort(sorted_list)

    assert result_merge_sort_sorted_list == sorted(sorted_list)
    assert result_quick_sort_sorted_list == sorted(sorted_list)

def test_reversed_sorted():
    reversed_sorted = list(range(10_000, 0, -1))

    result_merge_sort_reversed_sorted = mergesort(reversed_sorted)
    result_quick_sort_reversed_sorted = quicksort(reversed_sorted)

    assert result_merge_sort_reversed_sorted == sorted(reversed_sorted)
    assert result_quick_sort_reversed_sorted == sorted(reversed_sorted)

