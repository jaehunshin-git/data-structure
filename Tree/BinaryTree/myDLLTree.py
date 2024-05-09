from __future__ import annotations
from typing import Any, Type

class Node():
    def __init__(self, key, value, left: Node = None, right: Node = None) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        
class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None
        
    def recursiveAdd(self, key, value = None) -> bool:
        def add_node(node: Node, key, value) -> None:
            if key == node.key:
                print("Key Repetition Detected. Updating Value.")
                node.value = value
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    return add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    return add_node(node.right, key, value)
            return True
        
        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)
        
    def iterativeAdd(self, key, value = None) -> bool:
        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        
        current = self.root
        while current:
            if key == current.key:
                print("Key Repetition Detected. Updating Value.")
                current.value = value
                return False
            elif key < current.key:
                if current.left is None:
                    current.left = Node(key, value, None, None)
                    return True
                else:
                    current = current.left
            else: #key > current.key
                if current.right is None:
                    current.right = Node(key, value, None, None)
                    return True
                else:
                    current = current.right
        
        return False
    
    
    
        
bst = BinarySearchTree()
keyset = [5,2,3,8,9,6,7,0]
for key in keyset:
    bst.iterativeAdd(key)

                        