'''
'a'와 'b'로 이루어진 문자열 S가 주어진다.
문자열을 3부분으로 나눈다고 할때, 각 부분에 같은 개수의 'a'가 들어가도록 나누는 방법의 수를 구하여라.

S = "babaa"가 주어지면 return값은 2이다. 
"ba|ba|a", "bab|a|a" 과 같이 2가지 경우가 있기 때문이다.

S = "bbbbb"가 주여지면 return값은 6이다.
"b|b|bbb", "b|bb|bb", "b|bbb|b", "bb|b|bb", "bb|bb|b", "bbb|b|b" 와 같이 6가지 경우가 있기 때문이다.

S = "aabaabaa"가 주어지면 return값은 4이다.

'''

def solution(s):
 
    cnt = 0

    # 안에 있는 a의 개수를 파악한다.
    for c in s:
        if c == 'a':
            cnt += 1

    # 3으로 나누어떨어지지 않는다면? -> 0이다
    if (cnt % 3 != 0):
        return 0
 
    res = 0  
    k = cnt // 3 # 몫
    sum = 0
 
    mp = {} # dictionay in python. 다른 구조에서는 hash table이나 hash map
 
    for i in range(len(s)):

        # Increment count if 0 appears
        if s[i] == 'a':
            sum += 1 
    
        # k는 몫, a가 각 부분에 개수 k만큼 들어가 있음
        '''
        aabaabaa 에서,
        aab aa baa
        k번째 에서 b를 추가하면 이후 2k이후에 나오는 것도 k번째에 나오는 b의 갯수와 같다는 것을 풀어보다가 알았다.
        ** 처음에는 떠올리기 힘들어서 노트에 그려보고 규칙을 찾았다.
        '''
        if (sum == 2 * k and k in mp 
        and i < len(s) - 1 and i > 0): # 처음이랑 마지막은 상관없어
            res += mp[k]
 
        if sum in mp:
            mp[sum] += 1
        else:
            mp[sum] = 1
             
    return res


print(solution("aabaabaa"))
