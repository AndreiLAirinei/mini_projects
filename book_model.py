from dataclasses import dataclass
from typing import Optional


@dataclass
class Book:
    title: str
    author: str
    publisher: str
    publication_year: Optional[int]
    ISBN: str
    stock: Optional[int] = 0

    def fields(self):
        return [self.title, self.author, self.publisher, self.publication_year, self.ISBN, self.stock]

    @staticmethod
    def required_fields():
        return ['title', 'author', 'publisher', 'ISBN']

    @classmethod
    def create_instance(cls, title, author, publisher, isbn, **kwargs):
        instance = cls(title=title, author=author, publisher=publisher, isbn=isbn, **kwargs)
        return instance
