# Creating file in a particular directory

import os
import random
directory = os.getcwd()

fileName = "09_Practice.txt"

poemFile = "09_twinkle.txt"

file_path = os.path.join(directory , "FirstFolder" ,poemFile)

print(file_path)
#### Writing from the file

# with open(file_path , 'w') as f:
#     f.write("This is a sample practice file created\n")
#     f.write("This is a awesome course done by me ")
#     print("File Created")

### Reading from the file 

# with open(file_path ) as f:
#     content = f.read()
#     if("twinkle" in content):
#         print("This poem is twinle twinkle")
#     else:
#         print("Word twinke is not present")
    


### Important
# file_path = "hiscore.txt"

# def game():
#     print("You are playing the game")
#     score = random.randint(1, 62)

#     # Fetch the hiscore
#     try:
#         with open(file_path, 'r') as f:
#             hiscore = f.read()
#             hiscore = int(hiscore) if hiscore else 0
#     except FileNotFoundError:
#         hiscore = 0

#     print(f"Your score: {score}")

#     if score > hiscore:
#         # Write the hiscore into the file
#         with open(file_path, 'w') as f:
#             f.write(str(score))
#         print("New high score!")

#     return score

# game()


### Generate table

# def generateTable(n):
#     table = ""
#     for i in range(1 , 11):
#         table += f"{n} X {i} = {n*i}\n"
    
#     with open(f"tables/table_{n}" , 'w') as f:
#         f.write(table)

# for i in range(2 , 21):
#     generateTable(i)


### Replace the word donkey


# word = "Donkey"

# with open("09_ReplaceDonkey.txt", 'r') as f:
#     content = f.read()
#     print(content)

# newContent = content.replace(word , "#####")
# newContent1 = newContent.replace("donkey" , "#####")

# with open("09_ReplaceDonkey.txt" , 'w') as f:
#     f.write(newContent1)



### Replace the word for censored

# words = ["Donkey" , "bad" , "ganda"]

# with open("09_ReplaceDonkey.txt", 'r') as f:
#         content = f.read()
#         print(content)

# for word in words:
#     content = content.replace(word , "#" * len(word))
#     print(content)
    
# with open("09_ReplaceDonkey.txt" , 'w') as f:
#     f.write(content)
   

### To find the line where python is present

# with open("log.txt" , 'r') as f:
#     content = f.readlines()
#     cnt= 1
#     for line in content:
#         if("Python" in line):
#             print(cnt , end="")
#             break
#         cnt+=1  
#     else:
#         print("Done !")
    


### Problem 9: to check wheather the file1 is identical to file2

### Problem 10 to wipe out the content of file 

# with open("log.txt" , 'w') as f:
#     f.write("")


### just check the shutil