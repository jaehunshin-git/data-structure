class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_sort_linked_list(head):
    # Base case: If the list is empty or has only one element, it's already sorted
    if head is None or head.next is None:
        return head
    
    # Find the middle of the list
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None  # Split the list into two halves
    
    # Recursively sort the two halves
    left_half = merge_sort_linked_list(head)
    right_half = merge_sort_linked_list(next_to_middle)
    
    # Merge the sorted halves
    sorted_list = merge(left_half, right_half)
    
    return sorted_list

def get_middle(head):
    if head is None:
        return head
    
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(left, right):
    # Create a dummy node to serve as the head of the merged list
    dummy = Node(0)
    current = dummy
    
    # Merge the two sorted lists
    while left and right:
        if left.data < right.data:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next
    
    # Append any remaining nodes from either list
    if left:
        current.next = left
    if right:
        current.next = right
    
    # Return the head of the merged list (excluding the dummy node)
    return dummy.next

# Helper function to print linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Example usage:
head = Node(3)
head.next = Node(1)
head.next.next = Node(5)
head.next.next.next = Node(2)
head.next.next.next.next = Node(4)

print("Original linked list:")
print_linked_list(head)

sorted_head = merge_sort_linked_list(head)
print("\nSorted linked list:")
print_linked_list(sorted_head)

