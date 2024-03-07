
class ISBNNotFound(Exception):
    def __init__(self, isbn, message="ISBN not found"):
        super().__init__(message)
        self.message = message
        self.isbn = isbn

    def __str__(self):
        return f"{self.message}: (Book ISBN : {self.isbn})"


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
