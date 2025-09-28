"""
Capstone Project: Library Management System
"""

class Book:
    def __init__(self, title: str, author: str, available: bool = True):
        self.title = title
        self.author = author
        self.available = available

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.available})"


class User:
    def __init__(self, name: str):
        self.name = name
        self.borrowed_books: list[Book] = []

    def borrow(self, book: Book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True

    def __repr__(self):
        return f"User({self.name}, borrowed={len(self.borrowed_books)})"


class Library:
    def __init__(self):
        self.books: list[Book] = []
        self.users: list[User] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def add_user(self, user: User):
        self.users.append(user)

    def list_available(self) -> list[Book]:
        return [book for book in self.books if book.available]

    def borrow_book(self, user: User, title: str):
        for book in self.books:
            if book.title == title and book.available:
                user.borrow(book)
                return

    def return_book(self, user: User, title: str):
        for book in user.borrowed_books:
            if book.title == title:
                user.return_book(book)
                return
