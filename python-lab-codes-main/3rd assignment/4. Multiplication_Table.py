num = int(input("Enter a number: "))
i = 1
print(f"\nMultiplication Table of {num}:")
print("-" * 20)
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1
