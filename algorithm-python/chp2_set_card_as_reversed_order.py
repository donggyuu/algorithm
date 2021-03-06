'''
1부터 20까지 숫자가 하나씩 쓰인 20장의 카드가 오름차순으로 한 줄로 놓여있다.
각 카드의 위치는 순차대로 1부터 20까지로 나타낸다.

구간 [a, b] (단, 1 ≤ a ≤ b ≤ 20)가 주어지면 위치 a부터 위치 b까지의 카드를 현재의 역순으로 놓는다.
예를 들어, 구간이 [5, 10]으로 주어진다면, 위치 5부터 위치 10까지의 카드 5, 6, 7, 8, 9, 10을 역순으로 하여 10, 9, 8, 7, 6, 5로 놓는다.
- AS IS : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
- TO BE : 1 2 3 4 10 9 8 7 6 5 11 12 13 14 15 16 17 18 19 20

오름차순으로 놓여있는 20장의 카드에 대해 10개의 구간이 주어지면,
위의 규칙에 따라 순서를 뒤집는 작업을 수행한 뒤 마지막 카드들의 배치를 구하는 프로그램을 작성하시오.

** input
5 10
9 13
1 2
3 4
5 6
1 2
3 4
5 6
1 20
1 20

** output
1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20
'''
# What is "underscore(_)" in Python
# https://mingrammer.com/underscore-in-python/

# --------------------------------------------------------

# [0, 1, 2, 3 ... 20]
dftList = list(range(21)) 

for _ in range(10): # i로 해도 쓸 일이 없는데, i에 숫자 대입하는거도 시간 걸리니.. _를 사용.
    start, end = map(int, input().split())

    for i in range((end-start+1)//2 ):
        # 1,2,3 -> 3,2,1 이면, (3-1+1)/2 = 1 번의 변경이 필요
        # 1과 3을 변경, 2는 그대로 -> 총 1번의 변경

        # change
        dftList[start+i], dftList[end-i] = dftList[end-i], dftList[start+i]


# 맨 앞 0 제거
dftList.pop()
for ele in dftList:
    print(ele, end=' ')
