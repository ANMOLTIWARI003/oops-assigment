# Menu Driven Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a % b

print("LAB ASSIGNMENT 1 - CALCULATOR")
while True:
    print("\n===== CALC MENU =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")
    choice = input("Enter choice: ")

    if choice == "6":
        print("Exiting Calculator...")
        break

    if choice in ["1","2","3","4","5"]:
        a = float(input("Enter first number : "))
        b = float(input("Enter second number: "))

        if   choice == "1": print(f"Result: {add(a, b)}")
        elif choice == "2": print(f"Result: {subtract(a, b)}")
        elif choice == "3": print(f"Result: {multiply(a, b)}")
        elif choice == "4": print(f"Result: {divide(a, b)}")
        elif choice == "5": print(f"Result: {modulus(a, b)}")
    else:
        print("Invalid choice! Try again.")