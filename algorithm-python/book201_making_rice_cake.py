'''
절단기에 높이(H)를 지정하면 떡을 한번에 절단한다.
높이가 H보다 긴 떡은 H 위의 부분이 잘리고 낮은 떡은 잘리지 않는다.

예를 들어 높이가 19, 14, 10, 17cm 인 떡이 있고 절단기 높이가 15cm이라면
자른 뒤의 떡 높이는 15, 14, 10, 15cm이고 잘린 떡의 길이는 4, 0, 0, 2cm이다.
이때 손님은 6cm만큼을 가져간다.

손님이 요청한 길이기 M일때 적어도 M만큼의 길이를 얻기 위한 절단기H의 최대 높이를 구하시오.

**input
4 6
19 15 10 17

**output
15
'''

# -------- 개선된 풀이 by Parametric Search --------

n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

# 시작점, 끝점 설정 for 이진 탐색
start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2

    # 잘린 떡의 양 계산
    for x in array:
        if x > mid:
            total += x - mid
    
    # 떡의 양이 부족하면 왼쪽 탐색
    if total < m:
        end = mid - 1
    else:
        result = mid # 최대한 덜 잘렸을 대가 정답이기에, 여기서 result에 기록
        start = mid + 1

print(result)
    



# -------- 초기 풀이 by 순차탐색 --------

# def getCuttingCake(h):
#     cuttingLength = 0
#     for i in range(n):
#         if cakeList[i] - h > 0:
#             cuttingLength += cakeList[i] - h
#     return cuttingLength

# # input
# n, m = map(int, input().split())
# cakeList = list(map(int, input().split()))
# h = 0
# absLenth = 9999

# while True:
#     # 손님이 요청한 길이와, 절단기로 자른 길이의 차가 최소인 h를 구해한다.
#     if absLenth >= abs(m-getCuttingCake(h)):
#         absLenth = abs(m-getCuttingCake(h))
#         h += 1 # (1)다음번에 break라면 이 +1은 뺴줘 한다.
#     else:
#         h -= 1 # (1)에 의한 처리를 해줌
#         break
        
# print(h)
