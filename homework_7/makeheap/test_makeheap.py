from makeheap import makeheap, makeheap_n_log_n
from typing import List, Union


def is_min_heap(heap: List[Union[int, float]]) -> bool:
    if not heap:
        return True

    n = len(heap)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and heap[left] < heap[i]:
            print("left")
            print(heap[left], heap[i])
            return False
        if right < n and heap[right] < heap[i]:
            print("right")
            print(heap[right], heap[i])
            return False

    return True


def test_base():
    arr = [1, 4, 2, 7, 5, 6, 3]
    result_makeheap = makeheap(arr)
    result_makeheap_n_log_n = makeheap_n_log_n(arr)

    assert is_min_heap(result_makeheap)
    assert is_min_heap(result_makeheap_n_log_n)


def test_makeheap_basic():
    arr = [4, 2, 8, 1, 5]
    result_makeheap = makeheap(arr)
    result_makeheap_n_log_n = makeheap_n_log_n(arr)

    assert is_min_heap(result_makeheap)
    assert is_min_heap(result_makeheap_n_log_n)


def test_empty_array():
    arr = []

    result1 = makeheap(arr)
    result2 = makeheap_n_log_n(arr)

    assert result1 == []
    assert result2 == []


def test_single_element():
    arr = [42]

    result1 = makeheap(arr)
    result2 = makeheap_n_log_n(arr)

    assert result1 == [42]
    assert result2 == [42]


def test_already_heap():
    arr = [1, 3, 2, 6, 4, 5]

    result1 = makeheap(arr)
    result2 = makeheap_n_log_n(arr)

    assert is_min_heap(result1)
    assert is_min_heap(result2)


def test_reverse_sorted():
    arr = [10, 8, 6, 4, 2, 1]

    result1 = makeheap(arr)
    result2 = makeheap_n_log_n(arr)

    assert is_min_heap(result1)
    assert is_min_heap(result2)


def test_duplicate_values():
    arr = [3, 1, 3, 2, 1, 2]

    result1 = makeheap(arr)
    result2 = makeheap_n_log_n(arr)

    assert is_min_heap(result1)
    assert is_min_heap(result2)
