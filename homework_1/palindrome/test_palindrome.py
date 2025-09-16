import pytest
from palindrome import is_palindrome


def test_negative_value():
    assert is_palindrome(-1) == False


def test_zero():
    assert is_palindrome(0) == True


def test_digit():
    assert is_palindrome(4) == True


def test_not_palindrome():
    assert is_palindrome(12345) == False
    assert is_palindrome(10) == False
    assert is_palindrome(1212) == False


def test_palindrome():
    assert is_palindrome(1234321) == True
    assert is_palindrome(1) == True
    assert is_palindrome(909) == True
