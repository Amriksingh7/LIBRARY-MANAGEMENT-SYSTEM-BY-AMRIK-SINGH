class Book:
    def __init__(self, title, author, isbn, status):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status  # available or checked out

    def get_info(self):
        return f"'{self.title}' by {self.author}, isbn no. {self.isbn}. Status: {self.status}"
    def check_out(self):
        if self.status == "available":
            self.status = "Issued"
            return f"You have checked out '{self.title}'."
        else:
            return f"Sorry, '{self.title}' is already checked out."
    def return_book(self):
        if self.status == "Issued":
            self.status = "available"
            return f"You have returned '{self.title}'."
        else:
            return f"'{self.title}' was not checked out."
        

import json
from pathlib import Path

class LibraryInventory:
    def __init__(self, inventory_file):
        self.inventory_file = Path(inventory_file)
        self.books = self.load_inventory()

    def load_inventory(self):
        if not self.inventory_file.exists():
            return []
        with open(self.inventory_file, 'r') as file:
            data = json.load(file)
            return [Book(**book) for book in data]

    def save_inventory(self):
        with open(self.inventory_file, 'w') as file:
            data = [book.__dict__ for book in self.books]
            json.dump(data, file, indent=4)

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn, "available")
        self.books.append(new_book)
        self.save_inventory()
        return f"Book '{title}' added to inventory."

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                self.save_inventory()
                return f"Book '{book.title}' removed from inventory."
        return "Book not found."

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book.get_info()
        return "Book not found."
        
    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.get_info()
        return "Book not found."

    def list_books(self):
        return [book.get_info() for book in self.books]
    
    
    





def menu():
    print("Library Management System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Find Book by ISBN")
    print("4. Find Book by Title")
    print("5. List All Books")
    print("6. Exit")

def main():
    library = LibraryInventory('library_inventory.json')
    
    while True:
        menu()
        choice = input("Enter your choice (1-6): ")

        try:
            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                isbn = input("Enter book ISBN: ")
                print(library.add_book(title, author, isbn))
            elif choice == '2':
                isbn = input("Enter book ISBN to remove: ")
                print(library.remove_book(isbn))
            elif choice == '3':
                isbn = input("Enter book ISBN to find: ")
                print(library.find_book(isbn))
            elif choice == '4':
                title = input("Enter book title to find: ")
                print(library.find_book_by_title(title))
            elif choice == '5':
                books = library.list_books()
                for book in books:
                    print(book)
            elif choice == '6':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()




        
        


    