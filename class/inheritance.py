# class Vehicle():
#     def start(self):
#         print("The cars has started")

# class Car(Vehicle):
#     def drive(self):
#         print("The car is driving")

# car = Car()
# car.start()
# car.drive()


class Emp:
    cmp_lang = "java"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary   
         
    def emp_info(self):
        print(f" {self.name} is a {self.cmp_lang} developer")
        
class Dev(Emp):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
    def emp_info(self):
        if self.name == "Rahul":
           print(f"{self.name} works on {self.language} and his salary is {self.salary}")
        else:
            super().emp_info()
name=input("Enter the name of the employee: ")
dev1 = Dev(name, 50000, "Python")
dev1.emp_info()