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

@timer
def mergesort(arr: List[int | float]) -> List[int | float]:
    def merge(left: List[int | float], right: List[int | float]) -> List[int | float]:
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def split(arr: List[int | float]) -> List[int | float]:
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = split(arr[:mid])
        right = split(arr[mid:])

        return merge(left, right)

    return split(arr)

@timer
def quicksort(arr: List[int | float]) -> List[int | float]:
    def recursive_quicksort(arr: List[int | float]) -> List[int | float]:
        if len(arr) <= 1:
            return arr

        pivot = arr[0]  # можно брать первый/последний/по середине элемент
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return recursive_quicksort(left) + middle + recursive_quicksort(right)

    return recursive_quicksort(arr)
