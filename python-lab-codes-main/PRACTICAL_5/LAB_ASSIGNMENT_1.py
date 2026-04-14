# User enters integers stored in a tuple, perform 5 operations

print("LAB ASSIGNMENT 1")
nums = tuple(map(int, input("Enter integers separated by spaces: ").split()))

# a) Total number of items in the Tuple
print("\na) Total number of items:", len(nums))

# b) Print the last item in the Tuple
print("b) Last item:", nums[-1])

# c) Print the Tuple elements in reverse order
print("c) Reversed tuple:", nums[::-1])

# d) Print Yes if Tuple contains 5 and No otherwise
if 5 in nums:
    print("d) Yes (5 is present in the tuple)")
else:
    print("d) No (5 is not present in the tuple)")

# e) Remove first and last items, sort remaining and print
remaining = nums[1:-1]
sorted_remaining = tuple(sorted(remaining))
print("e) After removing first & last, sorted:", sorted_remaining)