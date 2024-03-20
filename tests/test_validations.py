import unittest
from validations import validate_publication_year, validate_isbn, validate_book


class TestValidatePublicationYear(unittest.TestCase):
    def test_valid_publication_year(self):
        valid_years = [2000, 2022, 1500]
        current_year = 2024
        for year in valid_years:
            self.assertTrue(validate_publication_year(year, current_year),
                            f"Year {year} should be valid")

    def test_invalid_publication_year(self):
        invalid_years = [3000, 1000, -100, None, "2022"]
        current_year = 2024
        for year in invalid_years:
            self.assertFalse(validate_publication_year(year, current_year),
                             f"Year {year} should be invalid")


class TestValidateISBN(unittest.TestCase):
    def test_valid_isbn(self):
        valid_isbn = ["978-606-8126-35-7", "0-06-112008-1"]
        for isbn in valid_isbn:
            self.assertTrue(validate_isbn(isbn),
                            f"ISBN {isbn} should be valid")

    def test_invalid_isbn(self):
        invalid_isbn = ["978-606-8156-35-7", None, "978-233-8126-35-7", 232-8126-35-7]
        for isbn in invalid_isbn:
            self.assertFalse(validate_isbn(isbn),
                             f"ISBN {isbn} should not be valid")


class TestValidateBook(unittest.TestCase):

    def test_valid_instance(self):
        # to send each field instead of instance/ send a list
        valid_instances = [
            ("The Great Gatsby", "Scribner", "F. Scott Fitzgerald", 1925, "978-0743273565", 10),
            ("To Kill a Mockingbird", "Harper Lee", "J.B. Lippincott & Co.", 1960, "0-06-112008-1", 8)
        ]

        for instance in valid_instances:
            title, author, publisher, publication_year, isbn, stock = instance
            self.assertTrue(
                validate_book(title, author, publisher, publication_year, isbn, stock),
                f"Instance {instance[0]} should be valid."
            )

    def test_invalid_instances(self):
        invalid_instances = [
            ("Random Title", "Random author", "Random publisher", 2032, "05-4543-5435", 0)
        ]

        for instance in invalid_instances:
            title, publisher, author, publication_year, isbn, stock = instance
            self.assertFalse(
                validate_book(title, publisher, author, publication_year, isbn, stock),
                f"Instance {instance[0]} should be invalid."
            )


if __name__ == '__main__':
    unittest.main()
