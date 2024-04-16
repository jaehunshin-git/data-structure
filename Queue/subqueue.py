class DoubleNode:
    def __init__ (self, data):
        self.data = data
        self.right = None
        self.left = None

class SingleNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class ArrayStack():
    def __init__ (self, full):
        self.items = []
        self.full = full
        self.pushCount = 0
        self.top = None
    
    def isFull(self):
        if len(self) == self.full:
            return True
        else:
            return False
        
    def push(self, data):
        if self.isFull():
            print("Stack is full. Cannot push anymore. Pop to push.")
            return
        else:
            self.items.append(data)
            self.top = self.items[-1]
            self.pushCount += 1
        
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty. Nothing to pop. Push to pop.")
            return
        else:
            self.top = None
            del self.items[-1]
            self.top = self.items[-1]

    def peek(self):
        return self.top
    
    def __len__(self):
        return self.pushCount
    
    def isEmpty(self):
        if len(self) == 0:
            return True
        else:
            return False
    
    
    
class LinkedListStack():
    def __init__ (self, full):
        self.full = full
        self.top = None
    
    def push(self, data):
        newNode = DoubleNode(data)
        if self.top is None:
            self.top = newNode
        else:
            newNode.right = self.top
            self.top.left = newNode
            self.top = newNode
    
    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False
        
    def pop(self):
        if self.isEmpty():
            print("There is nothing to pop. Stack is Empty")
            return
        else:
            tempTop = self.top
            self.top = self.top.right
            return tempTop
        
class Queue():
    def __init__ (self, full):
        self.full = full
        self.front = None
        self.rear = None
        self.count = 0

    def enqueueRear(self, data):
        newNode = DoubleNode(data)
        if self.isEmpty():
            self.front = self.rear = newNode
        else:
            self.rear.right = newNode
            newNode.left = self.rear
            self.rear = newNode
        self.count += 1

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
            self.front = secondElement
            self.count -= 1
            return firstElement
        
    def printQueue(self):
        if self.isEmpty():
            print("Queue is Empty. Nothing to print.")
            return
        else:
            current = self.front
            while current is not None:
                print(current.data, end= " <--> ")
                current = current.right
            print("None")

    def __len__ (self):
        return self.count
    
    def subqueue(self, q1, q2):
        if len(q1) >= len(q2):
            stack = ArrayStack(len(q2))
            current = q2.front
            
            while current is not None:
                stack.push(current.data)
                current = current.right
            current = q1.front
            


        # 일단 시간복잡도 고려하지 않고 코딩하고 나서 리팩토링 해보자!
        # 스택을 사용하는 방법
        # 스택을 사용하지 않는 방법
        
                        
                                        
        


q = Queue(5)
q.enqueueRear(0)
q.enqueueRear(1)
q.enqueueRear(2)
q.enqueueRear(3)
q.enqueueRear(4)

q.printQueue()

