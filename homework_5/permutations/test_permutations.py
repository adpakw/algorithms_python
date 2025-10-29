from permutations import permute


def sort_result(result):
    return sorted([sorted(group) for group in result])


def test_single_element():
    assert permute([1]) == [[1]]


def test_two_elements():
    result = permute([0, 1])
    expected = [[0, 1], [1, 0]]
    assert sort_result(result) == sort_result(expected)


def test_three_elements():
    result = permute([1, 2, 3])
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert sort_result(result) == sort_result(expected)


def test_elements():
    result = permute([1, 2, 3, 4])
    expected = [
        [1, 2, 3, 4],
        [1, 2, 4, 3],
        [1, 3, 2, 4],
        [1, 3, 4, 2],
        [1, 4, 3, 2],
        [1, 4, 2, 3],
        [2, 1, 3, 4],
        [2, 1, 4, 3],
        [2, 3, 1, 4],
        [2, 3, 4, 1],
        [2, 4, 3, 1],
        [2, 4, 1, 3],
        [3, 2, 1, 4],
        [3, 2, 4, 1],
        [3, 1, 2, 4],
        [3, 1, 4, 2],
        [3, 4, 1, 2],
        [3, 4, 2, 1],
        [4, 2, 3, 1],
        [4, 2, 1, 3],
        [4, 3, 2, 1],
        [4, 3, 1, 2],
        [4, 1, 3, 2],
        [4, 1, 2, 3],
    ]
    assert sort_result(result) == sort_result(expected)


def test_empty_list():
    assert permute([]) == [[]]
