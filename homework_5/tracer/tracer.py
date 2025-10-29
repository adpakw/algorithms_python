from typing import Callable

def trace_recursion(func: Callable) -> Callable:
    """Декоратор для отслеживания стека вызовов рекурсивных функций"""

    depth = 0  # для отрисовки отступов

    def wrapper(*args, **kwargs):
        nonlocal depth  # используется для изменения переменных во вложенной функции, global нельзя
        indent = "\t" * depth
        print(f"{indent}->{func.__name__}{args}")
        depth += 1

        try:
            result = func(*args, **kwargs)
            depth -= 1
            print(f"{indent}<-{func.__name__}{args} = {result}")
            return result

        except Exception as e:
            depth -= 1
            print(f"{indent}ERROR: {func.__name__}{args} raised {type(e).__name__}: {e}")
            raise

    return wrapper