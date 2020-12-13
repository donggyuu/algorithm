# 삽입 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # i부터 1까지 감소하는 문법

        # 한 칸씩 왼쪽으로 이동
        # i의 좌측은 이미 정렬된 상태
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else: # 본인보다 작은 데이터를 만나면 멈춤. 왜냐면 좌측은 이미 정렬된 상태이니까
            break

print(array)