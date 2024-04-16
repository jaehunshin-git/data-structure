# swap() method using doubly linked list queue

class Node():
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None

class Queue():
    def __init__(self, full):
        self.full = full
        self.front = None
        self.rear = None

    def enqueueRear(self, data):
        newNode = Node(data)
        if self.front is None:
            self.front = self.rear = newNode
        else:
            self.rear.right = newNode
            newNode.left = self.rear
            self.rear = newNode
    
    def isEmpty(self):
        if self.front is None:
            return True
        else:
            return False
    
    def dequeueFront(self):
        if self.isEmpty():
            print("There is nothing to dequeue.")
            return
        else:
            firstElement = self.front
            secondElement = self.front.right
            self.front.right = None
            self.front.right.left = None
            self.front = self.front.right
            return firstElement
        
    def printQueue(self):
        current = self.front
        while current is not None:
            print(current.data, end= " <--> ")
            current = current.right
        print("None")

    # swap data of data1 & data2 index 
    def swap(self, data1, data2):
        current1 = self.front
        for i in range(0,data1):
            current1 = current1.right
        
        current2 = self.front
        for i in range(0, data2):
            current2 = current2.right

        current1.data, current2.data = current2.data, current1.data




q = Queue(5)
q.enqueueRear(0)
q.enqueueRear(1)
q.enqueueRear(2)
q.enqueueRear(3)
q.enqueueRear(4)
q.swap(2,4)

q.printQueue()