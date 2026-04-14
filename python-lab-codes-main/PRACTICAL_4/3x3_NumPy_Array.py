import numpy as np

numbers = list(map(int, input("Enter 9 space-separated integers: ").split()))
array = np.array(numbers).reshape(3, 3)
print("\n3x3 NumPy Array:")
print(array)