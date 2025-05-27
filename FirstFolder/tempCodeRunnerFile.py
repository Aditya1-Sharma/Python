class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # Copy constructor
#     @classmethod
#     def copy(cls, other):
#         return cls(other.name, other.age)   

# p1 = Person("Alice", 25)
# p2 = Person.copy(p1)
# p2.name = "Bob"
# print(p1.name, p1.age)  # Alice 25
# print(p2.name, p2.age)  # Bob 25