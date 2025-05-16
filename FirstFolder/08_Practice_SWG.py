
'''
1-> Snake
-1-> water
0 -> gun
'''

import random


i = 1
while(i<6):
   
    comp =  random.randint(-1 , 1)
    
    youStr = input("Enter your choice: ")
    youDict = {"s":1, "w":-1, "g":0}

    you = youDict[youStr.lower()]
    print(comp , you)
    if(comp == -1 and you ==1):
        print("You win")
    elif(comp == 1 and you == -1):
        print("Comp win")
    elif(comp ==-1 and you == 0):
        print("comp win")
    elif(you == 0 and comp == -1):
        print("You win")
    elif(comp == 0 and you == 1):
        print("Comp win")
    elif(you == 0 and comp == 1):
        print("You win")
    elif(comp == 0 and you == -1):
        print("You win")
    elif(comp == -1 and you == 0):
        print("Comp win")
    elif(comp == you):
        print("Draw")
    else:
        print("Something went wrong")
    i+=1