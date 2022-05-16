class BankAccount:
    def __init__(self, int_rate = 0.2, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, balance):
        self.balance += balance
        return self

    def withdraw(self, balance):
        if (self.balance > 0):
            self.balance -= balance
        else:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_balance(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if (self.balance > 0):
            self.balance += self.balance * self.int_rate
        return self

Checkings = BankAccount()
Savings = BankAccount()

Checkings.deposit(50).deposit(50).deposit(50).withdraw(100).yield_interest().display_account_balance()

print("-------------------")

Savings.deposit(100).deposit(200).withdraw(25).withdraw(25).withdraw(50).withdraw(25).yield_interest().display_account_balance()