'''
1.숫자가 쓰인 카드들이 N x M 의 형태로 놓여있다. 이때 N은 행의 개수, M은 열의 개수를 의미한다. 
2. 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
3. 그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑는다.
4. 따라서 처음에 행을 선택할 때, 해당 행에서 가장 낮은 숫자를 뽑을 것을 고려하여 

3 1 2
4 1 4
2 2 2

첫 번째 혹은 두 번째 행을 선택하는 경우, 최종적으로 뽑는 카드는 1이다.
하지만 세 번째 행을 선택하는 경우 최종 뽑는 카드는 2이다. 
따라서 세 번째 행을 선택하여 숫자 2가 쓰여진 카드를 뽑는 것이 정답이다. 

*** 첫 번째 줄에는 N, M이 주어지고 그 다음에는 행렬이 주어진다.
**input
3 3
3 1 2
4 1 4
2 2 2

*** 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.
**output
2
'''
# ------ 그리디로 풀이 ------
# 사실상 2중 for랑 다를게 없긴해...
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    # 애초에 그냥 min으로 뺴도 됨
    min_valie = min(data)
    result = max(result, min_valie)

print(result)



# ------ 다음 풀이 - 2중for ------
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 행에서 가장 작은 정수
    min_value = 999
    for j in data:
        min_value = min(min_value, j)
    # 가장 작은 정수 중 가장 큰 수 찾기
    result = max(result, min_value)

print(result)

# ------ 초기 풀이 - 2중for ------
n, m = map(int, input().split())
inputList = [list(map(int, input().split())) for _ in range(n)]

maxRowValue =0
for i in range(n):
    min = 999
    for j in range(m):
        if min > inputList[i][j]:
            min = inputList[i][j]

    if maxRowValue < min:
        maxRowValue = min

print(maxRowValue)