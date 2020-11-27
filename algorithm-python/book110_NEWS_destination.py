'''
NxN의 격자판이 있다.
여행가는 (0,0)에서 출발하여 아래와같이 움직인다.
L: 왼쪽으로 +1
R: 오른쪽으로 +1
U: 위로 +1
D: 아래로 +1

여행가가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램을 구하시오

**input
5
R R R U D D

**output
3 4
'''
# chp2_peak_area.py 문제와 비슷

nLRUDs = int(input())
inLRUDs = input().split()

# LRUD 순서(dx:행, dy:열)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
LRUD = ['L', 'R', 'U', 'D']

# 시작 좌표
x, y = 1, 1

# tempX선언해도 python이라 글로벌처럼 사용 가능하구나
# 지역 개념은 함수 안에서만인듯
for inLRUD in inLRUDs:
    for i in range(len(LRUD)):
        if inLRUD == LRUD[i]:
            tempX = x + dx[i]
            tempY = y + dy[i]

    # 범위 벗어났는지 판단
    if tempX<1 or tempX>nLRUDs or tempY<1 or tempY>nLRUDs:
        continue
    x, y = tempX, tempY


print(x, y)
