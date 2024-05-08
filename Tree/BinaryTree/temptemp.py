from __future__ import annotations
from typing import Any, Type

class Node():
    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None

    def isEmpty(self) -> None:
        return self.root is None
        
    def recursiveAdd(self, key, value = None, left = None, right = None):
        def add_node(node, key, value, left, right):
            if key == node.key:
                print("Key Repetition Detected. Updating Value")
                node.value = value
                return
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, left, right)
                else:
                    add_node(node.left, key, value, left, right)
            else:
                if node.right is None:
                    node.right = Node(key, value, left, right)
                else:
                    add_node(node.right, key, value, left, right)

        if self.isEmpty():
            self.root = Node(key, value, left, right)
        else:
            add_node(self.root, key, value, left, right)
            
    def iterativeAdd(self, key, value, left, right):
        if self.isEmpty():
            self.root = Node(key, value, left, right)
        else:
            current = self.root
            while current:
                if key == current.key:
                    print("Key Repetition Detected. Updating Value")
                    current.value = value
                    break
                elif key < current.key:
                    if current.left is None:
                        current.left = Node(key, value, left, right)
                    else:
                        current = current.left
                else: # key > current.key
                    if current.right is None:
                        current.right = Node(key, value, left, right)
                    else:
                        current = current.right


    def dump(self) -> None:
        """덤프(모든 노드를 키의 오름차순으로 출력)"""
        def print_subtree(node: Node):
            """node를 루트로 하는 서브 트리의 노드를 키의 오름차순으로 출력"""
            if node is not None:
                print_subtree(node.left)            # 왼쪽 서브 트리를 오름차순으로 출력
                print(f'{node.key}  {node.value}')  # node를 출력
                print_subtree(node.right)           # 오른쪽 서브 트리를 오름차순으로 출력

        print_subtree(self.root)


bst = BinarySearchTree()
bst.recursiveAdd(5)
bst.recursiveAdd(2)
bst.recursiveAdd(7)
bst.recursiveAdd(2)
bst.recursiveAdd(9)
bst.recursiveAdd(0)
bst.dump()


    