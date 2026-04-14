# Library Management System

class Book:
    def __init__(self, book_id, title, author):
        self.book_id   = book_id
        self.title     = title
        self.author    = author
        self.is_available = True

    def display(self):
        status = "Available" if self.is_available else "Issued"
        print(f"ID: {self.book_id} | Title: {self.title} | "
              f"Author: {self.author} | Status: {status}")


class Member:
    def __init__(self, member_id, name):
        self.member_id    = member_id
        self.name         = name
        self.borrowed     = []

    def display(self):
        print(f"Member ID: {self.member_id} | Name: {self.name} | "
              f"Books Borrowed: {self.borrowed}")


class Library:
    def __init__(self):
        self.books   = []
        self.members = []

    def add_book(self):
        bid    = input("Enter Book ID   : ")
        title  = input("Enter Title     : ")
        author = input("Enter Author    : ")
        self.books.append(Book(bid, title, author))
        print("Book added successfully!")

    def add_member(self):
        mid  = input("Enter Member ID : ")
        name = input("Enter Name      : ")
        self.members.append(Member(mid, name))
        print("Member added successfully!")

    def lend_book(self):
        bid = input("Enter Book ID to lend  : ")
        mid = input("Enter Member ID        : ")
        book   = next((b for b in self.books   if b.book_id   == bid), None)
        member = next((m for m in self.members if m.member_id == mid), None)

        if not book:
            print("Book not found!")
        elif not member:
            print("Member not found!")
        elif not book.is_available:
            print("Book is already issued!")
        else:
            book.is_available = False
            member.borrowed.append(bid)
            print(f"Book '{book.title}' issued to {member.name}.")

    def return_book(self):
        bid = input("Enter Book ID to return: ")
        mid = input("Enter Member ID        : ")
        book   = next((b for b in self.books   if b.book_id   == bid), None)
        member = next((m for m in self.members if m.member_id == mid), None)

        if not book:
            print("Book not found!")
        elif not member:
            print("Member not found!")
        elif bid not in member.borrowed:
            print("This member did not borrow this book!")
        else:
            book.is_available = True
            member.borrowed.remove(bid)
            print(f"Book '{book.title}' returned successfully.")

    def display_books(self):
        if not self.books:
            print("No books in library.")
        else:
            print("\n===== BOOK LIST =====")
            for b in self.books:
                b.display()

    def display_members(self):
        if not self.members:
            print("No members registered.")
        else:
            print("\n===== MEMBER LIST =====")
            for m in self.members:
                m.display()


print("\nLAB ASSIGNMENT 2 - LIBRARY MANAGEMENT SYSTEM")
lib = Library()

while True:
    print("\n===== LIBRARY MENU =====")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Lend Book")
    print("4. Return Book")
    print("5. Display All Books")
    print("6. Display All Members")
    print("7. Exit")
    choice = input("Enter choice: ")

    if   choice == "1": lib.add_book()
    elif choice == "2": lib.add_member()
    elif choice == "3": lib.lend_book()
    elif choice == "4": lib.return_book()
    elif choice == "5": lib.display_books()
    elif choice == "6": lib.display_members()
    elif choice == "7":
        print("Exiting Library System. Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")