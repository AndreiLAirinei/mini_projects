from dataclasses import dataclass
from typing import Optional


@dataclass
class Book:
    name: str
    author: str
    publisher: str
    publication_year: Optional[int]
    ISBN: str
    stock: Optional[int] = 0

    @property
    def publication_year_valid(self):
        if self.publication_year:
            if 1 <= self.publication_year <= 9999:
                return True
            else:
                return False
        else:
            return False

    # To do
    @property
    def check_isbn(self):
        return True

    def fields(self):
        return [self.name, self.author, self.publisher, self.publication_year, self.ISBN, self.stock]

    @classmethod
    def create_instance(cls, *args):
        instance = cls(*args)
        return instance
