# Employee Information
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
department = input("Enter Department: ")
basic = float(input("Enter Basic Salary: "))

# Calculations
da = 0.92 * basic
hra = 0.58 * basic
ta = 0.30 * basic
lic = 500
gross = basic + da + hra + ta
net_salary = gross - lic

# Display
print("=" * 40)
print(f"{'SALARY SLIP':^40}")
print("=" * 40)
print(f"Name           : {name}")
print(f"Employee ID    : {emp_id}")
print(f"Department     : {department}")
print("-" * 40)
print(f"Basic Salary   : Rs. {basic:.2f}")
print(f"DA (92%)       : Rs. {da:.2f}")
print(f"HRA (58%)      : Rs. {hra:.2f}")
print(f"TA  (30%)      : Rs. {ta:.2f}")
print(f"Gross Salary   : Rs. {gross:.2f}")
print("-" * 40)
print(f"LIC Deduction  : Rs. {lic:.2f}")
print(f"Net Salary     : Rs. {net_salary:.2f}")
print("=" * 40)