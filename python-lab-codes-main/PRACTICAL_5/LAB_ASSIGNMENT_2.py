# Store prices of sold items in a Tuple, perform 5 operations

print("\nLAB ASSIGNMENT 2")
prices = tuple(map(float, input("Enter prices of sold items separated by spaces: ").split()))

# a) Total number of items sold
print("\na) Total number of items sold:", len(prices))

# b) Price of cheapest item sold
print("b) Cheapest item price: Rs.", min(prices))

# c) Price of costliest item sold
print("c) Costliest item price: Rs.", max(prices))

# d) Price list in ascending order
sorted_prices = tuple(sorted(prices))
print("d) Price list in ascending order:", sorted_prices)

# e) Number of costliest items sold
costliest = max(prices)
count = prices.count(costliest)
print(f"e) Number of costliest items (Rs.{costliest}) sold: {count}")