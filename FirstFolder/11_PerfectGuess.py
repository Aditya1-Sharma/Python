from random import randint

n = randint(1 , 100)
a = -1
guess = 0
while(a!=n):
    guess+=1
    a = int(input("Guess a number"))
    if(a == n) :
        break
    elif(a>n):
        print("Please guess the lower number")
    else:
        print("Please guess the higher number")

print("Guess attempt:", guess)

