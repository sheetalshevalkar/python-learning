class Online_bank:
    __customer_info = {
        "john_doe": ["password123", 1000],
        "jane_smith": ["securepass", 2000],
        "alice_jones": ["mypassword", 1500]
    }

    def __init__(self, name, password):
        self._name  = name
        self.password = password

    def login(self, user_name, password):
        if user_name in self.customer_info:
            stored_password, stored_balance = Online_bank.__customer_info[user_name]
            if password == stored_password:
                print("Login successful")
                return True
        print("Invalid username or password")
        return False
    
    
    def show_balance(self):
        print(f"Your balance is {self.stored_balance}")
    
    def deposit(self, amount):
        pass
    def withdraw(self, amount):
        pass

user = input("Enter username: ")
password = input("Enter password: ")
bank = Online_bank(user, password)
if bank.login(user, password):
    bank.show_balance() 