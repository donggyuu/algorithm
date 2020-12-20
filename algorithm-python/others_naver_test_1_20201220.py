'''
높이를 원소로 가지는 리스트가 주어진다. 
개구리 a와 b가 있고, 리스트의 i번째 원소를 기준으로 각각 왼쪽과 오른쪽으로 점프를 뛴다.
(단, 현재 위치보다 높은 위치로만 점프가 가능하다)
이때 두 개구리의 최대 거리를 구하시오.

**
예를 들어,
리스트 -> [1, 5, 5, 2, 6]  가 주어지면

4번째 원소 2를 출발 지점으로 개구리들은 왼쪽과 오른쪽으로 점프를 한다.
최종 위치는 a가 2번쨰 원소인 5, b가 5번쨰 원소인 6이므로,
두 개구리의 최대 거리는 (5-2)+1 = 6 이다.
'''

blocks = [1, 5, 5, 2, 6] # test data
# blocks = [1, 1] # test data
res = []

for i in range(len(blocks)):

    left = 0   # a개구리의 최종 위치
    right = 0  # b개구리의 최종 위치
    lCount = 1 # 왼쪽으로 뛸 대마다 1씩 증가
    rCount = 1 # 오른쪽으로 뛸 대마다 1씩 증가

    while i - lCount >= 0: # 왼쪽으로 뛰어도 적어도 첫번쨰 원소 이상이어야 
        if blocks[i - lCount] >= blocks[i - lCount+1]: # 직전 위치보다 높은 원소여야 점프 가능
            left = i - lCount
            lCount += 1
        else:
            break

    while i + rCount < len(blocks):  # 오른쪽으로 뛰어도 적어도 첫번쨰 원소 이상이어야 
        if blocks[i + rCount] >= blocks[i + rCount-1]: # 직전 위치보다 높은 원소여야 점프 가능
            right = i + rCount
            rCount +=1
        else:
            break

    res.append(abs(left-right)+1)

print(max(res)) # 최대 거리를 출력
