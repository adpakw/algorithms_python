from typing import List


def quick_select(arr: List[int | float], k: int) -> int | float:
    pivot = arr[0]

    leftArr = [x for x in arr if x > pivot]

    midArr = [x for x in arr if x == pivot]

    rightArr = [x for x in arr if x < pivot]

    if k <= len(leftArr):
        return quick_select(leftArr, k)
    if len(leftArr) + len(midArr) < k:
        return quick_select(rightArr, k - len(leftArr) - len(midArr))

    return pivot
