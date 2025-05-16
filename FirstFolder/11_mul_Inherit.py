class Employee:
    name = "Aditya"
    salary = 1000000

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
    
class Coder:
    language = "Python"
    def print(self):
        print(f"Out of all language here is your language : {self.language}")
    

class Programmer(Employee , Coder):
    company = "Itc Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language}")


a = Employee()
b = Programmer()

b.show()
b.print()
b.showLanguage()