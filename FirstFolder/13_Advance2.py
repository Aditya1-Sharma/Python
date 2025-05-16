from functools import reduce
# Lambda function -> creating function using the expression

# square = lambda x:x**x

# print(square(4))

### Join Method

# a = ["Harry" , "Ron" , "Hermione"]

# final = "::".join(a)

# print(final)


### List Comprehension

# a = [i for i in range(10)]

# print(a)

### Formatting Strings
# a = "{0} is {1} years old".format("Harry" , 10)
# print(a)

### MAp filter and reduce

a = [1,2,3,4,5,6,7,8,9,10]

# b = map(lambda x:x**2, a)

# c = list(b)
# print(c)


#### filter
# def even(n):
#     if(n%2==0):
#         return True
#     return False
# onlyEven = filter(even , a)
# print(list(onlyEven))

#### reduce

# def sum(a , b):
#     return a+b

sum = lambda c, d: c + d

print(reduce(sum , a))