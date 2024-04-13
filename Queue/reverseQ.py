class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self, full):
        self.full = full
        self.pushCount = 0
        self.top = None
    
    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
        
    def push(self, data):
        if self.pushCount < self.full:
            self.pushCount += 1
            newNode = Node(data)
            newNode.next = self.top
            self.top = newNode
        else:
            print("Stack is full. Cannot push element anymore.")
            return

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty. There is nothing to pop.")
            return
        else:
            top = self.top
            self.top = self.top.next
            return top
        
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty. There is nothing to peek.")
            return
        else:
            return self.top
    
    
    def printLinkedList(self):
        ptr = self.top

        if(self.isEmpty): print("Empty")
        while ptr is not None:
            print(ptr.data, end=" -> ")
            ptr = ptr.next
        print("none")

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

    def reverseQ(self):
        stack = Stack(len(self))

        current = self.front
        while current is not None:
            stack.push(current.data)
            current = current.next

        self.front = self.rear = stack.pop()
        while(stack.isEmpty() == False):
            self.rear.next = stack.pop()
            self.rear = self.rear.next

        stack.printLinkedList()


# Example usage:
q = Queue(10)

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.enqueue(10)

print("Queue:")
q.printQueue()

q.reverseQ()
q.printQueue()

q.dequeue()
q.printQueue()

q.enqueue(20)
q.printQueue()