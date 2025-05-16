### walrus operator

# if(n := len([1 , 2, 2 , 3 , 4])) > 3:
#     print(f"The list is too long {n} , element > 3")


#### type.py

# n : int = 5

# name : str = "Harry"

# def sum(a:int , b:int)->int:
#     return a+b

# print(sum(2 , 4))


# from typing import List , Tuple , Dict , Union

# # List of integers
# a : List[int] = [1, 2, 3, 4, 5]

# # Tupple of string and integer
# b : Tuple[str, int] = ("Hello" , 5 , 6  , "World")

# # Dict of string and integer
# c : Dict[str, int] = {"a" : 1 , "b" : 2}

# # Union of string and integer
# d : Union[str, int] = "Hello123"

# print(a)
# print(b)
# print(c)
# print(d)

# def sum(a:int , b:int , c:int)->int:
#     return a+b+c

# print(sum(2 , 4 , 6))


### match case

# def httpstatus(code:int)->str:
#     match code:
#         case 200:
#             return "OK"
#         case 404:
#             return "Not Found"
#         case 500:
#             return "Internal Server Error"
#         case _:
#             return "Unknown"

# print(httpstatus(200))
# print(httpstatus(404))
# print(httpstatus(500))
# print(httpstatus(600))

### lambda

# import math

# def square(x:int)->int:
#     return x*x
    
# print(square(5))

# square2 = lambda x:x*x
# print(square2(5))

# square3 = math.pow
# print(square3(5,2))


#### Exception handling

# try:
#     a = int(input("Enter a number : "))
#     print(a)
# except ValueError:
#     print("Invalid input")
# finally:
#     print("This will always be printed")


### Raising Exception

# a = int(input("Enter a number : "))
# b = int(input("Enter another number : "))

# if(b == 0):
#     ### Raising exception defined in the code itself 
#     raise ZeroDivisionError("Division by zero is not allowed")
# else:
#     print(a/b)


# #### try else 

# try:
#     a = int(input("Hey , Enter the number: "))
#     print(a)

# except Exception as e:
#     print(e)

# else:
#     print("If it goes to try then else will run")


#### use case of finally

# def main():
#     try:
#         a: int = int(input("Enter a number: "))
#         b : int = int(input("Enter a number: "))
#         print(a/b)
#     except Exception as e:
#         print(e)
#     finally:
#         print("Hey i will run for sure")
    
# main()


# ### if __Name__ == __main__



#### Global keyword
# a = 89
# def fun():
#     # global a 
#     a = 3
#     print(a)

# fun() 
# print(a)


### Enumerate

# l = [3 , 54 , 535]
# index = 0
# for i in l:
#     index+=1
#     print(f"The item number {index} is {i}")

### This is the another way of enumerating the list items 
# for index , item in enumerate(l):
#     print(f"The item at {index} is {item}")

#### List Comprehension

# myList = [1 , 2 , 3 ,4]

# squaredList = [i*i for i in myList]
# print(squaredList)

