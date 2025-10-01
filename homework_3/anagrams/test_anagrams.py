from anagrams import group_anagrams


def sort_anagrams_result(result):
    """
        Функция для сортировки слов внутри каждого листа и затем сортировки самих листов,
        чтобы не было таких проблем:

            def test_group_anagrams():
    >       assert group_anagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]) == [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    E       AssertionError: assert [['eat', 'tea...at'], ['bat']] == [['bat'], ['n...'eat', 'tea']]
    E
    E         At index 0 diff: ['eat', 'tea', 'ate'] != ['bat']
    """
    return sorted([sorted(group) for group in result])


def test_group_anagrams():
    assert sort_anagrams_result(
        group_anagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"])
    ) == sort_anagrams_result([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])

    assert group_anagrams(strs=[""]) == [[""]]
    assert group_anagrams(strs=["a"]) == [["a"]]
    assert group_anagrams(strs=["bla"]) == [["bla"]]

    assert sort_anagrams_result(
        group_anagrams(strs=["abc", "def", "ghi"])
    ) == sort_anagrams_result([["abc"], ["def"], ["ghi"]])

    assert sort_anagrams_result(
        group_anagrams(strs=["abc", "bca", "cab", "cba"])
    ) == sort_anagrams_result([["abc", "bca", "cab", "cba"]])

    assert sort_anagrams_result(
        group_anagrams(strs=["a", "ab", "ba", "abc", "cba"])
    ) == sort_anagrams_result([["a"], ["ab", "ba"], ["abc", "cba"]])
