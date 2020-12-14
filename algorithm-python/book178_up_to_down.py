'''
수열을 입력받았을때, 내림차순으로 정렬하는 프로그램을 만드시오.

**input
첫째줄 에는 수열의 개수가 주어진다. 이후 수열이 주어진다.

3
15
27
12

**output
27 15 12
'''
# ----- sorted()사용 ---
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)
for i in array:
    print(i, end=' ')


# ----- sort()사용 -----
n = int(input())
numList = []
for _ in range(n):
    numList.append(int(input()))

numList.sort(reverse=True)
print(numList)