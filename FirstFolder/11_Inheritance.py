class Employee:
    company="ITC"
    name = "Harry"
    salary = 1200000
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")
    
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.showLanguage} language")


class Programmer(Employee):
    company = "ITC infotech"
    
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.showLanguage} language")


a = Employee()
b = Programmer()

print(a.company , b.company)

b.show()