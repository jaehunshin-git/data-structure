class Stack:
    def __init__ (self, data):
        self.data = data
        self.next = None

s0 = Stack(0)
s1 = Stack(1)
s2 = Stack(2)
s3 = Stack(3)
s4 = Stack(4)

s0.next = s1
s1.next = s2
s2.next = s3
s3.next = s4
head = s0


def printLinkedList(head):
    ptr = head

    while ptr is not None:
        print(ptr.data, end=" -> ")
        ptr = ptr.next
    print("none")

printLinkedList(head)


    
