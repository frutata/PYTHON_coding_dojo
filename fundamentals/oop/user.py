from Python.fundamentals.oop.bank_account import BankAccount


class User:
    def __init__(self, name):
        self.name = name
        self.amount = 0
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account.balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name} currently has ${self.account.balance} in their account.")
        return self

    def transfer_money(self, amount, user):
        self.account.balance -= amount
        user.accout.balance += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

JP = User("JP")
Kelly = User("Kelly")
Tyler = User("Tyler")

JP.make_deposit(50).make_deposit(50).make_deposit(50).display_user_balance().make_withdrawal(50).display_user_balance()

print("-------------------------")

Kelly.make_deposit(100).make_deposit(100).display_user_balance().make_withdrawal(100).display_user_balance()

print("-------------------------")

Tyler.make_deposit(500).display_user_balance().make_withdrawal(25).make_withdrawal(25).make_withdrawal(25).display_user_balance()

print("-------------------------")

JP.transfer_money(100, Tyler)