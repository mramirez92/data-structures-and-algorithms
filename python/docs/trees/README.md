# Trees
Implementation of tree classes and methods including binary tree creation and searching.
## Challenge
Create a Binary Tree class
- Define a method for each of the depth first traversals:
  - pre order
  - in order
  - post order

Create a Binary Search Tree class
- Class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
  - add
    - arg: value
    - return: nothing
    - adds new node with value in the correct location
  - contains:
    - arg: value
    - returns: boolean; is value present?

Create Node Class
  - Create node class with value property: left and right child node

## Approach & Efficiency
Binary Tree Class:
Because all three functions are traverse the tree recursively, the time complexity is O(n). "n" is the number of nodes in the tree, they are visited at only once. Time depends on the size of our tree.

Binary Search:
In this class, we are searching for nodes using less than or greater than values. Best case scenario our tree is balanced (both left and right are about the same size). If this is true time complexity will be O(log n), with n being the number of nodes. Time is halved if when traversal happens IF the tree is balance.

## API

Class BinaryTree:
- preorder:traverse from the root to the left subtree then to the right subtree, left to right.
- postorder: traverse from the left subtree, to the right subtree and lastly to the root.
- inorder: traverse tree from left subtree to root, then we traverse the right subtree
Class BinaryTreeSearch:
Methods:
- add: takes in an argument which is a value appended to a node. A node will be added to tree.
- contains: is used to search for a specific value and returns a boolean if or not the value is in our tree.
