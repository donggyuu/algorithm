'''
두 개의 정 N면체와 정 M면체의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확률이 높은 숫자를 출력하는 프로그램을 작성하시오.
(숫자가 중복될 경우 오름차순으로 출력한다)

첫 번째 줄에는 자연수 N과 M이 주어진다(N과 M은 4, 6, 8, 12, 20 중 하나).
첫 번째 줄에 답을 출력한다.
** input
4 6
** output
5 6 7
'''

n, m = map(int, input().split())

numPlusPoly = [0]*(n+m+1) # 합의 최대가 n+m니까 굳이 n*m개 배열 세팅 안해도 됨
maxValue = 0

# array for all plus
for i in range(n+1):
    for j in range(m+1):
        numPlusPoly[i+j]+=1

# find max values
for i in range(n+m+1):
    if maxValue < numPlusPoly[i]:
        maxValue = numPlusPoly[i]

# print
for i in range(n+m+1):
    if maxValue == numPlusPoly[i]:
        print(i, end = ' ') # 개행 안함
