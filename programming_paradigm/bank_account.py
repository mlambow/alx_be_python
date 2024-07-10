class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
        account_balance = 0

    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.account_balance += amount
        print(f"Amount Deposited: ", amount)

    def withdraw(self):
        amount = float(input("Enter amount to withdrawn: "))
        if self.account_balance >= amount:
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ", self.account_balance)