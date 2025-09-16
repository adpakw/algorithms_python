from sum import find_max_sum_div_2_v3


def test_sum():
    assert find_max_sum_div_2_v3("5 7 13 2 14") == 36
    assert find_max_sum_div_2_v3("3") == 0
    assert find_max_sum_div_2_v3("0") == 0
    assert find_max_sum_div_2_v3("12 9 23 54 89") == 178
