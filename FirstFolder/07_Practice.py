# n = input("Enter the number")
# for i in range(1 , 11):
#     print(f"{n} * {i} = ", int(n)*i)



# Greet if name start with the s

# l = ["Shubham" , "Aditya" , "Sanjana"]

# for i in l:
#     if(i.startswith("S")):
#         print(f"Hello {i}")


### Problem 3

# n = input("Enter the number")
# i = 1
# while(i<11):
#     print(f"{n} * {i} = ", int(n)*i)
#     i+=1


### Problem 4: To find wheather number is prime or not

# n = int(input("Enter a number"))

# for i in range(2 , n):
#     if(n%i == 0):
#         print("Number is not prime")
#         break
# else:
#     print("Number is prime")

### sum of first n natural number
# n = int(input("Enter a number"))
# i = 1
# sum = 0
# while(i<=n):
#     sum+=i
#     i+=1
# print(sum)

### Problem 6: Factorial of a number

# n = int(input("Enter the number"))
# fact = 1

# for i in range(1 , n+1):
#     fact*=i
# print(fact)

### Problem 7:

# n = int(input("Enter the number"))
# for i in range(1 , n+1):
#     print(" " * (n-i),end="")
#     print("*" * (2*i -1))
#     print("\n")

### Proble 8
# n = int(input("Enter the number"))
# for i in range(1 , n+1):
#     print("*" * (i))
#     # print("\n")


#### Problem 9
''''
***
* *
***

'''

# n = int(input("Enter the number"))

# for i in range(1 , n+1):
#     if(i == 1 or i == n):
#         print("*"* (n))
#     else:
#         print(f"*{ (n-2) *' '}*")


### Print table in reverse order

n = int(input("Enter the number"))
for i in range(10 , 0 , -1):
    print(f"{n} * {i} = {i*n}")
