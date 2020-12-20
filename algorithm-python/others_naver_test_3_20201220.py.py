# https://www.geeksforgeeks.org/count-ways-to-split-a-binary-string-into-three-substrings-having-equal-count-of-zeros/
# a를 포함하면서 3파트로 나누는 경우의 수 출력 

# 아래는 3파트를 
# 이거 35분까지 풀기 

def count(string):
 
    countA = 0
    for char in string:
        if char == 'a':
            countA += 1

    if (countA % 3 != 0):
        return 0
 
    result = 0
    eachA = countA // 3
    sum = 0
 
    tmpMap = {}
 
    for i in range(len(string)):
 
        if string[i] == 'a':
            sum += 1
 
        if (sum == 2 * eachA and eachA in tmpMap and i < len(string) - 1 and i > 0):
            result += tmpMap[eachA]
 
        if sum in tmpMap:
            tmpMap[sum] += 1
        else:
            tmpMap[sum] = 1
             
    return result


print(count("babaa"))