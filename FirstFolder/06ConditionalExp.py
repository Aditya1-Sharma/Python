age = int(input("Enter the age"))
if(age >= 18):
    print("You are above the age of consent")
elif(age<0):
    print("How can you enter negative age")
else:
    print("You are below the age of consent")

print("End of program")



## Elif conditional

#### Switch statement in python

age1 = int(input("Enter the age"))

match age:
    case 18:
        print("You are above the age of consent")
    case 0:
        print("How can you enter invalid age")
       
    case _:
        print("You are below the age of consent")


