import random

from utils import timer_func

ARRAY_SIZE = 100
MIN_ELEMENT = 1
MAX_ELEMENT = 100
ELEMENT_TO_FIND = 51


@timer_func
def fib_search(array: list[int], x: int) -> int:
    """* Returns index of x in array if present,  else returns -1 """
    n = len(array)
    # Initialize fibonacci numbers
    fib_m2 = 0
    fib_m1 = 1
    fib = fib_m2 + fib_m1
    # fibM is going to store the smallest Fibonacci
    # Number greater than or equal to n
    while fib < n:
        fib_m2 = fib_m1
        fib_m1 = fib
        fib = fib_m2 + fib_m1
    # 	Marks the eliminated range from front
    offset = -1
    # while there are elements to be inspected. Note that
    # we compare array[fib_m2] with x. When fib becomes 1,
    # fib_m2 becomes 0
    while fib > 1:
        # Check if fibMm2 is a valid location
        i = min(offset + fib_m2, n - 1)
        # If x is greater than the value at index fib_m2,
        # cut the subarray array from offset to i
        if array[i] < x:
            fib = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib - fib_m1
            offset = i
        # If x is greater than the value at index fib_m2,
        # cut the subarray after i+1
        elif array[i] > x:
            fib = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib - fib_m1
        # element found, return index
        else:
            return i

    # comparing the last element with x
    if fib_m1 and array[n-1] == x:
        return n-1

    # element found. return index
    return -1


if __name__ == "__main__":
    arr = random.sample(range(MIN_ELEMENT, MAX_ELEMENT + 1), ARRAY_SIZE)
    idx = fib_search(arr, ELEMENT_TO_FIND)
    if idx != -1:
        print(f"Found at index: {idx}")
    else:
        print(f"Not found!")


