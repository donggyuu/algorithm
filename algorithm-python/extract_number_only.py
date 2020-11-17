'''
숫자만 추출하여 그 순서대로 자연수를 만들고, 자연수와 그 자연수의 약수 개수를 출력한다.
만약 “t0e0a1c2h0er”에서 숫자만 추출하면 0, 0, 1, 2, 0이고 이것을 자연수를 만들면 120이 됩니다.
즉첫자리0은자연수화할때무시합니다. 출력은120를출력하고,다음줄에120의 약수의 개수를 출력하면 됩니다.
추출하여 만들어지는 자연수는 100,000,000을 넘지 않습니다.

**input
g0en2Ts8eSoft

**output
28
6
'''

# -----------------------------------
# isdecimal, isdigit의 차이
# -> https://it-neicebee.tistory.com/33

# 다른 풀이 -> isdecimal 사용, 각 if문에서 int()
s = input()
res = 0

for x in s:
    if x.isdecimal():
        # 원래 있던 res는 한 digit up해야해서 *10
        res = res*10 + int(x)

print(res)


# -----------------------------------
나의 풀이 -> isdigit을 이용

stringNatural = ""

# get number
inputString = input()
for x in inputString:
    if x.isdigit():
        stringNatural += x

# change number to int
numNatural = int(stringNatural)

# get divisor
numDiv = 0
for i in range(1, numNatural+1):
    if numNatural%i == 0:
        numDiv += 1        

# print
print(numNatural)
print(numDiv)