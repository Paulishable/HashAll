class LinearProbingHashTable(OpenAddressingHashTable):
    def __init__(self, initial_capacity=11):
        OpenAddressingHashTable.__init__(self, initial_capacity)

    # Returns the bucket index for the specified key and i value using the
    # linear probing sequence.
    def probe(self, key, i):
        return (self.hashKey(key) + i) % len(self.table)