from book_model import Book
from exceptions import ISBNNotFound


class Controller:
    def __init__(self, repository):
        self.repository = repository

    def create(self, title, author, publisher, publication_year, isbn, stock=0):
        # Another solution? (for dictionaries) IDK if this is good
        # for field, value in zip(Book.fields(), args):
        #     book_data[field] = value

        book = Book.create_instance(title=title, author=author, publisher=publisher, publication_year=publication_year,
                                    ISBN=isbn, stock=stock)
        return self.repository.create(book)

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

    def update(self, title, author, publisher, publication_year, isbn, stock=0):
        try:
            if not self.repository.isbn_exists(isbn):
                raise ISBNNotFound(isbn)

            updated_book = Book.create_instance(title=title, author=author, publisher=publisher,
                                publication_year=publication_year, ISBN=isbn, stock=stock)
            self.repository.update(isbn, updated_book)
        except ISBNNotFound as error:
            print(str(error))

    def delete(self, isbn):
        try:
            if not self.repository.isbn_exists(isbn):
                raise ISBNNotFound(isbn)
            else:
                return self.repository.delete(isbn)
        except ISBNNotFound as error:
            print(str(error))
