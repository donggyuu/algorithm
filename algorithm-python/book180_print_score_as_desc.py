'''
이름과 성적이 주어졌을 때, 성적이 낮은 순서대로 출력하는 프로그램을 작성하여라.

**input
첫 줄에는 학생의 수 입력된다.

2
홍길동 95
이순신 77

**output
이순신 홍길동
'''

n = int(input())
studentList = []

for _ in range(n):
    input_data = input().split()
    studentList.append((input_data[0], int(input_data[1])))

studentList = sorted(studentList, key=lambda student: student[1])

for student in studentList:
    print(student[0], end=' ')
