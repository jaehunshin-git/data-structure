class Node():
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__ (self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode

    def printList(self):
        current = self.head
        while current is not None:
            print(current.data, end= " -> ")
            current = current.next
        print("End")

list1 = LinkedList()
list1.push(3)
list1.push(5)
list1.push(10)
list1.push(21)
list1.printList()

list2 = LinkedList()
list2.push(4)
list2.push(6)
list2.push(15)
list2.push(26)
list2.push(33)
list2.printList()

#merge those two several fucking single linked list into one linked list.
#data of node must be sorted by the ascending order

def merge_sorted_lists(list1, list2):
    merged_head = Node(None)  # Dummy node to start merged list
    current = merged_head

    current1 = list1.head
    current2 = list2.head

    while current1 is not None and current2 is not None:
        if current1.data < current2.data:
            current.next = current1
            current1 = current1.next
        else:
            current.next = current2
            current2 = current2.next
        current = current.next

    # Append remaining elements of list1, if any
    if current1 is not None:
        current.next = current1

    # Append remaining elements of list2, if any
    if current2 is not None:
        current.next = current2

    # Update head of merged list to skip the dummy node
    merged_head = merged_head.next

    return merged_head

current = merge_sorted_lists(list1, list2)
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("End")
