'''
5*5 격자판에 아래롸 같이 숫자가 적혀있습니다.
N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합 니다.

** input
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19

** output
155
'''

n = int(input())
# 한줄로 2차원 배열 만들기
inputList = [list(map(int, input().split())) for _ in range(n)]

largest = 0

for i in range(n):
    sumOne, sumTwo = 0, 0 # 임시로 쓰일 값들

    for j in range(n):
        sumOne += inputList[i][j]
        sumTwo += inputList[j][i]

    if sumOne > largest:
        largest = sumOne
    if sumTwo > largest:
        largest = sumTwo

sumOne, sumTwo = 0, 0 # 다시 쓰기 위해 초기화

print(largest)
print(sumOne, sumTwo)

for i in range(n):
    sumOne += inputList[i][i]
    sumTwo += inputList[i][n-i-1]

    if sumOne > largest:
        largest = sumOne
    if sumTwo > largest:
        largest = sumTwo

print(largest)
