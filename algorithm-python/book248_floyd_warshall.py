'''
방문 안한 노드 중 가장 최단 거리가 짧은 노드의 번호를 큐에 저장하여 사용한다.
("book237_dijkstra_simple_version.py"에서는 순회하면서 짧은 노드를 일일이 확인함)

**heapq에 대한 설명
https://hellominchan.tistory.com/231
// 큐이긴 한데 최소힙으로 구현된 큐
'''

'''
아래 블로그가 가장 쉬운 설명
https://chanhuiseok.github.io/posts/algo-50/
'''

INF = int(1e9) # 무한

n = int(input()) # 노드 개수
m = int(input()) # 간선 개수

# 최단거리 저장을 위한 2차원 배열(python이니까 list)
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기자신 -> 자기자신 은 비용을 0으로 세팅
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# a에서 b로 가는 비용c 를 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            # 플로이드 워셜 수행
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INF", end=" ")
        else:
            print(graph[a][b], end=" ")
    print() # 개행
