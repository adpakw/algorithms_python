import time
from typing import Any, Callable, List


def timer(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.perf_counter()  # можно через time.process_time()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()  # можно через time.process_time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.4f} secs")
        return result

    return wrapper


def merge(arr: List[int | float], left: int, mid: int, right: int):
    # Вычисляем размеры двух подмассивов для слияния
    n1 = mid - left + 1
    n2 = right - mid

    arr1 = arr[left : left + n1]
    arr2 = arr[mid + 1 : mid + 1 + n2]

    i = 0  # индекс для левого подмассива (arr1)
    j = 0  # индекс для правого подмассива (arr2)
    k = left  # индекс для основного массива (arr)

    # Сливаем временные списки обратно в основной массив
    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = arr1[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = arr2[j]
        j += 1
        k += 1


@timer
def mergesort_iter(arr: List[int | float]) -> List[int | float]:
    arr = arr.copy()
    n = len(arr)

    currSize = 1
    while currSize <= n - 1:
        # Выбираем начальные точки различных подмассивов текущего размера
        leftStart = 0
        while leftStart < n - 1:
            mid = min(leftStart + currSize - 1, n - 1)
            rightEnd = min(leftStart + 2 * currSize - 1, n - 1)

            merge(arr, leftStart, mid, rightEnd)

            leftStart += 2 * currSize

        currSize = 2 * currSize

    return arr


def partition(arr: List[int | float], low, high):
    """
    Функция разделения массива относительно опорного элемента.
    Размещает элементы меньше опорного слева, больше - справа.

    Args:
        arr: массив для сортировки
        low: начальный индекс (low)
        high: конечный индекс (high)

    Returns:
        индекс опорного элемента после разделения
    """
    i = low - 1  # индекс меньшего элемента (изначально -1)
    x = arr[high]  # опорный элемент (pivot) - выбираем последний элемент

    for j in range(low, high):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    # Помещаем опорный элемент на правильную позицию
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # возвращаем индекс опорного элемента


@timer
def quicksort_iter(arr: List[int | float]) -> List[int | float]:
    """
    Итеративная реализация быстрой сортировки с использованием стека.
    Эмулирует рекурсию с помощью явного стека.

    Args:
        arr: массив для сортировки
    """
    arr = arr.copy()
    low = 0
    high = len(arr) - 1

    # Создаем вспомогательный стек для хранения границ подмассивов
    stack = [0] * (len(arr))  # стек для хранения границ [low, high]

    # Инициализируем вершину стека
    top = -1

    # Помещаем начальные значения low и high в стек
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high

    # Продолжаем извлекать из стека, пока он не пуст
    while top >= 0:
        # Извлекаем high и low из стека (в обратном порядке)
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1

        p = partition(arr, low, high)

        # Если есть элементы слева от опорного,
        # то помещаем левую часть в стек
        if p - 1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1

        # Если есть элементы справа от опорного,
        # то помещаем правую часть в стек
        if p + 1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high
    return arr
