# Made By AMRIK SINGH 
# 2501350058
# Library Management System
# Date: 11/29/2025


class Book:
    def __init__(self, title, author, isbn, status):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status  # ye btayega ki book available h ya checked out

# info method book ki details return karega, also it have check_out and return_book methods

    def get_info(self):
        return f"'{self.title}' by {self.author}, isbn no. {self.isbn}. Status: {self.status}"
    def issue(self):
        if self.status == "available":
            self.status = "Issued"
            return f"You have issued '{self.title}'."
        else:
            return f"Sorry, '{self.title}' is already issued."
    def returnit(self):
        if self.status == "Issued":
            self.status = "available"
            return f"You have returned '{self.title}'."
        else:
            return f"'{self.title}' was not issued."

        

        


# From here library.py file starts , jisme LibraryInventory class hai jo library ki books manage karega
# aur uski ek 'jsonfile' bna dega jisme books ki details store hongi



import json
from pathlib import Path

class LibraryInventory:
    def __init__(self, books_file):
        self.inventory_file = Path(books_file)
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

    def issue_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                result = book.issue()
                self.save_inventory()
                return result
        return "Book not found."
        

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                result = book.returnit()
                self.save_inventory()
                return result
        return "Book not found."
        
    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book.get_info()
        return "Book not found."

    def list_books(self):
        return [book.get_info() for book in self.books]
    
    
    


# yaha se main code start hai jisme user se input leke pura code run hoga 


def menu():
    print("Library Management System")
    print("1. Add Book")
    print("2. issue Book")
    print("3. return Book")
    print("4. Find Book by isbn")
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
                isbn = input("Enter book ISBN to issue: ")
                print(library.issue_book(isbn))
                
            elif choice == '3':
                isbn = input("Enter book ISBN to return: ")
                print(library.return_book(isbn))
            elif choice == '4':
                title = input("Enter book ISBN to find: ")
                print(library.find_book_by_title(isbn))
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





# THANK YOU 

# MADE UNDER THE GUIDANCE OF MR.Bhavesh Badani SIR
# thank you sir it was a great learning experience
# And sorry i didnt made the different files as you said 
# because it was showing one same error again and again
# so i made it in one file only

# i Tried to make it as simple as possible 

# and if you have any suggestions for me
# please tell me i will be very thankful to you sir
# and if you want to know the error i was facing
# i can tell you that also


# THANK YOU 

 
        


    