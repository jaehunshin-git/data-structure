class Node():
    def __init__ (self):
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

def delete(index):
    current = head

    for i in range(0,index-1):
        current = current.link
    
    current.link = current.link.link

delete(3)

current = head

while current is not None:
    print(current.data)
    current = current.link