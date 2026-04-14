# ─────────────────────────────────────────────────────────────
# TASK 5: Employee Performance Bonus
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("        TASK 5: Performance-Based Bonus")
print("=" * 55)

salary = float(input("Enter Employee Salary (Rs.): "))
percentage = float(input("Enter Performance Percentage: "))

if 90 <= percentage <= 100:
    bonus = 0.20 * salary
    grade = "Excellent"
elif 80 <= percentage < 90:
    bonus = 0.10 * salary
    grade = "Good"
elif 70 <= percentage < 80:
    bonus = 0.05 * salary
    grade = "Average"
else:
    bonus = 0
    grade = "Below Average"

print(f"\nPerformance Grade : {grade}")
print(f"Bonus Amount      : Rs. {bonus:.2f}")