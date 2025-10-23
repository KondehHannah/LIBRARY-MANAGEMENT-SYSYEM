# Design Rationale — Mini Library Management System

## Overview
This mini library system uses simple, built-in Python data structures to represent books, members, and genres. The focus was on clarity and educational value rather than advanced design patterns.

## Data Structures
### Dictionaries for Books
Books are stored in a dictionary keyed by ISBN. Reasons:
- ISBN is a natural unique identifier for books.
- Dictionary lookups by key are O(1), making search by ISBN fast and intuitive.
- Each book's metadata (title, author, genre, counts) naturally maps to a nested dictionary so it’s easy to extend.

I included available_copies in addition to total_copies to track real-time availability (borrowed vs. present copies). This makes borrow/return logic straightforward.

### Lists for Members
Members are stored as a list of dictionaries where each member dictionary contains member_id, name, email, and borrowed_books (a list of ISBNs).
- Lists are simple to use and iterate over — suitable for small to medium collections often used in assignments.
- borrowed_books is a list of ISBN strings; this keeps history simple and easy to display.

Note: for larger systems a dictionary keyed by member_id would be more efficient for lookups.

### Tuple for Genres
Genres are stored in a tuple to indicate a fixed set of valid options:
- Tuples are immutable, preventing accidental changes to the allowed genres.
- It’s small and expressive for demonstration.

## Functions and Behavior
Functions are written to be small and single-purpose:
- add_book, add_member handle validation and insertion.
- borrow_book, return_book update both the books and members structures so data stays consistent.
- update_ and delete_ functions include simple safety checks (e.g., cannot delete a book that is currently borrowed).

## Simplicity and Extensibility
- The design favors readability: helpers like _find_member_index encapsulate lookup logic.
- To extend: swap members to a dict keyed by member_id for speed, add persistence (saving to JSON/DB), or add borrowing limits / due dates.

## Conclusion
This mix of dictionaries, lists, and tuples uses each structure where it is most natural: dictionaries for keyed fast access, lists for ordered collections that are easy to iterate or display, and tuples for fixed configuration data. The design balances clarity and correctness for an introductory university assignment.