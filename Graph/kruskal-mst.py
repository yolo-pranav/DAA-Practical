from Graph.Graph import Graph
import heapq

def prim_mst(graph: Graph):
    min_spanning_tree = []

    return min_spanning_tree

def print_mst(mst):
    total_weight = 0
    for vertex, weight in mst:
        total_weight += weight
        print(f"Edge: 0 - {vertex}, Weight: {weight}")

    print(f"Total Weight of MST: {total_weight}")

if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 6)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 9)

    mst = prim_mst(g)
    print("Minimum Spanning Tree (MST):")
    print_mst(mst)
