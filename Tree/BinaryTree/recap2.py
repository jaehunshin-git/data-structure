from __future__ import annotations
from typing import Any, Type

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

    def preorderTraversal(self, node = False):
        if self.isEmpty():
            print("Tree is Empty. Nothing to print.")
            return
        
        if node is False:
            node = self.root

        if node is None:
            return
        else:
            print(f'{node.key}, {node.value}')
            self.preorderTraversal(node.left)
            self.preorderTraversal(node.right)
        
    def inorderTraversal(self, node = False):
        if self.isEmpty():
            print("Tree is Empty. Nothing to print.")
            return
        
        if node is False:
            node = self.root

        if node is None:
            return
        else:
            self.inorderTraversal(node.left)
            print(f'{node.key}, {node.value}')
            self.inorderTraversal(node.right)

    def postorderTraversal(self, node = False):
        if self.isEmpty():
            print("Tree is Empty. Nothing to print.")
            return
        
        if node is False:
            node = self.root

        if node is None:
            return
        else:
            self.postorderTraversal(node.left)
            self.postorderTraversal(node.right)
            print(f'{node.key}, {node.value}')
            
    def search(self, key):
        if self.isEmpty():
            print("Tree is Empty. Nothing to search.")
            return
        
        current = self.root
        prevCurrent = None
        while current:
            if key == current.key:
                print(f'Found {key}')
                return True, current, prevCurrent
                # boolean , current node, prev node
            elif key < current.key:
                prevCurrent = current
                current = current.left
            else: # key > current.key
                prevCurrent = current
                current = current.right
        
        print(f'Cannot found {key} in the tree')
        return False
  
    def countChild(self, node):
        childCount = 0
        
        if node.left:
            childCount += 1
        if node.right:
            childCount += 1
            
        return childCount 
                  
    def isLeftChild(self, childNode, parentNode) -> bool:
        if parentNode.left is childNode:
            return True
        elif parentNode.right is childNode:
            return False
        else: # not a child or has 2 child
            return -1
        
    def delete(self, key) -> bool:
        # when tree is empty
        if self.isEmpty():
            return
        
        found, targetNode, parentNode = self.search(key)
        
        # when key is not in the tree
        if not found:
            print(f'There is no {key} in the tree.')
            return
        
        # Case 1: targetNode is leaf = targetNode has no child
        if not targetNode.left and not targetNode.right:
            if parentNode:
                if parentNode.left is targetNode:
                    parentNode.left = None
                else:
                    parentNode.right = None
            else:
                self.root = None
        
        # Case 2: targetNode has just left child
        elif targetNode.left and not targetNode.right:
            if parentNode:
                if parentNode.left is targetNode:
                    parentNode.left = targetNode.left
                else:
                    parentNode.right = targetNode.left
            else:
                self.root = targetNode.left
        
        # Case 3: targetNode has just right child
        elif not targetNode.left and targetNode.right:
            if parentNode:
                if parentNode.left is targetNode:
                    parentNode.left = targetNode.right
                else:
                    parentNode.right = targetNode.right
            else:
                self.root = targetNode.right
                
        # Case 4: targetNode has 2 child
        else:
            pass

bst = BinarySearchTree()

keyset = [5,2,3,8,9,6,7,0]
for key in keyset:
    bst.iterativeAdd(key)

bst.search(5)
