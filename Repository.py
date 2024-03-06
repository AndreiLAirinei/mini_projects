from book_model import Book


class InMemoryRepository:
    def __init__(self):
        self.data = []

    def create(self, book_data):
        self.data.append(book_data)
        return True

    def read_all(self):
        return self.data.copy()

    def read_by_isbn(self, isbn):
        for book in self.data:
            if book.ISBN == isbn:
                return book
        return None

    def update(self, book):
        if not self.data:
            return False

        for i, existing_book in enumerate(self.data):
            if existing_book.ISBN == book.ISBN:
                self.data[i] = book
                return True
        return False

    def delete(self, isbn):
        if not self.data:
            return False

        for i, book in enumerate(self.data):
            if book.ISBN == isbn:
                self.data.pop(i)
                return True
        return False

    def isbn_exists(self, isbn):
        for book in self.data:
            if book.ISBN == isbn:
                return True
        return False
