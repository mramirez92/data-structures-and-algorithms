class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    # instantiates linked list, starts empty, includes HEAD
    def __init__(self):
        self.head = None

    def insert(self, value):
        # new node instantiates new Node by calling Node method
        new_node = Node(value)

        # assign new_node's next as acting HEAD
        new_node.next = self.head

        # assign HEAD to new_node, shifts new node to HEAD of linked list
        self.head = new_node

    def includes(self, value):
        # makes current node HEAD
        current_node = self.head

        """
        if current nodes  value matches argument return TRUE
        change current_node value to next
        return fals
        """
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def __str__(self):
        pass


class TargetError:
    pass
