# List and tuples

friends = ["Apple" , "Orange" , 5 , 345.06 , False , "Selena"]

print(friends[0])
friends[0] = "Naman"
print(friends)
# Unlike strings lists are mutable

# Slicing of the list
print(friends[1:4])

# List methods

friends.append("Harry")

print(friends)

l1 = [1 , 2 , 34 , 15 , 7 , 10  ,11]
## for sort the list
l1.sort()
print(l1)
## for reversing the list
l1.reverse()
print(l1)

## Inserting 3333 to a 3 index
l1.insert(3 , 3333)

print(l1)

#  Pop the index from the particular index
l1.pop(1)
#  Pop the last element from the list
l1.pop()

# This will pop out the last element from the list
l1.pop(-1) 
print(l1)

l1.remove(11)
print(l1)



fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')         # ['apple', 'banana', 'cherry', 'orange']
fruits.insert(1, 'grape')       # ['apple', 'grape', 'banana', 'cherry', 'orange']
fruits.remove('banana')         # ['apple', 'grape', 'cherry', 'orange']
print(fruits.pop())             # 'orange'
fruits.sort()                   # ['apple', 'cherry', 'grape']


