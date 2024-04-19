class Node():
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None
        
class DoubleLinkedList():
    def __init__ (self):
        self.head = None
        self.tail = None
        self.left = None
        self.right = None
        self.count = 0
        
    def add(self, data):
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            current = self.head
            while current.right is not None:
                current = current.right
            current.right = newNode
            newNode.left = current
            self.tail = newNode
        
        self.count += 1
    def pop(self):
        if self.head is None:
            print("List is empty. Nothing to pop.")
            return
        else:
            current = self.head
            # If this is Singly Linked List, have to find the second node from the tail not the last node.
            while current.right is not None:
                current = current.right
            current.left.right = None
            self.tail = current.left
            self.count -= 1
    def insert(self, data, index):
        if (index > self.count) or (index < 0):
            print("Invalid index.")
            return
        
        newNode = Node(data)
        current = self.head
        
        if index == 0:
            newNode.right = current
            current.left = newNode
            self.head = newNode
        elif index == self.count:
            while current.right is not None:
                current = current.right
            current.right = newNode
            newNode.left =current
            self.tail = newNode
        else:
            for i in range(0, index):
                current = current.right
            current.left.right = newNode
            newNode.left = current.left
            newNode.right = current
            current.left = newNode
        self.count += 1
    
    def delete(self, index):
        if (index >= self.count) or (index < 0):
            print("Invalid index.")
            return
        
        if index == 0:
            temp = self.head.right  # temp == 2nd element
            temp.left = None
            self.head.right = None
            self.head = temp
        elif index == self.count - 1:
            temp = self.tail.left    # temp == 2nd element from tail(last)
            self.tail.left = None
            temp.right = None
            self.tail = temp
        else:
            current = self.head
            for i in range(0, index):
                current = current.right
            current.left.right = current.right
            current.right.left = current.left
            current.right = current.left = None
            
        self.count -= 1
    
    def search(self, data):
        if self.head is None:
            print("Linked List is Empty. Nothing to search.")
        else:
            current = self.head
            while current is not None:
                if current.data == data:
                    return True
                else:
                    current = current.right
            return False

    def reverse(self):
        originalHead = self.head
        current = self.head
        prevCurrent = None
        while current is not None:
            nextCurrent = current.right
            current.right = prevCurrent
            prevCurrent = current
            current = nextCurrent
        self.head = prevCurrent
        self.tail = originalHead
        
    def swap(self, index1, index2):
        if (index1 < 0 or index1 >= self.count) or (index2 < 0 or index2 >= self.count):
            print("Invalid index.")
            return
        else:
            temp1 = temp2 = None
            
            current = self.head
            for i in range(0,index1):
                current = current.right
            temp1 = current
            
            current = self.head
            for i in range(0, index2):
                current = current.right
            temp2 = current
            
            temp1.data, temp2.data = temp2.data, temp1.data
            
    def printRight(self):
        if self.head is None:
            print("List is empty. Nothing to print.")
            return
        else:
            current = self.head
            while current is not None:
                print(current.data, end= " <--> ")
                current = current.right
            print("End")
            
    
    def printLeft(self):
        if self.head is None:
            print("List is empty. Nothing to print.")
            return
        else:
            current = self.tail
            while current is not None:
                print(current.data, end= " <--> ")
                current = current.left
            print("End")
            
list = DoubleLinkedList()
list.add(0)
list.add(1)
list.add(2)
list.add(3)
list.add(4)

list.swap(0,4)
list.printRight()

