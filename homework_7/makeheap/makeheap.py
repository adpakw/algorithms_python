import time
from typing import Any, Callable, List, Union


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
def makeheap_n_log_n(arr: List[Union[int, float]]) -> List[Union[int, float]]:
    def sift_up(heap: List[Union[int, float]], index: int) -> None:
        parent_index = (index - 1) // 2

        if index > 0 and heap[parent_index] > heap[index]:
            heap[parent_index], heap[index] = heap[index], heap[parent_index]
            index = parent_index

            sift_up(heap, parent_index)

    heap = arr.copy()
    for i in range(len(heap) - 1, 1, -1):
        sift_up(heap, i)

    return heap


@timer
def makeheap(arr: List[Union[int, float]]) -> List[Union[int, float]]:
    def sift_down(heap: List[Union[int, float]], index: int) -> None:
        if len(heap) <= 1:
            return

        left_idx = 2 * index + 1
        right_idx = 2 * index + 2
        smallest_idx = index

        if left_idx < len(heap) and heap[left_idx] < heap[smallest_idx]:
            smallest_idx = left_idx

        if right_idx < len(heap) and heap[right_idx] < heap[smallest_idx]:
            smallest_idx = right_idx

        if smallest_idx != index:
            heap[smallest_idx], heap[index] = heap[index], heap[smallest_idx]
            sift_down(heap, smallest_idx)

    heap = arr.copy()
    for i in range(len(heap) // 2 - 1, -1, -1):
        sift_down(heap, i)

    return heap
