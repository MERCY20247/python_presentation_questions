#3) Create a class called BankAccount with attributes account_number and balance. Add methods to:
# Deposit an amount
# Withdraw an amount (only if sufficient balance exists)
# Print the account balance.
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")
    def check_balance(self):
        print(f"Balance: {self.balance}")
account = BankAccount(12345,2000)
account.deposit(1000)
account.withdraw(500)
account.check_balance()

        