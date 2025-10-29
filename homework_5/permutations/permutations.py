from typing import Any, Callable, List


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
            print(
                f"{indent}ERROR: {func.__name__}{args} raised {type(e).__name__}: {e}"
            )
            raise

    return wrapper


@trace_recursion
def permute(nums: List[Any]) -> List[List[Any]]:
    @trace_recursion
    def backtrack(index: Any, perm_list: List[Any]):
        if index == len(perm_list):
            result.append(perm_list[:])
            return

        for i in range(index, len(perm_list)):
            perm_list[index], perm_list[i] = (
                perm_list[i],
                perm_list[index],
            )  # меняем местами элементы
            backtrack(index + 1, perm_list)
            perm_list[index], perm_list[i] = (
                perm_list[i],
                perm_list[index],
            )  # возвращаем массив в исходное состояние

    result: List[Any] = []
    backtrack(0, nums)
    return result
