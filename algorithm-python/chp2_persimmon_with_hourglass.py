'''
현수는 곳감을 만들기 위해 감을 깍아 마당에 말리고 있습니다.
현수의 마당은 N*N 격자판으 로 이루어져 있으며, 현수는 각 격자단위로 말리는 감의 수를 정합니다.
그런데 해의 위치에 따라 특정위치의 감은 잘 마르지 않습니다.
그래서 현수는 격자의 행을 기준으로 왼쪽, 또는 오른쪽으로 회전시켜 위치를 변경해 모든 감이 잘 마르게 합니다.
만약 회전명령 정보가 2 0 3이면 2번째 행을 왼쪽으로 3만큼 아래 그림처럼 회전시키는 명령 입니다.

그람 참고 : https://cheeseb.github.io/algorithm/algorithm-hourglass/

첫 번째 수는 행번호, 두 번째 수는 방향인데 0이면 왼쪽, 1이면 오른쪽이고, 세 번째 수는 회 전하는 격자의 수입니다.
M개의 회전명령을 실행하고 난 후 아래와 같이 마당의 모래시계 모양의 영역에는 감 이 총 몇 개가 있는지 출력하는 프로그램을 작성하세요.

** input
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
3
2 0 3
5 1 2
3 1 4

** output
362
'''
# point: 결국 회전 수 만큼 앞에 붙이거나 뒤에 붙이는 것임.

nList = int(input())
inputList = [list(map(int, input().split())) for _ in range(nList)]

nDry = int(input())

for _ in range(nDry):
    target, direction, time = map(int, input().split())
    if direction == 0: #왼쪽으로 이동
        for _ in range(time):
            inputList[target-1].append(inputList[target-1].pop(0)) # 2차원에서 (2,0)을 이런 식으로 뺌.
    else:
        for _ in range(time):
            inputList[target-1].insert(0, inputList[target-1].pop()) # 2차원에서 특정 행의 제일 마지막을 pop()


print(inputList)

# 모래시계 영역.
nPersimmon = 0
start = 0
end = nList - 1

for i in range(nList):
    for j in range(start, end+1):
        nPersimmon += inputList[i][j]

    if i < (nList//2):
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1

print(nPersimmon)
