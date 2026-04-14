# Read a text file and write contents in UPPERCASE to new file

print("LAB ASSIGNMENT 1")
source = input("Enter source file name (e.g. input.txt): ")
dest   = input("Enter destination file name (e.g. output.txt): ")

try:
    with open(source, "r") as f:
        content = f.read()

    with open(dest, "w") as f:
        f.write(content.upper())

    print(f"\nContents of '{source}':")
    print(content)
    print(f"\nContents written to '{dest}' in UPPERCASE:")
    print(content.upper())

except FileNotFoundError:
    print(f"Error: File '{source}' not found!")