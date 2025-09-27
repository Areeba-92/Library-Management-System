def greet_user():
    print("📚 Welcome to the Library System 📚")
    print("How can I help you today?\n")


# Dictionary: { "book_id": {"title": ..., "author": ...} }
library = {}

# Librarian password (can be changed)
LIBRARIAN_PASSWORD = "admin123#"


def display_menu(user_type):
    print("\n==== Library Menu ====")
    if user_type == "librarian":
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search a book by title")
        print("4. Search a book by author")
        print("5. Display all books")
        print("6. Check if a book exists (title + author)")
        print("7. Exit")
    else:  # customer
        print("1. Search a book by title")
        print("2. Search a book by author")
        print("3. Display all books")
        print("4. Check if a book exists (title + author)")
        print("5. Exit")


def add_book():
    book_id = input("Enter unique Book ID: ")
    if book_id in library:
        print("⚠️ Book with this ID already exists!")
        return
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    library[book_id] = {"title": title, "author": author}
    print(f"✅ Book '{title}' by {author} added successfully.")


def remove_book():
    book_id = input("Enter Book ID to remove: ")
    if book_id not in library:
        print("⚠️ Book not found!")
        return
    
    confirm1 = input(f"Are you sure you want to delete '{library[book_id]['title']}'? (yes/no): ").lower()
    if confirm1 == "yes":
        confirm2 = input("Please confirm again (yes/no): ").lower()
        if confirm2 == "yes":
            removed = library.pop(book_id)
            print(f"🗑️ Book '{removed['title']}' removed successfully.")
        else:
            print("❌ Deletion canceled.")
    else:
        print("❌ Deletion canceled.")


def search_by_title():
    title = input("Enter title to search: ").lower()
    found = [details for details in library.values() if title in details["title"].lower()]
    if found:
        print("🔎 Found books:")
        for book in found:
            print(f"- {book['title']} by {book['author']}")
    else:
        print("⚠️ No books found with that title.")


def search_by_author():
    author = input("Enter author to search: ").lower()
    found = [details for details in library.values() if author in details["author"].lower()]
    if found:
        print("🔎 Found books:")
        for book in found:
            print(f"- {book['title']} by {book['author']}")
    else:
        print("⚠️ No books found with that author.")


def display_books():
    if not library:
        print("📚 No books available in the library.")
    else:
        print("📚 Available books:")
        for book_id, details in library.items():
            print(f"[{book_id}] {details['title']} by {details['author']}")


def check_book_exists():
    title = input("Enter book title: ").lower()
    author = input("Enter author name: ").lower()
    for details in library.values():
        if details["title"].lower() == title and details["author"].lower() == author:
            print("✅ Yes, the book is available in the library.")
            return
    print("❌ Sorry, this book is not in the library.")


# Main Program Loop
def main():
    greet_user()
    
    # Choose role
    user_type = ""
    while user_type not in ["librarian", "customer"]:
        user_type = input("Are you a Librarian or a Customer? ").strip().lower()
    
    # Librarian password check
    if user_type == "librarian":
        for attempt in range(3):  # allow max 3 tries
            password = input("Enter Librarian Password: ")
            if password == LIBRARIAN_PASSWORD:
                print("✅ Access granted. Welcome Librarian!")
                break
            else:
                print("❌ Incorrect password.")
        else:
            print("🚫 Too many failed attempts. Exiting system.")
            return  # end program
    
    while True:
        display_menu(user_type)
        choice = input("Enter your choice: ")

        if user_type == "librarian":
            if choice == "1":
                add_book()
            elif choice == "2":
                remove_book()
            elif choice == "3":
                search_by_title()
            elif choice == "4":
                search_by_author()
            elif choice == "5":
                display_books()
            elif choice == "6":
                check_book_exists()
            elif choice == "7":
                print("👋 Thank you for using Library. Goodbye!")
                break
            else:
                print("⚠️ Invalid choice, please try again.")
        
        else:  # customer
            if choice == "1":
                search_by_title()
            elif choice == "2":
                search_by_author()
            elif choice == "3":
                display_books()
            elif choice == "4":
                check_book_exists()
            elif choice == "5":
                print("👋 Thank you for visiting Library. Goodbye!")
                break
            else:
                print("⚠️ Invalid choice, please try again.")


if __name__ == "__main__":
    main()
