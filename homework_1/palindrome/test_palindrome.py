from palindrome import is_palindrome


def test_negative_value():
    assert not is_palindrome(-1)


def test_zero():
    assert is_palindrome(0)


def test_digit():
    assert is_palindrome(4)


def test_not_palindrome():
    assert not is_palindrome(12345)
    assert not is_palindrome(10)
    assert not is_palindrome(1212)


def test_palindrome():
    assert is_palindrome(1234321)
    assert is_palindrome(1)
    assert is_palindrome(909)
