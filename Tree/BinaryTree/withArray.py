class BinaryTree:
    def __init__(self, size):
        self.MAX_SIZE = size
        self.tree = [None] * size

    def insert(self, value):
        if self.tree[0] is None:
            self.tree[0] = value
        else:
            self._insert_recursive(value, 0)

    def _insert_recursive(self, value, index):
        if index >= self.MAX_SIZE:
            print("Tree is full")
            return

        if self.tree[index] is None:
            self.tree[index] = value
        elif value <= self.tree[index]:
            self._insert_recursive(value, 2 * index + 1)
        else:
            self._insert_recursive(value, 2 * index + 2)

    def display(self):
        print(self.tree)


# Example usage:
tree = BinaryTree(10)
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(4)
tree.insert(6)
tree.display()
