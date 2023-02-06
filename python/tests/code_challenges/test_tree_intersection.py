import pytest
from code_challenges.tree_intersection import tree_intersection
from data_structures.binary_tree import BinaryTree, Node
from data_structures.queue import Queue


def test_exists():
    assert tree_intersection


def test_tree_intersection():
    tree_a = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [125, 175, 100, 160, 500, 200, 350]

    assert sorted(actual) == sorted(expected)


def add_values_to_empty_tree(tree, values):
    """
    Helper function to add given values to BinaryTree
    """
    tree.root = Node(values.pop())
    q = Queue()

    q.enqueue(tree.root)

    while values:
        node = q.dequeue()
        node.left = Node(values.pop())
        node.right = Node(values.pop()) if values else None
        q.enqueue(node.left)
        q.enqueue(node.right)


def test_small_tree():
    bt_1 = BinaryTree()
    bt_1.root = Node(1)
    bt_1.root.left = Node(2)
    bt_1.root.right = Node(3)
    bt_1.root.left.left = Node(4)
    bt_1.root.left.right = Node(5)
    bt_1.root.right.left = Node(6)
    bt_1.root.right.right = Node(7)

    bt_2 = BinaryTree()
    bt_2.root = Node(1)
    bt_2.root.left = Node(2)
    bt_2.root.right = Node(9)
    bt_2.root.left.left = Node(6)
    bt_2.root.left.right = Node(7)

    assert sorted(tree_intersection(bt_1, bt_2)) == [1, 2, 6, 7]


def test_one_empty_tree():
    bt_1, bt_1.root = BinaryTree(), Node(1)
    bt_2 = BinaryTree()
    assert (tree_intersection(bt_1, bt_2)) is None


def test_two_empty_trees():
    bt_1, bt_2 = BinaryTree(), BinaryTree()
    assert (tree_intersection(bt_1, bt_2)) is None


def test_trees_no_matches():
    bt_1, bt_2 = BinaryTree(), BinaryTree()
    values1, values2 = [1, 2, 3, 4], [6, 7, 8, 9]
    add_values_to_empty_tree(bt_1, values1)
    add_values_to_empty_tree(bt_2, values2)
    assert (tree_intersection(bt_1, bt_2)) is None
