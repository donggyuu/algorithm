'''
N개 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력 하는 프로그램을 작성하시오.
 
** details
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
각 자연수의 크기는 10,000,000를 넘지 않는다.

** input
3
125 15232 97

**output
97
(9+7=16으로 최대이므로 출력)
'''

# make func : digit_sum
# 방법_1 : int를 활용
def digit_sum(number):
    sum = 0

    while number > 0:
        sum += number%10
        number = number//10

    return sum


# 방법_2 : string을 활용
def digit_sum_by_str(strNumber):
    sum = 0

    for i in str(strNumber):
        sum+=int(i)

    return sum

# --------------------------------------------

nInput = int(input())
InputNumList = list(map(int, input().split()))

maxSum = -1
maxNumber = -1

for number in InputNumList:
    digitSum = digit_sum(number)
    if digitSum > maxSum:
        maxSum = digitSum
        maxNumber = number

print(maxNumber)
