# Singly Linked List
Challenge was to work on creating linked lists and nodes as well as having functions that can modify and traverse the linked list.

## Challenge

## Nodes
Create a `class Node`
  - attributes:
    - value stored in node
    - pointer to next node

### Linked List
Create `class LinkedList`
  - attributes:
    - head, upon instantiation, creates an empty Linked List.
    - methods:
      - `insert`:
          - Arguments: value
          - Returns: nothing
          - Adds a new node with that value to the head of the list with an O(1) Time performance.
      - `includes`:
        - Arguments: value
        - Returns: Boolean
        - Indicates whether that value exists as a Node’s value somewhere within the list.
      - `string`:
        - Arguments: none
        - Returns: a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"

## Approach & Efficiency
I worked one function at a time. Testing as I each method one by one. These methods run on Big O (1), it does need anymore resources than the ones already allocated to it.

## API
<!-- Description of each method publicly available to your Linked List -->
