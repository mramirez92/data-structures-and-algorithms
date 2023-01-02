from data_structures.stack import Stack
from data_structures.linked_list import Node


class PseudoQueue:
    def __init__(self):
        # self.top = None
        self.stack = Stack()
        self.temp = Stack()

    """
    []
    """
    def enqueue(self, value):

        while not self.stack.is_empty():
            current = self.stack.pop()
            self.temp.push(current)
        self.stack.push(value)

        while not self.temp.is_empty():
            current = self.temp.pop()
            self.stack.push(current)

    def dequeue(self):
        return self.stack.pop()


