'''
정수 N이 입력되면 00시00분00초부터 N시59분59초까지 모든 시각중에서
3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오

예로 1을 입력하면 다음은 3이 하나라도 포함되어있는 경우이다
- 00시00분03초
- 00시 13분 30초

**input
5
**output
11475
'''

hour = int(input())

count = 0
for i in range(hour+1): # 0~n
    for j in range(60): # 0~59
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)
