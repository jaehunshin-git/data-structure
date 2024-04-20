class Node():
    def __init__ (self, data):
        self.data = data
        self.next = None

class Stack():
    def __init__ (self, full):
        self.full = full
        self.top = None
        self.count = 0
    
    def isFull(self):
        if self.count >= self.full:
            return true
        else:
            return False
        
    def push(self, data):
        if self.isFull():
            print("Stack is full. Cannot push anymore.")
            return
        else:
            newNode = Node(data)
            if self.count == 0:
                self.top = newNode
            else:
                newNode.next = self.top
                self.top = newNode
            self.count += 1

    def isEmpty(self):
        if (self.count == 0) or (self.top is None):
            return True
        else:
            return False
        
    def pop(self):
        if self.isEmpty():
            print("Stack is empty. Cannot pop anymore.")
            return
        else:
            if self.count == 1:
                self.top = None
            else:
                temp = self.top.next
                self.top.next = None
                self.top = temp
            self.count -= 1

    def peek(self):
        if self.isEmpty():
            print("Stack is Empty. Nothing to peek")
            return -1
        else:
            return self.top.data
        
    def printStack(self):
        if self.isEmpty():
            print("Stack is Empty. Nothing to print")
            return
        else:
            current = self.top
            while current is not None:
                print(current.data, end= " -> ")
                current = current.next
            print("End")

# Don't work with the Korean string input.
def checkPalindrome(str):
        tempStack = Stack(len(str))
        if len(str) % 2 == 0:
            for i in str:
                if tempStack.peek() == i:
                    tempStack.pop()
                    continue
                
                tempStack.push(i)
        else:
            mid = str[len(str)//2]
            for i in str:
                if i is mid:
                    continue
                if tempStack.peek() == i:
                    tempStack.pop()
                    continue
                
                tempStack.push(i)
        
        if tempStack.count == 1 or tempStack.count == 0:
            return True
        else:
            return False

str = str(input())
print(checkPalindrome(str))