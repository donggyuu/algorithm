'''
어느 쇼핑몰의 아이템 데이터는 [아이템명, 관련도, 가격]로 이루어진다.
출력 조건에 해당하는 페이지의 아이템 데이터를 출력하는 프로그램을 작성하라.

예를 들어 아래의 "input values"는, 
1.관련도를 기준으로 아이템명을 오름차순으로 정렬한 후(item2, item1, item3)
2.한 페이지에 2아이템씩 할당 후 (0페이지:item2,item1, 1페이지:item3)
3.1페이지에 해당하는 아이템을 전부 출력 -> item3이 출력됨
이므로 최종 item3을 return하게 된다.
'''
# TODO : 아래 만족 못하는 데이터를 만족하도록 수정이 필요

########## input values ##########
# 아이템명, 관련도, 가격
# TODO : 현재 코드는 이 테스트 데이터를 만족못함, item3,4가 나와야 하는데 item3만 나옴
# items = [['item1', '10', '15'], ['item2', '3', '4'], ['item3', '17', '8'], ['item4', '19', '8'], ['item5', '22', '8']]
items = [['item1', '10', '15'], ['item2', '3', '4'], ['item3', '17', '8']]
orderBy = 1 #관련도 기준
orderDirection = 0 # 오름차순 //1은 내림차순
# ------------------------------------------------
pageSize = 2 # 한페이지에 2 아이템
pageNumber = 1 # 출력 페이지 num  ## 2*i 이런식응로 출력하면 됨.
##################################


# String -> int (문자열을 그대로 비교할 수 없으니...)
# DB에 저장할 때부터 int로 했어야 하지 않앗을까?
totalItems = len(items)
for i in range(totalItems):
    for _ in range(3):
        items[i][1] = int(items[i][1])
        items[i][2] = int(items[i][2])

# Sort
if orderBy == 0:
    if orderDirection == 0:
        items.sort(key=lambda x: x[orderBy])
    elif orderDirection == 1:
        items.sort(key=lambda x: x[orderBy], reverse=True)

elif orderBy == 1:
    if orderDirection == 0:
        items.sort(key=lambda x: x[orderBy])
    elif orderDirection == 1:
        items.sort(key=lambda x: x[orderBy], reverse=True)

elif orderBy == 2:
    if orderDirection == 0:
        items.sort(key=lambda x: x[orderBy])
    elif orderDirection == 1:
        items.sort(key=lambda x: x[orderBy], reverse=True)

# Print
# pageSize = 2 # 한페이지에 2 아이템
# pageNumber = 1 # 출력 페이지 num  ## 2*i 이런식응로 출력하면 됨
startItem = pageSize*pageNumber
diffNum = totalItems % pageSize
endItem = startItem + diffNum

print('startItem', startItem)
print('endItem', endItem)
print('diffNum', diffNum)
# endItem = pageSize*(pageNumber+1)
# print("totla", totalItems)

result = []
# for i in range(startItem, endItem+1):
for i in range(startItem, endItem):
    result.append(items[i][0])

print(result)
