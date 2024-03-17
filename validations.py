from datetime import datetime

from exceptions import ISBNInvalid, RequiredFieldsNotFound, PublicationYearInvalid, StockInvalid


def validate_publication_year(year, current_year):
    if year is None or isinstance(year, str):
        return False
    elif 1499 < year < current_year + 1:
        return True


def validate_isbn(isbn):

    if isinstance(isbn, int) or isbn is None:
        return False
    else:
        isbn = isbn.replace("-", "")
        if len(isbn) not in (10, 13):
            return False

    total_sum = 0
    if len(isbn) == 10:
        # ISBN-10 algorithm
        for i, char in enumerate(isbn):
            if char.isdigit():
                total_sum += int(char) * (10 - i)
        if total_sum % 11 == 0:
            return True
        else:
            return False

    elif len(isbn) == 13:
        # ISBN-13 algorithm
        for i, char in enumerate(isbn):
            if char.isdigit() and i % 2 == 0:
                total_sum += int(char)
            else:
                total_sum += int(char) * 3
        if total_sum % 10 == 0:
            return True
        else:
            return False


def validate_book(title, author, publisher, publication_year, isbn, stock):
    try:
        validate_not_none(title, author, publisher, publication_year, isbn)
        validate_instance_str(title)
        validate_instance_str(author)
        validate_instance_str(publisher)

        current_year = datetime.now().year
        if publication_year is not None:
            if not validate_instance_int(publication_year) or \
                    not validate_publication_year(publication_year, current_year):
                raise PublicationYearInvalid(publication_year)

        if stock is not None:
            if not validate_instance_int(stock):
                raise StockInvalid(stock)

        if not validate_isbn(isbn):
            raise ISBNInvalid(isbn)

    except (RequiredFieldsNotFound, PublicationYearInvalid, ISBNInvalid, StockInvalid):
        return False

    return True


def validate_not_none(title, author, publisher, publication_year, isbn):
    fields = ['title', 'author', 'publisher', 'publication_year', 'isbn']
    for field in fields:
        attribute_value = locals()[field]
        if attribute_value is None:
            raise RequiredFieldsNotFound(attribute_value)
    return True


def validate_instance_str(book_attribute):
    if not isinstance(book_attribute, str):
        raise RequiredFieldsNotFound(book_attribute)
    return True


def validate_instance_int(book_attribute):
    if not isinstance(book_attribute, int) and book_attribute < 0:
        raise RequiredFieldsNotFound(book_attribute)
    return True


