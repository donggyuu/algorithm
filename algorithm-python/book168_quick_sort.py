# 삽입 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    
    if start >= end: #원소 1개이면 종료
        return
    
    pivot = start # 첫 원소를 pivot으로 설정
    left = start+1
    right = end
    while left <= right: # 좌,우 교차될 때 까지 반복
        # 피봇보다 큰 것 찾을때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
         
        # 피봇보다 작은 것 찾을때까지 반복
        # start는 피봇이니까 >=이 아니고 >
        while right > start and array[right] >= array[pivot]:
            right -= 1
        
        if left > right: # 엇갈렸다면 피벗과 작은 데이터를 교체
            array[right], array[pivot] = array[pivot], array[right]
        
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]

        # 2파트로 나누어지면 반복적으로 수행한다
        quick_sort(array, start, right-1)
        quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)

