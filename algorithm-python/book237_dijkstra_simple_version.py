# simple dijkstra
import sys

'''
setup
'''
# 노드 개수, 간선
input = sys.stdin.readline
n, m = map(int, input().split())
# 시작 노드 입력
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for _ in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트
visited = [False] * (n+1)
# 최단거리 테이블을 무한으로 초기화
INF = int(1e9) # 10억
distance = [INF] * (n+1)


'''
func
'''
# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b,c))


# 방문 안한 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    
    return index

def dijkjstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True
    # 시작노드의 비용 초기화
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 실행 
dijkjstra(start)

for i in range(1, n+1):
    # 도달할 수 없는 경우 "무한"을 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달 가능하면 거리를 출력
    else:
        print(distance[i])
