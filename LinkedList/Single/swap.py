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

current = head

# 0 -> 1-> 2 -> 3 -> 4
# swap(1,3)
def swap(a,b):
    point = head
    point2 = head

    for i in range(0, a):
        point = point.link

    for i in range(0, b):
        point2 = point2.link

    temp = point.data
    point.data = point2.data
    point2.data = temp

swap(1,3)

while current is not None:
    print(current.data)
    current = current.link

    
    