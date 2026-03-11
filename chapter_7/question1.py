def DFS(graph, u, visited=None):
    """
    Perform Depth-First Search of the undiscovered portion of the graph starting at Vertex u.

    Parameters:
    - graph: A Graph object with adjacency map stored in _adj_map
    - u: Vertex to start DFS from
    - visited: Dictionary to track visited vertices and their parent vertices (default None)

    Returns:
    - visited: Dictionary mapping each visited vertex to the vertex from which it was first discovered
    """
    if visited is None:
        visited = {}

    # If vertex not visited yet, mark it
    if u not in visited:
        visited[u] = None if not visited else list(visited.keys())[-1]

    # Traverse neighbors
    for neighbor in graph._adj_map.get(u, {}):
        if neighbor not in visited:
            visited[neighbor] = u  # store parent
            DFS(graph, neighbor, visited)

    return visited