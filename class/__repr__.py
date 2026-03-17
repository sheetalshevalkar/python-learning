class User:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User name is {self.name}"

    def __repr__(self):
        return f"User name is {self.name}"
    def __len__(self):
        return len(self.name)

u = User("Rahul")
print(u) #User name is Rahul
print(repr(u)) #User name is Rahul
print(len(u)) #5