import math

# Area of Circle
r = float(input("Enter radius of circle: "))
area = math.pi * r ** 2
print(f"Area of Circle        = {area:.2f}")

# Circumference of Circle
circumference = 2 * math.pi * r
print(f"Circumference         = {circumference:.2f}")

# Volume of Cube
side = float(input("Enter side of cube: "))
vol_cube = side ** 3
print(f"Volume of Cube        = {vol_cube:.2f}")

# Volume of Cone
radius_cone = float(input("Enter radius of cone: "))
height_cone = float(input("Enter height of cone: "))
vol_cone = (1/3) * math.pi * radius_cone ** 2 * height_cone
print(f"Volume of Cone        = {vol_cone:.2f}")