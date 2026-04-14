
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ─────────────────────────────────────────────────────────────
# TASK 1: Plot y = 2x + 3  for x from -10 to 10
# ─────────────────────────────────────────────────────────────
print("=" * 50)
print("TASK 1: Line Plot y = 2x + 3")
print("=" * 50)

x = np.linspace(-10, 10, 200)
y = 2 * x + 3

plt.figure(figsize=(8, 5))
plt.plot(x, y, color="blue", linewidth=2, label="y = 2x + 3")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.title("Plot of y = 2x + 3", fontsize=14)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("11_task1_line_y2x3.png", dpi=120)
plt.show()
print("Saved: 11_task1_line_y2x3.png")


# ─────────────────────────────────────────────────────────────
# TASK 2: Bar Chart — Votes per Candidate in Public Survey
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("TASK 2: Bar Chart — Election Survey Votes")
print("=" * 50)

candidates = ["Candidate A", "Candidate B", "Candidate C",
              "Candidate D", "Candidate E"]
votes      = [340, 280, 410, 195, 360]
colors     = ["#4472C4","#ED7D31","#A9D18E","#FF0000","#7030A0"]

plt.figure(figsize=(9, 5))
bars = plt.bar(candidates, votes, color=colors, edgecolor="black", width=0.5)
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
             str(bar.get_height()), ha="center", fontsize=10)
plt.title("Public Survey — Votes per Candidate", fontsize=14)
plt.xlabel("Candidate")
plt.ylabel("Number of Votes")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("11_task2_bar_votes.png", dpi=120)
plt.show()
print("Saved: 11_task2_bar_votes.png")


# ─────────────────────────────────────────────────────────────
# TASK 3: Histogram — Student Exam Scores Distribution
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("TASK 3: Histogram — Exam Score Distribution")
print("=" * 50)

np.random.seed(10)
scores = np.random.randint(20, 100, 50)

plt.figure(figsize=(9, 5))
plt.hist(scores, bins=range(10, 101, 10), color="steelblue",
         edgecolor="black", rwidth=0.85)
plt.title("Distribution of Student Exam Scores", fontsize=14)
plt.xlabel("Score Range")
plt.ylabel("Number of Students")
plt.xticks(range(10, 101, 10))
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("11_task3_histogram_scores.png", dpi=120)
plt.show()
print("Saved: 11_task3_histogram_scores.png")


# ─────────────────────────────────────────────────────────────
# TASK 4: Scatter Plot — Height vs Weight
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("TASK 4: Scatter Plot — Height vs Weight")
print("=" * 50)

# Create a sample height-weight file
hw_data = "height,weight\n" + "\n".join(
    [f"{h},{w}" for h, w in zip(
        np.random.randint(150, 195, 40),
        np.random.randint(45, 95, 40)
    )]
)
with open("height_weight.txt", "w") as f:
    f.write(hw_data)

df_hw = pd.read_csv("height_weight.txt")

plt.figure(figsize=(8, 6))
plt.scatter(df_hw["height"], df_hw["weight"],
            color="coral", edgecolors="black", s=60, alpha=0.8)
plt.title("Height vs Weight Scatter Plot", fontsize=14)
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("11_task4_scatter_height_weight.png", dpi=120)
plt.show()
print("Saved: 11_task4_scatter_height_weight.png")


# ─────────────────────────────────────────────────────────────
# TASK 5: Earthquake lat-long Scatter Plot on World Map
# (Using matplotlib only — Cartopy optional)
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("TASK 5: Earthquake Lat-Long Scatter Plot")
print("=" * 50)

eq_lat  = [35.6, -6.2, 28.7, 37.7, 1.3, -33.9, 51.5, 19.4, 39.9, -23.5]
eq_long = [139.7, 106.8, 77.1, -122.4, 103.8, 151.2, -0.1, -99.1, 116.4, -46.6]
magnitudes = [6.5, 5.8, 4.2, 3.9, 5.1, 4.7, 3.5, 6.1, 4.9, 5.4]

plt.figure(figsize=(12, 6))
# Simple world background using axis limits
plt.xlim(-180, 180)
plt.ylim(-90, 90)
plt.axhline(0, color="gray", linewidth=0.5, linestyle="--")
plt.axvline(0, color="gray", linewidth=0.5, linestyle="--")

scatter = plt.scatter(eq_long, eq_lat, c=magnitudes, cmap="Reds",
                      s=[m * 40 for m in magnitudes],
                      edgecolors="black", alpha=0.8, linewidths=0.5)
plt.colorbar(scatter, label="Magnitude")
plt.title("Earthquake Locations — Lat/Long Scatter Plot", fontsize=14)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig("11_task5_earthquake_scatter.png", dpi=120)
plt.show()
print("Saved: 11_task5_earthquake_scatter.png")


# ─────────────────────────────────────────────────────────────
# TASK 6: Cosmetic Company Sales Visualization
#   a) Line Plot — total profit per month
#   b) Multiline Plot — all product sales
#   c) Bar Chart — Face Cream vs Face Wash
#   d) Pie Chart — total yearly sales per product
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("TASK 6: Cosmetic Company Sales Analysis")
print("=" * 50)

months   = ["Jan","Feb","Mar","Apr","May","Jun",
            "Jul","Aug","Sep","Oct","Nov","Dec"]
data = {
    "Month":         months,
    "FaceCream":     [1500,1800,2100,2400,2200,2600,2800,3000,2700,2500,2300,2900],
    "FaceWash":      [1200,1400,1600,1500,1700,1800,1900,2000,1850,1750,1650,2100],
    "MoistureCream": [800, 950,1100,1000,1200,1300,1400,1500,1350,1250,1150,1600],
    "Sunscreen":     [600, 700, 900,1100,1300,1500,1400,1200,1000, 800, 650, 700],
    "Lipstick":      [900,1000,1100,1050,1150,1200,1300,1400,1250,1100,1050,1500],
    "Profit":        [5000,5500,6200,6800,7000,7500,8000,8500,7800,7200,6800,8000]
}
df = pd.DataFrame(data)

# a) Line Plot — Total Profit
plt.figure(figsize=(10, 5))
plt.plot(df["Month"], df["Profit"], marker="o", color="blue",
         linewidth=2, markersize=7)
plt.title("Total Monthly Profit — Cosmetic Company", fontsize=14)
plt.xlabel("Month"); plt.ylabel("Profit (Rs.)")
plt.xticks(rotation=45); plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("11_task6a_line_profit.png", dpi=120)
plt.show()
print("Saved: 11_task6a_line_profit.png")

# b) Multiline Plot — All Products
products = ["FaceCream","FaceWash","MoistureCream","Sunscreen","Lipstick"]
colors_p = ["red","green","blue","orange","purple"]
plt.figure(figsize=(12, 6))
for prod, col in zip(products, colors_p):
    plt.plot(df["Month"], df[prod], marker="o", linewidth=2, label=prod, color=col)
plt.title("All Product Sales — Multiline Plot", fontsize=14)
plt.xlabel("Month"); plt.ylabel("Units Sold")
plt.xticks(rotation=45); plt.legend(); plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("11_task6b_multiline.png", dpi=120)
plt.show()
print("Saved: 11_task6b_multiline.png")

# c) Bar Chart — Face Cream vs Face Wash
x = np.arange(len(months)); w = 0.35
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x - w/2, df["FaceCream"], w, label="Face Cream", color="skyblue")
ax.bar(x + w/2, df["FaceWash"],  w, label="Face Wash",  color="salmon")
ax.set_title("Face Cream vs Face Wash Sales", fontsize=14)
ax.set_xlabel("Month"); ax.set_ylabel("Units")
ax.set_xticks(x); ax.set_xticklabels(months, rotation=45)
ax.legend(); ax.grid(axis="y", linestyle="--", alpha=0.5)
fig.tight_layout()
plt.savefig("11_task6c_bar_fc_fw.png", dpi=120)
plt.show()
print("Saved: 11_task6c_bar_fc_fw.png")

# d) Pie Chart — Total Yearly Sales
totals = [df[p].sum() for p in products]
plt.figure(figsize=(8, 8))
plt.pie(totals, labels=products, autopct="%1.1f%%",
        colors=colors_p, startangle=140, shadow=True)
plt.title("Total Yearly Sales per Product", fontsize=14)
plt.tight_layout()
plt.savefig("11_task6d_pie_yearly.png", dpi=120)
plt.show()
print("Saved: 11_task6d_pie_yearly.png")