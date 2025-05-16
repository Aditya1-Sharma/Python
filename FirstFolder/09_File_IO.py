import os


### Creating a file in particular directory
# directory = os.getcwd()
# print(directory)

# filename = "09_File.txt"

# file_path = os.path.join(directory, filename)
# print(file_path)

# with open(file_path, "w") as file:
#     file.write("This is a new file created by python.")
#     print("File created.")


### Reading from a file
# f = open("09_File.txt", "r")
# print(f.read())
# f.close()


### Writing in a file
# string = "Aditya is a good boy"

# f = open("09_File.txt", "w" )

# f.write(string)
# f.close()

#### readlines function
####  readline function

# f = open("09_File.txt")
# line1 = f.readlines()
# print(line1)
# f.close()

### Append the file

# strAppend = "Hey adi you are amazing\n"
# f = open("09_File.txt" , "a")
# f.write(strAppend)
# f.close()

