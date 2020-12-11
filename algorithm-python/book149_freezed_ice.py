'''
N x M 크기의 얼음 틀이 있다. 
구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시한다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하시오.

**input
가로 x 세로 (N x M)
얼음 틀 행렬

4 5
0 0 1 1 0
0 0 0 1 1
1 1 1 1 1
0 0 0 0 0

**output
3
'''

# input
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 배열을 돌면서, 방문한 것은 1로 바꾸자
# dfs의 약간 변형된 형태임
def dfs(x, y):

    # 범위 밖일 경우
    if x <= -1 or x>=n or y<=-1 or y>=m:
        return False

    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1

        # 상,하,좌,우 방문처리
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

        return True

    return False    

numIcecream = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            numIcecream += 1


print(numIcecream)