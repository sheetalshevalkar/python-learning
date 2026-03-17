def add_method(cls):

    def greet(self):
        print("Hello", self.name)

    cls.greet = greet

    return cls

@add_method
class Person:
    def __init__(self, name):
        self.name = name    
    
p = Person("Sheetal")
p.greet()