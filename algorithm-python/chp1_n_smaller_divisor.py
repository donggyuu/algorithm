'''
**problem
6의 약수는 1, 2, 3, 6의 4개이다.
두 개의 자연수 n, k가 주어졌을 때, n의 약수들 중 k번째로 작은 수를 출력하도록 하라.
(단, k번째 약수가 존재하지 않을 경우에는 -1을 출력)

**input_ex
input  : 6 3
result : 3
'''

n, k = map(int, input().split())
count = 0

for i in range(1, n+1):
    if n % i == 0:
        count += 1

    if count == k:
        print(i)
        break
else:
    print(-1)

# 처음 짠 코드
# def find_n_divisor(N, K):

#     result = []
#     for n in range(N):        

#         if N % (n+1) == 0:
#             result.append(n+1)

#     print('n번째 약수', result[K-1])