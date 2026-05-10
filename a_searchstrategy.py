import heapq

def a_star(graph, heuristics, start, goal):
    pq = [(heuristics[start], start, [start], 0)]
    visited = {}

    while pq:
        f, current, path, g = heapq.heappop(pq)

        if current == goal:
            return path, g

        if visited.get(current, float('inf')) <= g:
            continue
        
        visited[current] = g

        for neighbor, weight in graph.get(current, {}).items():
            new_g = g + weight
            heapq.heappush(pq, (new_g + heuristics.get(neighbor, 0), neighbor, path + [neighbor], new_g))

    return None, float('inf')

# Example setup
road_graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2},
    'C': {'F': 3},
    'D': {'G': 1},
    'F': {'G': 2},
    'G': {}
}

h_values = {'A': 7, 'B': 6, 'C': 2, 'D': 1, 'F': 1, 'G': 0}

path, cost = a_star(road_graph, h_values, 'A', 'G')
print(f"Path: {path}, Cost: {cost}")