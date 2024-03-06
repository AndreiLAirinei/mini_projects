from Repository import InMemoryRepository
from book_model import Book


class Controller:
    def __init__(self):
        self.repository = InMemoryRepository()

    def create(self, book_data):

        if not all(field in book_data for field in Book.required_fields()):
            raise Exception

        # create a book objects with the data
        book = Book(**book_data)

        return self.repository.create(book)

    def read_all(self):
        return self.repository.read_all()

    def read_by_id(self, isbn):
        # try:
        # to do with ISBN method in book_model
        # if not self.repository.valid_id(isbn):
        #     raise Exception

        if not self.repository.isbn_exists(isbn):
            raise Exception
        else:
            return self.repository.read_by_isbn(isbn)

    def update(self, isbn, book_data):
        if not self.repository.isbn_exists(isbn):
            raise Exception
        else:
            if not all(field in book_data for field in Book.required_fields()):
                raise Exception

            # create book object
            updated_book = Book(**book_data)

            return self.repository.update(isbn, updated_book)

    def delete(self, isbn):
        if not self.repository.isbn_exists(isbn):
            raise Exception
        else:
            return self.repository.delete(isbn)

    # adding random code for pull request
