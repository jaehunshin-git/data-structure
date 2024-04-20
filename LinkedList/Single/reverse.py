    class Node():
    def __init__(self):
        self.data = None
        self.link = None


n0 = Node()
n1 = Node()
n2 = Node()
n3 = Node()
n4 = Node()

n0.data = 1
n1.data = 2
n2.data = 3
n3.data = 4
n4.data = 5

n0.link = n1
n1.link = n2
n2.link = n3
n3.link = n4

head = n0

def reverse(head):
    current = head
    prevCurrent = None

    while current is not None:
        nextCurrent = current.link  // 다음 노드를 임시 저장 -> 다음 줄에서 현재 노드의 link 화살표가 변경되기 때문
        current.link = prevCurrent  // 현재 노드의 link 를 이전 노드와 연결
        prevCurrent = current   // 다음 반복문에 넘어갔을 때 현재 current는 prevCurrent 이다.
        current = nextCurrent   // 다음 노드로 넘어가기 위한 코드
    
    head = prevCurrent
    return head

head = reverse(head)
current = head
while current is not None:
    print(current.data)
    current = current.link

