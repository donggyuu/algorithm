# TODO 강사 코드 보기
# TODO 디버깅 print말고 VS Code에서는 어찌함?

'''
1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.
규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다.
규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다.
규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.

예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3*100으로 계산되어 1,300원을 받게 된다.
또 3개의 눈이 2, 2, 2로 주어지면 10,000+2*1,000 으로 계산되어 12,000원을 받게 된다.
3개의 눈이 6, 2, 5로 주어지면 그 중 가장 큰 값이 6이므로 6*100으로 계산되어 600원을 상금 으로 받게 된다.
N 명이 주사위 게임에 참여하였을 때, 가장 많은 상금을 받은 사람의 상금을 출력하는 프로그램 을 작성하시오

** 입력설명
첫째 줄에는 참여하는 사람 수 N(2<=N<=1,000)이 주어지고 그 다음 줄부터 N개의 줄에 사람 들이 주사위를 던진 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.
** 출력설명
첫째 줄에 가장 많은 상금을 받은 사람의 상금을 출력한다.

** 입력예제
3
3 3 6
2 2 2
6 2 5
** 출력예제
12000
'''

# ----------------------------------------

'''
개선된 코드 : count함수 안 쓰고 그냥 모든 경우의 수 단순 비교를 한다.
'''

nParticipant = int(input())
resultMoney = 0

for i in range(nParticipant):
    
    # 정렬을 해야 큰 수가 무엇인지 알기 쉽다.
    temp = input().split()
    temp.sort()

    a, b, c = map(int, temp)
    # 전부 같은 눈
    if a == b and b == c:
        money = 10000 + a * 1000
    # 같은 눈이 2개인 경우
    elif a == b or a == c:
        money = 1000 + (a * 1000)
    elif b == c:
        money = 1000 + (a * 1000)
    # 같은 눈이 없다
    else:
        money = c * 100
    
    if money > resultMoney:
        resultMoney = money

print(resultMoney)

# ----------------------------------------

'''
초기 코드 : 같은 눈의 갯수를 set&count함수로 세어서 중복을 확인한다.
'''

# def getReward(diceCaseList):

#     # set으로 변형해서 갯수 차이. 
#     # 같은 눈이 3개

#     lenList = len(diceCaseList)
#     lenSet = len(set(diceCaseList))

#     # 중복 없다
#     if (lenList - lenSet) == 0:
#         return max(diceCaseList) * 100

#     # 중복 있다.
#     for i in range(3):

#         checkingNum = diceCaseList[i]

#         # 2개 중복
#         if diceCaseList.count(checkingNum) == 2:
#             return  1000 + (checkingNum) * 100
#         # 3개 중복               
#         elif diceCaseList.count(i) == 3:
#             return 10000 + (checkingNum) * 1000

# nParticipant = int(input())

# maxReward = 0
# for i in range(nParticipant):

#     inputList = list(map(int, input().split()))

#     temp = getReward(inputList)
#     if maxReward < temp:
#         maxReward = temp

# print(maxReward)