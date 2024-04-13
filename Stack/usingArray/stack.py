class Stack:
    def __init__(self, full):
        self.full = full
        self.items = []

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    
    def push(self, element):
        if self.isStackFull():
            print("Stack is full. Cannot push element anymore.")
        else:
            self.items.append(element)

    def pop(self):
        if self.isEmpty():
            print("There is no element to pop.")
        else:
            self.items.pop()
        
    def peek(self):
        if self.isEmpty():
            print("There is no elements to peek")
        else:
            return self.items[-1]
        
    def size(self):
        return len(self.items)
    
    def isStackFull(self):
        if len(self.items) == self.full:
            return True
        else:
            return False
    
    def printStack(self):
        i = self.size() - 1
        while (i >= 0):
            print(self.items[i])
            i -= 1

stack = Stack(10)

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)

stack.printStack()

print("")
#print(stack.peek())
#stack.pop()
stack.printStack()

print(stack.isStackFull())

stack.push(8)
stack.push(9)
stack.push(10)
print(stack.isStackFull())

stack.push(11)


        

    
        