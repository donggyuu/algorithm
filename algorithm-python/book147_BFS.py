# BFS는 큐를 이용
# 방문한 노드의 인접 노트를 큐에 넣고 순차 방문 처리

# queue를 써도 된다
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start]) # start의 vertex를 큐에 집어 넣는다.

    # 현재 노드를 방문처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue: #empty queue이면 false
        v = queue.popleft()
        print(v, end=' ')

        # v와 연결된, 아직 방문 안한 원소를 큐에 삽입함
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
bfs(graph, 1, visited)
