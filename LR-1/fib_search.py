import random
from typing import List

from utils import timer_func

ARRAY_SIZE = 30_000
MIN_ELEMENT = 1
MAX_ELEMENT = 30_000
ELEMENT_TO_FIND = 25_000

fib_array = [0, 1]

def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n <= len(fib_array):
        return fib_array[n - 1]
    else:
        temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
        fib_array.append(temp_fib)
        return temp_fib

@timer_func
def fib_search(arr: List[int], key: int) -> int:
    print(arr.index(key) if key in arr else "-1")
    if key < arr[0] or key > arr[-1]:
        return -1
    offset = 0
    i = 1
    while True:
        fib = fibonacci(i)
        if fib >= len(arr):
            offset = fibonacci(i - 1) + offset
            i = 1
            continue
        if arr[offset] < key < arr[offset + 1]:
            break;
        if arr[offset + fib] < key:
            i += 1
        elif arr[offset + fib] > key:
            offset = fibonacci(i - 1) + offset
            i = 1
        else:
            return fib + offset
    return -1


if __name__ == "__main__":
    # arr = sorted(random.sample(range(MIN_ELEMENT, MAX_ELEMENT + 1), ARRAY_SIZE))
    arr = [1, 4, 9, 10, 19, 24, 31, 40, 51, 64]
    ELEMENT_TO_FIND = 24
    idx = fib_search(arr, ELEMENT_TO_FIND)
    if idx != -1:
        print(f"Found at index (fibonacci): {idx}")
    else:
        print(f"Not found!")
