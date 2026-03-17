class User:

    def __init__(self, name):
        self.name = name

u = User("Rahul")

print(u) #<__main__.User object at 0x000001E2B8C9F250> address of the object in memory not a human readable format

'''__str__ method is used to return a human readable format of the object when we print the object. 
It is a special method that is called when we print the object. It should return a string that represents the object.
'''


class User:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User name is {self.name}"  
u = User("Rahul")
print(u) #User name is Rahul