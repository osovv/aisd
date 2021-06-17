def bellman_ford(vertexes, edges, source):
	n = len(vertexes)
	distance = [float("inf") for _ in range(n+1)]
	predecessor = [None for _ in range(n+1)]
	distance[source] = 0

	for i in range(n):
		for u, v, w in edges:
			if distance[u] + w < distance[v]:
				distance[v] = distance[u] + w
				predecessor[v] = u

	return distance[1:], predecessor[1:]

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

	vertexes = [1,2,3,4,5,6,7,8,9,10]
	src = 1
	distance, predecessor = bellman_ford(vertexes, edges, src)
	print(distance)
	print(predecessor)
