'''
입력받은 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램을 작성하시오.
- 예로, 32를 뒤집으면 23이고 23은 소수이므로 출력한다. 
- 단 910를 뒤집으면 19로 숫자화 한다(첫 자리부터의 연속된 0은 무시한다)

** input
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
각 자연수의 크기는 100,000를 넘지 않는다.
** output
첫 줄에 뒤집은 소수를 출력합니다. 출력순서는 입력된 순서대로 출력한다.

** input_ex
5
32 55 62 3700 250
** output_ex
23 73

'''

# using for
def getReversedNum(inputNum):
    reversed = 0

    while inputNum > 0:
        # 맨 뒤 구하기
        tailNum = inputNum % 10

        # 맨 뒤 값 더하기. 결과값에다가!
        reversed = reversed * 10 + tailNum

        # 맨 뒤의 값은 활용 완료니까 제외한다.
        inputNum = inputNum // 10

    return reversed

# using while
def getReversedNum_byWhile(inputNum):
    reversed = 0
    while inputNum > 0:
        tailNum = inputNum % 10
        reversed = reversed * 10 + tailNum
        inputNum = inputNum // 10
    
    return inputNum


def isPrimeNum(inputNum):
    if inputNum == 1:
        return False
    # ex. 12면 7이상이라면 어차피 안 나누어 떨어짐
    for i in range(2, inputNum//2 + 1):
        if inputNum%i == 0:
            return False

    return True


# ----------------------------------------

n = int(input())
inputNumList = list(map(int, input().split()))

for i in range(len(inputNumList)):
    inputReversedNum = getReversedNum(inputNumList[i])

    if isPrimeNum(inputReversedNum):
        print(inputReversedNum, end=' ')
