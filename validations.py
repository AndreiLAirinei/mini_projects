from datetime import datetime
from exceptions import (ISBNInvalid, RequiredFieldsNotFound, PublicationYearInvalid,
                        StockInvalid, AddressFormatInvalid, NameFormatInvalid)
import re


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


def validate_name_format(attribute):
    if not isinstance(attribute, str) or attribute is None:
        return False

    if len(attribute) > 15:
        return False

    # for patterns like McDonald or O'Neil
    name_pattern = r'^[A-Z][a-z\'\-]*$'
    if re.match(name_pattern, attribute):
        return True
    else:
        return False


def validate_format_address(address):
    if not isinstance(address, str) or address is None:
        return False

    abbreviation_pattern = r"\b(?:Str\.|Nr\.|Ave\.|St\.|Blvd\.|Ln\.|Rd\.|Pl\.|Ct\.)\s"
    abbreviation_regex = re.compile(abbreviation_pattern)
    matches = abbreviation_regex.findall(address)

    for match in matches:
        abbreviation_last_index = address.find(match) + len(match)
        char_after_abbreviation = address[abbreviation_last_index]

        if not (char_after_abbreviation.isupper() or char_after_abbreviation.isdigit()):
            return False


def validate_book(title, author, publisher, publication_year, isbn, stock):
    try:
        validate_book_not_none(title, author, publisher, publication_year, isbn)
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


def validate_user(first_name, last_name, address):
    try:
        validate_user_not_none(first_name, last_name, address)
        validate_instance_str(first_name)
        validate_instance_str(last_name)
        validate_instance_str(address)

        # To add an address format validations

        if not validate_format_address(address):
            raise AddressFormatInvalid

        if not validate_name_format(first_name, last_name):
            raise NameFormatInvalid

    except (AddressFormatInvalid, NameFormatInvalid) as error:
        print(str(error))


def validate_book_not_none(title, author, publisher, publication_year, isbn):
    fields = ['title', 'author', 'publisher', 'publication_year', 'isbn']
    for field in fields:
        attribute_value = locals()[field]
        if attribute_value is None:
            raise RequiredFieldsNotFound(attribute_value)
    return True


def validate_user_not_none(first_name, last_name, address):
    fields = ['first_name', "last_name", "address"]
    for field in fields:
        attribute_value = locals()[field]
        if attribute_value in None:
            raise RequiredFieldsNotFound(attribute_value)
    return True


def validate_instance_str(attribute):
    if not isinstance(attribute, str):
        raise RequiredFieldsNotFound(attribute)
    return True


def validate_instance_int(attribute):
    if not isinstance(attribute, int) and attribute < 0:
        raise RequiredFieldsNotFound(attribute)
    return True


