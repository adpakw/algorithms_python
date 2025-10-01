def calc_two_sum(arr: list[int], k: int) -> tuple[int, int]:
    """
    Логика:
    - Создаем dict, в котором будем хранить key(k - элемент листа), value(индекс листа)
    - Идем итератитивно по листу, если есть в dict ключ = элементу листа, то выводим (значение для данного ключа, индекс элемента листа)
    - высчитываем {k - элемент листа}, если ключа = {k - элемент листа} нет в dict, то кладем в dict key={k - элемент листа}, value=индекса элемента листа
    """
    residuals: dict[int, int] = dict()

    for i in range(len(arr)):
        if arr[i] in residuals:
            return residuals[arr[i]], i

        residual = k - arr[i]
        if residual not in residuals:
            residuals[residual] = i

    return (0, 0)
