from typing import Optional


class Book:
    def __init__(self,
                 title: str,
                 author: str,
                 publisher: str,
                 publication_year: Optional[int],
                 isbn: str,
                 stock: Optional[int] = 0
                 ):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_year = publication_year
        self.isbn = isbn
        self.stock = stock

    @staticmethod
    def required_fields():
        return ['title', 'author', 'publisher', 'isbn']

    @classmethod
    def create_instance(cls, title, author, publisher,  publication_year, isbn, stock):
        instance = cls(title=title, author=author, publisher=publisher, publication_year=publication_year, isbn=isbn, stock=stock)
        return instance
