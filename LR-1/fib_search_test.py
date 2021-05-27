import pytest
import random

from fib_search import fib_search

MAX_ELEMENT = 500
ARRAY_SIZE = 100

@pytest.fixture
def array():
    return sorted(random.sample(range(1, MAX_ELEMENT), ARRAY_SIZE))

@pytest.fixture
def index():
    return random.randint(0, ARRAY_SIZE - 1)

@pytest.mark.repeat(100)
def test_present(array, index):
    element_to_find = array[index]
    assert index == fib_search(array, element_to_find)


def test_negative(array):
    element = -1
    assert -1 == fib_search(array, element)

