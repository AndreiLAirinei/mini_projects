from exceptions import ISBNInvalid, RequiredFieldsNotFound, PublicationYearInvalid, StockInvalid


def validate_publication_year(year):
    current_year = 2024
    if 1500 <= year <= current_year:
        return True
    else:
        return False


def validate_isbn(isbn):
    # Remove hyphens from the ISBN
    isbn = isbn.replace("-", "")

    # Checking the length of the string
    if len(isbn) not in (10, 13):
        return False

    total_sum = 0
    if len(isbn) == 10:
        # ISBN-10 algorithm
        for i, char in enumerate(isbn):
            if char.isdigit():
                total_sum += int(char) * (10 - i)

        if total_sum % 10 == 0:
            return True
        else:
            return False

    elif len(isbn) == 13:
        # ISBN-13 algorithm
        for i, char in enumerate(isbn):
            if char.isdigit() and i % 2 != 0:
                total_sum += int(char)
            else:
                total_sum += int(char) * 3

        if total_sum % 11 == 0:
            return True
        else:
            return False


def validate_book(book_instance):
    # Validation for individual fields
    try:
        if (book_instance.title is not None) and not isinstance(book_instance.title, str):
            raise RequiredFieldsNotFound(book_instance.title)

        if (book_instance.author is not None) and not isinstance(book_instance.author, str):
            raise RequiredFieldsNotFound(book_instance.author)

        if (book_instance.publisher is not None) and not isinstance(book_instance.publisher, str):
            raise RequiredFieldsNotFound(book_instance.publisher)

        if book_instance.publication_year is not None and (not isinstance(book_instance.publication_year, int)
                    or book_instance.publication_year < 0) and not validate_publication_year(book_instance.ISBN):
            raise PublicationYearInvalid(book_instance.publication_year)

        if (book_instance.ISBN is not None) and not validate_isbn(book_instance.ISBN):
            raise ISBNInvalid(book_instance.ISBN)

        if not isinstance(book_instance.stock, int) or book_instance.stock < 0:
            raise StockInvalid(book_instance.stock)

    except (RequiredFieldsNotFound, PublicationYearInvalid, ISBNInvalid, StockInvalid) as error:
        print(str(error))

    return True
