'''
어느 회의에 대하여,
각 회의의 시작시간과 각 회의의 발표 시간이 주어질 때,
최대로 가능한 회의의 회수를 구하라.
'''
# TODO : getMaxSession()는 왜 test_data_2를 만족못하는지 원인 파악
# TODO : 

# test_data_1
# 회의1은 1시에 시작, 2시간 소요 / 회의2는 3시에 시작, 2시간 소요 / ...
# start_time = [1, 3, 3, 5, 7]
# running_time = [2, 2, 1, 2, 1]

# test_data_2
start_time = [1, 1, 1, 1, 4]
running_time = [10, 3, 6, 4, 2]


def getMaxSession(start_time, running_time):
    # TODO
    '''
    start_time = [1, 1, 1, 1, 4]
    running_time = [10, 3, 6, 4, 2]
    일 떄, 2가 기대지만, 여기선 1이 나온다. 왜지?
    '''
    
    session = []
    
    for i in range(len(start_time)):
        session.append([])
        session[i].append(start_time[i])
        session[i].append(start_time[i]+running_time[i])
    
    count = 0
    start = 0
    for time in session:
        if time[0] >= start:
            start = time[1]
            count += 1
    
    return count


N = 5
session = []
    
# 참고 : https://hyeon9mak.github.io/python/Python-%EB%B0%B1%EC%A4%80-1931/
# TODO 개선이 필요(원래 주어진 것을 새로 바꾸는 것은 리소스 잡아먹으니 비추야...)
for i in range(len(start_time)):
    session.append([])
    session[i].append(start_time[i])
    session[i].append(start_time[i]+running_time[i])

session = sorted(sorted(session), key=lambda x: x[1])
count = 0
front_end = 0
for start, end in session:
    if start >= front_end:
        count += 1
        front_end = end
        
print(count)
