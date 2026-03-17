class ATM:

    bank_name = "State Bank"

    customer_info = {
        "rahul": ["123456", 1000],
        "sheetal": ["567890", 2000],
        "suraj": ["1234", 2000]
    }

    def __init__(self, user_name, password, email):
        self.user_name = user_name
        self.password = password
        self.email = email
        self.balance = 0

    def login(self):

        if self.user_name in ATM.customer_info:

            stored_password, stored_balance = ATM.customer_info[self.user_name]

            if self.password == stored_password:
                self.balance = stored_balance
                print("Login successful")
                return True

        print("Login failed")
        return False


    def show_balance(self):
        print(f"Your balance is {self.balance}")


    def deposit(self, amount):
        self.balance += amount
        ATM.customer_info[self.user_name][1] = self.balance
        print(f"Your new balance is {self.balance}")


    def withdraw(self, amount):

        if self.balance >= amount:

            self.balance -= amount
            ATM.customer_info[self.user_name][1] = self.balance
            print(f"Your new balance is {self.balance}")

        else:
            print("Insufficient balance")


    @staticmethod
    def validate_email(email):

        if email.endswith("@gmail.com"):
            print("Valid Gmail")

        elif email.endswith("@yahoo.com"):
            print("Valid Yahoo")

        else:
            print("Invalid email")


    @classmethod
    def show_bank(cls):
        print(f"Welcome to {cls.bank_name}")


user_name = input("Enter username: ")
password = input("Enter password: ")
email = input("Enter email: ")

atm = ATM(user_name, password, email)

if atm.login():

    atm.show_balance()

    deposit_choice = input("Do you want to deposit money? (yes/no): ")

    if deposit_choice.lower() == "yes":
        amount = int(input("Enter amount to deposit: "))
        atm.deposit(amount)


    withdraw_choice = input("Do you want to withdraw money? (yes/no): ")

    if withdraw_choice.lower() == "yes":
        amount = int(input("Enter amount to withdraw: "))
        atm.withdraw(amount)