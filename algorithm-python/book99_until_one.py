'''
N이 1이 될 때까지 두 과정중 하나를 반복적으로 수행한다.
단, 2번째 연산은 N이 K로 나누어떨어질 때만 선택 가능하다.

1. N에서 1을 뺀다.
2. N을 K로 나눈다. 

예로 N이 17, K가 4라고 가정하자. 
이때 1번을 수항하면 N은 16이된다.
이후 2번을 두 번 수행하면 N은 1이 된다. 
결과적으로 전체 3번 수행하게 되고 이는 N을 1로 만드는 최소 횟수이다.

이때 최소 횟수를 구하시오.

**input
** N과 K
25 5

**output
2
'''

# ----- 개선된 풀이 -----
# n이 매우 크다면... 한번에 빼는 방식으로 개선이 가능하다.

n, k = map(int, input().split())
result = 0

while True:
    target = (n//k) * k
    result += (n - target) # 미리 안 나눠떨어지는 수를 더해준다.

    n = target
    while n < k:
        result += 1
        n //= k
    
    # 남은 수 만큼 1빼기
    result += (n-1)

    print(result)


# ----- 초기 풀이 -----
n, k = map(int, input().split())
result = 0

while n >= k:
    # 나누어 떨어질 때까지 1빼기
    while n % k != 0:
        n -= 1
        result += 1
    # 나누어 떨어지니까 나누기
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)




# ----- 초기 풀이 -----
# 이건 나누는 경우만 구했지 최종은 안 구했으므로 틀리다.
# n, k = map(int, input().split())

# min = 100000
# result = 0

# while n > 1:
#     if n % k == 0:
#         n = n // k
#     else:
#         n -= 1

#     result += 1

# print(result)