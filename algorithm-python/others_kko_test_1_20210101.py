'''
[빌린 친구, 빌려준 친구, 빌린 포인트]의 그룹이 주어지면,
조건에 맞는 최소 잔여 포인트를 가진 친구를 반환하시오.
- 최소 잔여포인트는 음수값
- 모든 친구의 잔여포인트가 음수값이 아니면 None을 반환 
- 잔여포인트가 같은 친구가 여러명이면 알파벳 순으로 반환

예를 들어 아래와 같은 그룹이 주어집니다.
['Ap', 'Fr', '5'], ['Fr', 'Ap', '3']
Ap는 3을 빌려주고 5를 빌렸습니다. 그러므로 Ap의 잔여포인트는 3-5=-2 입니다.
'''
# test_data
testArr = [['Ap', 'Fr', '5'], ['Fr', 'Ap', '3'], ['Tu', 'Ap', '7'], ['Tu', 'Ap', '4'], ['Tu', 'Ap', '2']]


# minusPoint찾기
minusPoint = {}
for i in range(len(testArr)):
    name = testArr[i][0]
    point = int(testArr[i][2])
    if name not in minusPoint:
        minusPoint[name] = point
    else:
        minusPoint[name] += point

# plusPoint찾기
plusPoint = {}
for i in range(len(testArr)):
    name = testArr[i][1]
    point = int(testArr[i][2])
    if name not in plusPoint:
        plusPoint[name] = point
    else:
        plusPoint[name] += point

# 결과값을 찾자
resultPoint = {}
for key in plusPoint:
    if key in minusPoint:
        resultPoint[key] = plusPoint[key] - minusPoint[key]
for key in minusPoint:
    if key not in resultPoint:
        resultPoint[key] = 0 - minusPoint[key]

# None조건 체크
minValue = min(resultPoint.values())
if minValue >= 0:
    print("None")


# resultPoint['Abc'] = -13      # test_data
# print('result:', resultPoint) # test_data

# 최소잔여포인트에 해당하는, 1명 이상의 친구 찾기
res = [name for name, point in resultPoint.items() if point == minValue]
res.sort()
print(res)
