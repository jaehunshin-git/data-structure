class Node():
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None

class Queue():
    def __init__ (self, full):
        self.front = None
        self.rear = None
        self.full = full
        self.count = 0

    def enqueue(self, data):
        if self.count >= self.full:
            print("Queue is full. Cannot enqueue anymore.")
            return
        if (self.front is None):
            newNode = Node(data)
            self.front = newNode
            self.rear = newNode
        else:
            newNode = Node(data)
            self.rear.right = newNode
            newNode.left = self.rear
            self.rear = newNode
            # self.rear = self.rear.right
        self.count += 1

    def enqueueFront(self, data):
        if (self.front is None):
            newNode = Node(data)
            self.front = newNode
            self.rear = newNode
        else:
            newNode = Node(data)
            newNode.right = self.front
            self.front.left = newNode
            self.front = newNode

    def enqueueRear(self,data):
        if self.front is None:
            newNode = Node(data)
            self.front = newNode
            self.rear = newNode
        else:
            newNode = Node(data)
            self.rear.right = newNode
            newNode.left = self.rear
            self.rear = newNode
    
    def isEmpty(self):
        if (self.front is None):
            return True
        else:
            return False
    
    def dequeue(self):
        if self.isEmpty():
            print("There is nothing to dequeue.")
            return
        else:
            firstElement = self.front
            secondElement = self.front.right
            firstElement.right = None
            secondElement.left = None
            self.front = secondElement
            return firstElement.data
        
    def  dequeueFront(self):
        if (self.front is None):
            print("There is nothing to dequeue.")
            return
        else:
            firstElement = self.front
            secondElement = self.front.right
            self.front.right = None
            secondElement.left = None
            self.front = secondElement
            return firstElement
        
    def dequeueRear(self):
        if (self.front is None):
            print("There is nothing to dequeue.")
            return
        else:
            lastElement = self.rear
            prevLastElement = self.rear.left
            prevLastElement.right = None
            self.rear.left = None
            self.rear = prevLastElement
            return lastElement

    def printQueue(self):
        current = self.front
        while current is not None:
            print(current.data, end=" <--> ")
            current = current.right
        print("None")
        print("")
    
    def __len__(self):
        return self.count

q = Queue(10)

q.enqueueFront(1)
q.enqueueFront(2)
q.enqueueRear(3)
q.dequeueRear()
q.printQueue()
# print(len(q))



        

