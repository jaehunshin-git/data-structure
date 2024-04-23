# Queue with the Circular Linked List
class Node():
    def __init__ (self,data):
        self.data = data
        self.next = None

#Circular Stack
class Stack():
    def __init__ (self, full):
        self.top = None
        self.full = full
        self.count = 0

    def isFull(self):
        if self.count >= self.full:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False

    def push(self, data):
        if self.isFull():
            print("Queue is full. Cannot push anymore.")
            return
        
        newNode = Node(data)
        if self.isEmpty():
            self.top = newNode
            newNode.next = self.top
            self.count += 1
        else:
            # Find the bottom node.
            current = self.top
            while current.next is not self.top:
                current = current.next
            current.next = newNode
            newNode.next = self.top
            self.top = newNode

            self.count += 1

    def pop(self):
        if self.isEmpty():
            print("Queue is empty. Nothing to pop.")
            return
        
        if self.count == 1:
            self.top = None
            self.count -= 1
        else:
            #second node from the top
            secondNode = self.top.next
            #find the bottom node
            bottomNode = self.top
            while bottomNode.next is not self.top:
                bottomNode = bottomNode.next
            bottomNode.next = secondNode
            self.top.next = None
            self.top = secondNode
            self.count -= 1
        
    def printList(self):
        if self.isEmpty():
            print("Queue is Empty. Nothing to print")
            return
        else:
            current = self.top
            while current.next is not self.top:
                print(current.data)
                current = current.next
            print(current.data)
            
q = Stack(5)
q.push(0)
q.pop()
q.printList()