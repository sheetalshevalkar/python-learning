class Wallet:
    def __init__(self,name, money):
        self.name=name
        self.money=money
    def __add__(self, other):
          return self.money + other.money
    def __sub__(self, other):
         return self.money - other.money
    def __mul__(self, other):
         return self.money * 2
    def __truediv__(self, other):
            return self.money / 2
    def __str__(self):
        return f"{self.name} has {self.money} money in wallet"


w1 = Wallet("Rahul", 500)
w2 = Wallet("Sheetal", 300)

print(w1 + w2)  # → 800
print(w1 - w2)  # → 200
print(w1 * 2)   # → 1000
print(w1 / 2)   # → 250
print(w1)
print(w2)