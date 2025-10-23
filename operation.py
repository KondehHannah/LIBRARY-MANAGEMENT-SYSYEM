from typing import List, Dict, Optional
import itertools
# Data structures (in-memory)
genres = ("Fiction", "Non-Fiction", "Sci-Fi", "Biography", "Poetry", "Children")

books: Dict[str, Dict] = {}
members: List[Dict] = []

# a simple incremental member id generator
_member_id_counter = itertools.count(1)

# Helper functions
def _find_member_index(member_id: int) -> Optional[int]:
    for i, m in enumerate(members):
        if m["member_id"] == member_id:
            return i
    return None


def _member_exists(member_id: int) -> bool:
    return _find_member_index(member_id) is not None

# Core functions
def add_book(isbn: str, title: str, author: str, genre: str, copies: int = 1) -> bool:
    isbn = isbn.strip()
    if not isbn or copies < 1:
        return False
    if genre not in genres:
        return False
    if isbn in books:
        return False  # avoid duplicate ISBN
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": copies,
        "available_copies": copies,
    }
    return True


def add_member(name: str, email: str) -> int:
    member_id = next(_member_id_counter)
    members.append({
        "member_id": member_id,
        "name": name,
        "email": email,
        "borrowed_books": []
    })
    return member_id


def search_books(query: str = "", by: str = "title") -> List[Dict]:
    q = query.lower().strip()
    results = []
    for isbn, info in books.items():
        if not q:
            results.append({"isbn": isbn, **info})
            continue
        if by == "title" and q in info["title"].lower():
            results.append({"isbn": isbn, **info})
        elif by == "author" and q in info["author"].lower():
            results.append({"isbn": isbn, **info})
        elif by == "genre" and q in info["genre"].lower():
            results.append({"isbn": isbn, **info})
    return results


def update_book(isbn: str, title: Optional[str] = None, author: Optional[str] = None,
                genre: Optional[str] = None, total_copies: Optional[int] = None) -> bool:
    if isbn not in books:
        return False
    book = books[isbn]
    if title:
        book["title"] = title
    if author:
        book["author"] = author
    if genre:
        if genre not in genres:
            return False
        book["genre"] = genre
    if total_copies is not None:
        if total_copies < 0:
            return False
        diff = total_copies - book["total_copies"]
        book["total_copies"] = total_copies
        # adjust available copies (don't make negative)
        book["available_copies"] = max(0, book["available_copies"] + diff)
    return True


def delete_book(isbn: str) -> bool:
    if isbn not in books:
        return False
    book = books[isbn]
    if book["available_copies"] != book["total_copies"]:
        # some copies are out on loan
        return False
    del books[isbn]
    return True


def update_member(member_id: int, name: Optional[str] = None, email: Optional[str] = None) -> bool:
    idx = _find_member_index(member_id)
    if idx is None:
        return False
    if name:
        members[idx]["name"] = name
    if email:
        members[idx]["email"] = email
    return True


def delete_member(member_id: int) -> bool:
    idx = _find_member_index(member_id)
    if idx is None:
        return False
    if members[idx]["borrowed_books"]:
        return False
    members.pop(idx)
    return True


def borrow_book(member_id: int, isbn: str) -> bool:
    idx = _find_member_index(member_id)
    if idx is None:
        return False
    if isbn not in books:
        return False
    book = books[isbn]
    if book["available_copies"] < 1:
        return False
    if isbn in members[idx]["borrowed_books"]:
        return False  # already borrowed by this member
    # perform borrow
    members[idx]["borrowed_books"].append(isbn)
    book["available_copies"] -= 1
    return True


def return_book(member_id: int, isbn: str) -> bool:
    idx = _find_member_index(member_id)
    if idx is None or isbn not in books:
        return False
    if isbn not in members[idx]["borrowed_books"]:
        return False
    members[idx]["borrowed_books"].remove(isbn)
    books[isbn]["available_copies"] += 1
    # Do not allow available > total (just in case), keep it capped:
    if books[isbn]["available_copies"] > books[isbn]["total_copies"]:
        books[isbn]["available_copies"] = books[isbn]["total_copies"]
    return True


# Utility for demo / display
def list_all_books() -> List[Dict]:
    return [{"isbn": isbn, **info} for isbn, info in books.items()]


def list_all_members() -> List[Dict]:
    return members.copy()