from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        if self.top is None:
            self.top = Node(value)
            return
        """
        node at top is old
        new node is assigned as TOP of stack
        top node (now the new  node) next value is assigned to old node value

        """
        old = self.top
        self.top = Node(value)
        self.top.next = old

    def pop(self):

        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        """
        TOP is assigned to popped variable
        TOP is assigned to its next value (next value now new TOP)
        return popped value (old top)
        """
        popped = self.top
        self.top = self.top.next
        return popped.value

    # return value of node at TOP, raise exception when stack is empty
    def peek(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")

        return self.top.value

    def is_empty(self):
        if self.top is None:
            return True

