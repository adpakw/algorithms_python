def rabin_karp_search(text: str, pattern: str) -> list[int]:
    base = 37
    prime = 1e9 + 7

    n = len(text)
    m = len(pattern)

    if m == 0 or n < m:
        return []

    pattern_hash = 0
    text_hash = 0
    h = 1 

    for i in range(m - 1):
        h = (h * base) % prime

    # хэши для pattern и первого окна text
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime

    result = []

    # идем по тексту окном размера m
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            # При совпадении хэшей проверяем посимвольно
            if text[i : i + m] == pattern:
                result.append(i)

        # Вычисляем хэш для следующего окна
        if i < n - m:
            text_hash = (
                base * (text_hash - ord(text[i]) * h) + ord(text[i + m])
            ) % prime

            if text_hash < 0:
                text_hash += prime

    return result