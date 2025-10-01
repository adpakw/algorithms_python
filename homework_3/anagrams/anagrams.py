def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Логика:
    - Создаем dict, в котором будем хранить key(отсортированную строку), value(лист с анаграммами)
    - Идем итератитивно по листу и сортируем строку, если есть в dict ключ = отсортированной строке, то добавляем в value лист слово, иначе создаем лист со словом
    """
    dict_anagrams: dict[str, list[str]] = {}

    for str_ in strs:
        str_sorted = "".join(sorted(str_))
        if str_sorted in dict_anagrams:
            dict_anagrams[str_sorted].append(str_)
        else:
            dict_anagrams[str_sorted] = [str_]

    return list(dict_anagrams.values())
