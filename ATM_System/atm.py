class ATM:
    def __init__(self, balance: float):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")

        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive!")
        elif amount > self.balance:
            raise ValueError("Insufficient funds!")

        self.balance -= amount
        return True

    def __str__(self):
        return f"Your current balance is: {self.balance:.2f}€"
