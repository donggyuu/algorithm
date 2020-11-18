'''
N개의 수로 된 수열 A[1], A[2], ..., A[N] 이 있다.
이 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+...+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

**input(크기8의 배열, 연속으로 원소를 골라서 3이 되도록 해라)
8 3
1 2 1 3 1 1 1 2
**output(연속인 원소의 합이 3이 되는 경우는 5가지)
5
'''

# 입력 받기
len, sum = map(int, input().split())
targetList = list(map(int, input().split()))

totalCount = 0
for i in range(len):

    resultSum = 0
    for j in range(len):

        # i번째부터 순차적으로 1씨 늘려가며 합을 구함
        if i+j < len:
            resultSum += targetList[i+j]

        # 합이 구하고자 하는 sum이면 break
        if resultSum == sum:
            totalCount += 1
            break

print(totalCount)