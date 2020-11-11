'''
**문제
N개의 숫자로 이루어진 숫자열이 주어진다.
해당 숫자열중에서 s번째부터 e번째 까지의 수를 오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하시오.

**상세
각 케이스별
첫 번째 줄은 자연수 N(5<=N<=500), s, e, k가 차례로 주어진다.
두 번째 줄에 N개의 숫자가 차례로 주어진다.

*** input
2  //총 테스트 케이스 개수
6 2 5 3
5 2 7 3 8 9
15 3 10 3
4 15 8 16 6 6 17 3 10 11 18 7 14 7 15
*** output
#1 7
#2 6
'''

# 총 테스트 케이스 개수 입력
T = int(input())

for t in range(T):
    n, s, e, k = map(int, input().split())
    inputList = list(map(int, input().split()))

    # 리스트 필터링&정렬
    inputList = inputList[s-1:e]
    inputList.sort()
    
    print("#%d %d" %(t+1, inputList[k-1]))