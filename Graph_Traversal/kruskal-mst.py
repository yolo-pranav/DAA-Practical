from Graph import Graph
from Graph import print_mst

def kruskal_mst(graph: Graph):
    min_spanning_tree = []
    edges = []

    # Create a list of edges with their weights
    for vertex in range(graph.num_vertices):
        for neighbor, weight in graph.adjacency_list[vertex]:
            edges.append((vertex, neighbor, weight))

    # Sort the edges by weight in ascending order
    edges.sort(key=lambda x: x[2])

    parent = [i for i in range(graph.num_vertices)]

    def find_set(v):
        if v == parent[v]:
            return v
        parent[v] = find_set(parent[v])
        return parent[v]

    for edge in edges:
        start, end, weight = edge
        if find_set(start) != find_set(end):
            min_spanning_tree.append((end, weight))

    return min_spanning_tree

if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 6)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 9)

    mst = kruskal_mst(g)
    print("Minimum Spanning Tree (MST):")
    print_mst(mst)
