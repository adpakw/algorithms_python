from typing import List, Tuple


def lcs_length(x: str, y: str) -> Tuple[List[List[int]], List[List[int]]]:
    m, n = len(x), len(y)

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    direction = [
        [0] * (n + 1) for _ in range(m + 1)
    ]  # 0 = диагональ, 1 = вверх, 2 = влево

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                direction[i][j] = 0
            elif dp[i - 1][j] >= dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j]
                direction[i][j] = 1
            else:
                dp[i][j] = dp[i][j - 1]
                direction[i][j] = 2

    return dp, direction


def get_lcs(x: str, y: str) -> str:
    dp, direction = lcs_length(x, y)
    m, n = len(x), len(y)

    # Восстанавливаем LCS
    result = []
    i, j = m, n

    while i > 0 and j > 0:
        if direction[i][j] == 0:
            result.append(x[i - 1])
            i -= 1
            j -= 1
        elif direction[i][j] == 1:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(result))
