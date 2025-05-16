from functools import reduce
### PRoblem2

# name = input("Enter the name: ")
# marks = int(input("Enter the marks: "))
# phoneNo = int(input("Enter the phone number: "))

# s = "The student name is {} , his phone number is{} and he got {} marks".format(name , phoneNo , marks)
# print(s)

### Problem 3

# table = [str(7*i) for i in range(1 , 11)]

# s = "\n".join(table)

# print(s)


#### Problem 5

def divBy5(n):
    if(n%5==0):
        return True
    return False

def greater(a , b):
    if(a>b):
        return a
    return b

a = [1 , 10 , 23 , 21 , 10 , 15 ]

b = list(filter(divBy5 , a))
c = reduce(greater , a)
print(b)
print(c)