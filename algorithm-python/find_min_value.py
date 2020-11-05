
arr = [5, 3, 4, 5, 6, 7, 9]

# 방법_1
minValue = float('inf') # 최댓값을 설정

for i in range(len(arr)):
    if arr[i] < minValue:
        minValue = arr[i]


# 방법_2
minValue = arr[0] # 초기값 설정

for i in range(1, len(arr)):
    if arr[i] < minValue:
        minValue = arr[i]

# 방법_3
minValue = float('inf') # 최댓값을 설정

for x in arr:
    if x < minValue:
        minValue = x


# print
print('minimum value is', minValue)