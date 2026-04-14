# Employee and Manager classes with inheritance

class Employee:
    def __init__(self):
        self.name    = ""
        self.age     = 0
        self.salary  = 0.0
        self.address = ""

    def get_info(self):
        self.name    = input("Enter Name   : ")
        self.age     = int(input("Enter Age    : "))
        self.salary  = float(input("Enter Salary : Rs. "))
        self.address = input("Enter Address: ")

    def print_info(self):
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Salary  : Rs. {self.salary:.2f}")
        print(f"Address : {self.address}")


class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.department = ""
        self.team_size  = 0

    def get_info(self):
        super().get_info()
        self.department = input("Enter Department : ")
        self.team_size  = int(input("Enter Team Size  : "))

    def print_info(self):
        super().print_info()
        print(f"Department : {self.department}")
        print(f"Team Size  : {self.team_size}")


print("LAB ASSIGNMENT 1 - EMPLOYEE & MANAGER")
managers = []

for i in range(10):
    print(f"\nEnter details for Manager {i+1}:")
    m = Manager()
    m.get_info()
    managers.append(m)

print("\n===== ALL MANAGER DETAILS =====")
for i, m in enumerate(managers):
    print(f"\nManager {i+1}:")
    m.print_info()