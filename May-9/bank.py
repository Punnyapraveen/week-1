class BankAccount:
    def __init__(self, owner, initial_balance=0):
        # Initialize account with owner name and starting balance
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        # Add money to the account
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Subtract money if funds are sufficient
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")

    def get_balance(self):
        # Return current balance
        return self.balance

# Create account
owner = input("Enter account owner name: ")
initial = float(input("Enter initial balance: "))
account = BankAccount(owner, initial)

# Menu loop
while True:
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amt = float(input("Enter amount to deposit: "))
        account.deposit(amt)
    elif choice == "2":
        amt = float(input("Enter amount to withdraw: "))
        account.withdraw(amt)
    elif choice == "3":
        print(f"Current balance: ${account.get_balance()}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
