from validate import count_primes_v2


def test_sum():
    assert count_primes_v2(114) == 30
    assert count_primes_v2(10) == 4
    assert count_primes_v2(2) == 0
    assert count_primes_v2(1) == 0
    assert count_primes_v2(0) == 0
    assert count_primes_v2(-10) == 0
