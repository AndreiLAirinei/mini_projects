
class InMemoryRepository:
    def __init__(self):
        self.data = []
        self.last_book_id = 0

    def create(self, instance):
        instance.book_id = self.generate_id()
        self.data.append(instance)
        return True

    def read_all(self):
        return self.data

    def read_by_id(self, book_id):
        for book in self.data:
            if book.book_id == book_id:
                return book
        return None

    def update(self, book):
        if not self.data:
            return False

        for i, existing_book in enumerate(self.data):
            if existing_book.book_id == book.book_id:
                self.data[i] = book
                return True
        return False

    def delete(self, book_id):
        if not self.data:
            return False

        for i, book in enumerate(self.data):
            if book.book_id == book_id:
                del self.data[i]
                return True
        return False

    def id_exists(self, book_id):
        for book in self.data:
            if book.book_id == book_id:
                return True
        return False

    def generate_id(self):
        self.last_book_id += 1
        return self.last_book_id
