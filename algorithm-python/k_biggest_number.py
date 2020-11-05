'''
1부터 100사이의 자연수가 적힌 N장의 카드가 있다(같은 숫자의 카드가 여러장 있을 수 있다).
이 중 3장을 뽑아 3장의 수의 합을 기록할 때, 
기록한 값 중 K번째로 큰 수를 출력 하는 프로그램을 작성하시오.

만약 3장의 수의 합들이 25 25 23 23 22 20 19......이고 K값이 3이라면 K번째 큰 값 은 22입니다.

** 입력설명
첫 줄에 자연수 N(3<=N<=100)과 K(1<=K<=50) 입력되고, 그 다음 줄에 N개의 카드값이 입력 된다.

** 출력설명
첫 줄에 K번째 수를 출력한다. K번째 수는 반드시 존재한다.


** 입력예제
10 3
13 15 34 23 45 65 33 11 26 42

** 출력예제
143
'''

n, k = map(int, input().split())
inputList = list(map(int, input().split()))

# 결과 합의 중복 제거를 위한 set
resultSet = set()

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            # set은 append가 아니라 add
            resultSet.add(inputList[i] + inputList[j] + inputList[m])

resultList = list(resultSet)
resultList.sort(reverse=True)

print(resultList[k-1])
