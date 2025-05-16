# print('''Twinkle twinkle little star.
# How I wonder what you are.
# Up above the world so high.
# Like a diamond in the sky.
# Twinkle twinkle little star.
# How I wonder what you are.

# Twinkle twinkle little star.
# How I wonder what you are.
# Up above the world so high.
# Like a diamond in the sky.
# Twinkle twinkle little star.
# How I wonder what you are.''')


# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Aditya is a cool developer")
# engine.runAndWait()


# Power of Os module

import os

# Specific directory you want to list

directory_path = "/Users/All Users"
# List all files and directory
content = os.listdir(directory_path)
userId = os.getpid()

print(userId)

for item in content:
    print(item)






