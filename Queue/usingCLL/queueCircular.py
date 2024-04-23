class Node():
    def __init__ (self, data):
        self.data = data
        self.next = None

class Queue():
    def __init__ (self, full):
        self.full = full
        self.front = None
        self.rear = None
        self.count = 0

    def isFull(self):
        if self.count >= self.full:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.front is None:
            return True
        else:
            return False
        
    def enqueue(self, data):
        if self.isFull():
            print("Queue is full. Cannot enqueue anymore.")
            return
        
        newNode = Node(data)
        if self.isEmpty():
            self.front = self.rear = newNode
            newNode.next = self.front
        elif self.front is self.rear:
            self.front.next = newNode
            self.rear = newNode
            newNode.next =  self.front
        else:
            self.rear.next = newNode
            self.rear = newNode
            newNode.next = self.front
        
        self.count += 1
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty. Nothing to dequeue.")
            return
        else:
            target = self.front
            self.front = self.front.next
            self.rear.next = self.front
            self.count -= 1
            return target
    
    def enqueueFront(self, data):
        if self.isFull():
            print("Queue is full. Cannot enqueue anymore.")
            return
        else:
            newNode = Node(data)
            newNode.next = self.front
            self.front = newNode
            self.rear.next = newNode
            self.count += 1

    def dequeueRear(self):
        if self.isEmpty():
            print("Queue is empty. Nothing to dequeue.")
            return
        
        if self.count == 1:
            self.front = self.rear = None
            self.count -= 1
        else:
            #find the second node from the rear
            current = self.front
            while current.next.next is not self.front:
                current = current.next
            self.rear = current
            current.next = self.front
            self.count -= 1
        
    def printQueue(self):
        if self.isEmpty():
            print("Queue is Empty. Nothing to print.")        
            return
        
        current = self.front
        while current is not self.rear:
            print(current.data)
            current = current.next
        print(current.data)

q = Queue(5)
q.enqueue(0)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

q.dequeueRear()
q.dequeueRear()

q.printQueue()