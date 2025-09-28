"""
Capstone Project: Library Management System

Follow the TODO comments carefully.
If all are completed, the project will be functional.
"""

# TODO: Define a class Book
# - attributes: title (str), author (str), available (bool, default True)
# - __init__ should set these attributes
# - implement __repr__ to return "Book(title, author, available)"

class Book:
    def __init__(self, title: str, author: str, available: bool = True):
        # TODO: initialize attributes
        pass

    def __repr__(self):
        # TODO: Should return Book(title, author, available)
        return ""


# TODO: Define a class User
# - attributes: name (str), borrowed_books (list of Book, default empty)
# - __init__ should set these attributes
# - implement a method borrow(book: Book) that adds book if available
# - implement a method return_book(book: Book) that removes book if present
# - implement __repr__ to return "User(name, borrowed=N)"

class User:
    def __init__(self, name: str):
        # TODO: initialize name and empty borrowed_books list
        pass

    def borrow(self, book: Book):
        # TODO: add book if available, mark unavailable
        pass

    def return_book(self, book: Book):
        # TODO: remove book if in borrowed_books, mark available
        pass

    def __repr__(self):
        # TODO: return "User(name, borrowed=N where N is the number of books checked out by user)"
        return ""


# TODO: Define a class Library
# - attributes: books (list of Book), users (list of User)
# - __init__ should create empty lists
# - method add_book(book: Book) → adds to books
# - method add_user(user: User) → adds to users
# - method list_available() → return list of available books
# - method borrow_book(user: User, title: str)
#   * find the book by title
#   * if available, mark it unavailable and add to user.borrowed_books
#   * otherwise, do nothing
# - method return_book(user: User, title: str)
#   * find the book in user.borrowed_books
#   * mark it available and remove from user.borrowed_books

class Library:
    def __init__(self):
        # TODO: initialize empty lists for books and users
        pass

    def add_book(self, book: Book):
        # TODO: append book to self.books
        pass

    def add_user(self, user: User):
        # TODO: append user to self.users
        pass

    def list_available(self) -> list[Book]:
        # TODO: return only available books
        return []

    def borrow_book(self, user: User, title: str):
        # TODO: implement borrowing logic
        pass

    def return_book(self, user: User, title: str):
        # TODO: implement return logic
        pass
