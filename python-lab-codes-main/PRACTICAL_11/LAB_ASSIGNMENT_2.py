"""
Practical No: 11
Lab Assignment-2
Import a dataset of new recruitments in companies such as:
Microsoft, Google, Amazon, IBM, Deloitte, Capgemini, ATOS Origin, Amdocs etc.
Visualize using:
  a) Bar Chart
  b) Pie Chart
  c) Customize Pie Chart
  d) Doughnut Chart
Compare new recruitments in IBM & Amdocs using visualization.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── Sample Recruitment Data ────────────────────────────────────────────────────
data = {
    "Company":      ["Microsoft","Google","Amazon","IBM","Deloitte",
                     "Capgemini","ATOS Origin","Amdocs"],
    "Recruitments": [4500, 5200, 6800, 3200, 4100, 3800, 2700, 2900]
}

df = pd.DataFrame(data)

companies    = df["Company"].tolist()
recruitments = df["Recruitments"].tolist()
colors = ["#4472C4","#ED7D31","#A9D18E","#FF0000",
          "#7030A0","#00B050","#FFC000","#00B0F0"]

# ──────────────────────────────────────────────────────────────────────────────
# a) Bar Chart
# ──────────────────────────────────────────────────────────────────────────────
plt.figure(figsize=(12, 6))
bars = plt.bar(companies, recruitments, color=colors, edgecolor="black", width=0.6)
plt.title("New Recruitments in IT Companies (Bar Chart)", fontsize=14, fontweight="bold")
plt.xlabel("Company")
plt.ylabel("Number of Recruitments")
plt.xticks(rotation=30, ha="right")
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 50,
             str(bar.get_height()),
             ha="center", va="bottom", fontsize=9)
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("11_LA2_a_bar_recruitments.png", dpi=120)
plt.show()
print("(a) Bar Chart saved as 11_LA2_a_bar_recruitments.png")

# ──────────────────────────────────────────────────────────────────────────────
# b) Pie Chart
# ──────────────────────────────────────────────────────────────────────────────
plt.figure(figsize=(9, 9))
plt.pie(recruitments, labels=companies, autopct="%1.1f%%",
        colors=colors, startangle=90)
plt.title("New Recruitments Distribution (Pie Chart)",
          fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("11_LA2_b_pie_recruitments.png", dpi=120)
plt.show()
print("(b) Pie Chart saved as 11_LA2_b_pie_recruitments.png")

# ──────────────────────────────────────────────────────────────────────────────
# c) Customized Pie Chart  (explode + shadow + custom start angle)
# ──────────────────────────────────────────────────────────────────────────────
explode = [0.08 if c in ["IBM","Amdocs"] else 0.02 for c in companies]

plt.figure(figsize=(10, 10))
wedges, texts, autotexts = plt.pie(
    recruitments,
    labels=companies,
    autopct="%1.1f%%",
    colors=colors,
    explode=explode,
    startangle=140,
    shadow=True,
    textprops={"fontsize": 10}
)
for at in autotexts:
    at.set_fontweight("bold")

plt.title("New Recruitments — Customized Pie Chart",
          fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("11_LA2_c_custom_pie.png", dpi=120)
plt.show()
print("(c) Customized Pie Chart saved as 11_LA2_c_custom_pie.png")

# ──────────────────────────────────────────────────────────────────────────────
# d) Doughnut Chart
# ──────────────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 9))
wedges, texts, autotexts = ax.pie(
    recruitments,
    labels=companies,
    autopct="%1.1f%%",
    colors=colors,
    startangle=90,
    wedgeprops=dict(width=0.5)   # <-- creates the doughnut hole
)
ax.set_title("New Recruitments — Doughnut Chart", fontsize=14, fontweight="bold")
# Centre label
ax.text(0, 0, "Total\nRecruits", ha="center", va="center",
        fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig("11_LA2_d_doughnut.png", dpi=120)
plt.show()
print("(d) Doughnut Chart saved as 11_LA2_d_doughnut.png")

# ──────────────────────────────────────────────────────────────────────────────
# Comparison: IBM vs Amdocs Recruitments
# ──────────────────────────────────────────────────────────────────────────────
ibm_val   = df.loc[df["Company"]=="IBM",   "Recruitments"].values[0]
amdocs_val= df.loc[df["Company"]=="Amdocs","Recruitments"].values[0]

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle("IBM vs Amdocs — Recruitment Comparison", fontsize=15, fontweight="bold")

# Bar comparison
axes[0].bar(["IBM","Amdocs"], [ibm_val, amdocs_val],
            color=["#FF0000","#00B0F0"], edgecolor="black", width=0.4)
axes[0].set_title("Bar Chart Comparison")
axes[0].set_ylabel("Recruitments")
for i, v in enumerate([ibm_val, amdocs_val]):
    axes[0].text(i, v + 40, str(v), ha="center", fontweight="bold")
axes[0].set_ylim(0, max(ibm_val, amdocs_val) * 1.2)
axes[0].grid(axis="y", linestyle="--", alpha=0.6)

# Pie comparison
axes[1].pie([ibm_val, amdocs_val],
            labels=["IBM","Amdocs"],
            autopct="%1.1f%%",
            colors=["#FF0000","#00B0F0"],
            startangle=90, shadow=True)
axes[1].set_title("Pie Chart Comparison")

plt.tight_layout()
plt.savefig("11_LA2_ibm_vs_amdocs.png", dpi=120)
plt.show()
print("IBM vs Amdocs comparison saved as 11_LA2_ibm_vs_amdocs.png")