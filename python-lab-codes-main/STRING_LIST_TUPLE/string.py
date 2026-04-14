# ASSIGNMENT-2 

# 1. Capitalizes the first letter of each word in a string
s = "python is a great language"
print("Title case:", s.title())
manual = " ".join(w.capitalize() for w in s.split())
print("Manual    :", manual)

# 2. Python program to check if a string is palindrome or not
s = input("Enter a string: ")
if s == s[::-1]:
    print(f"'{s}' IS a palindrome.")
else:
    print(f"'{s}' is NOT a palindrome.")

# 3. Python program to count occurrence of a word in the given text
text = input("Enter a text: ")
word = input("Enter word to count: ")
count = text.lower().split().count(word.lower())
print(f"'{word}' appears {count} times.")

# 4. Python program for removing i-th character from a string
s = input("Enter a string: ")
i = int(input("Enter index to remove: "))
result = s[:i] + s[i+1:]
print(f"After removing index {i} ('{s[i]}') from '{s}': {result}")

# 5. Python program to split and join a string
s = input("Enter a string: ")
words = s.split()
print("After split:", words)
joined = "-".join(words)
print("After join with '-':", joined)
joined2 = " ".join(words)
print("After join with ' ':", joined2)

# 6. Convert a String to camelCase in Python
s = input("Enter a string (words separated by spaces): ")
words = s.split()
camel = words[0].lower() + "".join(w.capitalize() for w in words[1:])
print("camelCase:", camel)

# 7. Python program to reverse a given string (5 different ways)
s = input("Enter a string: ")
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

# 8. Check if a substring presents in a string using 'in' operator
s = input("Enter main string: ")
sub = input("Enter substring to search: ")
if sub in s:
    print(f"'{sub}' IS present in the string.")
else:
    print(f"'{sub}' is NOT present in the string.")

# 9. Input a string and find total number uppercase and lowercase letters
s = input("Enter a string: ")
upper = sum(1 for ch in s if ch.isupper())
lower = sum(1 for ch in s if ch.islower())
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")

# 10. Input a string and find total number of letters and digits
s = input("Enter a string: ")
letters = sum(1 for ch in s if ch.isalpha())
digits  = sum(1 for ch in s if ch.isdigit())
print(f"Total Letters: {letters}")
print(f"Total Digits : {digits}")

# 11. Python program to convert a list of characters into a string
char_list = list(input("Enter characters separated by spaces: ").split())
result = "".join(char_list)
print("List          :", char_list)
print("Joined string :", result)

# 12. Replace a special string from a given paragraph with another string
paragraph = input("Enter a paragraph: ")
old = input("Enter word to replace: ")
new = input("Enter new word: ")
result = paragraph.replace(old, new)
print("After replacement:", result)

# 13. Replace a special string from a given paragraph with another string
paragraph = input("Enter a paragraph: ")
old = input("Enter word to replace: ")
new = input("Enter new word: ")
count = int(input("Enter how many times to replace (0 for all): "))
if count == 0:
    result = paragraph.replace(old, new)
else:
    result = paragraph.replace(old, new, count)
print("After replacement:", result)