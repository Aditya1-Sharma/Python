# class Programmer:
#     company = "Microsoft"

#     def __init__(self , name , salary , pinCode):
#         self.name = name
#         self.salary = salary
#         self.pincode = pinCode


# p = Programmer("Harry" , 1200000 , 1102029)
# print(p.name , p.salary , p.company , p.pincode)
# r = Programmer("Rohan" , 1000000 , 1102029)
# print(r.name , r.salary , r.company , r.pincode)


# Problem 2

# class Calculator:
#     def __init__(self , n):
#         self.n = n

#     def square(self):
#         print(f"The square of {self.n} is {self.n * self.n}")

#     def squareRoot(self):
#          print(f"The square of {self.n ** 1/2}")

# a = Calculator(4)
# a.square()
# a.squareRoot()


# Problem 3

# class Demo:
#     a = 4

# o = Demo()
# print(o.a) ## It prints the class attribute because instance attribute is not present
# o.a = 0  ## Instance attribute is set
# print(o.a)  ## Print instance attribute because instance attribute is present
# print(Demo.a) ## Prints the class attribute


# Problem 4

# class Calculator:
#     def __init__(self, n):
#         self.n = n

#     def square(self):
#         print(f"The square of {self.n} is {self.n ** 2}")

#     def squareRoot(self):
#         print(f"The square of {self.n ** 1/2}")

#     @staticmethod
#     def hello(name):
#         print(f"Hello {name}")


# a = Calculator(4)
# a.square()
# a.squareRoot()
# a.hello("Harry")


# Problem 5

# from random import randint
# class Train:

#     def __init__(self , trainNo):
#         self.trainNo = trainNo
#     def book(self  , src , to):
#         print(f"Ticket is booked in train no.: {self.trainNo} from {src} to {to}")

#     def getStatus(self ):
#         print(f"The train with trainNo : {self.trainNo} is running on time")

#     def getFare (self , src , to):
#         print(f"The fare in train no. : {self.trainNo} from {src} to {to} is {randint(222 , 555)}")


# t = Train(12339)
# t.book("Rampur" , "Delhi")
# t.getStatus()
# t.getFare("Delhi" , "Jharkhand")


# shallow vs Deep copy

# In shallow copy the the primive datatypes are copied but the objects are not copied
# # In deep copy the objects are copied
# import copy

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("Bob", 30)
# p2 = copy.copy(p1)  # Shallow copy
# p3 = copy.deepcopy(p1)  # Deep copy

# p2.age = 31
# print(p1.name, p1.age)
# print(p2.name, p2.age)  # Bob 30
# print(p3.name, p3.age)  # Bob 30


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Copy constructor
    @classmethod
    def copy(cls, other):
        return cls(other.name, other.age)

p1 = Person("Alice", 25)
p2 = Person.copy(p1)
p2.name = "Bob"
print(p1.name, p1.age)  # Alice 25
print(p2.name, p2.age)  # Bob 25
