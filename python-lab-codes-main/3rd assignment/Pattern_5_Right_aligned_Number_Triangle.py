n = 5
i = 1
while i <= n:
    # Print spaces
    j = 1
    while j <= (n - i):
        print("  ", end="")
        j += 1
    # Print numbers
    k = 1
    while k <= i:
        print(k, end=" ")
        k += 1
    print()
    i += 1