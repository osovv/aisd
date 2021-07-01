# from https://codereview.stackexchange.com/questions/81865/travelling-salesman-using-brute-force-and-heuristics

import doctest
from itertools import permutations

def length(adj_mat, tour):
    return sum([adj_mat[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)])

def tsp_brute_force(matrix):
    matr = matrix[:]
    n = len(matr)
    min_length = float('inf')
    path = []
    vertexes = list(range(0, n))
    perms = list(permutations(vertexes))
    for i in range(len(perms)):
        perms[i] = list(perms[i])
        perms[i].append(perms[i][0])

    for p in perms:
        length_ = length(matrix, p)
        if length_ < min_length:
            min_length = length_
            path = p.copy()

    return path, min_length
