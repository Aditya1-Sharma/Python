## fstring
# name = input("Enter your name")
# print(f"Good Afternoon {name}")

# Problem2
letter = ''' Dear <|Name|>
you are selected!
<|Date|>
            '''
print(letter.replace("<|Name|>" , "Aditya").replace("<|Date|>" , "23 May 2025"))

# Detect double space in the string

name = "Aditya is a good  boy"
print(name.find("  "))

# Replace the double space with single space

## Immutability of the string : the copy of the string is created not the 
print(name.replace("  " , " "))


