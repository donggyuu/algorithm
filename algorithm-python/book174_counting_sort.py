# 계수 정렬
# 0~max array까지 설정해두고, 정렬할 원소에 해당하는 인덱스 값을 1씩 증가시키는 방식

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8, 0]

count = [0] * (max(array) + 1) # 이후 for문활용을 위해 미리 +1 해둔다

# 해당하면 하나씩 증가시킨다.

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for _ in range(count[i]): # count[i]==0이면, 해당위치의 원소는 없으니까 출력 안한다
        print(i, end=' ')
