def print_distances(dist, V):
    print("\nVertex\t Distance")
    for i in range(V):
        if dist[i] != float("inf"):
            print(i+1, "\t", int(dist[i]), end="\t")
        else:
            print(i+1, "\t", "INF", end="\t")
        print()


def min_distance(mdist, visited, V):
    min_value = float("inf")
    min_idx = -1
    for i in range(V):
        if i not in visited and mdist[i] < min_value:
            min_idx = i
            min_value = mdist[i]
    return min_idx


def dijkstra(graph, V, src):
    min_distances = [float("inf") for i in range(V)]
    visited = set()
    min_distances[src] = 0.0

    for i in range(V - 1):
        u = min_distance(min_distances, visited, V)
        visited.add(u)

        for v in range(V):
            if (
                v not in visited
                and graph[u][v] != float("inf")
                and min_distances[u] + graph[u][v] < min_distances[v]
            ):
                min_distances[v] = min_distances[u] + graph[u][v]

    print_distances(min_distances, V)


if __name__ == "__main__":
	vertex_count = 10
	g = [[float("inf") for i in range(vertex_count)] for j in range(vertex_count)]
	for i in range(vertex_count):
		g[i][i] = 0
	edges = [
		(1, 4, 8),
		(1, 8, 7),
		(2, 6, 9),
		(3, 6 ,4),
		(3, 9, 6),
		(3, 10, 3),
		(4, 1, 8),
		(4, 7, 4),
		(4, 10, 8),
		(5, 6, 8),
		(5, 7, 5),
		(5, 8, 7),
		(5, 9, 5),
		(5, 10, 3),
		(6, 2, 9),
		(6, 3, 4),
		(6, 5, 8),
		(6, 7, 8),
		(6, 8, 2),
		(6, 9, 3),
		(7, 4, 4),
		(7, 5, 5),
		(7, 6, 8),
		(7, 8, 7),
		(7, 9, 5),
		(7, 10, 8),
		(8, 1, 7),
		(8, 5, 7),
		(8, 6, 2),
		(8, 7, 7),
		(9, 3, 6),
		(9, 5, 5),
		(9, 6, 3),
		(9, 7, 5),
		(9, 10, 1),
		(10, 3, 3),
		(10, 4, 8),
		(10, 5, 3),
		(10, 7, 8),
		(10, 9, 1)
	]
	for u, v, w in edges:
		g[u-1][v-1] = w

	from_ = 1
	dijkstra(g, vertex_count, from_ - 1)
