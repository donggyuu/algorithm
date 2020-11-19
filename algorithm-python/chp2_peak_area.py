'''
지도 정보가 N*N 격자판에 주어집니다. 각 격자에는 그 지역의 높이가 쓰여있습니다.
각 격자 판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역입니다.
봉우리 지역이 몇 개 있는 지 알아내는 프로그램을 작성하세요.
-격자의 가장자리는 0으로 초기화 되었다고 가정한다.
-만약 N=5 이고, 격자판의 숫자가 다음과 같다면 봉우리의 개수는 10개입니다.

그림 참고 : https://cheeseb.github.io/algorithm/algorithm-bonguri/

**input
5
5 3 7 2 3
3 7 1 6 1
7 2 5 3 4
4 3 6 4 1
8 7 3 5 2
**output
10

'''
# point1: 2차원에서 초기값 0 세팅 방법
# point2: all 내장함수 사용하면 결더 간결 : 참고-> https://codepractice.tistory.com/8단


# 입력 받기
n = int(input())
inputList = [list(map(int, input().split())) for _ in range(n)]

# 위, 아래 초기값 0 세팅
inputList.insert(0, [0]*n)
inputList.append([0]*n)

# 앞, 뒤 초기값 0 세팅
for element in inputList:
    element.insert(0, 0)
    element.append(0)

# 반복문을 돌면서 봉우리인지 확인한다.

peak = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        # 봉우리인지 판단

        # 상
        if inputList[i][j] < inputList[i-1][j]:
            continue
        # 하
        elif inputList[i][j] < inputList[i+1][j]:
            continue
        # 좌
        elif inputList[i][j] < inputList[i][j-1]:
            continue
        # 우
        elif inputList[i][j] < inputList[i][j+1]:
            continue
        # 봉우리
        else:
            peak += 1

print(peak)


# ------------------------------------------------
# all 내장함수 사용
dx = [-1, 0, 1, 0] # 미리 상하좌우의 좌표를 세팅
dy = [0, 1, 0, -1]

for i in range(1, n+1):
    for j in range(1, n+1):
        if all(inputList[i][j] > inputList[i+dx[k]][j+dy[k]] for k in range(4))
        peak += 1
# ------------------------------------------------
