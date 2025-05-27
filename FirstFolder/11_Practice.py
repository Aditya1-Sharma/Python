# PRoblem 1

# class TwoDVector:
#     def __init__(self , i , j):
#         self.i = i
#         self.j = j
#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j")

# class ThreeDVector(TwoDVector):
#     def __init__(self , i  , j , k):
#         super().__init__(i , j)
#         self.k = k

#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j + {self.k}k")


# a = TwoDVector(1 , 2)
# a.show()

# b = ThreeDVector(1 ,2 , 3)
# b.show()


# PRoblem 2

# class Animals:
#     pass

# class Pets(Animals):
#     pass

# class Dogs(Pets):
#     @staticmethod
#     def bark():
#         print("Bhow Bhow!!!")


# dog = Dogs()

# dog.bark()


# Problem 3

class Employee:
    salary = 234
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):

        self.increment = ((salary/self.salary)-1)*100


e = Employee()
e.salaryAfterIncrement = 280.8
print(e.salaryAfterIncrement)
print(round(e.increment, 2))
print(Employee.increment)


# Problem 4

# class Complex:
#     def __init__(self , r , i):
#         self.r = r
#         self.i = i

#     def __add__(self , c2):
#         return Complex(self.r + c2.r , self.i + c2.i)

#     def __str__(self):
#         return f"{self.r} + {self.i}i"


# c1 = Complex(1 , 2)
# c2 = Complex(3 , 4)


# # c1 + c2 triggers: c1.__add__(c2)
# # Returns: Complex(1+3, 2+4) → Complex(4, 6)
# print(c1+c2)


# Problem 5 ->

# class Complex:
#     def __init__(self , r , i):
#         self.r = r
#         self.i = i

#     def __add__(self , c2):
#         return Complex(self.r + c2.r , self.i + c2.i)

#     def __mul__(self, c2):
#         real = self.r * c2.r - self.i * c2.i
#         imag = self.r * c2.i + self.i * c2.r
#         return Complex(real, imag)

#     def __str__(self):
#         return f"{self.r} + {self.i}i"


# c1 = Complex(1 , 2)
# c2 = Complex(3 , 4)


# # c1 + c2 triggers: c1.__add__(c2)
# # Returns: Complex(1+3, 2+4) → Complex(4, 6)
# print(c1+c2)
# print(c1*c2)


# Problem 6

# class Vector:
#     def __init__(self , i , j):
#         self.i = i
#         self.j = j

#     def __add__(self , c2):
#         return Vector(self.i + c2.i , self.j + c2.j)

#     def __mul__(self , c2):
#         res = self.i * c2.i + self.j * c2.j
#         return res

#     def __str__(self):
#         return f"{self.i} + {self.j}"

# v1 = Vector(1 , 2)
# v2 = Vector(3 , 4)

# print(v1+v2)
# print(v1*v2)


# Problem 7
