words = {
    "maddad": "Help",
    "kursi": "chair",
    "kitab": "Book"
}

# word = input("Enter the word to be searched : ")

# print(words[word])

# s = set()
# for i in range(1,9):
#     ele = int(input("Enter the number: "))
#     s.add(ele)

# print(list(s))


# Question 3 : To add the 18 and '18' in the set
print("Question 3 : To add the 18 and '18' in the set")
s1 = set()
s1.add(18)
s1.add('18')

print(s1)

# Question 4 what will be the length of the set

s2 = set()
s2.add(20)
s2.add(20.0)
s2.add('20')
print(len(s2))  # It will give 2
print(20.0 == 20)  # It will give True

#  Question 5
s = {}
print(type(s))  # dict


# Qusetion 6
# s = {}

# for i in range(1 , 6):
#     name = input("Enter the name : ")
#     lang = input("Enter the langunage : ")
#     s.update({name: lang})
# print(s)


# Question 9

# can you change the value inside the set
print("Question 9 : can you change the value inside the set ")
s4 = {8, 7, 12, "Harry", [1, 2]}
