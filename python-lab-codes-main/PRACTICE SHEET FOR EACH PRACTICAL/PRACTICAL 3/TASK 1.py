# ─────────────────────────────────────────────────────────────
# TASK 1: Descending Star Pattern
# Pattern:
# * * * *
# * * *
# * *
# *
# ─────────────────────────────────────────────────────────────
print("=" * 40)
print("TASK 1: Descending Star Pattern")
print("=" * 40)

n = 4
for i in range(n, 0, -1):
    print("* " * i)