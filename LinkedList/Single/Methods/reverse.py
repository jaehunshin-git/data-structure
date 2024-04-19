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
        nextCurrent = current.link
        current.link = prevCurrent
        prevCurrent = current
        current = nextCurrent
    
    head = prevCurrent
    return head

head = reverse(head)
current = head
while current is not None:
    print(current.data)
    current = current.link

