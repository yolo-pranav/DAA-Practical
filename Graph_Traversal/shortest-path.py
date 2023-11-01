from Graph import Graph
import heapq

def shortest_path(graph: Graph, start, end):
    num_vertices = graph.num_vertices
    visited = [False] * num_vertices
    distance = [float('inf')] * num_vertices
    parent = [-1] * num_vertices

    distance[start] = 0

    for _ in range(num_vertices):
        u = min_distance_vertex(graph, visited, distance)
        visited[u] = True

        for v, weight in graph.get_adjacency_list()[u]:
            if not visited[v] and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u

    return construct_path(start, end, parent), distance[end]

def min_distance_vertex(graph: Graph, visited, distance):
    min_dist = float('inf')
    min_vertex = -1

    for v in range(graph.num_vertices):
        if not visited[v] and distance[v] < min_dist:
            min_dist = distance[v]
            min_vertex = v

    return min_vertex

def construct_path(start, end, parent):
    path = []
    while end != -1:
        path.insert(0, end)
        end = parent[end]
    return path

if __name__ == "__main__":
    num_vertices = 5
    g = Graph(num_vertices)
    
    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 6)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 9)

    start_node = 0
    end_node = 4

    path, min_cost = shortest_path(g, start_node, end_node)

    if path:
        print(f"Shortest Path from {start_node} to {end_node}: {path}")
        print(f"Shortest Distance: {min_cost}")
    else:
        print(f"No path found from {start_node} to {end_node}")
