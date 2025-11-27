from k_th import quick_select


def test_simple_example():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    assert quick_select(nums, k) == 5


def test_all_duplicates():
    nums = [5, 5, 5, 5, 5]
    k = 3
    assert quick_select(nums, k) == 5


def test_single_element():
    nums = [42]
    k = 1
    result = quick_select(nums, k)
    assert result == 42


def test_two_elements():
    nums = [2, 1]
    k = 1
    result = quick_select(nums, k)
    assert result == 2

    k = 2
    result = quick_select(nums, k)
    assert result == 1


def test_negative_numbers():
    nums = [-1, -5, -3, -2]
    k = 1
    result = quick_select(nums, k)
    assert result == -1


def test_zeros():
    nums = [0, 0, 0, 1, 0]
    k = 2
    result = quick_select(nums, k)
    assert result == 0


def test_reverse_sorted():
    nums = [5, 4, 3, 2, 1]
    k = 3
    result = quick_select(nums, k)
    assert result == 3
