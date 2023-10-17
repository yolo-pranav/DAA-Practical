from Graph.Graph import Graph
import heapq

def dijkstra(graph: Graph, start, end):
    min_distance = {vertex: float('infinity') for vertex in range(graph.num_vertices)}
    min_distance[start] = 0
    previous_nodes = {}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > min_distance[current_vertex]:
            continue

        for neighbor, weight in graph.get_adjacency_list()[current_vertex]:
            distance = current_distance + weight

            if distance < min_distance[neighbor]:
                min_distance[neighbor] = distance
                previous_nodes[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    path, current_vertex = [], end
    while current_vertex is not None:
        path.insert(0, current_vertex)
        current_vertex = previous_nodes.get(current_vertex)

    return path, min_distance[end]

def main():
    num_vertices = 5
    graph = Graph(num_vertices)
    
    # Add edges to the graph
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 2)
    graph.add_edge(1, 2, 5)
    graph.add_edge(1, 3, 10)
    graph.add_edge(2, 3, 3)
    graph.add_edge(3, 4, 7)
    graph.add_edge(2, 4, 2)

    start = 0
    end = 3

    path, min_cost = dijkstra(graph, start, end)

    print(f"Minimum cost path from {start} to {end} is: {path} with cost {min_cost}")

main()