'''
스도쿠는 매우 간단한 숫자 퍼즐이다.
9×9 크기의 보드가 있을 때, 각 행과 각 열, 그리고 9 개의 3×3 크기의 보드에 1부터 9까지의 숫자가 중복 없이 나타나도록 보드를 채우면 된다.
예를 들어 다음을 보자.

문제 전문 : https://cheeseb.github.io/algorithm/algorithm-sudoku/

위 그림은 스도쿠를 정확하게 푼 경우이다.
각 행에 1부터 9까지의 숫자가 중복 없이 나오고, 각 열에 1부터 9까지의 숫자가 중복 없이 나오고, 각 3×3짜리 사각형(9개이며, 위에서 색깔로 표시되었다)에 1부터 9까지의 숫자가 중복 없이 나오기 때문이다.
완성된 9×9 크기의 스도쿠가 주어지면 정확하게 풀었으면 “YES”, 잘 못 풀었으면 “NO”를 출력하는 프로그램을 작성하세요.

**input
1 4 3 6 2 8 5 7 9
5 7 2 1 3 9 4 6 8
9 8 6 7 5 4 2 3 1
3 9 1 5 4 2 7 8 6
4 6 8 9 1 7 3 5 2
7 2 5 8 6 3 9 1 4
2 3 7 4 8 1 6 9 5
6 1 9 2 7 5 8 4 3
8 5 4 3 9 6 1 2 7

** output
YES
'''

# CheckList를 만들어, 확인했으면 1을 넣는다.
# point_1 : 전체 행, 열을 도는 방법
# point_2 : 3x3의 각 그룹을 도는 방법 -> 행,열의 시작점을 잘 해야.

def isSudoku(input):

    # 9x9의 행, 열 체크
    for i in range(9):
        checkRow = [0]*10 # 행 체크용, *9를 해도 될듯
        checkCol = [0]*10 # 열 체크용
        for j in range(9):
            checkRow[input[i][j]] = 1
            checkCol[input[j][i]] = 1
        if sum(checkRow) != 9 or sum(checkCol) != 9:
            return False

    # 3x3(그룹)의 행, 열 체크
    ## 3x3인 그룹은 총 9개 있다.
    for i in range(3):
        for j in range(3):
            checkGroup = [0]*10 # 3x3의 한 그룹 체크
            
            ## 하나의 3x3그룹을 체크
            for m in range(3):
                for n in range(3):
                    # [해당그룹시작위치 + 각 그룹 안에서 시작위치]
                    checkGroup[input[i*3+m][j*3+n]] = 1
            if sum(checkGroup) != 9:
                return False
    return True

input = [list(map(int, input().split())) for _ in range(9)]
if isSudoku(input):
    print('YES')
else:
    print('NO')
