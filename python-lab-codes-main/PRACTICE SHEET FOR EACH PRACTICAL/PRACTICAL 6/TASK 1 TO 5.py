
# ─────────────────────────────────────────────────────────────
# TASK 1: Word Count Estimator (count spaces + 1)
# ─────────────────────────────────────────────────────────────
print("=" * 50)
print("TASK 1: Word Count Estimator")
print("=" * 50)

sentence = input("Enter a string: ")
word_count = sentence.count(" ") + 1
print(f"Estimated number of words: {word_count}")


# ─────────────────────────────────────────────────────────────
# TASK 2: Palindrome Checker
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("TASK 2: Palindrome Checker")
print("=" * 50)

word = input("Enter a word: ").strip().lower()
if word == word[::-1]:
    print(f'"{word}" is a PALINDROME.')
else:
    print(f'"{word}" is NOT a palindrome.')


# ─────────────────────────────────────────────────────────────
# TASK 3: Auto-Generate Email ID & Password from Full Name
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("TASK 3: Auto Email ID & Password Generator")
print("=" * 50)

full_name  = input("Enter your full name: ").strip()
parts      = full_name.split()
first_name = parts[0].lower()
last_name  = parts[-1].lower() if len(parts) > 1 else ""

email    = first_name + "." + last_name + "@example.com"
password = first_name[:3] + last_name[:3] + str(len(full_name)) + "@"

print(f"Generated Email    : {email}")
print(f"Generated Password : {password}")


# ─────────────────────────────────────────────────────────────
# TASK 4: Lowercase + Remove periods and commas
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("TASK 4: String Cleaner (lowercase, remove . and ,)")
print("=" * 50)

text = input("Enter a string: ")
result = text.lower().replace(".", "").replace(",", "")
print(f"Cleaned string: {result}")


# ─────────────────────────────────────────────────────────────
# TASK 5: Count Vowels in a Word
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("TASK 5: Vowel Counter")
print("=" * 50)

word   = input("Enter a word: ").lower()
vowels = "aeiou"
count  = sum(1 for ch in word if ch in vowels)
found  = [ch for ch in word if ch in vowels]

print(f"Word           : {word}")
print(f"Vowels found   : {found}")
print(f"Number of vowels: {count}")