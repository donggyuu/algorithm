'''
1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하시오(N은 자연수).
만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개이다.

** input
첫 줄에 자연수의 개수 N(2<=N<=200,000)이 주어집니다.

20

** output
첫 줄에 소수의 개수를 출력합니다.

8
'''

# 1은 제외
# 본인은 제외하고 배수 거르기

# 코드 초안

nInteger = int(input())
arr = [0]*nInteger

arr[0] = -1
arr[1] = -1

for i in range(2, nInteger):

    while i < nInteger:
        i += i
        if i < nInteger:
            arr[i] = -1

for i in range(nInteger):
    if arr[i] == 0:
        print(i, end=' ')
