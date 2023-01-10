# Tree-Max
Implementation of tree classes and methods including binary tree creation and searching.

Author: Monica Ramirez

## Challenge
Extending the implementation of Binary Tree class with an addition of find_maximum_value method:

- `find_maximum_value`
- Arguments: none
- Returns: number
- Find the maximum value stored in the tree.

## Whiteboard

[](/treemax.jpg)

## Approach & Efficiency

Big O notation for this method depends on the tree height and number of nodes, because of this the find_maximum_value method functions at O(n). 

##Solution:
implement existing method of preorder to traverse the tree from the root to the left child, going down before moving to the right child and side of tree. Get max method was also implemented to easily find max value of node. 
