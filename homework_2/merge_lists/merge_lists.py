def find_max_sum_div_2_v3(array: str) -> int:
    arr = list(map(int, array.split()))

    odd_min = float("inf")
    for i in range(len(arr)):
        if arr[i] % 2 and arr[i] < odd_min:
            odd_min = arr[i]

    max_sum = sum(arr)
    if max_sum % 2 == 0:
        return max_sum
    else:
        return int(max_sum - odd_min)
