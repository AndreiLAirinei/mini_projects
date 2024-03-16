from book_model import Book
from validations import validate_book
from exceptions import IDNotFound, BookFormatInvalid


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

    def read_by_id(self, book_id):
        try:
            if not self.repository.id_exists(book_id):
                raise IDNotFound(book_id)
            else:
                return self.repository.read_by_id(book_id)
        except IDNotFound as error:
            print(str(error))

    def update(self, book_id, title, author, publisher, isbn, publication_year, stock=0):
        try:
            if not self.repository.id_exists(book_id):
                raise IDNotFound(book_id)

            updated_book = Book.create_instance(title=title, author=author, publisher=publisher,
                                                isbn=isbn, publication_year=publication_year, stock=stock)

            if validate_book(updated_book):
                if self.repository.update(book_id, updated_book):
                    return True
            else:
                raise BookFormatInvalid(book_id)

        except (IDNotFound, BookFormatInvalid) as error:
            print(str(error))

    def delete(self, book_id):
        try:
            if not self.repository.id_exists(book_id):
                raise IDNotFound(book_id)
            else:
                return self.repository.delete(book_id)

        except IDNotFound as error:
            print(str(error))
