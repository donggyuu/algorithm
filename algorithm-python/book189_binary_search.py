## by recursion
def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    # 찾고자 하는 값이 mid 보다 작은 경우
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid + 1, end)


## by loop
def binary_search_by_loop(array, target, start, end):

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

# ------------------------------------------

# input
n, target = map(int, input().split())
array = list(map(int, input().split()))

# execute bibary search
result = binary_search(array, target, 0, n-1)

if result == None:
    print("원소 존재 안함")
else:
    print(result+1) #n번째이기에 +1을 해줌
