from random import randint

import pytest
from asymptotic import find_asymptotic as fa
from asymptotic import funcs

input_N = range(1, 11)


class TestDefault:
    def test_for_1(self):
        array = list(map(funcs["1"], input_N))
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "1"

    def test_for_log2log2N(self):
        array = list(map(funcs["log2(log2(N))"], input_N))
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "log2(log2(N))"

    def test_for_log2N(self):
        array = list(map(funcs["log2(N)"], input_N))
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "log2(N)"

    def test_for_log2N2(self):
        array = list(map(funcs["log2(N)^2"], input_N))
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "log2(N)^2"

    def test_for_log2N3(self):
        array = list(map(funcs["log2(N)^3"], input_N))
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "log2(N)^3"

    def test_for_log2N3(self):
        array = list(map(funcs["log2(N)^3"], input_N))
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "log2(N)^3"

    def test_for_N1o4(self):
        array = list(map(funcs["N^(1/4)"], input_N))
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "N^(1/4)"

    def test_for_N1o3(self):
        array = list(map(funcs["N^(1/3)"], input_N))
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "N^(1/3)"

    def test_for_N1o2(self):
        array = list(map(funcs["N^(1/2)"], input_N))
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "N^(1/2)"

    def test_for_N(self):
        array = list(map(funcs["N"], input_N))
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "N"

    def test_for_Nlog2N(self):
        array = list(map(funcs["N*log2(N)"], input_N))
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "N*log2(N)"

    def test_for_N2(self):
        array = list(map(funcs["N^2"], input_N))
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "N^2"

    def test_for_N3(self):
        array = list(map(funcs["N^3"], input_N))
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "N^3"

    def test_for_N4(self):
        array = list(map(funcs["N^4"], input_N))
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "N^4"

    def test_for_2N(self):
        array = list(map(funcs["2^N"], input_N))
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "2^N"

    def test_for_eN(self):
        array = list(map(funcs["e^N"], input_N))
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "e^N"

    def test_for_3N(self):
        array = list(map(funcs["3^N"], input_N))
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "3^N"

    def test_for_4N(self):
        array = list(map(funcs["4^N"], input_N))
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "4^N"

    def test_for_Nfact(self):
        array = list(map(funcs["N!"], input_N))
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "N!"


percents = [1, 5, 10, 15]


@pytest.mark.parametrize("percent", percents)
class TestDefaultPercentChanged:
    def test_for_1(self, percent):
        array = list(map(funcs["1"], input_N))
        for i in range(len(array)):
            array[i] += (randint(1, 3) - 2) * array[i] * percent / 100
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "1"

    def test_for_log2log2N(self, percent):
        array = list(map(funcs["log2(log2(N))"], input_N))
        for i in range(len(array)):
            array[i] += (randint(1, 3) - 2) * array[i] * percent / 100
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "log2(log2(N))"

    def test_for_log2N(self, percent):
        array = list(map(funcs["log2(N)"], input_N))
        for i in range(len(array)):
            array[i] += (randint(1, 3) - 2) * array[i] * percent / 100
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "log2(N)"

    def test_for_log2N2(self, percent):
        array = list(map(funcs["log2(N)^2"], input_N))
        for i in range(len(array)):
            array[i] += (randint(1, 3) - 2) * array[i] * percent / 100
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "log2(N)^2"

    def test_for_log2N3(self, percent):
        array = list(map(funcs["log2(N)^3"], input_N))
        for i in range(len(array)):
            array[i] += (randint(1, 3) - 2) * array[i] * percent / 100
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "log2(N)^3"

    def test_for_log2N4(self, percent):
        array = list(map(funcs["log2(N)^4"], input_N))
        for i in range(len(array)):
            array[i] += (randint(1, 3) - 2) * array[i] * percent / 100
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "log2(N)^4"

    def test_for_N1o4(self, percent):
        array = list(map(funcs["N^(1/4)"], input_N))
        for i in range(len(array)):
            array[i] += (randint(1, 3) - 2) * array[i] * percent / 100
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "N^(1/4)"

    def test_for_N1o3(self, percent):
        array = list(map(funcs["N^(1/3)"], input_N))
        for i in range(len(array)):
            array[i] += (randint(1, 3) - 2) * array[i] * percent / 100
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "N^(1/3)"

    def test_for_N1o2(self, percent):
        array = list(map(funcs["N^(1/2)"], input_N))
        for i in range(len(array)):
            array[i] += (randint(1, 3) - 2) * array[i] * percent / 100
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "N^(1/2)"

    def test_for_N(self, percent):
        array = list(map(funcs["N"], input_N))
        for i in range(len(array)):
            array[i] += (randint(1, 3) - 2) * array[i] * percent / 100
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "N"

    def test_for_Nlog2N(self, percent):
        array = list(map(funcs["N*log2(N)"], input_N))
        for i in range(len(array)):
            array[i] += (randint(1, 3) - 2) * array[i] * percent / 100
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "N*log2(N)"

    def test_for_N2(self, percent):
        array = list(map(funcs["N^2"], input_N))
        for i in range(len(array)):
            array[i] += (randint(1, 3) - 2) * array[i] * percent / 100
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "N^2"

    def test_for_N3(self, percent):
        array = list(map(funcs["N^3"], input_N))
        for i in range(len(array)):
            array[i] += (randint(1, 3) - 2) * array[i] * percent / 100
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "N^3"

    def test_for_N4(self, percent):
        array = list(map(funcs["N^4"], input_N))
        for i in range(len(array)):
            array[i] += (randint(1, 3) - 2) * array[i] * percent / 100
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "N^4"

    def test_for_2N(self, percent):
        array = list(map(funcs["2^N"], input_N))
        for i in range(len(array)):
            array[i] += (randint(1, 3) - 2) * array[i] * percent / 100
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "2^N"

    def test_for_eN(self, percent):
        array = list(map(funcs["e^N"], input_N))
        for i in range(len(array)):
            array[i] += (randint(1, 3) - 2) * array[i] * percent / 100
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "e^N"

    def test_for_3N(self, percent):
        array = list(map(funcs["3^N"], input_N))
        for i in range(len(array)):
            array[i] += (randint(1, 3) - 2) * array[i] * percent / 100
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "3^N"

    def test_for_4N(self, percent):
        array = list(map(funcs["4^N"], input_N))
        for i in range(len(array)):
            array[i] += (randint(1, 3) - 2) * array[i] * percent / 100
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "4^N"

    def test_for_Nfact(self, percent):
        array = list(map(funcs["N!"], input_N))
        for i in range(len(array)):
            array[i] += (randint(1, 3) - 2) * array[i] * percent / 100
        print()
        print(array)
        res = fa(array)
        assert res['func'] == "N!"

class TestCustom:
    def test_seminar(self):
        array = [0, 0, 1,  5, 10, 22, 25, 50, 99]
        res = fa(array)
        assert res['func'] == "2^N"

    def test_N2(self):
        array = [2, 5, 10, 17, 26, 37]
        res = fa(array)
        assert res['func'] == 'N^2'
