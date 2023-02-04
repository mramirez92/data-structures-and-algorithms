# Tree Intersection
Practice in using python dictionaries and binary trees. 

## Challenge
Write a function called tree_intersection that takes two binary trees as parameters that return a set of values found in both trees.
- use python dictionaries

## Whiteboard
![](tree_interction.jpg)

## Approach & Efficiency
Both time and space complexity are O(n). The time is takes to traverse each tree is dependent on the amount of nodes it has. When building out each dictionary, space is dependent again on the size of the tree.

## Solution
My solution to this challenge was to instantiate two different dictionaries to hold tree node values as its keys. In order to do this we need to traverse the tree and add the nodes to the corresponding dictionaries. For this, I created a recursive helper function. Once the trees have been fully added to the corresponding dictionaries, we will return a list containing only values found in both tree dictionaries. Empty trees will return None. Trees witout matches will return None.  

