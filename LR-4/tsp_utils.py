from random import randint

def generate_matrix(n, zeros_number=0):
    a = [[0 for j in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            a[i][j] = randint(1, 100)
    for i in range(n):
        a[i][i] = 0
    c = 0
    while c != zeros_number:
        i = randint(0, n-1)
        j = randint(0, n-1)
        if i == j:
            continue
        a[i][j] = 0
        c += 1
    return a

def print_matrix(a):
    for i in range(len(a)):
        print(a[i])
