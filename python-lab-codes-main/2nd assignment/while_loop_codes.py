
#  PYTHON WHILE LOOP PROGRAMS - 16 QUESTION


n = int(input("Enter value of n (used for most programs): "))


# 1. NATURAL NUMBERS UP TO N

print("\n--- 1. Natural Numbers up to", n, "---")
i = 1
while i <= n:
    print(i, end=" ")
    i += 1


# 2. EVEN NUMBERS UP TO N

print("\n\n--- 2. Even Numbers up to", n, "---")
i = 2
while i <= n:
    print(i, end=" ")
    i += 2


# 3. ODD NUMBERS UP TO N

print("\n\n--- 3. Odd Numbers up to", n, "---")
i = 1
while i <= n:
    print(i, end=" ")
    i += 2


# 4. SUM OF NATURAL NUMBERS UP TO N

print("\n\n--- 4. Sum of Natural Numbers up to", n, "---")
i = 1
total = 0
while i <= n:
    total += i
    i += 1
print(f"Sum = {total}")


# 5. SUM OF ODD NUMBERS UP TO N

print("\n--- 5. Sum of Odd Numbers up to", n, "---")
i = 1
total = 0
while i <= n:
    if i % 2 != 0:
        total += i
    i += 1
print(f"Sum of Odd Numbers = {total}")


# 6. SUM OF EVEN NUMBERS UP TO N

print("\n--- 6. Sum of Even Numbers up to", n, "---")
i = 1
total = 0
while i <= n:
    if i % 2 == 0:
        total += i
    i += 1
print(f"Sum of Even Numbers = {total}")


# 7. NATURAL NUMBERS IN REVERSE ORDER

print("\n--- 7. Natural Numbers from", n, "in Reverse ---")
i = n
while i >= 1:
    print(i, end=" ")
    i -= 1


# 8. FIBONACCI SERIES UP TO N

print("\n\n--- 8. Fibonacci Series up to", n, "---")
a, b = 0, 1
while a <= n:
    print(a, end=" ")
    a, b = b, a + b


# 9. FACTORIAL OF A GIVEN NUMBER

print("\n")
num9 = int(input("Enter a number for Factorial (Q9): "))
print(f"--- 9. Factorial of {num9} ---")
factorial = 1
i = 1
while i <= num9:
    factorial *= i
    i += 1
print(f"Factorial of {num9} = {factorial}")


# 10. PRIME OR NOT

num10 = int(input("\nEnter a number to check Prime (Q10): "))
print(f"--- 10. Prime Check for {num10} ---")
i = 2
is_prime = True
if num10 < 2:
    is_prime = False
while i <= num10 // 2:
    if num10 % i == 0:
        is_prime = False
        break
    i += 1
if is_prime:
    print(f"{num10} is a PRIME number.")
else:
    print(f"{num10} is NOT a prime number.")


# 11. SUM OF DIGITS OF A NUMBER

num11 = int(input("\nEnter a number to find Sum of Digits (Q11): "))
print(f"--- 11. Sum of Digits of {num11} ---")
temp = num11
total = 0
while temp > 0:
    digit = temp % 10
    total += digit
    temp //= 10
print(f"Sum of digits of {num11} = {total}")


# 12. PALINDROME OR NOT

num12 = int(input("\nEnter a number to check Palindrome (Q12): "))
print(f"--- 12. Palindrome Check for {num12} ---")
temp = num12
reversed_num = 0
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10
if num12 == reversed_num:
    print(f"{num12} is a PALINDROME.")
else:
    print(f"{num12} is NOT a palindrome.")


# 13. REVERSE A GIVEN NUMBER

num13 = int(input("\nEnter a number to Reverse (Q13): "))
print(f"--- 13. Reverse of {num13} ---")
temp = num13
reversed_num = 0
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10
print(f"Reverse of {num13} = {reversed_num}")


# 14. MULTIPLICATION TABLE

num14 = int(input("\nEnter a number for Multiplication Table (Q14): "))
print(f"--- 14. Multiplication Table of {num14} ---")
i = 1
while i <= 10:
    print(f"{num14} x {i} = {num14 * i}")
    i += 1

# 15. LARGEST OF N NUMBERS

count15 = int(input("\nHow many numbers to find Largest (Q15)? "))
print(f"--- 15. Largest among {count15} Numbers ---")
i = 1
largest = None
while i <= count15:
    num = float(input(f"  Enter number {i}: "))
    if largest is None or num > largest:
        largest = num
    i += 1
print(f"Largest number = {largest}")

# 16. SMALLEST OF N NUMBERS

count16 = int(input("\nHow many numbers to find Smallest (Q16)? "))
print(f"--- 16. Smallest among {count16} Numbers ---")
i = 1
smallest = None
while i <= count16:
    num = float(input(f"  Enter number {i}: "))
    if smallest is None or num < smallest:
        smallest = num
    i += 1
print(f"Smallest number = {smallest}")
