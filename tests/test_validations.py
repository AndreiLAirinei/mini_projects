import unittest
from book_model import Book
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
        invalid_isbn = [978-606-8126-35-7, None, 978-233-8126-35-7, 232-8126-35-7]
        for isbn in invalid_isbn:
            self.assertFalse(validate_isbn(isbn),
                             f"ISBN {isbn} should not be valid")


class TestValidateBook(unittest.TestCase):

    def test_valid_instance(self):
        valid_instances = [
            Book("The Great Gatsby", "Scribner", "F. Scott Fitzgerald",
                1925, "978-0743273565", 10),
            Book("To Kill a Mockingbird", "Harper Lee", "J.B. Lippincott & Co.",
                1960, "0-06-112008-1", 8)
        ]

        for instance in valid_instances:
            self.assertTrue(validate_book(instance), f"Instance {instance.title} should be valid.")

    def test_invalid_instances(self):
        invalid_instances = [
            Book("Random Title", "Random author", "Random publisher",
                 2053, "05-4543-5435")
        ]

        for instance in invalid_instances:
            self.assertFalse(validate_book(instance), f"Instance {instance.title} should not be valid.")


if __name__ == '__main__':
    unittest.main()
