# Menu Driven Bank Account

def display_balance(balance):
    print(f"\nCurrent Balance: Rs. {balance:.2f}")

def deposit(balance):
    amount = float(input("Enter amount to deposit: Rs. "))
    if amount <= 0:
        print("Invalid amount!")
    else:
        balance += amount
        print(f"Rs. {amount:.2f} deposited successfully.")
    return balance

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: Rs. "))
    if amount <= 0:
        print("Invalid amount!")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print(f"Rs. {amount:.2f} withdrawn successfully.")
    return balance

print("\nLAB ASSIGNMENT 2 - BANK ACCOUNT")
name    = input("Enter Account Holder Name: ")
balance = float(input("Enter Initial Balance   : Rs. "))

while True:
    print(f"\n===== BANK MENU ({name}) =====")
    print("1. Display Balance")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Exit")
    choice = input("Enter choice: ")

    if   choice == "1": display_balance(balance)
    elif choice == "2": balance = deposit(balance)
    elif choice == "3": balance = withdraw(balance)
    elif choice == "4":
        print("Thank you for using our Bank. Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")