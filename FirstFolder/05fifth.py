# Sets and dictionary

# Defination of dictionary in python 

# Dictionary is a collection of key-value pairs
# Key is a unique identifier
# Value is the data associated with the key
# Dictionary is a mutable data structure
# Dictionary is an unordered collection of key-value pairs
# Cannot contain duplicate keys
# Dictionary is a mapping of keys to values

marks = {
    "Harry":100,
    "Aditya":99,
    "Selena":100,
    "Sanjana":99,
    0:"Rohan"
}



# print(marks , type(marks))

# print(marks["Aditya"])

# Dictionary methods

## To print the item of dictionary
print((marks.items()))

# # To print the keys of dictionary
# print(marks.keys())

# print(marks.values())
marks.update({"Sanjana": 98 , "Deepak": 92})
print(marks)


# Explain dict.__reversed__() method 
# It returns a reversed iterator over the keys of the dictionary

rev = marks.__reversed__()

# for i in rev:
#     print(i)

print(list(rev))

# print(marks.get("Aditya1")) ## It will print none
# print(marks["Aditya1"]) ## It will give keyError

marks.pop("Deepak")
print(marks)

s = {1 , 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(s.pop())
print(s.pop())
print(s.pop())

