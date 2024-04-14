class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre


class Library:
    def __init__(self, library_file):
        self.library_file = library_file

    def add_book(self, title, author, genre):
        new_book = Book(title, author, genre)
        with open(self.library_file, "a") as file:
            file.write(f"{new_book.title}, {new_book.author}, {new_book.genre}\n")

    def search_book(self, search_term):
        found_books = []
        try:
            with open(self.library_file, "r") as file:
                for i in file:
                    try:
                        title, author, genre = i.strip().split(',')
                        if search_term.lower() in title.lower() or search_term.lower() in author.lower()\
                                or search_term.lower() in genre.lower():
                            found_books.append(Book(title, author, genre))
                    except ValueError:
                        continue
        except FileNotFoundError:
            pass
        return found_books


def add_new_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    genre = input("Enter the genre: ")
    library.add_book(title, author, genre)


def user_choice():
    print("1. Search for a book")
    print("2. Add a new book")
    answer = input("Enter your choice (1 or 2): ")
    return answer


library_file = "library.txt"
library = Library(library_file)

while True:
    answer = user_choice()

    if answer == '1':
        search_term = input("Enter the title, author, or genre of the book: ")
        results = library.search_book(search_term)
        if len(results) == 0:
            print("No matching books found.")
        else:
            print("Matching books:")
            for book in results:
                print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}")

    elif answer == '2':
        add_new_book(library)

    else:
        print("Please enter 1 or 2.")

