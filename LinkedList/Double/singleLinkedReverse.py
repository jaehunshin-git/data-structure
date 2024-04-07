class Node():
    def __init__(self):
        self.data = None
        self.link = None

n0 = Node()
n1 = Node()
n2 = Node()
n3 = Node()
n4 = Node()

head = n0
n0.link = n1
n1.link = n2
n2.link = n3
n3.link = n4

n0.data = "a"
n1.data = "b"
n2.data = "c"
n3.data = "d"
n4.data = "e"

def reverse(head):
    current = head
    prev = None
    while current is not None:
        nextCurrent = current.link
        current.link = prev
        prev = current
        current = nextCurrent
    head = prev
    return head

head = reverse(head)



current = head
while current is not None:
    print(current.data)
    current = current.link