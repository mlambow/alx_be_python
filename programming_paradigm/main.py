import sys
from robust_division_calculator import safe_divide
from library_management import Book, Library


def main():
    if len(sys.argv) !=3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]


    result = safe_divide(numerator, denominator)
    print(result)

def main():
    #setup a small library
    library = Library()
    library.add_book(Book("Brave New World.", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    #initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    #simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    #simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()