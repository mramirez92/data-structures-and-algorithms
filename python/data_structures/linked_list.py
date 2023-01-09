class TargetError(Exception):
    pass


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    # instantiates linked list, starts empty, includes HEAD
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
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
        end_node = Node(value)

        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = end_node

    def insert_after(self, value, new_value):
        if self.head is None:
            raise TargetError("Empty list")

        if not self.includes(value):
            raise TargetError('Value not found')

        current_node = self.head

        new_insert = Node(new_value)

        while current_node:
            if current_node.value == value:
                new_insert.next = current_node.next
                current_node.next = new_insert
                break
            else:
                current_node = current_node.next

    def insert_before(self, value, new_value):

        if self.head is None:
            raise TargetError("Empty list")

        if not self.includes(value):
            raise TargetError('Value not found')

        if self.head.value is value:
            new_node = Node(new_value, self.head)
            self.head = new_node
        else:
            current = self.head
            while current:
                if current.next.value is value:
                    new_node = Node(new_value, current.next)
                    current.next = new_node
                    break
                else:
                    current = current.next

    def kth_from_end(self, n):
        length = 0
        current_node = self.head

        # traverses list to find length while true

        while current_node is not None:
            length = 0
            curr = self.head
            while curr is not None:
                length += 1
                curr = curr.next

            # Calculate the position of the node to remove
            pos = length - n

            # Check if the position is valid
            if pos < 0:
                return

            # Traverse the list and remove the node
            prev = None
            curr = self.head
            for i in range(pos):
                prev = curr
                curr = curr.next
            prev.next = curr.next






