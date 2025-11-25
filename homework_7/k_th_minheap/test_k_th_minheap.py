from k_th_minheap import find_kth_largest_custom_heap, find_kth_largest_heapq

def test_basic_case_1():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    result_custom = find_kth_largest_custom_heap(nums, k)
    result_heapq = find_kth_largest_heapq(nums, k)
    expected = 5
    assert result_custom == expected
    assert result_heapq == expected

def test_basic_case_2():
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    result_custom = find_kth_largest_custom_heap(nums, k)
    result_heapq = find_kth_largest_heapq(nums, k)
    expected = 4
    assert result_custom == expected
    assert result_heapq == expected

def test_single_element():
    nums = [1]
    k = 1
    result_custom = find_kth_largest_custom_heap(nums, k)
    result_heapq = find_kth_largest_heapq(nums, k)
    expected = 1
    assert result_custom == expected
    assert result_heapq == expected

def test_k_equals_array_length():
    nums = [1, 2, 3, 4, 5]
    k = 5
    result_custom = find_kth_largest_custom_heap(nums, k)
    result_heapq = find_kth_largest_heapq(nums, k)
    expected = 1 
    assert result_custom == expected
    assert result_heapq == expected

def test_k_equals_1():
    nums = [1, 2, 3, 4, 5]
    k = 1
    result_custom = find_kth_largest_custom_heap(nums, k)
    result_heapq = find_kth_largest_heapq(nums, k)
    expected = 5
    assert result_custom == expected
    assert result_heapq == expected

def test_duplicate_elements():
    nums = [5, 5, 5, 5, 5]
    k = 3
    result_custom = find_kth_largest_custom_heap(nums, k)
    result_heapq = find_kth_largest_heapq(nums, k)
    expected = 5
    assert result_custom == expected
    assert result_heapq == expected

def test_negative_numbers():
    nums = [-1, -3, -2, -5, -4]
    k = 2
    result_custom = find_kth_largest_custom_heap(nums, k)
    result_heapq = find_kth_largest_heapq(nums, k)
    expected = -2
    assert result_custom == expected
    assert result_heapq == expected

def test_mixed_numbers():
    nums = [-1, 2, -3, 4, 0]
    k = 3
    result_custom = find_kth_largest_custom_heap(nums, k)
    result_heapq = find_kth_largest_heapq(nums, k)
    expected = 0
    assert result_custom == expected
    assert result_heapq == expected

def test_large_k():
    nums = [7, 10, 4, 3, 20, 15]
    k = 3
    result_custom = find_kth_largest_custom_heap(nums, k)
    result_heapq = find_kth_largest_heapq(nums, k)
    expected = 10
    assert result_custom == expected
    assert result_heapq == expected