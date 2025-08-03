from library_management import Book, Library

def main():
    library = Library()

    book1 = Book("1984", "George Orwell")
    book2 = Book("The Hobbit", "J.R.R. Tolkien")
    book3 = Book("Python Crash Course", "Eric Matthes")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    print("\nAvailable books:")
    library.list_available_books()

    print("\nChecking out '1984':")
    library.check_out_book("1984")

    print("\nAvailable books after checkout:")
    library.list_available_books()

    print("\nReturning '1984':")
    library.return_book("1984")

    print("\nAvailable books after return:")
    library.list_available_books()

if __name__ == "__main__":
    main()