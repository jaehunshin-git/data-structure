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

head = n0

n0.link = n1
n1.link = n2
n2.link = n3
n3.link = n4


# 0 -> 1 -> 2 -> 3 -> 4
#(위치, 값)
def insert(a,b):
    temp = Node()
    temp.data = b
    current = head

    for i in range(0,a-1):
        current = current.link
    
    temp.link = current.link
    current.link = temp

insert(2, 888)

current = head
# linked list 확인 출력
while current is not None:
   print(current.data)
   current = current.link

