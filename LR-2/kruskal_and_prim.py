class Graph:
    def __init__(self, vertex_number):
        self.vertex_number = vertex_number
        self.edges = []
        self.vertexes = []
        for i in range(vertex_number):
            self.vertexes.append([i])
        self.matrix = [[0 for i in range(vertex_number)] for j in range(vertex_number)]

    def add_edge(self, u, v, w):
        if v < u:
            u, v = v, u
        self.edges.append((u - 1, v - 1, w))
        self.matrix[u - 1][v - 1] = w
        self.matrix[v - 1][u - 1] = w

    def len_of_comp(self, u):
        for i in range(len(self.vertexes)):
            if u in self.vertexes[i]:
                return len(self.vertexes[i]), i
        return 0, -1

    def kruskal(self):
        print('\t\tKRUSKAL')
        used_vertexes = set()
        used_edges = set()
        ostov_size = 0
        ostov_weight = 0
        components = self.vertexes.copy()
        sorted_edges = sorted(self.edges, key=lambda x: x[2])
        for edge in sorted_edges:
            u, v, w = edge
            u_len, u_i = self.len_of_comp(u)
            v_len, v_i = self.len_of_comp(v)
            if u_i != v_i:
                used_vertexes.add(u), used_vertexes.add(v)
                if u_len > v_len:
                    components[u_i] += components[v_i]
                    components[v_i].clear()
                else:
                    components[v_i] += components[u_i]
                    components[u_i].clear()
                used_edges.add(edge)
                ostov_weight += w
                ostov_size += 1
        print(f"Ostov weight: {ostov_weight}")
        for edge in sorted_edges:
            out_str = f"{edge[0] + 1} - {edge[1] + 1} : {edge[2]}"
            if edge in used_edges:
                print("OSTOV {} OSTOV".format(out_str))
            else:
                print(out_str)
        print("Components:", [comp for comp in components])

    def min_dist(self, node, used):
        mini = -1
        for v in range(self.vertex_number):
            if self.matrix[node][v] < mini and v not in used:
                mini = self.matrix[node][v]
                min_index = v
        return mini, min_index

    def find_distances(self, new, distances):
        for v in range(self.vertex_number):
            if self.matrix[new][v] < distances[v] and self.matrix[new][v] != 0 and distances[v] != -1:
                distances[v] = self.matrix[new][v]
        return distances

    def min_v(self, distances):
        minv = float('inf')
        for x in distances:
            if x != -1 and x < minv:
                minv = x
        return minv

    def prim(self):
        print('\t\tPRIM')
        ostov_weight = 0
        ostov_size = 1
        used_vertexes = list([0])
        distances = [float('inf') for i in range(self.vertex_number)]
        distances[0] = -1
        used_edges = []
        v = 0
        while ostov_size < self.vertex_number:
            distances = self.find_distances(v, distances)
            min_w = self.min_v(distances)
            if min_w != float('inf'):
                vv = v
                v = distances.index(min_w)
                distances[v] = -1
                used_edges.append([vv, v])
                used_vertexes.append(v)
                ostov_weight += min_w
            ostov_size += 1
        for i in range(len(used_vertexes)):
            used_vertexes[i] += 1
        print('Ostov weight:', ostov_weight)
        print('Used vertexes:', used_vertexes)


if __name__ == '__main__':
    graph = Graph(8)
    graph.add_edge(1, 2, 6)
    graph.add_edge(2, 3, 12)
    graph.add_edge(3, 8, 1)
    graph.add_edge(8, 7, 2)
    graph.add_edge(7, 6, 5)
    graph.add_edge(6, 1, 10)
    graph.add_edge(1, 4, 1)
    graph.add_edge(2, 4, 1)
    graph.add_edge(6, 4, 1)
    graph.add_edge(7, 4, 7)
    graph.add_edge(7, 5, 5)
    graph.add_edge(8, 5, 8)
    graph.add_edge(3, 5, 1)
    graph.add_edge(2, 5, 1)
    graph.add_edge(4, 5, 4)
    graph.kruskal()
    graph.prim()
