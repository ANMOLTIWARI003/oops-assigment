# 1. Find the maximum of three numbers
def maximum_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

a = float(input("Enter first number : "))
b = float(input("Enter second number: "))
c = float(input("Enter third number : "))
print(f"Maximum of {a}, {b}, {c} = {maximum_of_three(a, b, c)}")


# 2. Sum all numbers in a list
def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

lst = [8, 2, 3, 0, 7]
print(f"\nList: {lst}")
print(f"Sum of all numbers: {sum_list(lst)}")


# 3. Multiply all numbers in a list
def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

lst = [8, 2, 3, -1, 7]
print(f"\nList: {lst}")
print(f"Product of all numbers: {multiply_list(lst)}")


# 4. Reverse a string
def reverse_string(s):
    return s[::-1]

s = "1234abcd"
print(f"\nOriginal String : {s}")
print(f"Reversed String : {reverse_string(s)}")


# 5. Calculate factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input("\nEnter a non-negative integer: "))
print(f"Factorial of {n} = {factorial(n)}")


# 6. Check whether a number falls within a given range
def check_range(num, low, high):
    if low <= num <= high:
        print(f"{num} IS within the range [{low}, {high}]")
    else:
        print(f"{num} is NOT within the range [{low}, {high}]")

num  = float(input("\nEnter a number     : "))
low  = float(input("Enter range start  : "))
high = float(input("Enter range end    : "))
check_range(num, low, high)


# 7. Count uppercase and lowercase letters in a string
def count_cases(s):
    upper = sum(1 for ch in s if ch.isupper())
    lower = sum(1 for ch in s if ch.islower())
    return upper, lower

s = "The quick Brow Fox"
upper, lower = count_cases(s)
print(f"\nSample String          : '{s}'")
print(f"No. of Upper case characters : {upper}")
print(f"No. of Lower case Characters : {lower}")

# 8. Return a new list with distinct elements from the first list
def distinct_elements(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

lst = [1, 2, 3, 3, 3, 4, 5]
print("Sample List  :", lst)
print("Unique List  :", distinct_elements(lst))


# 9. Check whether a number is prime or not
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

n = int(input("\nEnter a number to check prime: "))
if is_prime(n):
    print(f"{n} IS a Prime number.")
else:
    print(f"{n} is NOT a Prime number.")


# 10. Print even numbers from a given list
def print_even(lst):
    even = [num for num in lst if num % 2 == 0]
    return even

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\nSample List     :", lst)
print("Even Numbers    :", print_even(lst))


# 11. Check whether a number is Perfect or not
def is_perfect(n):
    if n <= 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

n = int(input("\nEnter a number to check perfect: "))
divisors = [i for i in range(1, n) if n % i == 0]
print(f"Proper divisors of {n}: {divisors}")
print(f"Sum of divisors     : {sum(divisors)}")
if is_perfect(n):
    print(f"{n} IS a Perfect number.")
else:
    print(f"{n} is NOT a Perfect number.")


# 12. Check whether a passed string is palindrome or not
def is_palindrome(s):
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

s = input("\nEnter a string to check palindrome: ")
if is_palindrome(s):
    print(f"'{s}' IS a Palindrome.")
else:
    print(f"'{s}' is NOT a Palindrome.")

# 13. Check whether a string is a pangram or not
def is_pangram(s):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet.issubset(set(s.lower()))

s = input("Enter a string to check pangram: ")
if is_pangram(s):
    print(f"'{s}' IS a Pangram.")
else:
    print(f"'{s}' is NOT a Pangram.")


# 14. Accept hyphen-separated words, sort alphabetically and print
def sort_hyphen_words(s):
    words = s.split("-")
    words.sort()
    return "-".join(words)

s = input("\nEnter hyphen-separated words (e.g. green-red-yellow): ")
print("Sorted Result:", sort_hyphen_words(s))


# 15. Create and print list of squares of numbers from 1 to 30
def squares_list():
    return [x**2 for x in range(1, 31)]

result = squares_list()
print("\nSquares from 1 to 30:")
print(result)


# 16. Chain of function decorators (bold, italic, underline)
def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

def underline(func):
    def wrapper():
        return "<u>" + func() + "</u>"
    return wrapper

@bold
@italic
@underline
def styled_text():
    return "Hello Python"

print("\nDecorator Chain Output:")
print(styled_text())


# 17. Execute a string containing Python code
def execute_code(code_string):
    exec(code_string)

code = "print('Hello from exec!') \nfor i in range(1,4): print(i)"
print("\nExecuting string as Python code:")
execute_code(code)


# 18. Access a function inside a function (nested function)
def outer_function():
    print("This is the outer function.")

    def inner_function():
        print("This is the inner function accessed inside outer.")

    inner_function()

print("\nNested Function:")
outer_function()


# 19. Detect number of local variables declared in a function
import inspect

def sample_function():
    a = 10
    b = 20
    c = 30

code_obj = sample_function.__code__
print("\nNumber of local variables in sample_function:", code_obj.co_nlocals)


# 20. Invoke a function after a specified period of time
import time
import math

def invoke_after(seconds, func, *args):
    time.sleep(seconds)
    return func(*args)

print("\nSquare root after specific milliseconds:")
print(invoke_after(0, math.sqrt, 16))
print(invoke_after(0, math.sqrt, 100))
print(invoke_after(0, math.sqrt, 25133))