class Employee:
    language = "Python"
    salary = 1200000

    def __init__(self , name , salary , langugae):  ### Dunder method which automatically called
        print("I am creating an object")
        self.name = name
        self.salary = salary
        self.language = langugae

    def getInfo(self):
        print(f"The language is {self.language} and salary is {self.salary}")
    @staticmethod
    def greet():
        print("Hello Good morning")
    
# aditya = Employee()
# aditya.language = "JS"


# Employee.getInfo(harry) 
# aditya.getInfo() ## It will be converted to above line 
# aditya.greet()

# Employee.getInfo(aditya) ##This will also work

### Init constructor

# harry = Employee()
# print(harry.getInfo())

selena = Employee("Selena" , 1300000 , "JavaScript")
selena.name = "Selena Gomez"
print(selena.name , selena.salary , selena.language)



