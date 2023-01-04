class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError:
    pass


class LinkedList:
    # instantiates linked list, starts empty, includes HEAD
    def __init__(self):
        self.head = None

    def insert(self, value):
        # new node instantiates new Node by calling Node method
        new_node = Node(value)

<<<<<<< Updated upstream
        # assign new_node's next as acting HEAD
        new_node.next = self.head

        # assign HEAD to new_node, shifts new node to HEAD of linked list
=======
        # assign new_node's next as acting HEAD, the nodes current head before addition, whatever the head was right before new assignment happens
        new_node.next = self.head
        # assign HEAD to new_node, shifts new node to HEAD of linked list

>>>>>>> Stashed changes
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

<<<<<<< Updated upstream

# TA's I don't quite understand what this is for

=======
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

    # def kth_from_end(self, k):
    #     length = 0
    #     current_node = self.head
    #
    #     # traverses list to find length while true
    #
    #     while current_node is not None:
    #         length += 1
    #         current_node = current_node.next
    #
    #         position = length - k
    #
    #         if k >= length:
    #             raise TargetError("Value exceeds linked list length")
    #
    #         if k < 0:
    #             raise TargetError("Value too low")
    #
    #         if position == 0:
    #             return self.head.value
    #         current_node = self.head
    #     # iterate to the node at the calculated position and return its value
    #         for i in range(position - 1):
    #             current_node = current_node.next
    #         return current_node.value
>>>>>>> Stashed changes
