import numpy as np

print("Enter values for 5x3 Matrix, row by row:")
A = np.array([list(map(int, input(f"Row {i+1}: ").split())) for i in range(5)])

print("Enter values for 3x2 Matrix, row by row:")
B = np.array([list(map(int, input(f"Row {i+1}: ").split())) for i in range(3)])

product = np.dot(A, B)
print("\n5x3 Matrix:")
print(A)
print("\n3x2 Matrix:")
print(B)
print("\nProduct Matrix (5x2):")
print(product)