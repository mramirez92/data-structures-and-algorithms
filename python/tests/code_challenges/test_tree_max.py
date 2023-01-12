import pytest
from data_structures.binary_tree import BinaryTree, Node


@pytest.mark.skip("TODO")
def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected


def test_none_val():
    tree = BinaryTree()
    tree.root = None
    actual = tree.find_maximum_value()
    expected = None

    assert actual == expected


def test_max_val32():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.left.left = Node(31)
    tree.root.left.right = Node(32)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 32

    assert actual == expected


def test_max_val6():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.left.left = Node(3)

    actual = tree.find_maximum_value()
    expected = 2

    assert actual == expected
