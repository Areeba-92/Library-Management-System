# Library-Management-System

## Overview
This is a simple console-based Library Management System built in Python.
It allows two types of users:
1) Librarians (with admin access)
2) Customers (general users)

Librarians can manage the library by adding, removing, and checking books, while customers can search and view available books.

## Features
### Librarian

- Add a new book (with unique Book ID)

- Remove a book (double confirmation before deletion)

- Search books by title or author

- Display all available books

- Check if a specific book exists (by title + author)

- Password-protected access (default: admin123#)

### Customer

- Search books by title or author

- Display all available books

- Check if a specific book exists

## How It Works

When the program starts, the user selects their role (Librarian or Customer).
If Librarian is chosen, a password is required (default: admin123#).
Based on role, a menu is shown with options.
User can interact through the menu until they choose Exit.

▶️ How to Run

Install Python (version 3.7 or later recommended).

- Clone this repository:

```git clone https://github.com/your-username/library-system.git```


- Run the program:

```python library_system.py```

## Future Improvements

- Save books to a file (currently data resets when program ends).

- Add book categories/genres.

- Improve UI (maybe with Tkinter or a web version).

- Add user accounts for customers.

## EXAMPLE:
```
📚 Welcome to the Library System 📚
How can I help you today?

Are you a Librarian or a Customer? librarian
Enter Librarian Password: ******
✅ Access granted. Welcome Librarian!

==== Library Menu ====
1. Add a book
2. Remove a book
3. Search a book by title
4. Search a book by author
5. Display all books
6. Check if a book exists (title + author)
7. Exit
Enter your choice: 1

Enter unique Book ID: 101
Enter book title: Atomic Habits
Enter book author: James Clear
✅ Book 'Atomic Habits' by James Clear added successfully.

==== Library Menu ====
1. Add a book
2. Remove a book
3. Search a book by title
...

```
