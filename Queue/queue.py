class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Queue:
    def __init__(self, full):
        self.count = 0
        self.front = None
        self.rear = None
        self.full = full
    
    def enqueue(self, data):
        if self.isFull():
            print("Queue is full. Cannot enqueue anymore.")
            return
        
        if(self.count == 0):
            self.count += 1
            newNode = Node(data)    
            self.front = newNode
            self.rear = newNode
        else:
            self.count += 1
            newNode = Node(data)
            self.rear.next = newNode
            self.rear = newNode
    
    def isEmpty(self):
        if ((self.count == 0) or (self.front == None) or (self.rear == None)):
            return True
        else:
            return False
    
    def isFull(self):
        if self.count >= self.full:
            return True
        else:
            return False
        
    def dequeue(self):
        if(self.isEmpty()):
            print("Queue is Empty. There is nothing to dequeue.")
            return
        elif (self.count == 1):
            self.front = None
            self.rear = None
            self.count = 0
        else:
            front = self.front
            self.front = self.front.next
            return front.data
        
    def printQueue(self):
        ptr = self.front
        while (ptr is not None):
            print(ptr.data)
            ptr = ptr.next
        print("")


q = Queue(3)

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

q.printQueue()

q.dequeue()

q.printQueue()
q.dequeue()
q.dequeue()
q.printQueue()
q.dequeue()
q.printQueue()