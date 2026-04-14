# Vendor Details
name = input("Enter Vendor Name: ")
year = input("Enter Year of Association: ")
contact = input("Enter Contact Number: ")
email = input("Enter eMail ID: ")

# Monthly Purchases
months = ["Jan","Feb","Mar","Apr","May","Jun",
          "Jul","Aug","Sep","Oct","Nov","Dec"]
purchases = []

print("\nEnter monthly purchase amounts:")
for month in months:
    amount = float(input(f"  {month}: Rs. "))
    purchases.append(amount)

total = sum(purchases)
average = total / 12

# Report
print("\n" + "=" * 45)
print(f"{'ANNUAL PURCHASE / BILLING REPORT':^45}")
print("=" * 45)
print(f"Vendor Name       : {name}")
print(f"Year of Association: {year}")
print(f"Contact Number    : {contact}")
print(f"eMail ID          : {email}")
print("-" * 45)
print(f"{'Month':<10} {'Purchase Amount':>20}")
print("-" * 45)
for i in range(12):
    print(f"{months[i]:<10} Rs. {purchases[i]:>15.2f}")
print("-" * 45)
print(f"{'Total':<10} Rs. {total:>15.2f}")
print(f"{'Average':<10} Rs. {average:>15.2f}")
print("=" * 45)