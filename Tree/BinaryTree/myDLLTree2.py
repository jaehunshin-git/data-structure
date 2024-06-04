from __future__ import annotations
from typing import Any, Type
import random

class Node():
    def __init__(self, key, value=None) -> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None
    
    def get_root(self) -> Node:
        return self.root
    
    def is_empty(self) -> bool:
        return self.root is None
    
    def recursive_add(self, key, value=None) -> None:
        def node_add(node, key, value) -> None:
            if key == node.key:
                print("Key Repetition Detected. Updating Value.")
                node.value = value
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value)
                else:
                    node_add(node.left, key, value)
            else:  # key > node.key
                if node.right is None:
                    node.right = Node(key, value)
                else:
                    node_add(node.right, key, value)

        if self.is_empty():
            self.root = Node(key, value)
        else:
            node_add(self.root, key, value)

    def iterative_add(self, key, value=None) -> None:
        if self.is_empty():
            self.root = Node(key, value)
            return

        current = self.root
        while True:
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
            else:  # key > current.key
                if current.right is None:
                    current.right = Node(key, value)
                    return
                else:
                    current = current.right

    def preorder_traversal(self, node = False) -> None:
        if self.is_empty():
            print("Tree is Empty. Nothing to print.")
            return
        
        if node is False:
            node = self.root

        if node is not None:
            print(f'{node.key}, {node.value}')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
        
    def inorder_traversal(self, node = False) -> None:
        if self.is_empty():
            print("Tree is Empty. Nothing to print.")
            return
        
        if node is False:
            node = self.root

        if node is not None:
            self.inorder_traversal(node.left)
            print(f'{node.key}, {node.value}')
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node = False) -> None:
        if self.is_empty():
            print("Tree is Empty. Nothing to print.")
            return
        
        if node is False:
            node = self.root

        if node is not None:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(f'{node.key}, {node.value}')

    def search(self, key):
        if self.is_empty():
            print("Tree is Empty. Nothing to search.")
            return False, None, None
        
        current = self.root
        parent = None
        while current:
            if key == current.key:
                print(f'Found {key}')
                return True, current, parent
            elif key < current.key:
                parent = current
                current = current.left
            else:  # key > current.key
                parent = current
                current = current.right
        
        print(f'Cannot find {key} in the tree')
        return False, None, None
  
    def delete(self, key) -> bool:
        # when tree is empty
        if self.is_empty():
            print("Tree is Empty. Nothing to remove.")
            return False
        
        found, target_node, parent_node = self.search(key)
        
        # when key is not in the tree
        if not found:
            print(f'There is no {key} in the tree.')
            return False
        
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
                
        # Case 4: target_node has 2 children
        else:
            #Case 4-1: Find the Predecessor (largerst in the left subtree)
            predecessor_parent = target_node
            predecessor = target_node.left
            while predecessor.right:
                predecessor_parent = predecessor
                predecessor = predecessor.right

            # Replace target_node's key and value with predecessor's key and value
            target_node.key = predecessor.key
            target_node.value = predecessor.value 

            # Delete the original predecessor node
            if predecessor_parent != target_node:
                predecessor_parent.right = predecessor.left
            else:
                predecessor_parent.left = predecessor.left

            # Case 4-2: Find the successor (smallest in the right subtree)
            # successor_parent = target_node
            # successor = target_node.right
            # while successor.left:
            #     successor_parent = successor
            #     successor = successor.left
                
            # # Replace target_node's key and value with successor's key and value
            # target_node.key = successor.key
            # target_node.value = successor.value 
            
            # # Delete the original successor node
            # if successor_parent != target_node:
            #     successor_parent.left = successor.right
            # else:
            #     successor_parent.right = successor.right
        
        print(f'Removed {key} from the tree.')
        return True

    def find_max(self, node=None):
        if self.is_empty():
            print("Tree is Empty.")
            return None
        
        current = node if node else self.root
        while current.right:
            current = current.right
        
        return current.key, current.value
    
    def find_min(self, node=None):

        if self.is_empty():
            print("Tree is Empty.")
            return None
        
        current = node if node else self.root
        while current.left:
            current = current.left

        return current.key, current.value
    
    def get_height(self, node = None):
        pass
    
def merge_bst(aBST, bBST):
    pass
    # 가정: aBST의 모든 원소 < x < bBST의 모든 원소
    # 어떤 bst 가 작은 트리인지 판별해야함.
    # 위의 가정대로라면 root 끼리 비교하면 뭐가 큰 트리인지 알수 있다.

    # if aBST.find_max() < bBST.get_root().key:
    # newKey = random.randrange(aBST.find_max() + 1, bBST.find_min())




bst = BinarySearchTree()

keyset = [5,2,3,8,9,6,7,0]
for key in keyset:
    bst.iterative_add(key)

# Traversals to verify the structure of the tree
print("In-order Traversal:")
bst.inorder_traversal()

print("\nPre-order Traversal:")
bst.preorder_traversal()

print("\nPost-order Traversal:")
bst.postorder_traversal()

# Finding the maximum value in the tree
max_key, max_value = bst.find_max()
print(f"\nMaximum key in the tree: {max_key}, value: {max_value}")

min_key, min_value = bst.find_min()
print(f"\nMinimum key in the tree: {min_key}, value: {min_value}")

