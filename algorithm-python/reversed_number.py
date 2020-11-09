'''
입력받은 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램을 작성하시오.
- 예로, 32를 뒤집으면 23이고 23은 소수이므로 출력한다. 
- 단 910를 뒤집으면 19로 숫자화 한다(첫 자리부터의 연속된 0은 무시한다)

** input
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
각 자연수의 크기는 100,000를 넘지 않는다.
** output
첫 줄에 뒤집은 소수를 출력합니다. 출력순서는 입력된 순서대로 출력한다.

** input_ex
5
32 55 62 3700 250
** output_ex
23 73

'''

# 뒤집는 함수인 def reverse(x) 와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성하 여 프로그래밍 한다.

n = int(input())
nList = list(map(int, input().split()))

reversed_list = []

# 맨 뒤부터 나머지로 얻는다


def reverse_function(number):
    res = 0
    while number > 0:
        # 맨 뒤 구하기
        t = number % 10

        # 맨 뒤 값 더하기. 결과값에다가!
        # 결과값을 res로 따로 선언하는게 편함.
        res = res * 10 + t

        # 맨 뒤의 값은 활용 완료니까 제외한다.
        number = number // 10

    return res

print('find last val', reverse_function(nList[0]))