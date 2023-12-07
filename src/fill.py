def fill(coll, value, begin=0, end=None):
    if value is None:
        return coll
    coll_length = len(coll)
    if not end:
        end = coll_length
    chunk = [value for _ in coll[begin:end]]
    coll[begin:end] = chunk
    return coll

print([1, 2, 3, 4, 5], '*', 1, 3)