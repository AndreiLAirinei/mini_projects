from typing import Optional


class Book:
    _id_counter = 0  # Class variable to track the last assigned book_id

    def __init__(self,
                 title: str,
                 author: str,
                 publisher: str,
                 publication_year: int,
                 isbn: str,
                 stock: Optional[int] = 0
                 ):
        self.book_id = Book._id_counter + 1  # Increment the book_id counter
        Book._id_counter += 1  # Increment the counter for the next book
        self.book_id = 0
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_year = publication_year
        self.isbn = isbn
        self.stock = stock if stock is not None else 0

    @staticmethod
    def required_fields():
        return ['title', 'author', 'publisher', 'publication_year', 'isbn']

    @classmethod
    def create_instance(cls, *args):
        instance = cls(*args)
        return instance

    def __str__(self):
        return (f"Book({self.title}, {self.author}, {self.publisher}, {self.publication_year}, "
                f"{self.isbn}, {self.stock})")
