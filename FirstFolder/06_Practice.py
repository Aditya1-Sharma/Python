# Program to find the greatest of 4 number

# a1 = int(input("Enter number 1: "))
# a2 = int(input("Enter number 2: "))
# a3 = int(input("Enter number 3: "))
# a4 = int(input("Enter number 4: "))

# if(a1>=a2 and a1>=a3 and a1>=a4):
#     print("Greatest number is " , a1)
# elif(a2>=a1 and a2>=a3 and a2>=a4):
#     print("Greatest number is " , a2)
# elif(a3>=a1 and a3>=a2 and a3>=a4):
#     print("Greatest number is " , a3)
# elif(a4>=a1 and a4>=a3 and a4>=a2):
#     print("Greatest number is " , a4)


marks = []

print(type(marks))
res = ""
for i in range(1 , 6):
    ele = int(input(f"Enter the marks {i} :"))
    if(ele<33):
        res = "fail"
    marks.append(ele)

print(marks)
percentage = sum(marks)*100/500
if(percentage>=40 and res==""):
    print("You passed with a percentage of " , percentage)
else:
    print("You failed with a percentage of " , percentage)


#### Problem 3

## using in keyword in the string
# p1 = "Make a lot of money"
# p2 = "Buy Now"
# p3 = "Subcribe Now"
# p4 = "Click this"

# messgae = input("Enter your comment")

# if(p1 in messgae or p2 in messgae or p3 in messgae or p4 in messgae):
#     print("This comment is a spam")
# else:
#     print("Put this in the inbox")

#### PRoblem 4 

# username = input("Enter your username: ")

# if(len(username)<10):
#     print("User contain less than 10 char")
# else:
#     print("User contain more than 10 char")

#### Problem 5 :- Using in keyword in the list

# l = ["Harry" , "Aditya" , "Sanjana" , "Selena"]

# name = input("Enter your name")

# if(name in l):
#     print("Your name is present in the list")
# else:
#     print("Your name is not in the list")

### Problem 6 :- 

# marks = input("Enter your Marks: ")

# marks = int(marks)

# if(marks>=90 and marks <=100):
#     print("You have got A+ grade")
# elif(marks>=80 and marks<90):
#     print("You have got A grade")
# elif(marks>=70 and marks<80):
#     print("You have got B+ grade")
# elif(marks>=60 and marks<70):
#     print("You have got B grade")
# elif(marks>=50 and marks<60):
#     print("You have got C grade")
# elif(marks>=40 and marks<50):
#     print("You have got D grade")
# else:
#     print("You are fail")

#### Write a program to find post is about aditya or not

writePost = input("Write your post")
post = "Aditya is a good boy , a very smart anf intelligent person"

if("Aditya".lower() in post.lower()):
    print("This post is talking about aditya")
else:
    print("This post is not talking about aditya")
