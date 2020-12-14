'''
가게의 부품이 5개 있다.
N = 5 (부품 개수)
[8, 3, 7, 9, 2]

손님이 3개의 부품이 있는지 확인을 요청한다.
M = 3 (부품 개수)
[5, 7, 3]

손님이 요청한 부품이 있으면 yes, 없으면 no를 출력하는 프로그램을 작성하시오.

**input
5
8 3 7 9 2
3
5 7 9

**output
no yes yes
'''

# ------------------- 이진 탐색 이용 -------------------
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

# 보유한 부품 개수
n = int(input())
# 보유한 부품
array = list(map(int, input().split()))
array.sort()

# 손님 요청한 부품 개수
m = int(input())
# 손님 요청한 부품
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')



# ------------------- 계수 정렬 이용 -------------------
n = int(input())
array = [0] * 1000001

# 이런 식으로 input받아서 하나씩 받는 것도 가능
for i in input().split():
    array[int(i)] = 1 # 8 3이면, index의 8과 3지점에 1을 세팅

# 손님의 부품 수
m = int(input())
# 손님 부품 요청 한 것
x = list(map(int, input().split()))

# 손님 부품 번호를 하나씩 확인
for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end= ' ')


# ------------------- 집합(set) 이용 -------------------
# 부품 개수 및 부품 입력
n = int(input())
array = set(map(int, input().split()))

# 손님 부품 개수 및 찾으려는 부품 입력
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')



# ------------------- 초기 풀이 - 순차 탐색 이용 -------------------
n = int(input())
nList = list(map(int, input().split()))

m = int(input())
mList = list(map(int, input().split()))

strList = []

for i in range(m):
    count = 0
    for j in range(n):
        if mList[i] == nList[j]:
            count += 1

    if count > 0:
        strList.append('yes')
    else:
        strList.append('no')

print(strList)
