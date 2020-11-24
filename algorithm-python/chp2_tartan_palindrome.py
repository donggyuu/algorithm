'''
1부터 9까지의 자연수로 채워진 7x7 격자판이 주어지면
격자판 위에서 가로방향 또는 세로방향으로 길이 5자리 회문수가 몇 개 있는지 구하는 프로그램을 작성하세요.

회문수란 121과 같이 앞에서부터 읽으나 뒤에서부터 읽으나 같은 수를 말합니다.

그림 : https://cheeseb.github.io/algorithm/algorithm-numOfPalindrome/

빨간색처럼 구부러진 경우(87178)는 회문수로 간주하지 않습니다.

**input
2 4 1 5 3 2 6
3 5 1 8 7 1 7
8 3 2 7 1 3 8
6 1 2 3 2 1 1
1 3 1 3 5 3 2
1 1 2 5 6 5 2
1 2 2 2 2 1 5

**output
3

'''
# point_1 행은 ::-1로 역방향 순회 가능
# point_2 열은 ::-1을 못쓰니, 인덱스로 직접 접근해서 원하는 작업한다

input = [list(map(int, input().split())) for _ in range(7)]
count = 0

### 행 기준해서 회문 체크
# 길이가 5니까, 행 시작은 0,1,2까지(range 3) 돈다
for i in range(3):
    # 총 7열이니까 7바퀴 돈다.
    for j in range(7):
        temp = input[j][i:i+5] # ex. [1][1:6]
        if temp == temp[::-1]:
            count += 1

        ### 열 기준해서 회문 체열
        ### j for문을 다시 뺴고싶지 않기 때문에 그냥 좀 중복 있어도 한번에 처리하자.
        # [1,2,3,4,5]이면 (1,5),(2,4) 이렇게 비교. 
        # 뒤에서부터 5,4 즉 2회에 해당하는 원소를 끄집어내야해서 range(2)
        for k in range(2):
            if input[i+k][j] != input[i+5-k-1][j]:
                break
        else:
            count += 1

print(count)
