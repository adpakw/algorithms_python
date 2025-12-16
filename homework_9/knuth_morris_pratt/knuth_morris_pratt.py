def prefix_function(text):
    n = len(text)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and text[j] != text[i]:
            j = pi[j - 1]
        if text[i] == text[j]:
            j += 1
        pi[i] = j
    return pi


def kmp_search(text, sub_text):
    j = 0
    pi = prefix_function(sub_text)
    for i in range(len(text)):
        while j > 0 and text[i] != sub_text[j]:
            j = pi[j - 1]
        if text[i] == sub_text[j]:
            j += 1
        if j >= len(sub_text):
            return i - j + 1
    return None
