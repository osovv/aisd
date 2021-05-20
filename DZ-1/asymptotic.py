from math import factorial as fact
from sys import maxsize
from numpy import log2, power, exp, exp2

funcs = {
    "1": lambda n: 1,
    "log2(log2(N))": lambda n: log2(log2(n)),
    "log2(N)": lambda n: log2(n),
    "log2(N)^2": lambda n: power(log2(n), 2),
    "log2(N)^3": lambda n: power(log2(n), 3),
    "log2(N)^4": lambda n: power(log2(n), 4),
    "N^(1/4)": lambda n: power(n, 1 / 4),
    "N^(1/3)": lambda n: power(n, 1 / 3),
    "N^(1/2)": lambda n: power(n, 1 / 2),
    "N": lambda n: n,
    "N*log2(N)": lambda n: n * log2(n),
    "N^2": lambda n: power(n, 2),
    "N^3": lambda n: power(n, 3),
    "N^4": lambda n: power(n, 4),
    "2^N": lambda n: exp2(n),
    "e^N": lambda n: exp(n),
    "3^N": lambda n: power(3, n),
    "4^N": lambda n: power(4, n),
    "N!": lambda n: fact(n),
}


def find_asymptotic(array: list[int], max_iter=1000) -> dict[int, str]:
    array = list(enumerate(array))
    result = None
    result_a = None
    min_deviation = maxsize
    max_a = 2
    for i in range(max_iter):
        min_deviation = maxsize
        for func_name, func in funcs.items():
            deviation = -1
            break_flag = False
            a = -1
            for item in array:
                n = item[0] + 1
                value = item[1]
                func_value = func(n)
                if value != 0:
                    a = max(a, func_value / value)
                if a > max_a:
                    break_flag = True
                    break
                deviation = max(deviation, abs(func_value -value))
            if not break_flag:
                min_deviation = min(deviation, min_deviation)
                if deviation == min_deviation:
                    result, result_a = func_name, a
        max_a += 1
        if min_deviation != maxsize:
            break
    return dict(a=result_a, func=result)


if __name__ == "__main__":
    array_str = input("Enter array:\n")
    array = [float(c) for c in array_str.split(',')]
    result = find_asymptotic(array)
    print(f"Result is: {round(result['a'], 2)}* {result['func']}")
    # 1.15, 2.3, 3.45, 3.4, 5.0, 5.1, 5.95, 8.0, 9.0, 8.5