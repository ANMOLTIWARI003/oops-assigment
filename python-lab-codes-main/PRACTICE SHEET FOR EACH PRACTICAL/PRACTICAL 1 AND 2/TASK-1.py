# ─────────────────────────────────────────────────────────────
# TASK 1: House Painting Cost Estimator
# ─────────────────────────────────────────────────────────────
print("=" * 55)
print("        TASK 1: House Painting Cost Estimator")
print("=" * 55)

INTERIOR_RATE = 18  # Rs. per sq.ft
EXTERIOR_RATE = 12  # Rs. per sq.ft

num_interior = int(input("Enter number of Interior walls: "))
if num_interior == 0:
    interior_area = 0
else:
    interior_area = float(input(f"Enter surface area of each Interior wall (sq.ft): "))

num_exterior = int(input("Enter number of Exterior walls: "))
if num_exterior == 0:
    exterior_area = 0
else:
    exterior_area = float(input(f"Enter surface area of each Exterior wall (sq.ft): "))

total_interior_cost = num_interior * interior_area * INTERIOR_RATE
total_exterior_cost = num_exterior * exterior_area * EXTERIOR_RATE
total_cost = total_interior_cost + total_exterior_cost

print("\n--- Painting Cost Report ---")
print(f"Interior Painting Cost : Rs. {total_interior_cost:.2f}")
print(f"Exterior Painting Cost : Rs. {total_exterior_cost:.2f}")
print(f"Total Painting Cost    : Rs. {total_cost:.2f}")