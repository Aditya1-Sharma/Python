# Sets
## Sets are collections of unique elements
## Sets are unordered collections
## Sets are mutable
## sets are unindexed
## Sets are hashable
## Sets are iterable

s = {1 , 2 , 32 , 23 , 23 , 12, "Harry"}
e = set()  ## It is empty set

# e.add(1)
# e.add(2)

# e.remove(1)
# print(e)

print(s)

print(len(s))
s.pop()
s.pop()
print(s)

print("Sets methods for union and intersection")
s1 = {1 , 45 , 6}
s2 = {7 , 8 , 45 , 5 , 6}

print(s1.union(s2))

print(s1.intersection(s2))
