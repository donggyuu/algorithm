'''
체스판은 8x8 의 좌표평면이다.
나이트는 L자로 움직인다.

좌표평면이 아래와 같이 주어지고 나이트가 a1에 있다면 
나이트는 c2, b3으로 이동할 수 있다.

a1 b1 c1 ...
a2 b2 c2
a3 b3 c3
...

나이트가 이동할 수 있는 경우의 수를 출력하시오.

**input
a1

**output
2
'''

inputData = input()
#받은 문자열의 2번째가 행의 숫자

row = int(inputData[1])
# ascii code를 가지고 열의 숫자를 파악 
# 참고: https://wikidocs.net/32#ord
column = int(ord(inputData[0])) - ord('a') + 1

# 움직이는 전체 경로 -> 보통은 [1,-1,0,0] 이런 식으로 나오지만...
# 움직임은 고정값, 리스트 안의 튜플로 설정하자
movements = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

count = 0
for move in movements:
    nextRow = row + move[0]
    nextCol = column + move[1]

    # 다음 위치 문제 없으면 다음 위치로 이동
    if nextRow>=1 and nextRow<=8 and nextCol>=1 and nextCol<=8:
        count += 1

print(count)

# --- 초기 풀이 ---
# 총 8가지의 이동 경우가 있는데, 그걸 다 고려하려면 코드가 너무 길어진다
# inputChar = input()
# charY = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# count = 0
# for i in range(len(charY)):
#     if inputChar[0] == charY[i] and i+2 < 8:
#         if int(inputChar[1]) + 1 < 8:
#             count += 1
#             print('start_a: ', i)
#             print('start_a')

# for i in range(len(charY)):
#     if inputChar[0] == charY[i] and i+1 < 8:
#         if int(inputChar[1]) + 2 < 8:
#             count += 1
#             print('start_b: ', i)
#             print('start_b')

# print(count)