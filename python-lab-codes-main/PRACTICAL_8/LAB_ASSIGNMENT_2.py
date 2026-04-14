# Copy python script to another file without comments

print("\nLAB ASSIGNMENT 2")
source = input("Enter source Python file name (e.g. source.py): ")
dest   = input("Enter destination file name  (e.g. output.py): ")

try:
    with open(source, "r") as f:
        lines = f.readlines()

    no_comments = [line for line in lines
                   if not line.strip().startswith("#") and line.strip() != ""]

    with open(dest, "w") as f:
        f.writelines(no_comments)

    print(f"\nContents of SOURCE file '{source}':")
    print("".join(lines))

    print(f"\nContents of DESTINATION file '{dest}' (without comments):")
    print("".join(no_comments))

except FileNotFoundError:
    print(f"Error: File '{source}' not found!")