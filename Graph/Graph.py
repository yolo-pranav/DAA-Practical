class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
        self.adjacency_list = {i: [] for i in range(num_vertices)}

    def add_edge(self, start, end, weight):
        self.adjacency_matrix[start][end] = weight
        self.adjacency_list[start].append((end, weight))

    def get_adjacency_matrix(self):
        return self.adjacency_matrix

    def get_adjacency_list(self):
        return self.adjacency_list