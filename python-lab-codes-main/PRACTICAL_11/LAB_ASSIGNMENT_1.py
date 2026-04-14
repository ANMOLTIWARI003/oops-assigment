"""
Practical No: 11
Lab Assignment-1
Import sales data of a Cosmetic Company.
Analyze through visualization using Matplotlib:
  a) Total profit of all months  - Line Plot
  b) All product sales data       - Multiline Plot
  c) Face Cream & Face Wash       - Bar Chart
  d) Total sale per product       - Pie Chart
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ── Create sample Cosmetic Sales Data ─────────────────────────────────────────
months = ["Jan","Feb","Mar","Apr","May","Jun",
          "Jul","Aug","Sep","Oct","Nov","Dec"]

data = {
    "Month":        months,
    "FaceCream":    [1500,1800,2100,2400,2200,2600,2800,3000,2700,2500,2300,2900],
    "FaceWash":     [1200,1400,1600,1500,1700,1800,1900,2000,1850,1750,1650,2100],
    "MoistureCream":[800, 950, 1100,1000,1200,1300,1400,1500,1350,1250,1150,1600],
    "Sunscreen":    [600, 700, 900, 1100,1300,1500,1400,1200,1000,800, 650, 700],
    "Lipstick":     [900, 1000,1100,1050,1150,1200,1300,1400,1250,1100,1050,1500],
    "Profit":       [5000,5500,6200,6800,7000,7500,8000,8500,7800,7200,6800,8000]
}

df = pd.DataFrame(data)

# ──────────────────────────────────────────────────────────────────────────────
# a) Total profit of all months — Line Plot
# ──────────────────────────────────────────────────────────────────────────────
plt.figure(figsize=(10, 5))
plt.plot(df["Month"], df["Profit"], marker="o", color="blue",
         linewidth=2, markersize=7, label="Monthly Profit")
plt.title("Total Profit of All Months", fontsize=14, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Profit (Rs.)")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("11_LA1_a_line_profit.png", dpi=120)
plt.show()
print("(a) Line Plot saved as 11_LA1_a_line_profit.png")

# ──────────────────────────────────────────────────────────────────────────────
# b) All product sales data — Multiline Plot
# ──────────────────────────────────────────────────────────────────────────────
products = ["FaceCream","FaceWash","MoistureCream","Sunscreen","Lipstick"]
colors   = ["red","green","blue","orange","purple"]

plt.figure(figsize=(12, 6))
for product, color in zip(products, colors):
    plt.plot(df["Month"], df[product], marker="o", linewidth=2,
             label=product, color=color)

plt.title("All Product Sales Data (Multiline Plot)", fontsize=14, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.xticks(rotation=45)
plt.legend(loc="upper left")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("11_LA1_b_multiline_products.png", dpi=120)
plt.show()
print("(b) Multiline Plot saved as 11_LA1_b_multiline_products.png")

# ──────────────────────────────────────────────────────────────────────────────
# c) Face Cream & Face Wash — Bar Chart
# ──────────────────────────────────────────────────────────────────────────────
x = np.arange(len(months))
width = 0.35

fig, ax = plt.subplots(figsize=(12, 6))
bars1 = ax.bar(x - width/2, df["FaceCream"], width, label="Face Cream", color="skyblue")
bars2 = ax.bar(x + width/2, df["FaceWash"],  width, label="Face Wash",  color="salmon")

ax.set_title("Face Cream vs Face Wash Sales (Bar Chart)", fontsize=14, fontweight="bold")
ax.set_xlabel("Month")
ax.set_ylabel("Units Sold")
ax.set_xticks(x)
ax.set_xticklabels(months, rotation=45)
ax.legend()
ax.grid(axis="y", linestyle="--", alpha=0.6)
fig.tight_layout()
plt.savefig("11_LA1_c_bar_facecream_facewash.png", dpi=120)
plt.show()
print("(c) Bar Chart saved as 11_LA1_c_bar_facecream_facewash.png")

# ──────────────────────────────────────────────────────────────────────────────
# d) Total sale per product for last year — Pie Chart
# ──────────────────────────────────────────────────────────────────────────────
total_sales = [df[p].sum() for p in products]
explode = (0.05, 0.05, 0.05, 0.05, 0.05)

plt.figure(figsize=(8, 8))
plt.pie(total_sales, labels=products, autopct="%1.1f%%",
        explode=explode, colors=["red","green","blue","orange","purple"],
        startangle=140, shadow=True)
plt.title("Total Sale Per Product - Last Year (Pie Chart)",
          fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("11_LA1_d_pie_total_sales.png", dpi=120)
plt.show()
print("(d) Pie Chart saved as 11_LA1_d_pie_total_sales.png")