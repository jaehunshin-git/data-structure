import sys
sys.setrecursionlimit(100000)

class Node():
    def __init__(self, key, value)-> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None
    
    def isEmpty(self) -> bool:
        return self.root is None
    
    def recursiveAdd(self, key, value = None) -> None:
        def node_add(node, key, value) -> None:
            if key == node.key:
                print("Key Repetition Detected. Updating Value.")
                node.value = value
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value)
                else:
                    node_add(node.left, key, value)
            else: #key > node.key
                if node.right is None:
                    node.right = Node(key, value)
                else:
                    node_add(node.right, key, value)

        if self.isEmpty():
            self.root = Node(key, value)
        else:
            node_add(self.root, key, value)

    def iterativeAdd(self, key, value = None) -> None:
        if self.isEmpty():
            self.root = Node(key, value)
            return
        
        current = self.root
        while current:
            if key == current.key:
                print("Key Repetition Detected. Updating Value.")
                current.value = value
                return
            elif key < current.key:
                if current.left is None:
                    current.left = Node(key, value)
                    return
                else:
                    current = current.left
            else: #key > current.key
                if current.right is None:
                    current.right = Node(key, value)
                    return
                else:
                    current = current.right

    def preorderTraversal(self, node = None):
        if node is None:
            node = self.root

        if node is not None:
            print(node.key)
            self.preorderTraversal(node.left)
            self.preorderTraversal(node.right)

bst = BinarySearchTree()

keyset = {5,2,3,8,9,6,7,0}
for key in keyset:
    bst.iterativeAdd(key)

bst.preorderTraversal()
