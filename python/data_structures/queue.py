from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError


class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        # check to see if queue is empty
        if self.rear:
            self.rear.next = Node(value)
            self.rear = self.rear.next
            return
        self.rear = self.front = Node(value)

    def dequeue(self):
        if self.front is None:
            raise InvalidOperationError
        else:
            # node leaving queued is self.front
            dequeued = self.front
            # new front is now old front.next
            self.front = self.front.next
            return dequeued.value

    def peek(self):
        if self.front is None:
            raise InvalidOperationError
        return self.front.value

    def is_empty(self):
        if self.front is None:
            return True
