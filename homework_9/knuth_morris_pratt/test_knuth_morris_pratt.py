from knuth_morris_pratt import kmp_search


def test_basic_search():
    text = "hello world"
    pattern = "world"
    result_opt = kmp_search(text, pattern)
    assert result_opt == 6

def test_multiple_occurrences():
    text = "ababcababcababc"
    pattern = "ababc"
    result = kmp_search(text, pattern)
    assert result == 0

def test_no_occurrence():
    text = "abcdefgh"
    pattern = "xyz"
    
    result_opt = kmp_search(text, pattern)
    assert result_opt == None

def test_pattern_longer_than_text():
    text = "abc"
    pattern = "abcd"
    result = kmp_search(text, pattern)
    assert result == None


def test_empty_text():
    text = ""
    pattern = "abc"
    result = kmp_search(text, pattern)
    assert result == None


def test_both_empty():
    text = ""
    pattern = ""
    result = kmp_search(text, pattern)
    assert result == None


def test_pattern_at_beginning():
    text = "abcdefgh"
    pattern = "abc"
    result = kmp_search(text, pattern)
    assert result == 0
    

def test_pattern_at_end():
    text = "abcdefgh"
    pattern = "fgh"
    result = kmp_search(text, pattern)
    assert result == 5


def test_pattern_equals_text():
    text = "abcdef"
    pattern = "abcdef"
    result = kmp_search(text, pattern)
    assert result == 0


def test_partial_matches_and_backtracking():
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    result = kmp_search(text, pattern)
    assert result == 10
