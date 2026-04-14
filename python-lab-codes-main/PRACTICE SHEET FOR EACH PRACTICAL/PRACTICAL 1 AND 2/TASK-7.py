# ─────────────────────────────────────────────────────────────
# TASK 7: Python Programming Marks Analysis
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("    TASK 7: Python Programming — Marks Analysis")
print("=" * 55)

n = int(input("Enter number of students: "))
marks_list = []
for i in range(n):
    m = float(input(f"  Enter marks of student {i + 1}: "))
    marks_list.append(m)

highest = max(marks_list)
lowest = min(marks_list)
average = sum(marks_list) / n
passed = sum(1 for m in marks_list if m >= 50)
failed = n - passed
result_pct = (passed / n) * 100

print("\n--- Marks Report ---")
print(f"Highest Marks   : {highest}")
print(f"Lowest Marks    : {lowest}")
print(f"Average Marks   : {average:.2f}")
print(f"Students Passed : {passed}")
print(f"Students Failed : {failed}")
print(f"Percentage Result: {result_pct:.2f}%")