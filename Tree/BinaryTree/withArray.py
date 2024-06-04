class BinaryTree:
    def __init__(self, size):
        self.MAX_SIZE = size
        # Start with an array filled with None, with the first element unused
        self.tree = [None] * (self.MAX_SIZE + 1)

    def insert(self, value):
        if self.tree[1] is None:
            self.tree[1] = value
        else:
            self._insert_recursive(value, 1)

    def _insert_recursive(self, value, index):
        if index > self.MAX_SIZE:
            print("Tree is full")
            return

        if self.tree[index] is None:
            self.tree[index] = value
        elif value <= self.tree[index]:
            self._insert_recursive(value, 2 * index)
        else:
            self._insert_recursive(value, 2 * index + 1)

    def display(self):
        # Display the tree, skipping the first unused element
        print(self.tree[1:])

# Example usage:
tree = BinaryTree(10)
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(4)
tree.insert(6)
tree.display()
