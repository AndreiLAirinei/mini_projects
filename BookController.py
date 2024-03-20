from book_model import Book
from validations import validate_book
from exceptions import IDNotFound, BookFormatInvalid


class BookController:
    def __init__(self, repository):
        self.repository = repository

    def create_book(self, title, author, publisher, publication_year, isbn, stock=0):
        try:
            book_instance = Book(title, author, publisher, publication_year, isbn, stock)

            if validate_book(title, author, publisher, publication_year, isbn, stock):
                self.repository.book_create(book_instance)
            else:
                raise BookFormatInvalid(isbn)
            return True

        except BookFormatInvalid as error:
            print(str(error))

    def read_all_books(self):
        return self.repository.book_read_all()

    def read_book_by_id(self, book_id):
        try:
            if not self.repository.id_exists(book_id):
                raise IDNotFound(book_id)
            else:
                return self.repository.book_read_by_id(book_id)
        except IDNotFound as error:
            print(str(error))

    def update_book(self, book_id, title, author, publisher, publication_year, isbn, stock=0):
        try:
            if not self.repository.id_exists(book_id):
                raise IDNotFound(book_id)

            updated_book = Book(title, author, publisher, publication_year, isbn, stock)

            if validate_book(title, author, publisher, publication_year, isbn, stock):
                return self.repository.book_update(book_id, updated_book)
            else:
                raise BookFormatInvalid(book_id)

        except (IDNotFound, BookFormatInvalid) as error:
            print(str(error))

    def delete_book(self, book_id):
        try:
            if not self.repository.id_exists(book_id):
                raise IDNotFound(book_id)
            else:
                return self.repository.book_delete(book_id)

        except IDNotFound as error:
            print(str(error))
