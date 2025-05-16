### Function and recursion

# a = 12
# b = 45
# c = 56
# avg = (a+b+c)/3
# print(avg)


### Function

# Function Defenation
def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))

    average = (a+b+c)/3
    print(average)

## Function call
# avg()

### Quick Quiz

def goodDay(name , ending):
    print(f"Good Day {name} \n{ending}" )

# goodDay("Aditya")
# goodDay("Rohan" , "Thankyou")


### Default Parameter value

def goodDay(name , ending = "Thankyou"):
    print(f"Good Day, {name}")
    print(ending)
# goodDay("Aditya")
# goodDay("Selena" , "Thanks")






