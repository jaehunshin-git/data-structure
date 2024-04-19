# Making MyLinkedList Class
class Node():
    def __init__ (self, data):
        self.data = data
        self.next = None
    
class MyLinkedList():
    def __init__ (self):
        self.head = None
        self.countNode = 0
    
    # add new node to the tail of linked list.
    def add(self, data):
        self.countNode +=1
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
            
    # add new node to the index
    # when index is out of the range, then print execption.
    def insert(self, data, index):
        if index > self.countNode:
            print("Invalid index.")
            return
        
        newNode = Node(data)
        current = self.head
        for i in range(0, index-1):
            current = current.next
        
        if current.next is None:
            current.next = newNode
        else:
            nextNode = current.next
            current.next = newNode
            newNode.next = nextNode
    
    # delete the node which is located in the index. 
    def delete(self, index):
        current = self.head
        
        if current is None:
            print("Linked List is Empty. There is Nothing to delete.")
            return
        if index >= self.countNode:
            print("Invalid index.")
            return
        
        if index == 0:
            self.head = self.head.next
        else:
            for i in range(0,index-1):
                current = current.next
            nextNode = current.next.next
            current.next = nextNode
    
    # Return true when the data is in the list, if not return false.
    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        
        return False
    
    # return the index when the data is in the linked list.
    # when the data is not in the list return -1
    def index(self, data):
        current = self.head
        for i in range(0, self.countNode):
            if current.data == data:
                return i
            current = current.next
        
        return -1
    
    # swap nodes' data
    def swap(self, a, b):
        if (0 <= a and a < self.countNode) and (0<= b and b < self.countNode):
            current = self.head
            temp1 = temp2 = None
            while current is not None:
                if current.data == a:
                    temp1 = current
                if current.data == b:
                    temp2 = current
                current = current.next
            temp1.data, temp2.data = temp2.data, temp1.data
        else:
            print("Invalid index of parameters.")
            return
    
    def reverse(self):
        current = self.head
        prevCurrent = None
        while current is not None:
            nextCurrent = current.next
            current.next = prevCurrent
            prevCurrent = current
            current = nextCurrent
        self.head = prevCurrent
         
    # print all nodes in the linked list.
    def printLinkedList(self):
        current = self.head
        if current is None:
            print("Liked List is Empty.")
        else:
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

list.reverse()
list.printLinkedList()