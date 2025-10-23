# tests.py
from operation import (
    books, members,
    add_book, add_member, borrow_book, return_book,
    delete_book, delete_member
)

# Reset data (simple reset by clearing lists/dicts)
books.clear()
members.clear()

# 1) Add book and member
assert add_book("ISBN001", "Python Basics", "Alice Author", "Non-Fiction", copies=3) is True
member_id = add_member("John Doe", "john@example.com")
assert isinstance(member_id, int)

# 2) Borrow book -> available should reduce
assert borrow_book(member_id, "ISBN001") is True
assert books["ISBN001"]["available_copies"] == 2
assert "ISBN001" in members[0]["borrowed_books"]

# 3) Prevent double-borrow by same member
assert borrow_book(member_id, "ISBN001") is False  # already borrowed

# 4) Return book -> available increases
assert return_book(member_id, "ISBN001") is True
assert books["ISBN001"]["available_copies"] == 3
assert "ISBN001" not in members[0]["borrowed_books"]

# 5) Delete book only when no copies borrow_book
# borrow and attempt delete
borrow_book(member_id, "ISBN001")
assert delete_book("ISBN001") is False  # can't delete, one copy is borrowed
# return and delete
assert return_book(member_id, "ISBN001") is True
assert delete_book("ISBN001") is True

# 6) Member delete safety
assert delete_member(member_id) is True  # member has no borrowed books now

print("All asserts passed.")