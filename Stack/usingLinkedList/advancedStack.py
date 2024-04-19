class Node():
    def __init__ (self, data):
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
            self.pushCount -= 1
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

        while ptr is not None:
            print(ptr.data, end=" -> ")
            ptr = ptr.next
        print("none")

stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

stack.printLinkedList()

stack.pop()
stack.printLinkedList()

print(stack.peek().data)
stack.printLinkedList()



#printLinkedList(head)


    
