from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def __init__(self):
        super().__init__()

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        current = self.root
        while current:
            if current.value == value:
                return
            # if value is less than current value, add left if left is None
            # else move left
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                else:
                    current = current.left
            # if value is greater than current value, add right if none
            # else move to the right
            if value > current.value:
                if current.right is None:
                    current.right = Node(value)
                else:
                    current = current.right


    """
    traverse the tree, left if value is less than root or parent
    traverse right if value is greater than root or parent
    traverse until value is current value
    return false if not there
    """
    def contains(self, value):
        current = self.root
        while current:
            if value == current.value:
                return True
            if value < current.value:
                current = current.left
            if value > current.value:
                current = current.right
        return False
