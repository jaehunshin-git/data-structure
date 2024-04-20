# I made palindromeCheck func and parenthesesCheck fun with the Linked List Stack
# so I'm gonna make bracketCheck func with the list in python.

class Stack():
    def __init__(self, full):
        self.items = []
        self.full = full
        self.top = None
        self.count = 0

    def isFull(self):
        if self.count >= self.full:
            print("Stack is full.")
            return  True
        else:
            return False    

    def push(self, data):
        if self.isFull():
            print("Stack is full. Cannot push anymore.")
            return
        else:
            self.items.append(data)
            self.top = self.items[-1]
            self.count += 1
        
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    
    def pop(self):
        if self.isEmpty():
            return
        else:
            del self.items[-1]

            if len(self.items) == 0:
                self.top = None
            elif len(self.items) == 1:
                self.top = self.items[0]
            else:
                self.top = self.items[-1]
            self.count -= 1
            
    def printStack(self):
        if self.isEmpty():
            print("Stack is empty. Nothing to print.")
            return
        else:
            print(self.items)

def checkBracket(str):
    bracketStack = Stack(len(str))
    judge = False
    for i in str:
        if i == ')':
            if bracketStack.top == '(':
                bracketStack.pop()
                continue
        elif i == '}':
            if bracketStack.top == '{':
                bracketStack.pop()
                continue
        elif i == ']':
            if bracketStack.top == '[':
                bracketStack.pop()
                continue
        elif i == '>':
            if bracketStack.top == '<':
                bracketStack.pop()
                continue

        if i == '(':
            bracketStack.push(i)
            judge = True
        elif i == '{':
            bracketStack.push(i)
            judge = True
        elif i == '[':
            bracketStack.push(i)
            judge = True
        elif i == '<':
            bracketStack.push(i)
            judge = True

    print(bracketStack.items)
    if (bracketStack.isEmpty()) and (judge is True):
        return True
    else:
        return False

temp = str(input())
print(checkBracket(temp))