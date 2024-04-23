class Node():
    def __init__ (self, data):
        self.data = data
        self.next = None

class CircularLinkedList():
    def __init__ (self):
        self.head = None
    
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
        
    def push(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            newNode.next = self.head
        else:
            current = self.head
            while current.next is not self.head:
                current = current.next
            current.next = newNode
            newNode.next = self.head

    def printList(self):
        if self.isEmpty():
            print("List is empty.")
            return
        else:
            current = self.head
            print(current.data)
            current = current.next
            while current is not self.head:
                print(current.data)
                current = current.next

    def pop(self):
        current = self.head
        if self.isEmpty():
            print("LinkedList is Empty.")
            return
        elif current.next is self.head:
            current.next = None
            current.data = None
            self.head = None
        else:
            while current.next.next is not self.head:
                current = current.next
            current.next = self.head

            

    def len(self):
        current = self.head
        if current is None:
            return 0
        else:
            n = 1
            while current.next is not self.head:
                n += 1
                current = current.next

            return n
    
            

def len(list):
    current = list.head
    if current.next is list.head:
        return 1
    else:
        n = 0
        while current.next is not list.head:
            current = current.next
            n += 1
        return n + 1

            
list = CircularLinkedList()
list.push(0)

list.pop()
list.printList()
