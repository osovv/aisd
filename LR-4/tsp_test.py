import pytest
import random

from tsp import tsp
from tsp_brute_force import tsp_brute_force
from tsp_utils import generate_matrix

N = 5

@pytest.fixture
def matrix():
    return generate_matrix(N, zeros_number=3)

@pytest.mark.repeat(100)
def test_present(matrix):
    mine = tsp(matrix)
    brute_force = tsp_brute_force(matrix)
    assert mine[1] == brute_force[1]


