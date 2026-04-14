import pandas as pd

# ── Create the States DataFrame ───────────────────────────────────────────────
data = {
    "state": ["Maharashtra", "Uttar Pradesh", "Rajasthan", "Tamil Nadu", "Karnataka"],
    "area_km2": [307713, 240928, 342239, 130058, 191791],
    "population": [112374333, 199812341, 68548437, 72147030, 61095297]
}

df = pd.DataFrame(data)

# ──────────────────────────────────────────────────────────────────────────────
# a) Print the complete information of states
# ──────────────────────────────────────────────────────────────────────────────
print("=" * 65)
print("         COMPLETE INFORMATION OF STATES")
print("=" * 65)
print(df.to_string(index=False))
print()

# ──────────────────────────────────────────────────────────────────────────────
# b) Print the name of the State having largest Area
# ──────────────────────────────────────────────────────────────────────────────
print("=" * 65)
print(" STATE WITH LARGEST AREA")
print("=" * 65)
largest_area_state = df.loc[df["area_km2"].idxmax(), "state"]
print(f"State with Largest Area : {largest_area_state}")
print(f"Area : {df['area_km2'].max()} km²")
print()

# ──────────────────────────────────────────────────────────────────────────────
# c) Print the name of State having largest population
# ──────────────────────────────────────────────────────────────────────────────
print("=" * 65)
print(" STATE WITH LARGEST POPULATION")
print("=" * 65)
largest_pop_state = df.loc[df["population"].idxmax(), "state"]
print(f"State with Largest Population : {largest_pop_state}")
print(f"Population : {df['population'].max():,}")
print()

# ──────────────────────────────────────────────────────────────────────────────
# d) Calculate the population density of States
# ──────────────────────────────────────────────────────────────────────────────
df["pop_density"] = (df["population"] / df["area_km2"]).round(2)

print("=" * 65)
print(" POPULATION DENSITY OF STATES  (persons per km²)")
print("=" * 65)
print(df[["state", "area_km2", "population", "pop_density"]].to_string(index=False))
print()

# ──────────────────────────────────────────────────────────────────────────────
# e) Determine the name of State with highest population density
# ──────────────────────────────────────────────────────────────────────────────
print("=" * 65)
print(" STATE WITH HIGHEST POPULATION DENSITY")
print("=" * 65)
highest_density_state = df.loc[df["pop_density"].idxmax(), "state"]
print(f"State with Highest Population Density : {highest_density_state}")
print(f"Population Density : {df['pop_density'].max()} persons/km²")
print()