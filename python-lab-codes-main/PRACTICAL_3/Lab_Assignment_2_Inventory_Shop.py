# Input items
items = list(map(int, input("Enter item numbers separated by spaces: ").split()))

# a) Total number of items
print(f"\na) Total number of items: {len(items)}")

# b) Last item number
print(f"b) Last item number: {items[-1]}")

# c) Sorted list
print(f"c) Sorted list: {sorted(items)}")

# d) Check for item 515
if 515 in items:
    print("d) Yes (515 found in list)")
else:
    print("d) No (515 not in list)")

# e) Add 121, 321 and sort
items.extend([121, 321])
items.sort()
print(f"e) Updated sorted list: {items}")