from collections import deque

def DFS(graph, start, visited=set()):
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            DFS(graph, neighbor, visited)

    return visited

def BFS(graph, start, visited={}):
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        visited.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)

    return visited