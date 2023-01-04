import pytest
from data_structures.linked_list import LinkedList


def zip_lists(a, b):
    a_current = a.head
    b_current = b.head

    if a.head is None:
        return b
    if b.head is None:
        return a

    while a_current and b_current:
        # set pointers
        a_next = a_current.next
        b_next = b_current.next

        # a_current next becomes b current head
        a_current.next = b_current
        if a_next:
            # seconds linked list node next is inserted and its next becomes first ll node next
            b_current.next = a_next

        # move pointers
        a_current = a_next
        b_current = b_next
        b.head = b_current


llist1 = LinkedList()
llist2 = LinkedList()

# Creating LLs

# 1.
llist1.insert(3)
llist1.insert(2)
llist1.insert(1)
llist1.insert(0)

# 2.
for i in range(8, 3, -1):
    llist2.insert(i)

print("First Linked List:" + str(llist1))
llist1.__str__()

print("Second Linked List:" + str(llist2))


# Merging the LLs
zip_lists(a=llist1, b=llist2)

print("Modified first linked list:" + str(llist1))

