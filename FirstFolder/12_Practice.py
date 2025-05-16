# l = [1 , 2, 3, 4, 5 , 6, 7, 8, 9]

# for i , item in enumerate(l):
#     if i == 2 or i == 4 or i  == 6:
#         print(item)


#### Problem 2

# n = 5

# table = [i*n for i in range(1 , 11)]
# print(table)


### Problem 3 ->zeroDivisionError

### Problem 4 --> 

n = int(input("Enter the number: "))

table = [i*n for i in range(1 , 11)]
print(table) 

try:
    with open("12_EnumTab.txt" , 'a') as f:
        f.write(str(table) + "\n")
except Exception as e:
    print(e)
