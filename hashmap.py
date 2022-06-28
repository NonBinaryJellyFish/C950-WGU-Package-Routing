class hash_table:

    def __init__(self):
        self.initial_size = 10
        self.table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.initial_size)]

    def insert_entry(self, key, data):
        hash_val = key_hash_val(key)
        key_value = [key, data]

        if not self.table[hash_val]:
            self.table[hash_val] = list([key_value])
            return True
        else:
            for pair in self.table[hash_val]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True
            self.table[hash_val].append(key_value)
            return True

    # returns a [key, data] array.
    def lookup(self, key):
        hash_val = key_hash_val(key)
        for pair in self.table[hash_val]:
            if pair[0] == key:
                return pair


def key_hash_val(key):
    key_hash_ = 0
    for i in str(key):
        key_hash_ += ord(i)

    return key_hash_ % 10