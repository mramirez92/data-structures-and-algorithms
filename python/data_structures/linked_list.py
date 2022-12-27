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
        return false
        """
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def __str__(self):
        string = ""
        current_node = self.head
        """
        while curent head is not None, format the current node value and add it to our string variable.
        string variable will expand as function iterates through linked list
        """
        while current_node is not None:
            string += "{{ {} }} -> ".format(current_node.value)
            current_node = current_node.next
        # if current value is NONE append "NULL" to our string variable
        string += "NULL"
        return string


# TA's i dont quite understand what this is for
class TargetError:
    pass


