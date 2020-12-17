class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
# head는 첫번째 노드
# 중간 삽입은 구현 X
class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, data):
        new_node = Node(data) # 삽입할 노드 생성

        if not self.head: # node가 존재하지 않는 경우
            self.head = new_node
        else:
            node = self.head # head의 위치를 파악
            while node.next: # 마지막 노드를 찾는다
                node = node.next
            node.next = new_node # 마지막 노드에 새 노드를 삽입
    
    def delete(self, data):
        node = self.head
        if node.data == data: # 노드가 head라면
            self.head = node.next # head를 None으로 설정
            del node # 노드를 삭제
        else:
            while node.next: # 삭제할 노드를 찾는다
                next_node = node.next
                if next_node.data == data:
                    node.next = next_node.next # 삭제할 노드 직전의 point를 삭제할 노드 다음으로 변경
                    del next_node
                else:
                    node = node.next # 삭제할 값이 없다면 다음 노드로 이동

    def find(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
    
    def print(self):
        node =self.head
        while node:
            print(node.data)
            node =node.next

ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.delete(2)
ll.print()
