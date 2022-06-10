from OpenAddressingHashTableClass import OpenAddressingHashTable


class DoubleHashingHashTable(OpenAddressingHashTable):
    def __init__(self, initial_capacity=11):
        OpenAddressingHashTable.__init__(self, initial_capacity)

    def h2(self, key):
        return 7 - self.hashKey(key) % 7

    # Returns the bucket index for the specified key and i value using the
    # double hashing probing sequence.
    def probe(self, key, i):
        return (self.hashKey(key) + i * self.h2(key)) % len(self.table)
