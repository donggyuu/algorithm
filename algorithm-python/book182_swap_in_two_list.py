'''
두 배열은 N개의 원소로 구성되어 있다.
최대 K번의 바꿔치기 연산을 수행할 수 있다.
배열 A의 원소의 합을 최대로 하는 프로그램을 작성하시오.

예를 들어 N=5, K=3 이라면,
A = [1, 2, 5, 4, 3]
B = [5, 5, 6, 6, 5]

1_A의 원소 1과 B의 원소 6을 교환
2_A의 원소 2와 B의 원소 6을 교환
3_A의 원소 3와 B의 원소 5를 교환

이때 A의 모든 합은 26이고 이것이 정답이다.

**input
5 3
1 2 5 4 3
5 5 6 6 5

**output
26
'''
# ----- 개선 풀이 -----
# A,B비교해서 바꿀 필요가 없으면 안 바꾸겠다.
n, k = map(int, input().split())
aList = list(map(int, input().split()))
bList = list(map(int, input().split()))

aList.sort() # 오름차순 정렬
bList.sort(reverse=True) # 내림차순 정렬

for i in range(k):
    if aList[i] < bList[i]:
        aList[i], bList[i] = bList[i], aList[i]
    else:
        # A의 원소가 B보다 크거나 같으면 swap의 의미가 없으니 break
        break

print(sum(aList))



# ----- 초기 풀이 -----
n, k = map(int, input().split())
aList = list(map(int, input().split()))
bList = list(map(int, input().split()))

# 정렬
aList.sort()
bList.sort()

# 최소값과 최대값을 swap
for i in range(k):
    aList[i], bList[n-i-1] = bList[n-i-1], aList[i]

print(sum(aList))
