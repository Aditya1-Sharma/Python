a = 1
b = 2
c = 3

def greatest(a , b , c):
    if(a>b and b>c): return a
    elif(b>a and b>c) : return b
    else: return c
greatest = greatest(a , b , c)
# print(greatest)



## Recursive function to print sum of n number

# n = int(input("Enter the number"))
def recSum(n):
    if(n<1):
        return n
    else:
        return n+recSum(n-1)

# natSum = recSum(n)
# print(natSum)

### Recursive functiont to print the pattern

def pattern(n):
    if(n==0):return
    print("*"*n)
    return pattern(n-1)
pattern(5)

### inches to cm
# n = int(input("Enter the inches: "))
# def inch_to_cm(n):
#     return 2.54*n

# print(inch_to_cm(n))


### Problem 7 
l = ["Harry" , "Rohan" ,"Shubham" , "Roshan" , "an" , "Lasando"]

def remList(l , word):
    n = []
    for item in l:
        if not (item == word):
            n.append(item.strip(word))
    return n
print(remList(l , "an"))



