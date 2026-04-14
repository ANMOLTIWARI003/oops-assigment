# ─────────────────────────────────────────────────────────────
# TASK 2: Employee Bonus Calculator
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("        TASK 2: Employee Bonus Calculator")
print("=" * 55)

test_cases = [10, 8, 6, 4, 2, 0]  # 6 different cases as required

for years in test_cases:
    if years >= 10:
        bonus = 10000
    elif years >= 7:
        bonus = 7000
    elif years >= 5:
        bonus = 5000
    elif years >= 3:
        bonus = 3000
    elif years >= 1:
        bonus = 2000
    else:
        bonus = 1000
    print(f"Years of Service: {years:2d}  -->  Bonus: Rs. {bonus}")