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
    
    def is_Empty(self) -> bool:
        return self.root is None
    
    def recursive_add(self, key, value = None) -> None:
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

        if self.is_Empty():
            self.root = Node(key, value)
        else:
            node_add(self.root, key, value)

    def iterative_add(self, key, value = None) -> None:
        if self.is_Empty():
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

    def preorder_traversal(self, node = False):
        if self.is_Empty():
            print("Tree is Empty. Nothing to print.")
            return
        
        if node is False:
            node = self.root

        if node is None:
            return
        else:
            print(f'{node.key}, {node.value}')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
        
    def inorder_traversal(self, node = False):
        if self.is_Empty():
            print("Tree is Empty. Nothing to print.")
            return
        
        if node is False:
            node = self.root

        if node is None:
            return
        else:
            self.inorder_traversal(node.left)
            print(f'{node.key}, {node.value}')
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node = False):
        if self.is_Empty():
            print("Tree is Empty. Nothing to print.")
            return
        
        if node is False:
            node = self.root

        if node is None:
            return
        else:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(f'{node.key}, {node.value}')
            
    def search(self, key):
        if self.is_Empty():
            print("Tree is Empty. Nothing to search.")
            return
        
        current = self.root
        prev_current = None
        while current:
            if key == current.key:
                print(f'Found {key}')
                return True, current, prev_current
                # boolean , current node, prev node
            elif key < current.key:
                prev_current = current
                current = current.left
            else: # key > current.key
                prev_current = current
                current = current.right
        
        print(f'Cannot found {key} in the tree')
        return False
  
    # def count_child(self, node):
    #     childCount = 0
        
    #     if node.left:
    #         childCount += 1
    #     if node.right:
    #         childCount += 1
            
    #     return childCount 
                  
    # def is_left_child(self, childNode, parentNode) -> bool:
    #     if parentNode.left is childNode:
    #         return True
    #     elif parentNode.right is childNode:
    #         return False
    #     else: # not a child or has 2 child
    #         return -1
        
    def remove(self, key) -> bool:
        # when tree is empty
        if self.is_Empty():
            return
        
        found, target_node, parent_node = self.search(key)
        
        # when key is not in the tree
        if not found:
            print(f'There is no {key} in the tree.')
            return
        
        # Case 1: target_node is leaf = target_node has no child
        if not target_node.left and not target_node.right:
            if parent_node:
                if parent_node.left is target_node:
                    parent_node.left = None
                else:
                    parent_node.right = None
            else:
                self.root = None
        
        # Case 2: target_node has just left child
        elif target_node.left and not target_node.right:
            if parent_node:
                if parent_node.left is target_node:
                    parent_node.left = target_node.left
                else:
                    parent_node.right = target_node.left
            else:
                self.root = target_node.left
        
        # Case 3: target_node has just right child
        elif not target_node.left and target_node.right:
            if parent_node:
                if parent_node.left is target_node:
                    parent_node.left = target_node.right
                else:
                    parent_node.right = target_node.right
            else:
                self.root = target_node.right
                
        # Case 4: target_node has 2 child
        # Method 1: replace target_node with the predecessor
        # Method 2: replace target_node with the successor
        else:
            # Method 2
            
            # find successor of the target_node and successor_parent
            successor_parent = None
            successor = target_node.right
            while successor.left:
                successor_parent = successor
                successor = successor.left
                
            # replace the key and value of the target_node to successor's
            target_node.key = successor.key
            target_node.value = successor.value 
            
            # delete the original successor node.
            # original successor node can be leaf node or has one right child
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
            
        
            
            
                
            
            

bst = BinarySearchTree()

keyset = [5,2,3,8,9,6,7,0]
for key in keyset:
    bst.iterative_add(key)

bst.search(5)
bst.remove(5)
bst.search(5)
