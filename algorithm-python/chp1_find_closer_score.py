
'''
N명 학생들의 평균(소수 첫째자리 반올림)을 구하고,
학생들중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하시오.
- 평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 출력
- 높은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 출력

** 입력설명
첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 각 학생의 수학점수인 N개의 자연 수가 주어진다. 학생의 번호는 1~N이다.
▣ 출력설명
첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다. 평균은 소수 첫째 자리에서 반올림한다.

** input
10 
45 73 66 87 92 67 75 79 75 80
** output
74 7
(평균 74에 근접한 값은 )
'''

nStudents = int(input())
scoreList = list(map(int, input().split()))

avgScore = round(sum(scoreList) / nStudents)
diffValue = 999999
resultIndex = 0

for index, value in enumerate(scoreList):
    tmp = abs(avgScore - value)

    # 차기아 가장 작은 값으로 갱신
    if diffValue > tmp:
        diffValue = tmp
        resultIndex = index+1
        resultScore = value

    # 차이가 같을 경우, 큰 숫자로 갱신
    elif diffValue == tmp:
        if value > resultScore:
            resultScore = value
            resultIndex = index+1

print(avgScore, resultIndex)
