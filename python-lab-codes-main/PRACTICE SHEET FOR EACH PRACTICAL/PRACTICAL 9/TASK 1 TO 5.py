
import math

# ─────────────────────────────────────────────────────────────
# TASK 1: Employee → Manager Inheritance
# ─────────────────────────────────────────────────────────────
print("=" * 55)
print("TASK 1: Employee & Manager (Inheritance)")
print("=" * 55)

class Employee:
    def __init__(self, name, age, salary, address):
        self.name    = name
        self.age     = age
        self.salary  = salary
        self.address = address

    def get_info(self):
        self.name    = input("  Employee Name   : ")
        self.age     = int(input("  Age             : "))
        self.salary  = float(input("  Salary (Rs.)    : "))
        self.address = input("  Address         : ")

    def display(self):
        print(f"  Name    : {self.name}")
        print(f"  Age     : {self.age}")
        print(f"  Salary  : Rs. {self.salary:.2f}")
        print(f"  Address : {self.address}")


class Manager(Employee):
    def __init__(self):
        super().__init__("", 0, 0.0, "")
        self.department = ""
        self.team_size  = 0

    def get_info(self):
        super().get_info()
        self.department = input("  Department      : ")
        self.team_size  = int(input("  Team Size       : "))

    def display(self):
        super().display()
        print(f"  Department : {self.department}")
        print(f"  Team Size  : {self.team_size}")


managers = []
n = 3    # process 3 managers for demo (change to 10 in full run)
print(f"\nEnter details for {n} managers:\n")
for i in range(n):
    print(f"--- Manager {i+1} ---")
    m = Manager()
    m.get_info()
    managers.append(m)

print("\n--- All Manager Details ---")
for i, m in enumerate(managers, 1):
    print(f"\nManager {i}:")
    m.display()


# ─────────────────────────────────────────────────────────────
# TASK 2: Bookshop Inventory System
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("TASK 2: Bookshop Inventory System")
print("=" * 55)

class Books:
    def __init__(self, title, author, price, publisher, stock):
        self.title     = title
        self.author    = author
        self.price     = price
        self.publisher = publisher
        self.stock     = stock

    def display(self):
        print(f"  Title     : {self.title}")
        print(f"  Author    : {self.author}")
        print(f"  Price     : Rs. {self.price:.2f}")
        print(f"  Publisher : {self.publisher}")
        print(f"  Stock     : {self.stock} copies")

    def sell(self, copies):
        if copies <= self.stock:
            self.stock -= copies
            print(f"  Total Cost : Rs. {copies * self.price:.2f}")
            print(f"  Remaining Stock : {self.stock} copies")
        else:
            print("  Required number of copies are not available.")


inventory = [
    Books("Python Basics",       "John Smith",    450, "TechPress",  10),
    Books("Data Science",        "Jane Doe",      650, "InfoBooks",   5),
    Books("Clean Code",          "Robert Martin", 550, "PearsonEd",  15),
    Books("Machine Learning",    "Alan Turing",   800, "TechPress",   3),
]

search_title  = input("Enter book title to search : ").strip().lower()
search_author = input("Enter author name          : ").strip().lower()

found = None
for book in inventory:
    if book.title.lower() == search_title and book.author.lower() == search_author:
        found = book
        break

if not found:
    print("Book not found in inventory.")
else:
    print("\nBook Found:")
    found.display()
    qty = int(input("Enter number of copies required: "))
    found.sell(qty)


# ─────────────────────────────────────────────────────────────
# TASK 3: Area of 2D Shapes using Function Overloading
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("TASK 3: Area of 2D Shapes (Function Overloading)")
print("=" * 55)

class Shape:
    def area(self, *args):
        if len(args) == 1:          # square: side
            return args[0] ** 2
        elif len(args) == 2:        # rectangle/ellipse: a, b
            return args[0] * args[1]
        else:
            return 0

    def area_triangle(self, base, height):
        return 0.5 * base * height

    def area_circle(self, radius):
        return math.pi * radius ** 2

    def area_ellipse(self, a, b):
        return math.pi * a * b

s = Shape()
print(f"Square (side=5)              : {s.area(5):.4f}")
print(f"Rectangle (4x6)              : {s.area(4, 6):.4f}")
print(f"Triangle (base=8, height=5)  : {s.area_triangle(8, 5):.4f}")
print(f"Circle (r=7)                 : {s.area_circle(7):.4f}")
print(f"Ellipse (a=6, b=4)           : {s.area_ellipse(6, 4):.4f}")


# ─────────────────────────────────────────────────────────────
# TASK 4: Bank Account — Saving & Current Account
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("TASK 4: Bank Account System")
print("=" * 55)

class Account:
    def __init__(self, name, acc_no, acc_type, balance=0):
        self.name     = name
        self.acc_no   = acc_no
        self.acc_type = acc_type
        self.balance  = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"  Rs. {amount} deposited. New Balance: Rs. {self.balance:.2f}")

    def display_balance(self):
        print(f"  Account Holder : {self.name}")
        print(f"  Account No     : {self.acc_no}")
        print(f"  Balance        : Rs. {self.balance:.2f}")


class SavingAccount(Account):
    def __init__(self, name, acc_no, balance=0, rate=4.0):
        super().__init__(name, acc_no, "Savings", balance)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate / 100
        self.balance += interest
        print(f"  Interest @ {self.rate}% : Rs. {interest:.2f}. Balance: Rs. {self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"  Rs. {amount} withdrawn. New Balance: Rs. {self.balance:.2f}")
        else:
            print("  Insufficient balance.")


class CurrentAccount(Account):
    MIN_BALANCE  = 5000
    SERVICE_CHARGE = 200

    def __init__(self, name, acc_no, balance=0):
        super().__init__(name, acc_no, "Current", balance)

    def withdraw(self, amount):
        if self.balance - amount >= self.MIN_BALANCE:
            self.balance -= amount
            print(f"  Rs. {amount} withdrawn. New Balance: Rs. {self.balance:.2f}")
        else:
            self.balance -= self.SERVICE_CHARGE
            print(f"  Balance below minimum! Service charge of Rs. {self.SERVICE_CHARGE} imposed.")
            print(f"  New Balance: Rs. {self.balance:.2f}")

    def issue_cheque(self, amount):
        print(f"  Cheque of Rs. {amount} issued.")
        self.withdraw(amount)


print("\n-- Saving Account Demo --")
sav = SavingAccount("Rahul Sharma", "SAV001", balance=10000)
sav.display_balance()
sav.deposit(5000)
sav.add_interest()
sav.withdraw(3000)
sav.display_balance()

print("\n-- Current Account Demo --")
cur = CurrentAccount("Priya Mehta", "CUR001", balance=8000)
cur.display_balance()
cur.issue_cheque(2000)
cur.withdraw(5000)   # will trigger penalty
cur.display_balance()


# ─────────────────────────────────────────────────────────────
# TASK 5: Polar Coordinates — Operator Overloading (+)
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("TASK 5: Polar Coordinates — Operator Overloading")
print("=" * 55)

class Polar:
    def __init__(self, r, a):
        self.r = r     # radius
        self.a = a     # angle in radians

    def to_rect(self):
        x = self.r * math.cos(self.a)
        y = self.r * math.sin(self.a)
        return x, y

    def __add__(self, other):
        x1, y1 = self.to_rect()
        x2, y2 = other.to_rect()
        xr = x1 + x2
        yr = y1 + y2
        r  = math.sqrt(xr * xr + yr * yr)
        a  = math.atan2(yr, xr)
        return Polar(r, a)

    def __str__(self):
        return f"Polar(r={self.r:.4f}, angle={math.degrees(self.a):.4f}°)"


p1 = Polar(5, math.radians(30))
p2 = Polar(3, math.radians(60))
p3 = p1 + p2

print(f"P1 : {p1}")
print(f"P2 : {p2}")
print(f"P1 + P2 = {p3}")