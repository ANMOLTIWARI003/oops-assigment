age = int(input("Enter your age: "))

if age >= 18:
    print("You ARE eligible to vote in India.")
else:
    print(f"You are NOT eligible to vote. You need {18 - age} more year(s).")