a = (1,2,3,4,5 , False , "Hello" , "Selena")
print(a)

num = a.count(2)
print(num)

# It will return the index of the first appearance of the value in the tuple
# ValueError: tuple.index(x): x not in tuple
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


it = a.__add__((10 , 20 , 30))
print(it)


