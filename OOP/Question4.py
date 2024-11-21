#4) Implement a class called Library that manages a collection of books.
# Each book has a tittle, author, and available status. The class should have methods to:
# Add a book to the library.Remove a book from the library. 
# Check if a book is available by title. 
# Borrow a book (mark it as unavailable if it's available). 
# Return a book(mark it as available again if it was borrowed)

class Library:
    def __init__(self):
        self.books = {}
    def add_book(self, title, author):
        self.books[title] = {'author': author, 'available': True}
        print(f"Added '{title}' by {author}.")
    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            print(f"Removed '{title}'.")
        else:
            print(f"'{title}' not found in library.")
    def check_availability(self, title):
        if title in self.books and self.books[title]['available']:
            print(f"'{title}' is available.")
        else:
            print(f"'{title}' is not available.")
    def borrow_book(self, title):
        if title in self.books and self.books[title]['available']:
            self.books[title]['available'] = False
            print(f"You borrowed '{title}'.")
        else:
            print(f"'{title}' is not available for borrowing.")
    def return_book(self, title):
        if title in self.books:
            self.books[title]['available'] = True
            print(f"Returned '{title}'.")
        else:
            print(f"'{title}' is not found in the library.")
library = Library()
library.add_book("Heights", "Mark Oden")
library.check_availability("Heights")  
library.borrow_book("Heights")  
library.return_book("Heights") 
