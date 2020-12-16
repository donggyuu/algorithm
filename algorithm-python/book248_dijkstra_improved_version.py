'''
방문 안한 노드 중 가장 최단 거리가 짧은 노드의 번호를 큐에 저장하여 사용한다.
("book237_dijkstra_simple_version.py"에서는 순회하면서 짧은 노드를 일일이 확인함)

**heapq에 대한 설명
https://hellominchan.tistory.com/231
// 큐이긴 한데 최소힙으로 구현된 큐
'''

import heapq # 최소힙
import sys
input = sys.stdin.readline
INF = int(1e9) # 10억

# 노드&간선 개수 입력
n, m = map(int, input().split())
# 시작 노드 번호 입력
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보 List
graph = [[] for _ in range(n+1)]
# 최단 거리 테이블을 무한으로 초기화
distance = [INF] * (n+1)


# 모든 간선 정보 입력
for i in range(m):
    a, b, c = map(int, input().split())
    # a에서 b로 가는 비용이 c
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정
    heapq.heappush(q, (0, start)) # q에 집어넣는다, start까지의 거리는 0이다.
    distance[start] = 0

    while q: # 큐가 비어있지 않을때까지 실행

        # 거리가 가장 짧은 노드 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있다면 무시(이미 짧은 거리로 처리되어 있는 경우)
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 인접 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
