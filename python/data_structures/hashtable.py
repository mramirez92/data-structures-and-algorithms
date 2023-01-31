from .linked_list import LinkedList, Node

class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size

    def _hash(self, key):

        hash = 0

        for char in key:
            hash += ord(char)

        hash = (hash * 19) % self.size

        return hash

    def set(self, key, value):

        hashed_key = self._hash(key)

        bucket = self._buckets[hashed_key]

        if not bucket:
            self._buckets[hashed_key] = LinkedList()

        self._buckets[hashed_key].insert([key, value])

    def get(self, key):
        hashed_key = self._hash(key)
        bucket = self._buckets[hashed_key]

        current = bucket.head
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next

        raise KeyError(f'key not found: {key}')

    def has(self, key):
        # calculate hashbrown
        hashed_key = self._hash(key)
        # look at bucket located at hashed index
        bucket = self._buckets[hashed_key]
        # if key hashed is not in hashtable return False
        if bucket is None:
            return False

            # get head of ll
        current = bucket.head
        # while ll has nodes
        while current:
            # if current val == key, return True
            if current.value[0] == key:
                return True
                # pointer to move to next node in ll
            current = current.next
            # return false if key not in ll
        return False

    def keys(self):
        # instantiate list to store keys
        keys = []
        # iterate through each bucket in hashtable
        for bucket in self._buckets:
            # if bucket is not None, not empty
            if bucket:
                # set current to head
                current = bucket.head
                """
                while in this bucket, start at idx 0 and iterate through bucket and append to keys list
                """
                while current:
                    keys.append(current.value[0])
                    current = current.next
        return keys




