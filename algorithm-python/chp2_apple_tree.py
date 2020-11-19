'''
현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 한 그루의 사과나무가 심어저
있다. N의 크기는 항상 홀수이다. 가을이 되어 사과를 수확해야 하는데 현수는 격자판안의 사
과를 수확할 때 다이아몬드 모양의 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서
남겨놓는다.
만약 N이 5이면 아래 그림과 같이 진한 부분("로 둘러싸인 부분)의 사과를 수확한다.

 10  13 "10" 12  15
 12 "39  30  23" 11
"11  25  50  53  15"
 19 "27  29  37" 27
 19 13  "30" 13 19

(격자그림 참고: https://velog.io/@jiffydev/algo-17)

현수과 수확하는 사과의 총 개수를 출력하세요.

** input
5
0 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19

** output
379
'''

n = int(input())
tartanList = [list(map(int, input().split())) for _ in range(n)]

start = end = n//2
nApple = 0

for i in range(n):
    for j in range(start, end+1):
        nApple += tartanList[i][j]

    if i < (n//2):
        start -= 1
        end += 1
    else:
        start += 1
        end -= 1


print(nApple)