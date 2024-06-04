class Node():
    def __init__(self, key, value=None) -> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class MaxHeap():
    def __init__(self) -> None:
        self.root = None    

    def is_empty(self) -> bool:
        return self.root is None
    
    def insert(self, key, value=None) -> None:
        if self.is_empty():
            self.root = Node(key, value)
        else:
            self._insert_recursive(self.root, key, value)

    def _insert_recursive(self, node, key, value=None) -> None:
        if key > node.key:
            if node.right is None:
                node.right = Node(key, value)
                node.right.parent = node
                self._heapify_up(node.right)
            else:
                self._insert_recursive(node.right, key, value)
        else:
            if node.left is None:
                node.left = Node(key, value)
                node.left.parent = node
                self._heapify_up(node.left)
            else:
                self._insert_recursive(node.left, key, value)

    def _heapify_up(self, node) -> None:
        if node.parent and node.key > node.parent.key:
            node.key, node.value, node.parent.key, node.parent.value = node.parent.key, node.parent.value, node.key, node.value
            self._heapify_up(node.parent)

    # to-do list
    # 1. extract maximum
    # 2. peek maximum
    # 3. heapity down
    # 4. 

    def display(self):
        if self.is_empty():
            print("Heap is empty")
        else:
            self._display_recursive(self.root, 0)

    def _display_recursive(self, node, level):
        if node:
            self._display_recursive(node.right, level + 1)
            print(' ' * 4 * level + '->', node.key)
            self._display_recursive(node.left, level + 1)

maxHeap = MaxHeap()

keySet = [15, 10, 100, 50, 50,40,40]

for key in keySet:
    maxHeap.insert(key)

maxHeap.display()
