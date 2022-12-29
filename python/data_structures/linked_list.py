# Node class that is used to instantiate new node

class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_
    # using underscore because next exists as a built in method


class TargetError(Exception):
    pass


class LinkedList:
    # instantiates linked list, starts empty, includes HEAD
    def __init__(self):
        self.head = None

    def insert(self, value):
        # new node instantiates new Node by calling Node method
        new_node = Node(value)

        # assign HEAD to new_node, shifts new node to HEAD of linked list
        self.head = new_node

        # assign new_node's next as acting HEAD, the nodes current head before addition, whatever the head was right before new assignment happens
        new_node.next = self.head

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
        while current head is not None, format the current node value and add it to our string variable.
        string variable will expand as function iterates through linked list
        """
        while current_node is not None:
            string += "{{ {} }} -> ".format(current_node.value)
            current_node = current_node.next
        # if current value is NONE append "NULL" to our string variable
        string += "NULL"
        return string

    def append(self, value):

        current_node = self.head
        end_node = Node(value)

        if current_node is None:
            self.head = end_node
            return
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = end_node

    def insert_after(self, value, new_value):

        current_node = self.head
        new_insert = Node(new_value)

        if self.head is None:
            raise TargetError()
        while current_node:
            if current_node.value == value:
                new_insert.next = current_node.next
                current_node.next = new_insert
            else:
                # if search value doesnt match current value, traverse list
                current_node = current_node.next

    def insert_before(self, value, new_value):

        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return

        if self.head.data == value:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            if current.next.value == new_value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def kth_from_end(self, k):
        length = 0
        current_node = self.head

        # traverses list to find length while true

        while current_node:
            length += 1
            current_node = current_node.next

        # minus one at the end, k = 3 in a list of 5 elements returns len of 2, its index is at 1, so we need to subtract 1 from len fucntion to get correct index

        position = length - k - 1
        # resetting current to head

        if k == 0:
            return self.head.value

        current_node = self.head
        for i in range(position):
            current_node = current_node.next
        return current_node.value

# TA's I don't quite understand what this is for
