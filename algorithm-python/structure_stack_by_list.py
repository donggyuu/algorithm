class ListStack:
    def __init__(self):
        self.my_list = []
        # self.my_list = list()
    
    def push(self, data):
        self.my_list.append(data)
    
    def pop(self):
        return self.my_list.pop()

    # 스택 변형 없이 맨 위 값 출력
    def peek(self):
        return self.my_list[-1]
    
    def isEmpty(self):
        if len(self.my_list) == 0:
            return True
        return False


tmpStack = ListStack() # 객체 선언
tmpStack.push(1)
tmpStack.push(2)
tmpStack.push(3)
print(tmpStack.peek()) # 3이 출력됨