a = (1,2,3,4,5 , False , "Hello" , "Selena")
print(a)

num = a.count(2)
print(num)

num = a.index(2)
print(num)

print("Lenght of Tuple is : ", len(a))

# Slice in Tuple

b = a[1:3]
print(b)

c = a[1:]
print(c)
# ValueError: tuple.index(x): x not in tuple
# num = a.index(2, 3)
# print(num)


# AttributeError: 'tuple' object has no attribute 'remove'
# a.remove(2)
# print(a)

# a.reverse()
# print(a)

# a.sort()
# print(a)

