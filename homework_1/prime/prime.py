def count_primes_v2(number: int) -> int:
    """Реализация через решето Эратосфена"""
    if number <= 2:
        return 0
    sieve = [True] * number  # Сначала помечаю все числа как простые(True),
    sieve[0] = False  # 0 не является простым числом
    sieve[1] = False  # 1 не является простым числом

    for iter_el in range(2, number):
        if sieve[iter_el]:
            for composite_number in range(iter_el + iter_el, number, iter_el):
                sieve[composite_number] = False

    return sum(sieve)
