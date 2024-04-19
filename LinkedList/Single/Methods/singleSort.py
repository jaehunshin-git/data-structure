class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

n0 = Node(3)
n1 = Node(5)
n2 = Node(10)
n3 = Node(21)

ptr1 = n0
n0.next = n1
n1.next = n2
n2.next = n3

s0 = Node(4)
s1 = Node(6)
s2 = Node(15)
s3 = Node(26)
s4 = Node(33)

ptr2 = s0
s0.next = s1
s1.next = s2
s2.next = s3
s3.next = s4

# printing single linked list with arrow.
def printList(node):
    while node is not None:
        print(node.data, end=" -> ")
        node = node.next
    print("None")

# function that returns single linked list's length.
def listLen(ptr):
    i = 0;
    while ptr is not None:
        i += 1
        ptr = ptr.next

    return i


print(listLen(ptr1))
print("")
printList(ptr1)
print("")
print(listLen(ptr2))
print("")
printList(ptr2)



def mergeSort(ptr1, ptr2):
    
    # if one of the ptr is empty return another ptr.
    if ptr1 is None:
        return ptr2
    elif ptr2 is None:
        return ptr1
    
    # not creating new head Node() method. Make the first finalPtr.
    if (ptr1.data <= ptr2.data):
        head = ptr1
        ptr1 = ptr1.next
    else:
        head = ptr2
        ptr2 = ptr2.next

    current = head

    # while loop for the connection of two single linked list.
    while ptr1 is not None and ptr2 is not None:
        if ptr1.data <= ptr2.data:
            current.next = ptr1
            ptr1 = ptr1.next
        else:
            current.next = ptr2
            ptr2 = ptr2.next

        current = current.next

    #  If any elements remaining in list1 or list2, append them to the merged list
    if ptr1 is not None:
        current.next = ptr1
    elif ptr2 is not None:
        current.next = ptr2

    # return mergeSorted list
    return head

head = mergeSort(ptr1, ptr2)
print("")
printList(head)


