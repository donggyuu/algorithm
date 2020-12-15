'''
dynamic의 사용 조건
1. 큰 문제를 작은 문제로 나눌 수 있다.
2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

피보나치는 1과 2를 모두 만족한다. skill로서 메모제이션(배열 선언해서 저장)을 사용
'''

# ---- dynamic fibo ----
d = [0] * 100

def dynamic_fibo(x):
    if x == 1 or x == 2:
        return 1

    # 이미 계산한 적이 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    d[x] = dynamic_fibo(x-1) + dynamic_fibo(x-2)
    
    return d[x]

print(dynamic_fibo(99))


# ---- 재귀적 fibo -------
def fibo(x):
    if x == 1 or x == 2:
        return 1

    return fibo(x - 1) + fibo(x -2)

print(fibo(4))
