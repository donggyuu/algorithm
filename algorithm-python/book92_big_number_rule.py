'''
큰 수의 법칙
순서대로 2,4,5,4,6으로 이루어진 배열이 있을 때 M이8이고 K가3이라 가정하자.
특정한 인덱스의 수가 연속해서 3번까지만 더해질 수 있으므로 결과는
6+6+6+5+6+6+6+5인 46이다.

배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때
큰수 법칙에 따른 결과를 출력하시오.

**input
5 8 3
2 4 5 4 6

**output
46
'''
# 큰 거 우선으로 하고, 약수관련 issue가 없어보이니 그리디지 않을까 하는 생각


# --------------------------------------------
# 그리디로 풀기
# --------------------------------------------

n, m, k = map(int, input().split())
myList = list(map(int, input().split()))

myList.sort()
maxValue = myList[n-1]
secMaxValue = myList[n-2]

resultSum = 0
count = 0

while count < m:

    resultSum += maxValue
    count += 1

    # 3의 배수마다 두번째 큰 수를 더한다.
    if count % 3 == 0:
        resultSum += secMaxValue
        count += 1

# --- 개선된 풀이 --------------------------------
while True:
    for i in range(k):
        if m == 0:
            break
        resultSum += maxValue
        m -= 1
    
    if m == 0:
        break
    resultSum += secMaxValue
    m -= 1

# --- 개선된 풀이 --------------------------------

print(resultSum)


# --------------------------------------------
# 규칙성으로 풀기
# --------------------------------------------
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1] # 젤 큰수
second = data[n-2] # 두번째 큰 수

# 큰 수가 더해지는 횟수
count = m/(k+1) * k # (큰거3개, 작은거1개의 뭉텅이)
count += m % (k+1)

result = 0
result += (count) * first # 젤 큰수 더하기
result += (m-count) * second # 두번째 큰 수 더하기

print(result)