
import pandas as pd
import numpy as np

# ─────────────────────────────────────────────────────────────
# TASK 1: Read CSV and display first 5 rows
# ─────────────────────────────────────────────────────────────
print("=" * 55)
print("TASK 1: Read CSV & Display First 5 Rows")
print("=" * 55)

# Create a sample CSV for demo
csv_data = """product,category,price,stock
Denim Jeans,Bottomwear,1500,30
Cotton Shirt,Topwear,1200,50
Silk Saree,Ethnicwear,5000,20
Woolen Sweater,Winterwear,2000,15
Sports T-Shirt,Active Wear,800,60
Leather Jacket,Topwear,3500,10
Kurta,Ethnicwear,900,45
Track Pants,Active Wear,700,55
"""
with open("items.csv", "w") as f:
    f.write(csv_data.strip())

df = pd.read_csv("items.csv")
print("First 5 rows:")
print(df.head())


# ─────────────────────────────────────────────────────────────
# TASK 2: Mean & Standard Deviation of Chaotic Series
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("TASK 2: Mean & Std Dev of Chaotic Series")
print("=" * 55)

np.random.seed(42)
chaotic_series = pd.Series(np.random.randint(1, 500, size=20))
print(f"Chaotic Series:\n{chaotic_series.values}")
print(f"\nMean               : {chaotic_series.mean():.4f}")
print(f"Standard Deviation : {chaotic_series.std():.4f}")
print(f"Variance           : {chaotic_series.var():.4f}")
print(f"Min                : {chaotic_series.min()}")
print(f"Max                : {chaotic_series.max()}")


# ─────────────────────────────────────────────────────────────
# TASK 3: Automotive Store Dataset
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("TASK 3: Automotive Store Dataset")
print("=" * 55)

auto_data = """part_id,part_name,category,price,stock
A001,Engine Oil,Lubricants,450,100
A002,Brake Pads,Brakes,1200,50
A003,Air Filter,Filters,350,75
A004,Spark Plug,Ignition,200,120
A005,Car Battery,Electrical,4500,30
A006,Timing Belt,Engine,900,40
A007,Headlight Bulb,Lighting,250,90
A008,Windshield Washer,Body,150,200
A009,Clutch Plate,Transmission,3200,
A010,Gear Oil,Lubricants,600,60
"""
with open("automotive.csv", "w") as f:
    f.write(auto_data.strip())

df_auto = pd.read_csv("automotive.csv")

print("a) First & Last 5 Rows:")
print(df_auto.head())
print(df_auto.tail())

print("\nb) Cleaning Dataset (fill missing stock with 0):")
df_auto["stock"].fillna(0, inplace=True)
df_auto.to_csv("automotive.csv", index=False)
print("   Dataset cleaned and saved.")
print(df_auto)

print(f"\nc) Most Expensive Part: {df_auto.loc[df_auto['price'].idxmax(), 'part_name']} "
      f"- Rs. {df_auto['price'].max()}")
print(f"d) Total Automotive Parts in Store: {int(df_auto['stock'].sum())}")


# ─────────────────────────────────────────────────────────────
# TASK 4: Medical Store sales.csv
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("TASK 4: Medical Store — sales.csv")
print("=" * 55)

sales_data = """item_no,item_name,price,quantity_sold
M001,Paracetamol,35,200
M002,Amoxicillin,80,150
M003,Cough Syrup,95,100
M004,Vitamin C,60,180
M005,Antacid,45,130
M006,Ibuprofen,40,160
"""
with open("sales.csv", "w") as f:
    f.write(sales_data.strip())

df_med = pd.read_csv("sales.csv")
df_med["total_amount"] = df_med["price"] * df_med["quantity_sold"]

print("a) List of Medical Items:")
print(df_med[["item_no", "item_name", "price"]].to_string(index=False))
print(f"\nb) Total number of items sold : {df_med['quantity_sold'].sum()}")
print(f"c) Total price of all items   : Rs. {df_med['total_amount'].sum():.2f}")


# ─────────────────────────────────────────────────────────────
# TASK 5: Infosys employee.xlsx (simulated with DataFrame)
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("TASK 5: Infosys Employee Reports")
print("=" * 55)

emp_data = {
    "EmpID":       ["INF001","INF002","INF003","INF004","INF005","INF006","INF007","INF008"],
    "EmpName":     ["Amit Sharma","Priya Mehta","Rohit Verma","Sneha Patel",
                    "Arjun Nair","Kavya Reddy","Suresh Kumar","Meena Joshi"],
    "Department":  ["Automotive","Finance","Automotive","IT","Automotive",
                    "IT","Finance","Automotive"],
    "Designation": ["Developer","Analyst","Developer","Manager",
                    "Tester","Developer","Analyst","Developer"],
}

df_emp = pd.DataFrame(emp_data)
# save as xlsx if openpyxl available, else csv
try:
    df_emp.to_excel("employee.xlsx", index=False)
    df_read = pd.read_excel("employee.xlsx")
except Exception:
    df_emp.to_csv("employee.csv", index=False)
    df_read = pd.read_csv("employee.csv")

print("a) Employees in Automotive Domain:")
auto_emp = df_read[df_read["Department"] == "Automotive"]
print(auto_emp.to_string(index=False))

emp_id = input("\nb) Enter Employee ID to search: ").strip()
result = df_read[df_read["EmpID"] == emp_id]
if result.empty:
    print("Employee not found.")
else:
    print(result.to_string(index=False))

print("\nd) All Developers at Infosys:")
devs = df_read[df_read["Designation"] == "Developer"]
print(devs.to_string(index=False))