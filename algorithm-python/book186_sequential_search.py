
# n:원소의 개수
# target:찾고자 하는 문자열
# array: n만큼 입력할 문자열
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인해 간다
    for i in range(n):
        if array[i] == target:
            return i+1 #몇 번째인지 위치 반환(index는 0부터 시작이니 1더함)

# ---------------------------------------
print("생성할 원소 개수와 찾을 문자열을 입력하시오(ex. 5 donggyu )")
input_data = input().split()

n = int(input_data[0])
target = input_data[1]

print("원소 개수만큼 문자열을 입력하세요(ex. david donggyu lee ken abc)")
array = input().split()

print(sequential_search(n, target, array))
