# ─────────────────────────────────────────────────────────────
# TASK 3: Print 1 to n as a string without string methods
# Example: n=5 → 12345
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 40)
print("TASK 3: Print 1 to n (no string methods)")
print("=" * 40)

n = int(input("Enter n (1 to 150): "))
result = 0
for i in range(1, n + 1):
    # Count digits in i
    temp = i
    digits = 0
    while temp > 0:
        digits += 1
        temp //= 10
    result = result * (10 ** digits) + i
print(f"Output: {result}")