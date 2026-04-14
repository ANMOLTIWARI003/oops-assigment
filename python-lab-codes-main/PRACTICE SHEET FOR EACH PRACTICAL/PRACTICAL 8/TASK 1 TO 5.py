
import os

# ─────────────────────────────────────────────────────────────
# TASK 1: Create student details file & print it
# ─────────────────────────────────────────────────────────────
print("=" * 50)
print("TASK 1: Create & Read Student Details File")
print("=" * 50)

name    = input("Enter Student Name      : ")
dept    = input("Enter Department        : ")
year    = input("Enter Year              : ")
section = input("Enter Section           : ")
roll    = input("Enter Roll Number       : ")
contact = input("Enter Contact Number    : ")
email   = input("Enter E-Mail ID         : ")

with open("student.txt", "w") as f:
    f.write(f"Name           : {name}\n")
    f.write(f"Department     : {dept}\n")
    f.write(f"Year           : {year}\n")
    f.write(f"Section        : {section}\n")
    f.write(f"Roll Number    : {roll}\n")
    f.write(f"Contact Number : {contact}\n")
    f.write(f"E-Mail ID      : {email}\n")

print("\n--- Student Details (from file) ---")
with open("student.txt", "r") as f:
    print(f.read())


# ─────────────────────────────────────────────────────────────
# TASK 2: Create two files, merge into merge.txt
# ─────────────────────────────────────────────────────────────
print("=" * 50)
print("TASK 2: Merge Two Files into merge.txt")
print("=" * 50)

with open("file1.txt", "w") as f:
    f.write("Hello, this is content from File 1.\n")
    f.write("Python is a great programming language.\n")
    f.write("File handling is easy in Python.\n")

with open("file2.txt", "w") as f:
    f.write("Hello, this is content from File 2.\n")
    f.write("NumPy, Pandas, and Matplotlib are important libraries.\n")
    f.write("Keep learning and practicing Python!\n")

with open("file1.txt", "r") as f1, \
     open("file2.txt", "r") as f2, \
     open("merge.txt",  "w") as mf:
    mf.write("=== Content from File 1 ===\n")
    mf.write(f1.read())
    mf.write("\n=== Content from File 2 ===\n")
    mf.write(f2.read())

print("Files merged into merge.txt")
with open("merge.txt", "r") as f:
    print(f.read())


# ─────────────────────────────────────────────────────────────
# TASK 3: Count word occurrences, uppercase, lowercase, digits
# ─────────────────────────────────────────────────────────────
print("=" * 50)
print("TASK 3: Word Occurrence & Character Count")
print("=" * 50)

sample_text = ("Python is a great language. Python supports "
               "OOP and is used in Data Science. Python 3 is the latest Version of Python.\n"
               "Total Users: 1000, Downloads: 5000, Stars: 9999.\n")

with open("sample.txt", "w") as f:
    f.write(sample_text)

search_word = input("Enter word to search in file: ").strip()

with open("sample.txt", "r") as f:
    content = f.read()

occurrences = content.lower().split().count(search_word.lower())
upper_count  = sum(1 for ch in content if ch.isupper())
lower_count  = sum(1 for ch in content if ch.islower())
digit_count  = sum(1 for ch in content if ch.isdigit())

print(f"\nFile Content:\n{content}")
print(f"Occurrences of '{search_word}' : {occurrences}")
print(f"Uppercase letters              : {upper_count}")
print(f"Lowercase letters              : {lower_count}")
print(f"Digits                         : {digit_count}")


# ─────────────────────────────────────────────────────────────
# TASK 4: Write to money.txt, transfer to data.txt, print data.txt
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("TASK 4: money.txt → data.txt Transfer")
print("=" * 50)

with open("money.txt", "w") as f:
    f.write("Account Holder : Rahul Sharma\n")
    f.write("Account No     : 123456789\n")
    f.write("Balance        : Rs. 50,000\n")
    f.write("Last Transaction: Rs. 5,000 credited\n")

with open("money.txt", "r") as src, open("data.txt", "w") as dst:
    dst.write(src.read())

print("Data transferred from money.txt to data.txt")
print("\n--- Content of data.txt ---")
with open("data.txt", "r") as f:
    print(f.read())


# ─────────────────────────────────────────────────────────────
# TASK 5: Check Similarity Between Two Text Files
# ─────────────────────────────────────────────────────────────
print("=" * 50)
print("TASK 5: File Similarity Checker")
print("=" * 50)

with open("textA.txt", "w") as f:
    f.write("Python is an easy and powerful programming language.\n")
    f.write("It supports object-oriented and functional programming.\n")

with open("textB.txt", "w") as f:
    f.write("Python is an easy and powerful programming language.\n")
    f.write("It is widely used in data science and web development.\n")

with open("textA.txt", "r") as f:
    lines_a = set(f.readlines())
with open("textB.txt", "r") as f:
    lines_b = set(f.readlines())

common   = lines_a & lines_b
union    = lines_a | lines_b
similarity = (len(common) / len(union)) * 100 if union else 0

print(f"Common lines         : {len(common)}")
print(f"Total unique lines   : {len(union)}")
print(f"Similarity           : {similarity:.2f}%")
if similarity >= 80:
    print("Result: Files are HIGHLY SIMILAR")
elif similarity >= 50:
    print("Result: Files are PARTIALLY SIMILAR")
else:
    print("Result: Files are NOT SIMILAR")