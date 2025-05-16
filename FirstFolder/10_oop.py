class Employee:
    language = "Python"
    salary = 1200000


harry =  Employee()
harry.name = "Harry" ## Instance attribute
print(harry.language , harry.salary)
rohan = Employee()
rohan.name = "Rohon ro robin"
print(rohan.salary , rohan.language , rohan.name)

### Here name is the object attribute and the language and salary is the class attribute as they belong to the class


### Instance vs class attribute

aditya = Employee()

aditya.language = "Javascript"

print(aditya.language)