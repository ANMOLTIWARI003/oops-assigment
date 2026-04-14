import pandas as pd

# ── First, create the books.csv file with sample data ──────────────────────────
import os

csv_data = """title,author,edition,year,publisher,price
Python Basics,John Smith,1st,2018,TechPress,450
Data Science with Python,Jane Doe,2nd,2020,InfoBooks,650
Machine Learning,Alan Turing,3rd,2019,TechPress,800
Clean Code,Robert Martin,1st,2015,PearsonEd,550
Django for Beginners,William Vincent,2nd,2021,InfoBooks,500
Python Cookbook,David Beazley,3rd,2017,OReilly,750
Deep Learning,Ian Goodfellow,1st,2016,MITPress,900
Automate the Boring Stuff,Al Sweigart,2nd,2020,NoStarch,400
Fluent Python,Luciano Ramalho,1st,2015,OReilly,700
Intro to Algorithms,Thomas Cormen,4th,2022,MITPress,950
"""

with open("books.csv", "w") as f:
    f.write(csv_data.strip())

# ── Read the CSV file into a DataFrame ────────────────────────────────────────
df = pd.read_csv("books.csv")

# ──────────────────────────────────────────────────────────────────────────────
# a) Print the complete report of books in a Tabular form
# ──────────────────────────────────────────────────────────────────────────────
print("=" * 70)
print("           COMPLETE REPORT OF BOOKS")
print("=" * 70)
print(df.to_string(index=False))
print()

# ──────────────────────────────────────────────────────────────────────────────
# b) Print the list of available books of a given author
# ──────────────────────────────────────────────────────────────────────────────
given_author = "Jane Doe"  # <-- change author name as needed
print("=" * 70)
print(f" Books by Author: {given_author}")
print("=" * 70)
author_books = df[df["author"] == given_author]
if author_books.empty:
    print(f"No books found for author: {given_author}")
else:
    print(author_books.to_string(index=False))
print()

# ──────────────────────────────────────────────────────────────────────────────
# c) Print the list of available books of a given publishing house
# ──────────────────────────────────────────────────────────────────────────────
given_publisher = "OReilly"  # <-- change publisher name as needed
print("=" * 70)
print(f" Books from Publisher: {given_publisher}")
print("=" * 70)
pub_books = df[df["publisher"] == given_publisher]
if pub_books.empty:
    print(f"No books found for publisher: {given_publisher}")
else:
    print(pub_books.to_string(index=False))
print()

# ──────────────────────────────────────────────────────────────────────────────
# d) Print the Titles of cheapest & costliest book available
# ──────────────────────────────────────────────────────────────────────────────
print("=" * 70)
print(" CHEAPEST & COSTLIEST BOOKS")
print("=" * 70)
cheapest = df.loc[df["price"].idxmin()]
costliest = df.loc[df["price"].idxmax()]
print(f"Cheapest  Book : '{cheapest['title']}' - Rs. {cheapest['price']}")
print(f"Costliest Book : '{costliest['title']}' - Rs. {costliest['price']}")
print()

# ──────────────────────────────────────────────────────────────────────────────
# e) Print the list sorted based on the year of publication
# ──────────────────────────────────────────────────────────────────────────────
print("=" * 70)
print(" BOOKS SORTED BY YEAR OF PUBLICATION")
print("=" * 70)
sorted_df = df.sort_values(by="year", ascending=True)
print(sorted_df.to_string(index=False))
print()