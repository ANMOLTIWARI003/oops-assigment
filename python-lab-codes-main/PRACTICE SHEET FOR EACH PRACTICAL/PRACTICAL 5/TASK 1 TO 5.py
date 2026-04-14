
# ─────────────────────────────────────────────────────────────
# TASK 1: 20 integers — positive, negative, odd, even, zero
# ─────────────────────────────────────────────────────────────
print("=" * 50)
print("TASK 1: Integer Statistics (20 inputs)")
print("=" * 50)

print("Enter 20 integers:")
numbers = tuple(int(input(f"  Number {i+1}: ")) for i in range(20))

positive = sum(1 for x in numbers if x > 0)
negative = sum(1 for x in numbers if x < 0)
odd      = sum(1 for x in numbers if x % 2 != 0)
even     = sum(1 for x in numbers if x % 2 == 0)
zeros    = sum(1 for x in numbers if x == 0)

print(f"\nTuple       : {numbers}")
print(f"Positive    : {positive}")
print(f"Negative    : {negative}")
print(f"Odd numbers : {odd}")
print(f"Even numbers: {even}")
print(f"Zeros       : {zeros}")


# ─────────────────────────────────────────────────────────────
# TASK 2: Medical Kit Prices
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("TASK 2: Medical Kit Total Price")
print("=" * 50)

medical_items = ("Bandage", "Antiseptic", "Paracetamol",
                 "Cotton Roll", "Thermometer", "Gloves")
prices = (25.0, 60.0, 35.0, 45.0, 120.0, 50.0)

print("Medical Kit Contents:")
for item, price in zip(medical_items, prices):
    print(f"  {item:<15} : Rs. {price:.2f}")
print(f"\nTotal Price of Medical Kit : Rs. {sum(prices):.2f}")


# ─────────────────────────────────────────────────────────────
# TASK 3: Virat Kohli Runs Statistics
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("TASK 3: Virat Kohli Runs Analysis")
print("=" * 50)

kohli_runs = (82, 45, 100, 73, 12, 55, 120, 0, 91, 67,
              34, 88, 149, 23, 75, 56, 110, 4, 66, 95)

print(f"Runs Tuple   : {kohli_runs}")
print(f"a) Total runs scored  : {sum(kohli_runs)}")
print(f"b) Average runs       : {sum(kohli_runs)/len(kohli_runs):.2f}")
print(f"c) Highest score      : {max(kohli_runs)}")
print(f"d) Lowest score       : {min(kohli_runs)}")


# ─────────────────────────────────────────────────────────────
# TASK 4: Python Programming Certification Marks
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("TASK 4: Python Programming Certification")
print("=" * 50)

marks = (85, 42, 63, 91, 38, 74, 55, 88, 29, 70,
         95, 61, 47, 83, 66, 52, 78, 93, 35, 60)

cutoff = 40
highest = max(marks)
lowest  = min(marks)
certified = sum(1 for m in marks if m >= cutoff)
failed    = sum(1 for m in marks if m < cutoff)
elite     = sum(1 for m in marks if 60 <= m <= 70)
elite_silver = sum(1 for m in marks if 71 <= m <= 89)
elite_gold   = sum(1 for m in marks if m >= 90)

print(f"Marks Tuple : {marks}")
print(f"a) Highest marks    : {highest}")
print(f"b) Lowest marks     : {lowest}")
print(f"c) Students Certified (>=40) : {certified}")
print(f"d) Students Failed  (<40)    : {failed}")
print(f"e) Elite Certificate (60-70) : {elite}")
print(f"f) Elite+Silver (71-89)      : {elite_silver}")
print(f"g) Elite+Gold  (>=90)        : {elite_gold}")


# ─────────────────────────────────────────────────────────────
# TASK 5: Bank Token — Ajay & Vivek Duplicate Removal
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("TASK 5: Bank Token Management (Ajay & Vivek)")
print("=" * 50)

tuple_a = (101, 105, 108, 112, 115, 108, 120, 101, 130)
tuple_b = (102, 105, 109, 112, 116, 120, 125, 130, 140)

# Remove duplicates within each tuple
unique_a = tuple(set(tuple_a))
unique_b = tuple(set(tuple_b))

# Combine and remove duplicates
combined  = unique_a + unique_b
tuple_c   = tuple(sorted(set(combined)))

print(f"Ajay's Tokens   (A)   : {sorted(set(tuple_a))}")
print(f"Vivek's Tokens  (B)   : {sorted(set(tuple_b))}")
print(f"Combined Unique (C)   : {tuple_c}")
print(f"\nVivek must now service these token numbers: {tuple_c}")