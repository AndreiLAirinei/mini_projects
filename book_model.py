from dataclasses import dataclass
from typing import Optional


@dataclass
class Book:
    name: str
    author: Optional[str]
    publisher: Optional[str]
    publication_year: Optional[int]
    ISBN: str
    stock: Optional[int]

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

    def required_fields(self):
        field_list = [self.name, self.ISBN]
        return field_list
