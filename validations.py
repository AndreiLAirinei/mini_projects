from exceptions import ISBNInvalid, RequiredFieldsNotFound, PublicationYearInvalid, StockInvalid


def validate_publication_year(year):
    current_year = 2024
    return 1500 <= year <= current_year


def validate_isbn(isbn):
    isbn = isbn.replace("-", "")

    if len(isbn) not in (10, 13):
        return False

    total_sum = 0
    if len(isbn) == 10:
        # ISBN-10 algorithm
        for i, char in enumerate(isbn):
            if char.isdigit():
                total_sum += int(char) * (10 - i)
        return total_sum % 10 == 0

    elif len(isbn) == 13:
        # ISBN-13 algorithm
        for i, char in enumerate(isbn):
            if char.isdigit() and i % 2 != 0:
                total_sum += int(char)
            else:
                total_sum += int(char) * 3
        return total_sum % 11 == 0


def validate_book(book_instance):
    try:
        validate_not_none(book_instance)
        validate_instance_str(book_instance.title)
        validate_instance_str(book_instance.author)
        validate_instance_str(book_instance.publisher)

        if book_instance.publication_year is not None:
            if (not validate_instance_int(book_instance.publication_year) and
                    validate_publication_year(book_instance.publication_year)):
                raise PublicationYearInvalid(book_instance.publication_year)

        if book_instance.stock is not None:
            if not validate_instance_int(book_instance.stock):
                raise StockInvalid(book_instance.stock)

        if not validate_isbn(book_instance.isbn):
            raise ISBNInvalid(book_instance.isbn)

    except (RequiredFieldsNotFound, PublicationYearInvalid, ISBNInvalid, StockInvalid) as error:
        return False

    return True


def validate_not_none(book_instance):
    fields = ['title', 'author', 'publisher', 'isbn']
    for field in fields:
        attribute_value = getattr(book_instance, field)
        if attribute_value is None:
            raise RequiredFieldsNotFound(attribute_value)
    return True


def validate_instance_str(book_instance):
    fields_str = ['title', 'author', 'publisher']
    for field in fields_str:
        attribute_value = getattr(book_instance, field)
        if not isinstance(attribute_value, str):
            raise RequiredFieldsNotFound(attribute_value)
    return True


def validate_instance_int(book_instance):
    fields_int = ['publication_year', 'stock']
    for field in fields_int:
        attribute_value = getattr(book_instance, field)
        if not isinstance(attribute_value, int) and attribute_value < 0:
            raise RequiredFieldsNotFound(attribute_value)
    return True
