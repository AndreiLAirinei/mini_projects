from book_model import Book
from validations import validate_book
from exceptions import ISBNNotFound, BookFormatInvalid


class Controller:
    def __init__(self, repository):
        self.repository = repository

    def create(self, title, author, publisher, isbn, publication_year, stock=0):
        try:

            book_instance = Book.create_instance(title=title, author=author, publisher=publisher, isbn=isbn,
                                                 publication_year=publication_year, stock=stock)

            if validate_book(book_instance):
                return self.repository.create(book_instance)
            else:
                raise BookFormatInvalid(isbn)

        except BookFormatInvalid as error:
            print(str(error))

    def read_all(self):
        return self.repository.read_all()

    def read_by_id(self, isbn):
        try:
            if not self.repository.isbn_exists(isbn):
                raise ISBNNotFound(isbn)
            else:
                return self.repository.read_by_isbn(isbn)
        except ISBNNotFound as error:
            print(str(error))

    def update(self, title, author, publisher, isbn, publication_year, stock=0):
        try:
            if not self.repository.isbn_exists(isbn):
                raise ISBNNotFound(isbn)

            updated_book = Book.create_instance(title=title, author=author, publisher=publisher,
                                                ISBN=isbn, publication_year=publication_year, stock=stock)

            if validate_book(updated_book):
                self.repository.update(isbn, updated_book)
            else:
                raise BookFormatInvalid(isbn)

        except (ISBNNotFound, BookFormatInvalid) as error:
            print(str(error))

    def delete(self, isbn):
        try:
            if not self.repository.isbn_exists(isbn):
                raise ISBNNotFound(isbn)
            else:
                return self.repository.delete(isbn)

        except ISBNNotFound as error:
            print(str(error))
