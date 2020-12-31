'''
어느 한 문자의 대문자, 소문자가 모두 있는 String을 balanced 되어있다고 한다. 
예를 들어, CATattac는 a,c,t의 대소문자가 모두 포함된 String이므로 balanced 되어있다. 
반면 Madam는 d,a의 소문자만 포함된 String이므로 balanced 되어있지 않다. 

String인 S가 주어졌을때, 가장 짧은 balanced된 문자열의 길이를 출력하시오.
(만약 balanced되어있지 않다면 -1을  return하시오)

**example
S = "azABaabza" 의 가장 짧은 balanced된 문자열은 ABaab이므로 5가 return된다.
S = "TacoCat"은 balanced하지 않기 때문에 -1이 return된다.
'''

# 아래 풀이를 참고
# https://leetcode.com/discuss/interview-question/963586/Microsoft-or-OA-or-Codility/785106
def solution(S):
    for i in range(1, len(S)+1):
        for j in range(len(S)-i+1): #큰 문자열부터 줄이는 연습
            listLower = []
            listUpper = []
            tmpS = S[j:j+i]

            for char in tmpS:
                if char.islower():
                    listLower.append(char)
                else:
                    # 추후 비교를 위해 소문자로 변환 후 넣기
                    a = char.lower()
                    listUpper.append(a)
            
            # 두 리스트 비교
            tmpCount = 0
            print(i, j)
            print('lower :', listLower)
            print('upper :', listUpper)
            for m in listLower:
                if m not in listUpper:
                    tmpCount += 1
            for n in listUpper:
                if n not in listLower:
                    tmpCount += 1
            if tmpCount == 0:
                return i

    return -1

a = solution('AcZCbaBz')
print('answer: ', a)
