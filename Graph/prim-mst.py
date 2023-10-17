from Graph.Graph import Graph
import heapq

def prim_mst(graph: Graph):
    min_spanning_tree = []
    visited = [False] * graph.num_vertices
    min_heap = [(0, 0)]

    while min_heap:
        weight, vertex = heapq.heappop(min_heap)

        if visited[vertex]:
            continue

        visited[vertex] = True
        if weight > 0:
            min_spanning_tree.append((vertex, weight))

        for neighbor, edge_weight in graph.adjacency_list[vertex]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (edge_weight, neighbor))

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
