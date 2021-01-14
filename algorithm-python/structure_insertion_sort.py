'''
삽입정렬
데이터를 하나씩 확인하며, 각 테이터를 적절한 위치에 삽입
(첫 번째 데이터는 정렬되어 있다고 판단하므로 두 번째 데이터부터 시작)
'''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # i부터 1까지 감소하며 반복
        if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동하며 비교
            array[j], array[j-1] = array[j-1], array[j]
        else: # 작은 데이터를 만나면 stop
            break

print(array)