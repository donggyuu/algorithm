'''
N개의 문자열을 입력받아 회문이면 YES, 아니면 NO를 출력하는 프로그램을 작성한다.
(대소문자 구분은 안함, 각 단어 길이는 100을 넘지 않는다)

**input
5
level
moon
abcba
soon
gooG

**output
# 1 YES
# 2 NO
# 3 YES
# 4 NO
# 5 YES
'''
# ---------------------------------
# 여러 방법
# 1. for문으로 역순 구하기
# 2. [::-1]
# 3. method활용 -> reverse, reversed 

# 개선된 풀이 - [::-1]
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    if s == s[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))


# ---------------------------------
# 나의 초기 풀이 - for문 사용

def isPalindrome(inputString):

    lowerString = inputString.lower()

    fromStart = ""
    fromEnd = ""

    # get fromStart & fromEnd 
    for i in range(len(lowerString)):
        fromStart += lowerString[i]
        fromEnd += lowerString[-i-1]

    # print
    if fromStart == fromEnd:
        return 'YES'
    else:
        return 'NO'

# get result
nString = int(input())
nResultList = []

for i in range(nString):
    inputString = input()
    nResultList.append(isPalindrome(inputString))

# print result
for i in range(nString):
    print('#', i+1, nResultList[i])