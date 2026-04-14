# String statistics program

print("LAB ASSIGNMENT 1")
s = input("Enter a string: ")

vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

num_vowels     = sum(1 for ch in s if ch in vowels)
num_consonants = sum(1 for ch in s if ch in consonants)
num_spaces     = sum(1 for ch in s if ch == " ")
num_lowercase  = sum(1 for ch in s if ch.islower())

print("\nString Statistics:")
print(f"a) Number of Vowels          : {num_vowels}")
print(f"b) Number of Consonants      : {num_consonants}")
print(f"c) Number of Spaces          : {num_spaces}")
print(f"d) Number of Lowercase Letters: {num_lowercase}")