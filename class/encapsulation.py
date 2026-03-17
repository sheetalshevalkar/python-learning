# class Wallet:
#     # def __init__(self, money):
#     #     self.__money = money    

#     def show_money(self, money):
#         print(f"Money in wallet is {money}")

# wallet = Wallet()
# wallet.show_money(1000)
# # wallet.__money = 5000
# # print(wallet.__money)
# # # wallet.show_money()


class Online_bank:
    __customer_info = {
        "john_doe": ["password123", 1000],
        "jane_smith": ["securepass", 2000],
        "alice_jones": ["mypassword", 1500],
        "sheetal": ["12345", 2000]
    }

    def __init__(self, name, password):
        self._name  = name
        self.password = password

    def login(self, user_name, password):
        if user_name in Online_bank.__customer_info:
            stored_password, stored_balance = Online_bank.__customer_info[user_name]
            if password == stored_password:
                print("Login successful")
                self.stored_balance = stored_balance
                return True
        print("Invalid username or password")
        return False
    
    
    def show_balance(self):
        print(f"Your balance is {self.stored_balance}")
    
    def deposit(self, amount):
        self.stored_balance += amount
        Online_bank.__customer_info[self._name][1] = self.stored_balance
        print(f"your current balance is {self.stored_balance}")
    
    def withdraw(self, amount):
        if self.stored_balance >= amount:
            self.stored_balance -= amount
            Online_bank.__customer_info[self._name][1] = self.stored_balance
            print(f"your current balance is {self.stored_balance}")
        else:
            print("Insufficient balance")
        

user = input("Enter username: ")
password = input("Enter password: ")

bank = Online_bank(user, password)
if bank.login(user, password):
    bank.show_balance() 
    # get custome approval for deposit and withdraw
    service = input("Enter service (deposit/withdraw): ")
    if service == "deposit":
        amount = float(input("Enter amount to deposit: "))
        bank.deposit(amount)
    elif service == "withdraw":
        amount = float(input("Enter amount to withdraw: "))
        bank.withdraw(amount)
    elif service == "none":
        exit()

print("Thank you for using our service")
  