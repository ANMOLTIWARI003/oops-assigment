# ─────────────────────────────────────────────────────────────
# TASK 3: Steel Industry Boiler Control System
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("   TASK 3: Boiler Control System — Steel Industry")
print("=" * 55)

pressure = float(input("Enter Boiler Pressure (bars): "))
temperature = float(input("Enter Boiler Temperature (°C): "))
water_level = input("Enter Water Level (below/normal/above): ").strip().lower()

print("\n--- Boiler Control Decisions ---")
if water_level == "below":
    print("ACTION: Turn ON water pump & Open water inlet.")
elif water_level == "above":
    print("ACTION: Close water inlet & Turn OFF water pump.")
elif water_level == "normal":
    if pressure < 4:
        print("ACTION: Turn ON the furnace.")
    elif 15 <= pressure <= 17:
        print("ACTION: Turn OFF the furnace.")
    elif pressure > 18:
        print("ACTION: Open the pressure outlet.")
    else:
        print("ACTION: System operating normally. No action needed.")
else:
    print("Invalid water level input.")