# Library Book Management System

books = []

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_title = input("Enter book title: ")
        books.append(book_title)
        print("Book added successfully.")

    elif choice == "2":
        if not books:
            print("No books available.")
        else:
            print("Available books:")
            for book in books:
                print("-", book)

    elif choice == "3":
        book_title = input("Enter book title to borrow: ")
        if book_title in books:
            books.remove(book_title)
            print("Book borrowed successfully.")
        else:
            print("Book not available.")

    elif choice == "4":
        print("Exiting system...")
        break

    else:
        print("Invalid choice. Try again.")
