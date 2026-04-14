# Accept multiple lines and print in uppercase

print("\nLAB ASSIGNMENT 2")
print("Enter lines of text (type 'done' to stop):")
lines = []
while True:
    line = input()
    if line.lower() == "done":
        break
    lines.append(line)

print("\nOutput:")
for line in lines:
    print(line.upper())