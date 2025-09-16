def is_palindrome(number: int) -> bool:
    if number < 0:
        return False
    cur = 0
    buff = number
    while buff != 0:
        digit = buff % 10
        cur = cur * 10 + digit
        buff //= 10
    return cur == number
