class QuadraticProbingHashTable(OpenAddressingHashTable):
    def __init__(self, c1=1, c2=1, initial_capacity=11):
        OpenAddressingHashTable.__init__(self, initial_capacity)
        self.c1 = c1
        self.c2 = c2

    # Returns the bucket index for the specified key and i value using the
    # quadratic probing sequence.
    def probe(self, key, i):
        return (self.hashKey(key) + self.c1 * i + self.c2 * i * i) % len(self.table)