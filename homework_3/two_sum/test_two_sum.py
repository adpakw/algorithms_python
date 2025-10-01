from two_sum import calc_two_sum


def test_calc_two_sum():
    assert calc_two_sum(arr=[1, 3, 4, 10], k=7) == (1, 2)
    assert calc_two_sum(arr=[5, 5, 1, 4], k=10) == (0, 1)

    assert calc_two_sum(arr=[2, 7, 11, 15], k=9) == (0, 1)
    assert calc_two_sum(arr=[3, 2, 4], k=6) == (1, 2)
    assert calc_two_sum(arr=[3, 3], k=6) == (0, 1)

    assert calc_two_sum(arr=[3, 5, -9], k=-6) == (0, 2)

    assert calc_two_sum(arr=[50], k=50) == (0, 0)
    assert calc_two_sum(arr=[], k=50) == (0, 0)
