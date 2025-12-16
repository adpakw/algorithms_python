from lcs import get_lcs


def test_example_from_task():
    string_1 = "AGGTAB"
    string_2 = "GXTXAYB"
    result = get_lcs(string_1, string_2)
    assert result == "GTAB"


def test_empty_strings():
    assert get_lcs("", "") == ""
    assert get_lcs("abc", "") == ""
    assert get_lcs("", "abc") == ""


def test_identical_strings():
    string = "ABCDEF"
    result = get_lcs(string, string)
    assert result == string


def test_completely_different_strings():
    result = get_lcs("ABC", "XYZ")
    assert result == ""


def test_single_character_matching():
    assert get_lcs("A", "A") == "A"
    assert get_lcs("A", "B") == ""


def test_single_character_in_longer_string():
    assert get_lcs("A", "XYZAB") == "A"
    assert get_lcs("B", "AXYZ") == ""


def test_example_1():
    x = "ABCBDAB"
    y = "BDCAB"
    result = get_lcs(x, y)
    assert len(result) == 4
    assert result == "BCAB"


def test_example_2():
    x = "ABCDGH"
    y = "AEDFHR"
    result = get_lcs(x, y)
    assert result == "ADH"
    assert len(result) == 3


def test_example_3():
    x = "AGCAT"
    y = "GAC"
    result = get_lcs(x, y)
    assert len(result) == 2
    assert result == "AC"


def test_repeating_characters():
    x = "AAAA"
    y = "AA"
    result = get_lcs(x, y)
    assert result == "AA"


def test_multiple_repetitions():
    x = "ABABAB"
    y = "BABA"
    result = get_lcs(x, y)
    assert len(result) == 4
    assert result == "BABA"

