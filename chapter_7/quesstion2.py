def BFS(graph, start):
    """
    Perform Breadth-First Search of the graph starting from Vertex start.

    Parameters:
    - graph: Graph object with adjacency map stored in _adj_map
    - start: Vertex to start BFS from

    Returns:
    - visited: Dictionary mapping each vertex to the vertex from which it was first discovered
    """
    visited = {start: None}   # Mark start vertex as visited with no parent
    queue = [start]           # Initialize queue with start vertex

    while queue:
        u = queue.pop(0)  # Dequeue the first vertex
        for neighbor in graph._adj_map.get(u, {}):  # Iterate neighbors from _adj_map
            if neighbor not in visited:
                visited[neighbor] = u  # Record the parent vertex
                queue.append(neighbor) # Enqueue for future exploration

    return visited