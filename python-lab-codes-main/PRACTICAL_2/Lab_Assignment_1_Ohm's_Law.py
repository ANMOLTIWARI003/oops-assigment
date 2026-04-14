V = float(input("Enter Voltage (V): "))
R = float(input("Enter Resistance (R) in ohms: "))

# Ohm's Law: I = V / R
current = V / R

print(f"\nCurrent (I) = {current:.4f} A")

# Nature of current
if current < 0.5:
    print("Nature: Low Current")
elif 0.5 <= current <= 2:
    print("Nature: Normal Current")
else:
    print("Nature: High Current")