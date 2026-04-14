import numpy as np

print("Enter values for Matrix A (3x3), row by row:")
A = np.array([list(map(int, input(f"Row {i+1}: ").split())) for i in range(3)])

print("Enter values for Matrix B (3x3), row by row:")
B = np.array([list(map(int, input(f"Row {i+1}: ").split())) for i in range(3)])

print("\nMatrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nMatrix Addition (A + B):")
print(A + B)
print("\nMatrix Multiplication (A × B):")
print(np.dot(A, B))