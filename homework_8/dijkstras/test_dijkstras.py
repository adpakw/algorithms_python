import numpy as np
from homework_8.dijkstras.dijkstras import mergesort_iter, quicksort_iter


def test_random_list():
    random_list = list(np.random.randint(
        low=np.iinfo(np.int64).min, high=np.iinfo(np.int64).max, size=10_000_000
    ))

    result_merge_sort_random_list = mergesort_iter(random_list)
    result_quick_sort_random_list = quicksort_iter(random_list)

    assert result_merge_sort_random_list == sorted(random_list)
    assert result_quick_sort_random_list == sorted(random_list)


def test_random_w_dublicates_list():
    random_w_dublicates_list = list(np.random.randint(low=-10, high=10, size=10_000))

    result_merge_sort_random_w_dublicates_list = mergesort_iter(
        random_w_dublicates_list
    )
    result_quick_sort_random_w_dublicates_list = quicksort_iter(
        random_w_dublicates_list
    )

    assert result_merge_sort_random_w_dublicates_list == sorted(
        random_w_dublicates_list
    )
    assert result_quick_sort_random_w_dublicates_list == sorted(
        random_w_dublicates_list
    )


def test_all_same_list():
    all_same_list = [5] * 10_000

    result_merge_sort_all_same_list = mergesort_iter(all_same_list)
    result_quick_sort_all_same_list = quicksort_iter(all_same_list)

    assert result_merge_sort_all_same_list == sorted(all_same_list)
    assert result_quick_sort_all_same_list == sorted(all_same_list)


def test_sorted_list():
    sorted_list = list(range(10_000))

    result_merge_sort_sorted_list = mergesort_iter(sorted_list)
    result_quick_sort_sorted_list = quicksort_iter(sorted_list)

    assert result_merge_sort_sorted_list == sorted(sorted_list)
    assert result_quick_sort_sorted_list == sorted(sorted_list)


def test_reversed_sorted():
    reversed_sorted = list(range(10_000, 0, -1))

    result_merge_sort_reversed_sorted = mergesort_iter(reversed_sorted)
    result_quick_sort_reversed_sorted = quicksort_iter(reversed_sorted)

    assert result_merge_sort_reversed_sorted == sorted(reversed_sorted)
    assert result_quick_sort_reversed_sorted == sorted(reversed_sorted)
