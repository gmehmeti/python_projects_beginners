import atm


class ATMController:
    def __init__(self, balance):
        self.atm = atm.ATM(balance)

    def get_amount(self, text: str):
        while True:
            try:
                amount = float(input(f"Enter the amount to {text}: "))
                return amount
            except ValueError as e:
                print("Please enter a valid number!")

    def display_menu(self):
        print("\nWelcome to the ATM!")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

    def check_balance(self):
        balance = self.atm.check_balance()
        print(f"Your current balance is: {balance:.2f}€")

    def deposit(self):
        while True:
            try:
                amount = self.get_amount("deposit")
                noError = self.atm.deposit(amount)
                if noError:
                    print(f"Successfully deposited {amount}€")
                    break
            except ValueError as e:
                print(e)

    def withdraw(self):
        while True:
            try:
                amount = self.get_amount("withdraw")
                noError = self.atm.withdraw(amount)
                if noError:
                    print(f"Successfully withdraw {amount}€")
                    break
            except ValueError as e:
                print(e)

    def run(self):
        while True:
            self.display_menu()

            choice = input("Please choose an option: ")
            if choice == "1":
                self.check_balance()

            elif choice == "2":
                self.deposit()

            elif choice == "3":
                self.withdraw()

            elif choice == "4":
                print("Thank you for using the ATM")
                break
            else:
                print("Invalid choice. Please try again.")
