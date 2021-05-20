import random

from utils import timer_func

ARRAY_SIZE = 30_000
MIN_ELEMENT = 1
MAX_ELEMENT = 30_000


@timer_func
def shell_sort(array: list[int]) -> list[int]:
    n = len(array)
    step = n // 2
    while step > 0:
        for i in range(step, n):
            j = i
            delta = j - step
            while delta >= 0 and array[delta] > array[j]:
                array[delta], array[j] = array[j], array[delta]
                j = delta
                delta = j - step
        step //= 2
    return array


if __name__ == "__main__":
    arr = random.sample(range(MIN_ELEMENT, MAX_ELEMENT + 1), ARRAY_SIZE)
    # print("Before sort", arr)
    sorted_arr = shell_sort(arr)
    # print("After sort", arr)
    assert sorted_arr == sorted(arr)
