
class IDNotFound(Exception):
    def __init__(self, id_instance, message="ID not found"):
        super().__init__(message)
        self.message = message
        self.id = id_instance

    def __str__(self):
        return f"{self.message}: ( ID : {self.id})"


class RequiredFieldsNotFound(Exception):
    def __init__(self, message="Required fields are missing:", *args):
        self.message = message
        self.args = args

    def __str__(self):
        return f"{self.message}: ({self.args})"


class ISBNInvalid(Exception):
    def __init__(self, isbn, message="ISBN invalid"):
        self.message = message
        self.isbn = isbn

    def __str__(self):
        return f"{self.message}: (Book ISBN : {self.isbn})"


class BookFormatInvalid(Exception):
    def __init__(self, isbn, message="Book invalid"):
        self.message = message
        self.isbn = isbn

    def __str__(self):
        return f"{self.message}: (Book ISBN : {self.isbn})"


class UserFormatInvalid(Exception):
    def __init__(self, user_id, message="User invalid"):
        self.message = message
        self.user_id = user_id

    def __str__(self):
        return f"{self.message}: (User ID : {self.user_id})"


class PublicationYearInvalid(Exception):
    def __init__(self, message="Publication year is invalid: ", *args):
        self.message = message
        self.args = args

    def __str__(self):
        return f"{self.message}: (Year: {self.args})"


class StockInvalid(Exception):
    def __init__(self, message="Stock is invalid: ", *args):
        self.message = message
        self.args = args

    def __str__(self):
        return f"{self.message}: (Stock: {self.args})"


class NameFormatInvalid(Exception):
    def __init__(self, message="Name format is invalid: ", *args):
        self.message = message
        self.args = args

    def __str__(self):
        return f"{self.message}: (Name: {self.args})"


class AddressFormatInvalid(Exception):
    def __init__(self, message="Address format is invalid: ", *args):
        self.message = message
        self.args = args

    def __str__(self):
        return f"{self.message}: (Address: {self.args})"
