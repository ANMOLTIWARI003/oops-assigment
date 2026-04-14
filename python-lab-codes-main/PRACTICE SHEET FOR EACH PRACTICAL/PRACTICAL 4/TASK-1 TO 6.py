import numpy as np

# ─────────────────────────────────────────────────────────────
# TASK 1: Array Properties
# arr = [[1,2,3],[4,5,6]]
# ─────────────────────────────────────────────────────────────
print("=" * 50)
print("TASK 1: NumPy Array Properties")
print("=" * 50)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Array:\n", arr)
print("a) Number of dimensions :", arr.ndim)
print("b) Shape of the array   :", arr.shape)
print("c) Size of the array    :", arr.size)
print("d) Type of elements     :", arr.dtype)

# ─────────────────────────────────────────────────────────────
# TASK 2: Election Ballot Counter
# Candidates: 1 to 5, anything else = Spoilt Ballot
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("TASK 2: Election Ballot Counter")
print("=" * 50)

ballots = [1, 2, 3, 4, 5, 1, 2, 1, 6, 0, 3, 5, 5, 2, 7, 4, 1, 3]
count = np.zeros(5, dtype=int)  # count[0] = votes for candidate 1, etc.
spoilt = 0

for vote in ballots:
    if 1 <= vote <= 5:
        count[vote - 1] += 1
    else:
        spoilt += 1

print("Ballot Results:")
for i in range(5):
    print(f"  Candidate {i + 1} : {count[i]} votes")
print(f"  Spoilt Ballots : {spoilt}")
print(f"  Winner         : Candidate {np.argmax(count) + 1} with {np.max(count)} votes")

# ─────────────────────────────────────────────────────────────
# TASK 3: Max and Min Difference Pair in Array
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("TASK 3: Max & Min Difference Element Pairs")
print("=" * 50)

n = int(input("Enter number of elements: "))
arr = np.array([int(input(f"  Element {i + 1}: ")) for i in range(n)])

max_diff = -1
min_diff = float('inf')
max_pair = (None, None)
min_pair = (None, None)

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        diff = abs(int(arr[i]) - int(arr[j]))
        if diff > max_diff:
            max_diff = diff
            max_pair = (arr[i], arr[j])
        if diff < min_diff:
            min_diff = diff
            min_pair = (arr[i], arr[j])

print(f"\nArray        : {arr}")
print(f"Max Difference : {max_diff}  (pair: {max_pair[0]}, {max_pair[1]})")
print(f"Min Difference : {min_diff}  (pair: {min_pair[0]}, {min_pair[1]})")

# ─────────────────────────────────────────────────────────────
# TASK 4 & 5: Take 10 integers and copy in reverse order
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("TASK 4 & 5: Copy Array in Reverse Order")
print("=" * 50)

print("Enter 10 integers:")
arr = np.array([int(input(f"  Element {i + 1}: ")) for i in range(10)])
reversed_arr = arr[::-1].copy()

print(f"\nOriginal Array : {arr}")
print(f"Reversed Array : {reversed_arr}")

# ─────────────────────────────────────────────────────────────
# TASK 6: Set Difference Between Two Arrays
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("TASK 6: Set Difference Between Two Arrays")
print("=" * 50)

array1 = np.array([0, 10, 20, 40, 60, 80])
array2 = np.array([10, 30, 40, 50, 70, 90])

set_diff = np.setdiff1d(array1, array2)

print(f"Array1               : {array1}")
print(f"Array2               : {array2}")
print(f"Set Difference (A1 - A2): {set_diff}")