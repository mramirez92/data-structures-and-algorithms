class BinaryTree:

    def __init__(self):
        # initialization here
        self.root = None

    def post_order(self, root=None, nodes=None):

        if root is None:
            root = self.root

        # firs time method called, empty
        if nodes is None:
            nodes = []

        # left child
        if root.left:
            self.post_order(root.left, nodes)

        # right child, nodes is being passed, points to same list created
        if root.right:
            self.post_order(root.right, nodes)

        # root
        nodes.append(root.value)

        return nodes

    def pre_order(self, root=None, nodes=None):
        # start root
        if root is None:
            root = self.root

        if nodes is None:
            nodes = []

        nodes.append(root.value)

        # left child
        if root.left:
            self.pre_order(root.left, nodes)

        # right child
        if root.right:
            self.pre_order(root.right, nodes)

        return nodes

    def in_order(self, root=None, nodes=None):

        if root is None:
            root = self.root

        if nodes is None:
            nodes = []

        # left child
        if root.left:
            self.in_order(root.left, nodes)

        nodes.append(root.value)

        # right child
        if root.right:
            self.in_order(root.right, nodes)

        return nodes


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
