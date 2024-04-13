class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Queue:
    def __init__(self, full=None):
        self.count = 0
        self.front = None
        self.rear = None
        self.full = full
    
    def enqueue(self, data):
        if self.isFull():
            print("Queue is full. Cannot enqueue anymore.")
            return
        
        if self.count == 0:
            newNode = Node(data)    
            self.front = newNode
            self.rear = newNode
        else:
            newNode = Node(data)
            self.rear.next = newNode
            self.rear = newNode
        self.count += 1
    
    def isEmpty(self):
        return self.front is None
    
    def isFull(self):
        return self.full is not None and self.count >= self.full
        
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty. There is nothing to dequeue.")
            return
        else:
            front = self.front
            self.front = self.front.next
            self.count -= 1
            if self.front is None:
                self.rear = None
            return front.data
        
    def printQueue(self):
        current = self.front
        while current is not None:
            print(current.data)
            current = current.next
        print("")
    
    def __len__(self):
        return self.count


# Example usage:
q = Queue(3)

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)  # This should print "Queue is full. Cannot enqueue anymore."

print("Queue:")
q.printQueue()

print("Dequeue:", q.dequeue())
print("Queue:")
q.printQueue()

print("Queue size:", len(q))
