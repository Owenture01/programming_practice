class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        hash_code = self._hash(key)
        bucket = self.table[hash_code]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        hash_code = self._hash(key)
        bucket = self.table[hash_code]
        for k, v in bucket:
            if k == key:
                return v
        return None

# Example usage
ht = HashTable(10)
ht.insert("hello", "world")
ht.insert("foo", "bar")
print("Value for 'hello':", ht.get("hello"))
print("Value for 'foo':", ht.get("foo"))
