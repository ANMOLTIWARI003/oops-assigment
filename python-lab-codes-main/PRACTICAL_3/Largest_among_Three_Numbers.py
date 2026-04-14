a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(f"Largest = {a}")
elif b >= a and b >= c:
    print(f"Largest = {b}")
else:
    print(f"Largest = {c}")