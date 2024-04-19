class Node():
    def __init__ (self, data):
        self.data = data
        self.next = None
    
class Stack():
    def __init__ (self, full):
        self.full = full
        self.top = None
        self.countNode = 0
        
    def isFull(self):
        if self.countNode >= self.full:
            return True
        else:
            return False
        
    def push(self, data):
        if self.isFull():
            print("Stack is full. Cannot push anymore.")
            return
        else:
            newNode = Node(data)
            newNode.next = self.top
            self.top = newNode
            self.countNode += 1
    
    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False
        
    def pop(self):
        if self.isEmpty():
            print("Stack is empty. Cannot pop anymore.")
            return
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.countNode -=1
            return temp.data
        
    def printStack(self):
        current = self.top
        while current is not None:
            print(current.data, end= " -> ")
            current = current.next
        print("End")
    
class StackArr():
    def __init__ (self, full):
        self.items = []
        self.full = full
        self.top = None
        self.count = 0
    
    def isFull(self):
        if self.count >= self.full:
            return True
        else:
            return False
        
    def push(self, data):
        if self.isFull():
            print("Stack is full.")
            return
        else:
            self.count += 1
            self.items.append(data)
            self.top = self.items[-1]
            
    def isEmpty(self):
        if self.top is None or self.count == 0:
            return True
        else:
            return False
        
    def pop(self):
        if self.isEmpty():
            print("Stack is empty.")
            return
        else:
            if len(self.items) == 1:
                self.top = None
            elif len(self.items) == 2:
                self.top = self.items[0]
            else:
                self.top = self.items[-1]
        self.count -= 1
        return self.items.pop()
            
    def printStackArr(self):
        print(self.items)
        
        
def pCheck(str):
    s = Stack(len(str))
    judge = False
    
    for i in str:
        if i == '(':
            s.push(i)
            judge = True
        elif i == ')':
            s.pop()
    
    if s.isEmpty() and judge is True:
        return True
    else:
        return False
        
# temp = str(input())
# print(pCheck(temp))

def pCheckArr(str):
    s = StackArr(len(str))
    judge = False
    
    for i in str:
        if i == '(':
            s.push(i)
            judge = True
        elif i == ')':
            s.pop()
    
    if s.isEmpty() and judge is True:
        return True
    else:
        return False

temp = str(input())
print(pCheckArr(temp))
