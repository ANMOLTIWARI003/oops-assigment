# PYTHON TUPLE PROGRAMS - ALL 36 QUESTIONS

# 1. Create a tuple with three elements: 10, "hello", and 3.14
t = (10, "hello", 3.14)
print("Tuple:", t)

# 2. Given the tuple (1, 2, 3, 4, 5), access and print the third element
t = (1, 2, 3, 4, 5)
print("Third element:", t[2])

# 3. Concatenate the tuples (1, 2, 3) and (4, 5, 6) and store result in new tuple
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print("Concatenated tuple:", t3)

# 4. Unpack the tuple (a, b, c) into three variables and print their values
t = (10, 20, 30)
a, b, c = t
print(f"a={a}, b={b}, c={c}")

# 5. Check if the element 7 exists in the tuple (1, 3, 5, 7, 9)
t = (1, 3, 5, 7, 9)
if 7 in t:
    print("7 EXISTS in the tuple.")
else:
    print("7 does NOT exist in the tuple.")

# 6. Create a tuple (0,1,2,3,4,5) and print slice from index 2 to 4
t = (0, 1, 2, 3, 4, 5)
print("Slice index 2 to 4:", t[2:5])

# 7. Find the length of the tuple (10, 20, 30, 40, 50)
t = (10, 20, 30, 40, 50)
print("Length of tuple:", len(t))

# 8. Create a tuple (1, 2, 3) and repeat it three times
t = (1, 2, 3)
print("Repeated tuple:", t * 3)

# 9. Convert the list [1, 2, 3] to a tuple
lst = [1, 2, 3]
t = tuple(lst)
print("List to tuple:", t)

# 10. Find minimum and maximum values in the tuple (5, 12, 3, 8, 15)
t = (5, 12, 3, 8, 15)
print("Minimum:", min(t))
print("Maximum:", max(t))

# 11. Count the number of occurrences of element 2 in (1, 2, 3, 2, 4, 2)
t = (1, 2, 3, 2, 4, 2)
print("Occurrences of 2:", t.count(2))

# 12. Check if all elements in the tuple (True, True, False) are True
t = (True, True, False)
if all(t):
    print("ALL elements are True.")
else:
    print("NOT all elements are True.")

# 13. Find index of first occurrence of element 3 in (1, 2, 3, 4, 3, 5)
t = (1, 2, 3, 4, 3, 5)
print("First index of 3:", t.index(3))

# 14. Sort the elements of (5, 2, 8, 1, 3) and store result in new tuple
t = (5, 2, 8, 1, 3)
sorted_t = tuple(sorted(t))
print("Sorted tuple:", sorted_t)

# 15. Create a tuple containing squares of numbers from 1 to 5
squares = tuple(x**2 for x in range(1, 6))
print("Squares tuple:", squares)

# 16. Write a Python program to create a tuple
t = (1, 2, 3, 4, 5)
print("Created tuple:", t)

# 17. Write a Python program to create a tuple with different data types
t = (10, "hello", 3.14, True, [1, 2], (3, 4))
print("Mixed data type tuple:", t)

# 18. Create a tuple of numbers and print one item
t = (10, 20, 30, 40, 50)
print("Tuple:", t)
print("Item at index 2:", t[2])

# 19. Unpack a tuple into several variables
t = (1, 2, 3, 4, 5)
a, b, c, d, e = t
print(f"a={a}, b={b}, c={c}, d={d}, e={e}")

# 20. Add an item to a tuple
t = (1, 2, 3)
t = t + (4,)
print("After adding item:", t)

# 21. Convert a tuple to a string
t = ('p', 'y', 't', 'h', 'o', 'n')
s = "".join(t)
print("Tuple to string:", s)

# 22. Get the 4th element from the last element of a tuple
t = (1, 2, 3, 4, 5, 6, 7, 8)
print("4th element from last:", t[-4])

# 23. Create the colon of a tuple
t = (1, 2, 3, 4, 5)
print("First half :", t[:len(t)//2])
print("Second half:", t[len(t)//2:])
print("Full slice :", t[:])

# 24. Find repeated items in a tuple
t = (1, 2, 3, 2, 4, 3, 5, 1)
repeated = set(x for x in t if t.count(x) > 1)
print("Repeated items:", repeated)

# 25. Check whether an element exists within a tuple
t = (10, 20, 30, 40, 50)
elem = int(input("Enter element to search in tuple: "))
if elem in t:
    print(f"{elem} EXISTS in the tuple.")
else:
    print(f"{elem} does NOT exist in the tuple.")

# 26. Convert a list to a tuple
lst = [1, 2, 3, 4, 5]
t = tuple(lst)
print("List:", lst)
print("Converted tuple:", t)

# 27. Remove an item from a tuple
t = (1, 2, 3, 4, 5)
remove = 3
t = tuple(x for x in t if x != remove)
print(f"After removing {remove}:", t)

# 28. Slice a tuple
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("First 4      :", t[:4])
print("Last 4       :", t[-4:])
print("Middle       :", t[3:7])
print("Every 2nd    :", t[::2])
print("Reverse      :", t[::-1])

# 29. Find the index of an item in a tuple
t = (10, 20, 30, 40, 50)
item = int(input("Enter item to find index: "))
if item in t:
    print(f"Index of {item}:", t.index(item))
else:
    print(f"{item} not found in tuple.")

# 30. Find the length of a tuple
t = (1, 2, 3, 4, 5)
print("Length of tuple:", len(t))

# 31. Convert a tuple to a dictionary
keys   = ('name', 'age', 'city')
values = ('Alice', 25, 'Nagpur')
d = dict(zip(keys, values))
print("Tuple to dictionary:", d)

# 32. Unzip a list of tuples into individual lists
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
nums, chars = zip(*pairs)
print("Numbers list:", list(nums))
print("Chars list  :", list(chars))

# 33. Reverse a tuple
t = (1, 2, 3, 4, 5)
reversed_t = t[::-1]
print("Reversed tuple:", reversed_t)

# 34. Convert a list of tuples into a dictionary
lst = [('name', 'Alice'), ('age', 25), ('city', 'Nagpur')]
d = dict(lst)
print("List of tuples to dictionary:", d)

# 35. Remove empty tuple(s) from a list of tuples
lst = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d',)]
result = [t for t in lst if t and any(x != '' for x in t)]
print("After removing empty tuples:", result)

# 36. Convert a given string list to a tuple
s = "python 3.0"
t = tuple(s)
print("Original string:", s)
print("Converted tuple:", t)