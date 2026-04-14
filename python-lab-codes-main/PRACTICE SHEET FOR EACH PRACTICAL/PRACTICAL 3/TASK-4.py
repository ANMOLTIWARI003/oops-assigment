# ─────────────────────────────────────────────────────────────
# TASK 4: Intelligence Table
# Formula: i = 2 + (y + 0.5x)
# y: 1 to 6, x: 5.5 to 12.5 in steps of 0.5
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("TASK 4: Intelligence Table  i = 2 + (y + 0.5x)")
print("=" * 55)

print(f"{'y':>4} {'x':>6} {'i':>10}")
print("-" * 24)
y = 1
while y <= 6:
    x = 5.5
    while x <= 12.5:
        intelligence = 2 + (y + 0.5 * x)
        print(f"{y:>4} {x:>6.1f} {intelligence:>10.3f}")
        x += 0.5
    y += 1