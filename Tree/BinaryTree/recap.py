from __future__ import annotations
from typing import Any, Type

class Node():
    def __init__(self, key: Any, value = None, left: Node = None, right: Node = None) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        
class BinarySearchTree():
    def __init__ (self) -> None:
        self.root = None
        
    def recursiveAdd(self, key: Any, value = None) -> None:
        def add_node(node: Node, key, value):
            if key == node.key:
                print("Key Repetition Detected. Updating Key.")
                node.value = value
                return

            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)

            else: # key > node.key
                if node.right is None:
                    node.right = Node(key, value, None, None)
                    
                else:
                    add_node(node.right, key, value)
                    
        if self.root is None:
            self.root = Node(key, value, None, None)
        else:
            add_node(self.root, key, value)
            
    def iterationAdd(self, key, value = None) -> None:
        if self.root is None:
            self.root = Node(key, value, None, None)
            return

        current = self.root
        while current:
            if key == current.key:
                print("Key Repetition Detected. Updating Key.")
                current.value = value
                return
            elif key < current.key:
                if current.left is None:
                    current.left = Node(key, value, None, None)
                else:
                    current = current.left
            else: # key > current.key
                if current.right is None:
                    current.right = Node(key, value, None, None)
                else:
                    current = current.right
            
    