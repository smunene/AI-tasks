# Breadth first search
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs_path(graph, start, goal):
    queue = [[start]]
    visited = {start}
    pointer = 0 
    while pointer < len(queue):
        path = queue[pointer]
        pointer += 1
        
        current_node = path[-1]
        
        if current_node == goal:
            return path
            
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path) + [neighbor]
                queue.append(new_path)
                
    return None

start = 'A'
goal = 'F'
print("BFS Path:", " -> ".join(bfs_path(graph, start, goal)))
