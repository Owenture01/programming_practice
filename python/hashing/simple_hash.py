def simple_hash(key, table_size):
    hash_code = 0
    for char in key:
        hash_code += ord(char)     # return the Unicode for each char
    return hash_code % table_size   # so that the index will not exeed the table_size


# Example
key = "hello"
table_size = 10
print("Hash code: ", simple_hash(key, table_size))