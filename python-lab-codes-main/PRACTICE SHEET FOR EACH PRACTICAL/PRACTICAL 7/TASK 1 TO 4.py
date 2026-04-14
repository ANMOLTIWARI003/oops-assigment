
import math

# ─────────────────────────────────────────────────────────────
# TASK 1: Restaurant Bill Application
# ─────────────────────────────────────────────────────────────
print("=" * 55)
print("        TASK 1: Restaurant Bill Application")
print("=" * 55)

MENU = {
    "1": ("Paneer Butter Masala",   250),
    "2": ("Dal Tadka",              180),
    "3": ("Butter Naan",             40),
    "4": ("Steamed Rice",            60),
    "5": ("Mango Lassi",             80),
    "6": ("Gulab Jamun",             70),
}

def print_menu():
    print("\n======== MENU ========")
    print(f"{'No.':<4} {'Item':<25} {'Price':>8}")
    print("-" * 40)
    for key, (item, price) in MENU.items():
        print(f"{key:<4} {item:<25} Rs. {price:>5}")
    print("=" * 40)

def get_order():
    order = {}
    while True:
        choice = input("Enter item number (or 0 to finish): ").strip()
        if choice == "0":
            break
        if choice in MENU:
            qty = int(input(f"  Quantity of {MENU[choice][0]}: "))
            order[choice] = order.get(choice, 0) + qty
        else:
            print("  Invalid choice. Try again.")
    return order

def print_bill(order):
    print("\n======== BILL ========")
    print(f"{'Item':<25} {'Qty':>4} {'Rate':>8} {'Amount':>10}")
    print("-" * 52)
    total = 0
    for key, qty in order.items():
        name, price = MENU[key]
        amount = qty * price
        total += amount
        print(f"{name:<25} {qty:>4} {price:>8} {amount:>10}")
    print("-" * 52)
    gst = total * 0.05
    grand = total + gst
    print(f"{'Subtotal':>44}: Rs. {total:.2f}")
    print(f"{'GST (5%)':>44}: Rs. {gst:.2f}")
    print(f"{'Grand Total':>44}: Rs. {grand:.2f}")
    print("=" * 52)
    print("     Thank you! Visit Again!")

print_menu()
order = get_order()
if order:
    print_bill(order)
else:
    print("No items ordered.")


# ─────────────────────────────────────────────────────────────
# TASK 2: Employee Salary Calculator
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("        TASK 2: Employee Salary Calculator")
print("=" * 55)

def calculate_salary(basic):
    hra        = 0.40 * basic
    ta         = 0.30 * basic
    da         = 0.90 * basic
    incentives = 5000
    gross      = basic + hra + ta + da + incentives
    return hra, ta, da, incentives, gross

basic = float(input("Enter Basic Salary (Rs.): "))
hra, ta, da, inc, gross = calculate_salary(basic)

print(f"\n--- Salary Slip ---")
print(f"Basic Salary   : Rs. {basic:.2f}")
print(f"HRA (40%)      : Rs. {hra:.2f}")
print(f"TA  (30%)      : Rs. {ta:.2f}")
print(f"DA  (90%)      : Rs. {da:.2f}")
print(f"Incentives     : Rs. {inc:.2f}")
print(f"Gross Salary   : Rs. {gross:.2f}")


# ─────────────────────────────────────────────────────────────
# TASK 3: Series 2,5,10,17,26,37,50... (n^2 + 1) — first 20 terms
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("        TASK 3: Series 2,5,10,17,26... (first 20 terms)")
print("=" * 55)

def generate_series(count):
    series = []
    for n in range(1, count + 1):
        series.append(n * n + 1)
    return series

series = generate_series(20)
print("Series:", series)


# ─────────────────────────────────────────────────────────────
# TASK 4: Surface Area and Volume of a Sphere
# Surface = 4 * pi * r^2
# Volume  = (4/3) * pi * r^3
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("        TASK 4: Sphere — Surface Area & Volume")
print("=" * 55)

def sphere_surface_area(r):
    return 4 * math.pi * r ** 2

def sphere_volume(r):
    return (4 / 3) * math.pi * r ** 3

r = float(input("Enter radius of Sphere: "))
print(f"\nRadius         : {r}")
print(f"Surface Area   : {sphere_surface_area(r):.4f} sq. units")
print(f"Volume         : {sphere_volume(r):.4f} cubic units")