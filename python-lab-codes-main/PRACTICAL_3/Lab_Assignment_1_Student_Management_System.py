students = []

def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    students.append({"id": sid, "name": name})
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
    else:
        print(f"\n{'ID':<10} {'Name':<20}")
        print("-" * 30)
        for s in students:
            print(f"{s['id']:<10} {s['name']:<20}")

def update_student():
    sid = input("Enter Student ID to update: ")
    for s in students:
        if s["id"] == sid:
            s["name"] = input("Enter new name: ")
            print("Updated successfully!")
            return
    print("Student not found.")

def delete_student():
    sid = input("Enter Student ID to delete: ")
    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("Deleted successfully!")
            return
    print("Student not found.")

def search_student():
    key = input("Enter Name or ID to search: ")
    found = [s for s in students if s["id"] == key or s["name"].lower() == key.lower()]
    if found:
        for s in found:
            print(f"ID: {s['id']}, Name: {s['name']}")
    else:
        print("No student found.")

# Main Menu
while True:
    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")
    choice = input("Enter choice: ")

    if choice == "1": add_student()
    elif choice == "2": view_students()
    elif choice == "3": update_student()
    elif choice == "4": delete_student()
    elif choice == "5": search_student()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")