# class Employee:
#     a = 1
#     def __init__(self):
#         print("constructor of the class Employee")

# class Programmer(Employee):
#     def __init__(self):
#         print("constructor of the class Programmer")
#     b = 2
# class Manager(Programmer):
#     c = 3
#     def __init__(self):
#         super().__init__()
#         print("constructor of the class Manager")



# o = Employee()

# o = Programmer()
# o = Manager()

# print(o.a) 
# print(o.a , o.b)
# print(o.a , o.b , o.c)



#### Class Methods

class Employee:
    a =1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")
        print("The @classMethod is used to access the class attribute")

e = Employee()
e.a = 45

e.show()


#### Property Decorators 

# class Employee:
#     a =1

#     @classmethod
#     def show(cls):
#         print(f"The class attribute of a is {cls.a}")
#         print("The @classMethod is used to access the class attribute")
    
#     # This makes name act like a property — accessed like e.name instead of e.name().
#     @property
#     def name(self):
#         return f"{self.fname} {self.lname}"

#     @name.setter
#     def name(self , value):
#         self.fname = value.split(" ")[0]
#         self.lname = value.split(" ")[1]

# e = Employee()
# e.a = 45

# e.name = "Aditya Sharma"
# print(e.fname)

# e.show()


#### Operator overloading

# class Number:
#     def __init__(self , n):
#         self.n = n
    
#     def __add__(self , num):
#         return self.n+ num.n

# n = Number(1)
# m = Number(2)

# print(n+m)