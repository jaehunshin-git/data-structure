class Node():
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

n0 = Node()
n1 = Node()
n2 = Node()
n3 = Node()
n4 = Node()

head = n0
tail = n4
n0.right = n1
n1.right = n2
n2.right = n3
n3.right = n4

n4.left = n3
n3.left = n2
n2.left = n1
n1.left = n0

n0.data = "a"
n1.data = "b"
n2.data = "c"
n3.data = "d"
n4.data = "e"

current = head
while current is not None:
    print(current.data)
    current = current.right
print("")
current = tail
while current is not None:
    print(current.data)
    current = current.left
