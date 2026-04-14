# ─────────────────────────────────────────────────────────────
# TASK 4: Print 1 to n without string methods
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("   TASK 4: Print 1 to n (no string methods)")
print("=" * 55)

n = int(input("Enter value of n: "))
result = 0
for i in range(1, n + 1):
    result = result * (10 ** len(str(i))) + i
print(f"Output: {result}")