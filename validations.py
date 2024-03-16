from exceptions import ISBNInvalid, RequiredFieldsNotFound, PublicationYearInvalid, StockInvalid


def validate_publication_year(year, current_year):
    if year is None or isinstance(year, str):
        return False
    else:
        return 1499 < year < current_year + 1


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


def validate_instance_str(book_attribute):
    if not isinstance(book_attribute, str):
        raise RequiredFieldsNotFound(book_attribute)
    return True


def validate_instance_int(book_attribute):
    if not isinstance(book_attribute, int) and book_attribute < 0:
        raise RequiredFieldsNotFound(book_attribute)
    return True


# def validate_instance_int(book_attribute):
#     fields_int = ['publication_year', 'stock']
#     for field in fields_int:
#         attribute_value = getattr(book_instance, field)
#         if not isinstance(attribute_value, int) and attribute_value < 0:
#             raise RequiredFieldsNotFound(attribute_value)
#     return True
