# Making MyLinkedList Class
class Node():
    def __init__ (self, data):
        self.data = data
        self.next = None
    
class MyLinkedList():
    def __init__ (self):
        self.head = None
    
    def add(self, data):
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
    
    def printLinkedList(self):
        current = self.head
        while current is not None:
            print(current.data, end= " -> ")
            current = current.next  
        print("End")


list = MyLinkedList()
list.add(0)
list.add(1)
list.add(2)
list.add(3)
list.add(4)

list.printLinkedList()
