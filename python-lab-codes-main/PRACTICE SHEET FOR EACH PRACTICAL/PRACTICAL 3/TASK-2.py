# ─────────────────────────────────────────────────────────────
# TASK 2: Ascending Triangle Star Pattern (pyramid)
# Pattern:
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 40)
print("TASK 2: Ascending Triangle Star Pattern")
print("=" * 40)

rows = 5
for i in range(1, rows + 1):
    spaces = rows - i
    stars = 2 * i - 1
    print(" " * spaces + "* " * stars)