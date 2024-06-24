class BankAccount:
    def __init__(self,account_number,password):
        self.account_number = account_number
        self.password       = password
        self.balance        = 0.0

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance:${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self,amount):
        if amount>0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance
    def change_password(self, old_password, new_password):
        if self.password == old_password:
            self.password = new_password
            print("Password changed successfully.")
        else:
            print("Old password is incorrect")

def create_account(accounts):
    account_number = input("Enter account number:")
    if account_number in accounts:
        print("Account already exists")
        return
    password =input("Enter password:")
    accounts[account_number] = BankAccount(account_number,password)
    print("Account created successfully.")

def login(accounts):
    account_number = input("Enter account number:")
    password       = input("Enter password:")
    account        = accounts.get(account_number)
    if account and account.password == password:
       print("Login successful.")
       return account
    else:
        print("Invalid account number or password.")
        return None

def main():
    accounts ={}
    while True:
        print("\nWelcome to the Banking system")
        print("1.Create Account")
        print("2.Login")
        print("3.Exit")
        choice = input("Enter your choice:")

        if choice == "1":
             create_account(accounts)
        elif choice =="2":
            account = login(accounts)
            if account:
                while True:
                     print("\nAccount Menu")
                     print("1.Deposit")
                     print("2.withdraw")
                     print("3.view Balance")
                     print("4.Change password")
                     print("5.Logout")
                     sub_choice =input("Enter your choice:")

                     if sub_choice == "1":
                         amount = float(input("Enter amount to deposit:"))
                         account.deposit(amount)
                     elif sub_choice == "2":
                         amount = float(input("Enter amount to withdraw:"))
                         account.withdraw(amount)
                     elif sub_choice == "3":
                         balance = account.get_balance()
                         print(f"Current balance:${balance:.2f}")
                     elif sub_choice == "4" :
                         old_password = input("Enter old password:")
                         new_password = input("Enter new password:")
                         account.change_password(old_password, new_password)
                     elif sub_choice == "5":
                         print("Logging out...")
                         break
                     else:
                         print("Invalid choice.please try again")

        elif choice == "3":
            print("Thank you for using the Banking system.Goodbye!")
            break
        else:
            print("Invalid choice.please try again.")

if __name__== "__main__":
    main()










