from book_model import Book
from exceptions import ISBNNotFound


class Controller:
    def __init__(self, repository):
        self.repository = repository

    def create(self, *args):
        # if not all(field in book_data for field in Book.fields()):
        #     # missing_fields = [field for field in Book.required_fields() if field not in data]
        #     # raise FieldNotFound(*missing_fields)

        # Another solution? IDK which on is good
        # for field, value in zip(Book.fields(), args):
        #     book_data[field] = value

        book = Book().create_instance(*args)

        return self.repository.create(book)

    def read_all(self):
        return self.repository.read_all()

    def read_by_id(self, isbn):
        try:
            # to do with ISBN method in validation
            # if not self.repository.valid_id(isbn):
            #     raise Exception

            if not self.repository.isbn_exists(isbn):
                raise ISBNNotFound(isbn)
            else:
                return self.repository.read_by_isbn(isbn)
        except ISBNNotFound as error:
            print(str(error))

    def update(self, isbn, *args):

        if not self.repository.isbn_exists(isbn):
            raise ISBNNotFound(isbn)
        else:
            updated_book = Book.create_instance(*args)
            self.repository.update(isbn, updated_book)

    def delete(self, isbn):
        if not self.repository.isbn_exists(isbn):
            raise Exception
        else:
            return self.repository.delete(isbn)

