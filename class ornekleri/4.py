class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(f"Owner: {self.owner}, Balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} dollars deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Here’s your money  New balance: {self.balance}"
        else:
            return "Insufficient funds ❌"

p1 = BankAccount("Isil", 800)
p1.show_balance()
p1.deposit(100)
print(p1.withdraw(200))
