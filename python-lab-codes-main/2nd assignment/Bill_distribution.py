customer_number = input("Enter Customer Number: ")
units = float(input("Enter Power Consumed (units): "))

if units <= 100:
    amount = units * 1
elif units <= 300:
    amount = 100 + (units - 100) * 1.25
elif units <= 500:
    amount = 350 + (units - 300) * 1.50
else:
    amount = 650 + (units - 500) * 1.75

print("=" * 35)
print(f"{'ELECTRICITY BILL':^35}")
print("=" * 35)
print(f"Customer Number : {customer_number}")
print(f"Units Consumed  : {units}")
print(f"Amount to Pay   : Rs. {amount:.2f}")
print("=" * 35)