# 삽입 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):

    # 1개 이하면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0] # 첫번째 원소를 피벗
    tail = array[1:] # 피벗 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할 오른쪽 부분

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
