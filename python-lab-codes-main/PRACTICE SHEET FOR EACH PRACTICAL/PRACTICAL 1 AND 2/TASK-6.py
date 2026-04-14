# ─────────────────────────────────────────────────────────────
# TASK 6: Daily Sales Report
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("           TASK 6: Daily Sales Report")
print("=" * 55)

products = ["Operating Systems", "Antivirus", "Cabinet",
            "RAM", "Hard Disks", "Mother Boards"]
sales = {}

print("Enter units sold for each product:")
for product in products:
    units = int(input(f"  {product}: "))
    price = float(input(f"  Price per unit of {product} (Rs.): "))
    sales[product] = {"units": units, "price": price, "total": units * price}

print("\n--- Sales Report ---")
print(f"{'Product':<20} {'Units':>6} {'Price':>10} {'Total':>12}")
print("-" * 52)
grand_total = 0
for p, data in sales.items():
    print(f"{p:<20} {data['units']:>6} {data['price']:>10.2f} {data['total']:>12.2f}")
    grand_total += data["total"]
print("-" * 52)
print(f"{'Grand Total':>38}  Rs. {grand_total:.2f}")