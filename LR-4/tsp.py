from queue import PriorityQueue

class Node:
    def __init__(self, level=None, path=None, bound=None):
        self.level = level
        self.path = path
        self.bound = bound

    def __lt__(self, other):
        return self.bound < other.bound

    def __eq__(self, other):
        return self.bound == other.bound

    def __gt__(self, other):
        return self.bound > other.bound

    def __str__(self):
        return str(tuple([self.level, self.path, self.bound]))


def  tsp(adj_mat, src=0):
    optimal_tour = []
    n = len(adj_mat)
    u = Node()
    pq = PriorityQueue()
    optimal_length = 0
    v = Node(level=1, path=[0])
    min_length = float('inf')
    v.bound = bound(adj_mat, v)
    pq.put(v)
    while not pq.empty():
        v = pq.get()
        if v.bound < min_length:
            u.level = v.level + 1
            for i in filter(lambda x: x not in v.path, range(1, n)):
                u.path = v.path[:]
                u.path.append(i)
                if u.level == n - 1:
                    remaining_vertex = set(range(1, n)) - set(u.path)
                    print(f'{u.path=}')
                    print(f'{remaining_vertex=}')
                    u.path.append(list(remaining_vertex)[0])
                    u.path.append(0)
                    print(f'{u.path=}')
                    _len = length(adj_mat, u)
                    if _len < min_length:
                        min_length = _len
                        optimal_length = min_length
                        optimal_tour = u.path[:]
                else:
                    u.bound = bound(adj_mat, u)
                    if u.bound < min_length:
                        pq.put(u)
                u = Node(level=u.level)

    return optimal_tour, optimal_length


def length(adj_mat, node):
    tour = node.path
    return sum([adj_mat[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)])


def bound(adj_mat, node):
    path = node.path
    _bound = 0

    n = len(adj_mat)
    determined, last = path[:-1], path[-1]
    remain = list(filter(lambda x: x not in path, range(n)))
    # print(f"{remain=}")

    for i in range(len(path) - 1):
        _bound += adj_mat[path[i]][path[i + 1]]

    _bound += min([adj_mat[last][i] for i in remain])

    p = [path[0]] + remain
    # print(f"{remain=}")
    # print(f"{p=}")
    for r in remain:
        _bound += min([adj_mat[r][i] for i in filter(lambda x: x != r, p)])
    return _bound



if __name__ == '__main__':
	task_1 = [
	    [0, 7, 12, 25, 10],
	    [10, 0, 9, 5, 11],
	    [13, 8, 0, 6, 4],
	    [6, 11, 15, 0, 15],
	    [5, 9, 12, 17, 0]
	]
	print(tsp(task_1))
	task_2 = [
	    [0, 7, 12, 25, 10, 11],
	    [10, 0, 9, 5, 0, 23],
	    [13, 8, 0, 6, 0, 16],
	    [6, 11, 15, 0, 15, 21],
	    [5, 9, 12, 17, 0, 4],
        [1, 0, 5, 9, 12, 0]
	]
	print(tsp(task_2))

