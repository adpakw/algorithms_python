from rabin_karp import rabin_karp_search


def test_basic_search():
    text = "hello world"
    pattern = "world"
    result = rabin_karp_search(text, pattern)
    assert result == [6]

def test_multiple_occurrences():
    text = "ababaababa"
    pattern = "aba"
    result = rabin_karp_search(text, pattern)
    assert result == [0, 2, 5, 7]

def test_no_occurrence():
    text = "abcdefgh"
    pattern = "xyz"
    result = rabin_karp_search(text, pattern)
    assert result == []

def test_empty_pattern():
    text = "some text"
    pattern = ""
    result = rabin_karp_search(text, pattern)
    assert result == []

def test_pattern_longer_than_text():
    text = "abc"
    pattern = "abcd"
    result = rabin_karp_search(text, pattern)
    assert result == []

def test_empty_text():
    text = ""
    pattern = "abc"
    result = rabin_karp_search(text, pattern)
    assert result == []

def test_both_empty():
    text = ""
    pattern = ""
    result = rabin_karp_search(text, pattern)
    assert result == []

def test_pattern_at_beginning():
    text = "abcdefgh"
    pattern = "abc"
    result = rabin_karp_search(text, pattern)
    assert result == [0]

def test_pattern_at_end():
    text = "abcdefgh"
    pattern = "fgh"
    result = rabin_karp_search(text, pattern)
    assert result == [5]

def test_pattern_equals_text():
    text = "abcdef"
    pattern = "abcdef"
    result = rabin_karp_search(text, pattern)
    assert result == [0]
