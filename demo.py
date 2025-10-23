# demo.py
from operation import (
    add_book, add_member, borrow_book, return_book,
    list_all_books, list_all_members, genres
)

# Setup
print("Allowed genres:", genres)
print("\nAdding books...")
add_book("978-0-1111", "Intro to Python", "A. Programmer", "Non-Fiction", 2)
add_book("978-0-2222", "Sci-Fi Tales", "B. Writer", "Sci-Fi", 1)

print("\nBooks in system:")
for b in list_all_books():
    print(b)

# Add members
m1 = add_member("Hannah Kondeh", "hannah@example.com")
m2 = add_member("Alex Smith", "alex@example.com")

print("\nMembers:")
for m in list_all_members():
    print(m)

# Borrowing
print("\nHannah borrows 'Intro to Python' (978-0-1111):", borrow_book(m1, "978-0-1111"))
print("Hannah tries to borrow same book again:", borrow_book(m1, "978-0-1111"))
print("Alex borrows 'Intro to Python' too:", borrow_book(m2, "978-0-1111"))
print("Now books:")
for b in list_all_books():
    print(b)

# Returning
print("\nHannah returns book:", return_book(m1, "978-0-1111"))
print("Final books:")
for b in list_all_books():
    print(b)

print("\nFinal members:")
for m in list_all_members():
    print(m)