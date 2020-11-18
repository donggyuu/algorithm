'''
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로 그램을 작성하세요.

**input
3
1 3 5
5
2 3 6 7 9
**output
1 2 3 3 5 6 7 9
'''
# -------
# 강의 풀이 이해하기.

## 직접 구현하기.

lenA = int(input())
aList = list(map(int, input().split()))

lenB = int(input())
bList = list(map(int, input().split()))

pointOne = 0
pointTwo = 0
resultList = []

# 이미 오름차순 정렬이 되어있기 때문에 pointer의 크기비교로 가능
while pointOne < lenA and pointTwo < lenB:
    # 하나씩 비교하면서 작은 수를 resultList에 넣는다.
    if aList[pointOne] >= bList[pointTwo]:
        resultList.append(bList[pointTwo])
        pointTwo+=1
    else:
        resultList.append(aList[pointOne])
        pointOne+=1


# 대소비교 후 남은 리스트를 결과 리스트에 붙인다.
if pointOne < lenA:
    resultList = resultList + aList[pointOne:]
if pointTwo < lenB:
    resultList = resultList + bList[pointTwo:]

print(resultList)


# ----------------------------
# 초기 풀이, 단순히 append()로 붙임
# lenFstList = int(input())
# fstList = list(map(int, input().split()))

# lenScdList = int(input())
# scdList = list(map(int, input().split()))

# for i in range(lenScdList):
#     fstList.append(scdList[i])

# fstList.sort()
# print(fstList)