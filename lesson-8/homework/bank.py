import json
import os

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance
        }

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        if initial_deposit < 0:
            print("Initial deposit must be a positive amount!")
            return
        account_number = str(len(self.accounts) + 1).zfill(6)
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        self.save_to_file()
        print(f"Account created successfully! Your account number is {account_number}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Account Number: {account.account_number}\nName: {account.name}\nBalance: ${account.balance}")
        else:
            print("Account not found!")

    def deposit(self, account_number, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Deposit amount must be positive!")
            account = self.accounts.get(account_number)
            if account:
                account.balance += amount
                self.save_to_file()
                print(f"Deposited ${amount}. New balance: ${account.balance}")
            else:
                print("Invalid account number!")
        except ValueError as e:
            print(f"Error: {e}")

    def withdraw(self, account_number, amount):
        try:
            amount = float(amount)
            account = self.accounts.get(account_number)
            if not account:
                print("Invalid account number!")
                return
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive!")
            if amount > account.balance:
                print("Insufficient funds!")
                return
            account.balance -= amount
            self.save_to_file()
            print(f"Withdrew ${amount}. New balance: ${account.balance}")
        except ValueError as e:
            print(f"Error: {e}")

    def save_to_file(self):
        try:
            with open("information.json", "w") as file:
                json.dump({acc: self.accounts[acc].to_dict() for acc in self.accounts}, file)
        except Exception as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self):
        if os.path.exists("information.json"):
            try:
                with open("information.json", "r") as file:
                    data = json.load(file)
                    self.accounts = {acc: Account(**details) for acc, details in data.items()}
            except json.JSONDecodeError:
                print("Error reading file. Data might be corrupted!")

# Command-line Interface
def main():
    bank = Bank()
    while True:
        print("\nBanking System")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter your name: ")
            try:
                initial_deposit = float(input("Enter initial deposit amount: "))
                bank.create_account(name, initial_deposit)
            except ValueError:
                print("Invalid amount! Please enter a valid number.")
        elif choice == "2":
            acc_number = input("Enter account number: ")
            bank.view_account(acc_number)
        elif choice == "3":
            acc_number = input("Enter account number: ")
            amount = input("Enter amount to deposit: ")
            bank.deposit(acc_number, amount)
        elif choice == "4":
            acc_number = input("Enter account number: ")
            amount = input("Enter amount to withdraw: ")
            bank.withdraw(acc_number, amount)
        elif choice == "5":
            print("Thank you for using our banking system!")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()
