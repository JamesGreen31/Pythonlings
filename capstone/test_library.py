import pytest
from library import Book, User, Library

def test_book_repr_and_init():
    b = Book("1984", "Orwell")
    assert b.title == "1984"
    assert b.author == "Orwell"
    assert b.available is True
    assert "1984" in repr(b)

def test_user_borrow_and_return():
    u = User("Alice")
    b = Book("Dune", "Herbert")
    u.borrow(b)
    assert b in u.borrowed_books
    assert b.available is False
    u.return_book(b)
    assert b not in u.borrowed_books
    assert b.available is True

def test_library_add_and_list():
    lib = Library()
    b1 = Book("Dune", "Herbert")
    b2 = Book("1984", "Orwell")
    lib.add_book(b1)
    lib.add_book(b2)
    assert b1 in lib.books
    assert len(lib.list_available()) == 2

def test_library_borrow_and_return():
    lib = Library()
    user = User("Bob")
    b = Book("Dune", "Herbert")
    lib.add_user(user)
    lib.add_book(b)

    lib.borrow_book(user, "Dune")
    assert b not in lib.list_available()
    assert b in user.borrowed_books

    lib.return_book(user, "Dune")
    assert b in lib.list_available()
    assert b not in user.borrowed_books

def test_borrow_nonexistent_book():
    lib = Library()
    user = User("Charlie")
    lib.add_user(user)
    lib.borrow_book(user, "Nonexistent")  # should not crash
    assert user.borrowed_books == []
