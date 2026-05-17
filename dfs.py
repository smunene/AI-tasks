# Depth first search

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
def dfs_path(graph, start, goal):
    stack = [[start]]
    visited = set()
    
    while stack:
        path = stack.pop()
        current_node = path[-1]
        
        if current_node == goal:
            return path
            
        if current_node not in visited:
            visited.add(current_node)
            
            for neighbor in reversed(graph[current_node]):
                if neighbor not in visited:
                    new_path = list(path) + [neighbor]
                    stack.append(new_path)
    return None

start = 'A'
goal = 'F'
print("DFS Path:", " -> ".join(dfs_path(graph, start, goal)))
