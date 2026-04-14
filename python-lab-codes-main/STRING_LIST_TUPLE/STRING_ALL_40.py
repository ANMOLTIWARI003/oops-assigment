# PYTHON STRING PROGRAMS - ALL 40 QUESTIONS

# 1. Access and print characters from a string
s = "Hello Python"
print("First:", s[0], "| Last:", s[-1], "| Index 4:", s[4])

# 2. Print a string and extract characters
s = "Programming"
print("Full String:", s)
print("First 4 chars:", s[:4])
print("Chars 2 to 6:", s[2:7])

# 3. Print words with their length
sentence = "Python is easy to learn"
for word in sentence.split():
    print(f"'{word}' -> Length: {len(word)}")

# 4. Print EVEN length words
sentence = "Python is easy to learn"
print("Even length words:")
for word in sentence.split():
    if len(word) % 2 == 0:
        print(word)

# 5. Count vowels in a string
s = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for ch in s if ch in vowels)
print(f"Vowels in '{s}': {count}")

# 6. Passing string value to a function
def greet(name):
    print(f"Hello, {name}! Welcome to Python.")
greet("Student")

# 7. Create multiple copies using multiplication operator
s = "Hi! "
print(s * 4)

# 8. Appending text at end using += operator
s = "Hello"
s += " World! Python is great."
print(s)

# 9. Concatenate two strings using + operator
s1 = "Hello "
s2 = "Python"
s3 = s1 + s2
print("Concatenated:", s3)

# 10. Check if substring exists using 'in' operator
s = "Python is a powerful language"
sub = "powerful"
if sub in s:
    print(f"'{sub}' is present in the string.")
else:
    print(f"'{sub}' is NOT present.")

# 11. Assign Hexadecimal value and print in string format
hex_val = 0x1F4
print(f"Hex 0x1F4 = {hex_val} (decimal) = {hex(hex_val)} (hex)")

# 12. Print double quotes with string variable
s = "He said, \"Python is amazing!\""
print(s)
s2 = 'She replied, "Yes, it is!"'
print(s2)

# 13. Ignoring escape sequences (raw string)
s = r"C:\Users\new_folder\test.txt"
print("Raw string:", s)

# 14. Calculate number of all possible substrings
s = "abcd"
n = len(s)
total = n * (n + 1) // 2
print(f"Total substrings of '{s}': {total}")
for i in range(n):
    for j in range(i+1, n+1):
        print(s[i:j], end=" ")
print()

# 15. Reverse a string (5 different ways)
s = "Python"
print("1. Slicing       :", s[::-1])
print("2. reversed()    :", "".join(reversed(s)))
rev = ""
for ch in s:
    rev = ch + rev
print("3. For loop      :", rev)
rev2 = ""
i = len(s) - 1
while i >= 0:
    rev2 += s[i]
    i -= 1
print("4. While loop    :", rev2)
lst = list(s)
lst.reverse()
print("5. list.reverse():", "".join(lst))

# 16. Reverse a string using stack and reversed method
s = "Python"
stack = list(s)
rev_stack = ""
while stack:
    rev_stack += stack.pop()
print("Stack reverse    :", rev_stack)
print("reversed() method:", "".join(reversed(s)))

# 17. Split string into array of characters
s = "Python"
char_array = list(s)
print("Array of characters:", char_array)

# 18. Slicing a string
s = "Hello Python World"
print("Full          :", s)
print("First 5       :", s[:5])
print("Last 5        :", s[-5:])
print("Middle        :", s[6:12])
print("Every 2nd char:", s[::2])
print("Reverse       :", s[::-1])

# 19. Repeat M characters of a string N times
s = "Python"
M = 3
N = 4
result = s[:M] * N
print(f"First {M} chars of '{s}' repeated {N} times: {result}")

# 20. Swap characters of a string
s = "Python"
lst = list(s)
lst[0], lst[-1] = lst[-1], lst[0]
print("After swapping first & last:", "".join(lst))

# 21. Remove a character from a specified index
s = "Hello"
index = 2
result = s[:index] + s[index+1:]
print(f"After removing index {index} from '{s}': {result}")

# 22. Adding a given string with a fixed message
def add_message(name):
    fixed = "Welcome to Python Programming, "
    return fixed + name
print(add_message("Alice"))

# 23. Find matched characters in a given string
s1 = "hello"
s2 = "world"
matched = [ch for ch in s1 if ch in s2]
print(f"Matched characters between '{s1}' and '{s2}': {matched}")

# 24. Find frequency of each character
s = "programming"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print("Character frequencies:")
for ch, count in sorted(freq.items()):
    print(f"  '{ch}' : {count}")

# 25. Extract mobile number from a string
import re
text = "Contact us at 9876543210 or 8765432109 for help."
numbers = re.findall(r'\b[6-9]\d{9}\b', text)
print("Mobile numbers found:", numbers)

# 26. Replace a special string from a paragraph
paragraph = "Python is great. Python is easy. Learn Python today."
old = "Python"
new = "Java"
result = paragraph.replace(old, new)
print("After replacement:", result)

# 27. Find ASCII value of each character
s = "Hello"
print("ASCII values:")
for ch in s:
    print(f"  '{ch}' -> {ord(ch)}")

# 28. Print reverse of string that contains digits
s = "abc123def456"
digits_only = "".join([ch for ch in s if ch.isdigit()])
print(f"Digits in '{s}'     :", digits_only)
print("Reversed digits    :", digits_only[::-1])

# 29. Convert a string to camelCase
s = "hello world python programming"
words = s.split()
camel = words[0] + "".join(w.capitalize() for w in words[1:])
print("camelCase:", camel)

# 30. Capitalize first letter of each word
s = "python is a great language"
print("Title case:", s.title())
manual = " ".join(w.capitalize() for w in s.split())
print("Manual    :", manual)

# 31. Check if string is palindrome
s = "madam"
if s == s[::-1]:
    print(f"'{s}' IS a palindrome.")
else:
    print(f"'{s}' is NOT a palindrome.")

# 32. Count uppercase and lowercase letters
s = "Hello World Python"
upper = sum(1 for ch in s if ch.isupper())
lower = sum(1 for ch in s if ch.islower())
print(f"Uppercase: {upper} | Lowercase: {lower}")

# 33. Count total letters and digits
s = "Hello123World456"
letters = sum(1 for ch in s if ch.isalpha())
digits  = sum(1 for ch in s if ch.isdigit())
print(f"Letters: {letters} | Digits: {digits}")

# 34. Convert list of characters into a string
char_list = ['P', 'y', 't', 'h', 'o', 'n']
result = "".join(char_list)
print("List to string:", result)

# 35. Check whether a variable is a string or not
variables = ["Hello", 42, 3.14, True, "Python"]
for v in variables:
    if isinstance(v, str):
        print(f"'{v}' IS a string.")
    else:
        print(f"{v} is NOT a string.")

# 36. Count occurrence of a word in a text
text = "python is easy. python is powerful. learn python."
word = "python"
count = text.lower().split().count(word)
print(f"'{word}' appears {count} times.")

# 37. Search for a pattern in string
import re
text = "The price is 100 dollars and 200 euros."
pattern = r'\d+'
matches = re.findall(pattern, text)
print("Pattern matches (numbers):", matches)

# 38. Remove i-th character from a string
s = "Programming"
i = 4
result = s[:i] + s[i+1:]
print(f"After removing index {i} ('{s[i]}') from '{s}': {result}")

# 39. Find length of a string (different ways)
s = "Python"
print("1. len() :", len(s))
count = 0
for _ in s:
    count += 1
print("2. For loop      :", count)
count2 = 0
while True:
    try:
        s[count2]
        count2 += 1
    except IndexError:
        break
print("3. While loop    :", count2)

# 40. Accept strings which contain all vowels
def contains_all_vowels(s):
    vowels = set("aeiou")
    return vowels.issubset(set(s.lower()))

s = input("Enter a string: ")
if contains_all_vowels(s):
    print(f"'{s}' contains ALL vowels - YES")
else:
    print(f"'{s}' does not contain all vowels - NO")

# 41. Find the least frequent character in the string
s = "programming"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
least_char = min(freq, key=freq.get)
print(f"String: {s}")
print(f"Least frequent character: '{least_char}' (appears {freq[least_char]} time)")

# 42. Split and join a string
s = "Python is easy to learn"
words = s.split()
print("After split:", words)
joined = "-".join(words)
print("After join with '-':", joined)
joined2 = " ".join(words)
print("After join with ' ':", joined2)

# 43. Find words greater than given length k
sentence = "Python programming is fun and interesting"
k = int(input("Enter length k: "))
result = [word for word in sentence.split() if len(word) > k]
print(f"Words with length greater than {k}: {result}")

# 44. Check if string contains special characters
import re
s = input("Enter a string: ")
if re.search(r'[^a-zA-Z0-9\s]', s):
    print(f"'{s}' CONTAINS special characters.")
else:
    print(f"'{s}' does NOT contain special characters.")

# 45. Find maximum frequency character in the string
s = "programming"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
max_char = max(freq, key=freq.get)
print(f"String: {s}")
print(f"Maximum frequency character: '{max_char}' (appears {freq[max_char]} times)")

# 46. Check whether a given string is binary or not
s = input("Enter a string: ")
is_binary = all(ch in '01' for ch in s)
if is_binary:
    print(f"'{s}' IS a binary string.")
else:
    print(f"'{s}' is NOT a binary string.")

# 47. Find uncommon words from two strings
s1 = "python is great and easy"
s2 = "java is powerful and fast"
set1 = set(s1.split())
set2 = set(s2.split())
uncommon = (set1 - set2) | (set2 - set1)
print(f"String 1 : {s1}")
print(f"String 2 : {s2}")
print(f"Uncommon words: {uncommon}")